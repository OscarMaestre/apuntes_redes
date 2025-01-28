import networkx as nx
from random import randint, shuffle

import matplotlib.pyplot as plt

class Nodo(object):
    ESTADO_BLOQUEADO="Bloqueado"
    ESTADO_DESIGNADO="Designado"
    ESTADO_RAIZ="Raiz"
    def __init__(self, prioridad, num):
        self.prioridad=prioridad
        #La etiqueta se usa en las descripciones
        #de tipo restructuredText
        self.etiqueta="Switch "+str(num)+", prioridad "+ str(self.prioridad)
        #El número se dibuja en los grafos
        self.numero=num
        self.segmentos_vecinos=[]
        self.distancia_a_raiz=0
        self.es_raiz=False
        self.estado_puertos=dict()


    def set_estado_puerto(self, puerto, estado):
        print(f"Añadiendo puerto {puerto} a {self.etiqueta}")
        self.estado_puertos[puerto]=estado
        
    def set_bloqueado(self, puerto):
        # print("Bloqueando puerto "+puerto)
        self.set_estado_puerto(puerto, Nodo.ESTADO_BLOQUEADO)
    def set_designado(self, puerto):
        self.set_estado_puerto(puerto, Nodo.ESTADO_DESIGNADO)
    def set_raiz(self, puerto):
        self.set_estado_puerto(puerto, Nodo.ESTADO_RAIZ)

    def set_distancia_a_raiz(self, distancia_a_raiz):
        self.distancia_a_raiz=distancia_a_raiz
    def get_distancia_a_raiz(self):
        return self.distancia_a_raiz
    
    def get_mac_mas_baja(self):
        macs=self.estado_puertos.keys()
        lista_macs=list(macs)
        lista_macs_ordenada=sorted(lista_macs)
        return lista_macs_ordenada[0]
    
    def get_prioridad(self):
        mac_mas_baja=self.get_mac_mas_baja()
        texto=f"{self.prioridad}:{mac_mas_baja}"
        return texto
    
    def add_vecino(self, nodo_vecino, mac_nuestra,mac_vecino):
        tupla_vecindad=(nodo_vecino, mac_nuestra, mac_vecino)
        
        self.segmentos_vecinos.append(tupla_vecindad)

    def establecer_puerto_raiz(self):
        #Comprobar qué puertos NO están a DESIGNADO y averiguar
        #el que nos lleva por un mejor camino a la raíz. Si hay dos, elegir el
        #de menor MAC
        #Calculamos el coste a la raíz desde cada mac
        distancias_desde_mac=dict()
        for tupla_vecindad in self.segmentos_vecinos:
            (nodo_vecino, mac_nuestra, mac_vecino) = tupla_vecindad
            distancias_desde_mac[mac_nuestra]=nodo_vecino.get_distancia_a_raiz()
        print(distancias_desde_mac)
        mac_con_mejor_coste=min(distancias_desde_mac, key=distancias_desde_mac.get)
        self.set_raiz(mac_con_mejor_coste)

    def establecer_puertos_designados(self):
        #Buscar  nuestras MAC que NO SEAN RAÍZ y ver si son mejores
        #que las del "vecino de enfrente"
        pass
    def comparar_distancia_con_vecino(self, nodo_vecino):
        if (self.distancia_a_raiz<nodo_vecino.distancia_a_raiz):
            return -1
        if (self.distancia_a_raiz==nodo_vecino.distancia_a_raiz):
            return 0
        if (self.distancia_a_raiz>nodo_vecino.distancia_a_raiz):
            return 1

    def procesar_vecindades(self):
        for vecindad in self.segmentos_vecinos:
            (nodo_vecino, mac_nuestra, mac_vecino)=vecindad
            comparacion=self.comparar_distancia_con_vecino(nodo_vecino)

    def get_estado_puertos(self):
        estado=[self.get_prioridad()+", distancia a raíz:"+str(self.distancia_a_raiz)]
        for pos, puerto in enumerate(self.estado_puertos):
            cadena=f"* Puerto {puerto}, estado {self.estado_puertos[puerto]}"
            estado.append(cadena)
        return "\n".join(estado)

    def __hash__(self):
        return hash(self.etiqueta)

    def __eq__(self, value):
        return self.etiqueta == value.etiqueta

    def __str__(self):
        return "SW"+str(self.numero)+" P"+str(self.prioridad)

