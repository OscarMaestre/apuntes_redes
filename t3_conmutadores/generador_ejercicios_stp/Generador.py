import networkx as nx
from random import randint, shuffle
import matplotlib.pyplot as plt

class Nodo(object):
    def __init__(self, prioridad, num):
        self.prioridad=prioridad
        #La etiqueta se usa en las descripciones
        #de tipo restructuredText
        self.etiqueta="Switch "+num+", prioridad "+ str(self.prioridad)
        #El número se dibuja en los grafos
        self.numero=num
        self.segmentos_vecinos=[]

    def add_vecino(self, nodo_vecino, mac_nuestra,mac_vecino):
        tupla_vecindad=(nodo_vecino, mac_nuestra, mac_vecino)
        self.segmentos_vecinos.append(tupla_vecindad)

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
            self.nodos.append(nodo)
            self.grafo_nx.add_node(nodo)
        self.generar_aristas()

    def get_nodos_punteados(self):
        descripciones=[]
        for nodo in self.nodos:
            descripciones.append("* "+nodo.etiqueta)
        return "\n".join(descripciones)

    def averiguar_switch_raiz(self):
        prioridades_ordenadas=sorted(self.prioridades)
        prioridad_mejor=prioridades_ordenadas[0]
        print("La mejor es (prioridad, mac, num_switch):"+prioridad_mejor)

    def get_aristas_punteadas(self):
        descripciones=[]
        for arista in self.aristas:
            descripciones.append("* "+str(arista))
        return "\n".join(descripciones)
    
    def anadir_arista(self, nodo_origen, nodo_destino):
        mac_origen=self.macs.pop()
        mac_destino=self.macs.pop()
        prioridad_origen=f"{nodo_origen.prioridad}-{mac_origen}-{nodo_origen.numero}"
        prioridad_destino=f"{nodo_destino.prioridad}-{mac_destino}-{nodo_destino.numero}"
        self.prioridades.append(prioridad_origen)
        self.prioridades.append(prioridad_destino)
        self.grafo_nx.add_edge(nodo_origen, nodo_destino, inicio=mac_origen, fin=mac_destino)
        obj_arista=Arista(nodo_origen, mac_origen, nodo_destino, mac_destino)
        self.aristas.append(obj_arista)

    #Para generar aristas al azar, basta con barajar los n nodos y 
    #generar n-1 aristas entre ellos
    def generar_aristas(self, num_aristas_extra=2):
        nodos = list(self.grafo_nx.nodes)
        shuffle(nodos)  # Barajar nodos para crear un árbol aleatorio
        for i in range(len(nodos) - 1):
            nodo_origen=nodos[i]
            nodo_destino=nodos[i+1]
            self.anadir_arista(nodo_origen, nodo_destino)
            
            

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
    g.averiguar_switch_raiz()
    g.guardar_grafo("Grafo.png")