class Arista(object):
    def __init__(self, nodo1, mac1, nodo2, mac2):
        self.nodo1=nodo1;
        self.mac1=mac1;
        self.nodo2=nodo2;
        self.mac2=mac2;
    def __str__(self):
        texto=f"Conexion desde el {self.nodo1.etiqueta} con MAC {self.mac1} a la MAC {self.mac2} de {self.nodo2.etiqueta} "
        return texto
        
class Grafo(object):
    def __init__(self, num_nodos):
        self.nodos=[]
        self.aristas=[]
        self.prioridades=[]
        self.macs=[hex(num)[2:] for num in range(16, 255)]
        shuffle(self.macs)
        self.grafo_nx=nx.graph.Graph();
        for i in range(0, num_nodos):
            prioridad=randint(1,8)
            nodo=Nodo(prioridad, str(i+1))
            self.anadir_nodo(nodo)
        self.generar_aristas()

    def anadir_nodo(self,nodo):
        self.nodos.append(nodo)
        self.grafo_nx.add_node(nodo)

    def get_nodos_punteados(self):
        descripciones=[]
        for nodo in self.nodos:
            descripciones.append("* "+nodo.etiqueta)
        return "\n".join(descripciones)

    def get_estado_puertos(self):
        estado=[]
        for nodo in self.nodos:
            estado.append(nodo.get_estado_puertos())
        return "\n".join(estado)

    def get_distancias_punteadas(self):
        descripciones=[]
        for nodo in self.nodos:
            descripciones.append("* "+nodo.etiqueta + ". Distancia al raíz:"+str(nodo.distancia_a_raiz))
        return "\n".join(descripciones)

    def averiguar_switch_raiz(self):
        prioridades=[]
        for nodo in self.nodos:
            prioridades.append(nodo.get_prioridad())
        prioridades_ordenadas=sorted(prioridades)
        prioridad_mejor=prioridades_ordenadas[0]
        print("La mejor prioridad es --> "+ prioridad_mejor)

        for nodo in self.nodos:
            prioridad=nodo.get_prioridad()
            if prioridad==prioridad_mejor:
                return nodo
        assert(False)


    def establecer_distancias_al_raiz(self, nodo_raiz):
        for nodo in self.nodos:
            distancia = nx.shortest_path_length(self.grafo_nx, source=nodo, target=nodo_raiz)
            nodo.set_distancia_a_raiz(distancia)

    #Dado un numero de switch (por ejemplo el 3) nos devuelve
    #el nodo exacto (en realidad es el nodo con la posicion num_Switch-1)
    def get_nodo(self, num_switch):
        nodo=self.nodos[int(num_switch)-1]
        return nodo

    def get_aristas_punteadas(self):
        descripciones=[]
        for arista in self.aristas:
            descripciones.append("* "+str(arista))
        return "\n".join(descripciones)
    
    def resolver_stp(self):
        nodo_raiz=self.averiguar_switch_raiz()
        self.establecer_distancias_al_raiz(nodo_raiz) 
        
        for arista in self.aristas:
            u=arista.nodo1
            v=arista.nodo2
            mac_origen=arista.mac1
            mac_destino=arista.mac2

            print("--------Arista-------")
            origen=u.get_prioridad()+" puerto " +mac_origen
            destino=v.get_prioridad()+ " puerto " +mac_destino
            print(f"{origen}--{destino}")
            print("--------Fin de Arista-------\n")
            if u==nodo_raiz:
                print("Ponemos a designado el puerto  "+mac_origen)
                u.set_designado(mac_origen)
            if v==nodo_raiz:
                print("Ponemos a designado el puerto  "+mac_destino)
                v.set_designado(mac_destino)
            
            # if u.distancia_a_raiz<v.distancia_a_raiz:
            #     print(u, v, "<")
            # if u.distancia_a_raiz==v.distancia_a_raiz:
            #     print(u, v, "=")
            # if u.distancia_a_raiz>v.distancia_a_raiz:
            #     print(u, v, ">")
            
        
        print("Estableciendo puertos raíz...")
        for nodo in self.nodos:
            print("Comprobando nodo:"+nodo.get_prioridad())
            if nodo==nodo_raiz:
                print("Ignorando nodo raíz "+nodo.get_prioridad())
            else:
                nodo.establecer_puerto_raiz()

    def anadir_arista_con_macs(self, nodo_origen, nodo_destino, mac_origen, mac_destino):
        nodo_origen.set_bloqueado(mac_origen)
        nodo_destino.set_bloqueado(mac_destino)
        
        prioridad_origen=f"{nodo_origen.prioridad}-{mac_origen}-{nodo_origen.numero}"
        prioridad_destino=f"{nodo_destino.prioridad}-{mac_destino}-{nodo_destino.numero}"
        self.prioridades.append(prioridad_origen)
        self.prioridades.append(prioridad_destino)
        self.grafo_nx.add_edge(nodo_origen, nodo_destino, inicio=mac_origen, fin=mac_destino)
        obj_arista=Arista(nodo_origen, mac_origen, nodo_destino, mac_destino)
        nodo_origen.add_vecino(nodo_destino,mac_origen,mac_destino)
        nodo_destino.add_vecino(nodo_origen, mac_destino, mac_origen)
        self.aristas.append(obj_arista)
        print(str(obj_arista))
    def anadir_arista(self, nodo_origen, nodo_destino):
        mac_origen=self.macs.pop()
        mac_destino=self.macs.pop()
        self.anadir_arista_con_macs(nodo_origen, nodo_destino, mac_origen, mac_destino)

    #Para generar aristas al azar, basta con barajar los n nodos y 
    #generar n-1 aristas entre ellos
    def generar_aristas(self, num_aristas_extra=2):
        nodos = list(self.grafo_nx.nodes)
        print("Generando arbol mínimo...")
        shuffle(nodos)  # Barajar nodos para crear un árbol aleatorio
        for i in range(len(nodos) - 1):
            nodo_origen=nodos[i]
            nodo_destino=nodos[i+1]
            self.anadir_arista(nodo_origen, nodo_destino)
        print("Generando aristas extra")
            

        posibles_aristas = list(nx.non_edges(self.grafo_nx))  # Todas las aristas posibles que no están en el grafo
        shuffle(posibles_aristas)
        for i in range(min(num_aristas_extra, len(posibles_aristas))):
            arista_elegida=posibles_aristas[i]
            nodo_origen=arista_elegida[0]
            nodo_destino=arista_elegida[1]
            self.anadir_arista(nodo_origen, nodo_destino)

    def guardar_grafo(self, nombre_archivo):
        pos = nx.spring_layout(self.grafo_nx)
        nx.draw(self.grafo_nx, pos, with_labels=True, font_weight='bold', node_color="white")
        
        # Dibujar etiquetas de aristas
        for (u, v, data) in self.grafo_nx.edges(data=True):
            # Coordenadas de los nodos
            x1, y1 = pos[u]  # Coordenadas del nodo de origen
            x2, y2 = pos[v]  # Coordenadas del nodo de destino

            # Ajuste para las posiciones de las etiquetas
            ajuste_inicio = 0.8  # 20% hacia el destino
            ajuste_fin = 0.2     # 80% hacia el destino
            
            # Calcular posiciones interpoladas
            etiqueta_fin_pos = (
                (1 - ajuste_inicio) * x1 + ajuste_inicio * x2,
                (1 - ajuste_inicio) * y1 + ajuste_inicio * y2
            )
            etiqueta_inicio_pos = (
                (1 - ajuste_fin) * x1 + ajuste_fin * x2,
                (1 - ajuste_fin) * y1 + ajuste_fin * y2
            )
            
            # Dibujar las etiquetas
            plt.text(*etiqueta_inicio_pos, data["inicio"], fontsize=14, ha="center", va="center")
            plt.text(*etiqueta_fin_pos, data["fin"], fontsize=14,  ha="center", va="center")

        # Guardar el grafo
        plt.savefig(nombre_archivo)


    def guardar_grafo_dot(self, nombre_archivo_dot):
        lineas=["graph{"]
        for arista in self.aristas:
            #En dot el head label es el "destino"
            etiqueta1=arista.nodo1.get_prioridad()
            etiqueta2=arista.nodo2.get_prioridad()
            texto=f"\t\"{etiqueta1}\" -- \"{etiqueta2}\" [headlabel=\"{arista.mac2}\", taillabel=\"{arista.mac1}\"]"
            lineas.append(texto)
        lineas.append("}")
        grafo_para_guardar="\n".join(lineas)
        with open(nombre_archivo_dot, "w") as fich:
            fich.write(grafo_para_guardar)

    @staticmethod
    def get_grafo_azar():
        num_nodos=randint(5,7)
        g=Grafo(num_nodos)
        return g



if __name__=="__main__":
    g=Grafo.get_grafo_azar()
    print(g.grafo_nx)
    print(g.get_nodos_punteados())
    print(g.get_aristas_punteadas())
    g.resolver_stp()
    print(g.get_estado_puertos())
    # g.guardar_grafo("Grafo.png")
    g.guardar_grafo_dot("Grafo.dot")