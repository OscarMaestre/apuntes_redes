import unittest
from random import shuffle, randint
import heapq

class Arista(object):
    def __init__(self, nodo1, nodo2, mac1, mac2) -> None:
        self.nodo1=nodo1
        self.mac1=mac1

        self.nodo2=nodo2
        self.mac2=mac2

        
class Nodo(object):
    def __init__(self, prioridad, lista_macs, nombre):
        self.prioridad=prioridad
        self.lista_macs=lista_macs
        self.nombre=nombre
        self.prioridad_stp=self.calcular_prioridad_stp()
        self.estado_macs=["B" for mac in self.lista_macs]
        self.costo_a_la_raiz=None

    def set_costo_a_la_raiz(self, costo):
        self.costo_a_la_raiz=costo
    
    def calcular_prioridad_stp(self):
        copia_lista=self.lista_macs.copy()
        copia_lista.sort()
        mejor_mac=copia_lista[0]
        #print("La mejor mac es:"+mejor_mac)
        
        prioridad_stp="{0}:{1}".format(self.prioridad, mejor_mac)
        #print("Prioridad stp:"+prioridad_stp)
        return prioridad_stp
    
    def __str__(self) -> str:
        macs=",".join(self.lista_macs)
        cad=f"Nombre:{self.nombre}, Prioridad {self.prioridad}, macs=[{macs}], prioridad STP {self.prioridad_stp} "
        return cad


class Grafo:
    def __init__(self):
        self.aristas = []
        self.nodos=[]
        self.mejor_prioridad="ZZZZZZZ"
        self.nodo_raiz=Nodo

    def agregar_arista(self, arista):
        nodo_origen=arista.nodo1
        nodo_destino=arista.nodo2
        if arista not in self.aristas:
            self.aristas.append(arista)
            if (nodo_origen, []) in self.nodos or (nodo_destino, []) in self.nodos:
                for nodo, adyacentes in self.nodos:
                    #print(nodo, adyacentes)
                    if nodo == nodo_origen:
                        adyacentes.append(nodo_destino)
                    elif nodo == nodo_destino:
                        adyacentes.append(nodo_origen)
            

    def agregar_nodo(self, nodo):
        # print(nodo)
        if nodo not in self.nodos:
            self.nodos.append ( (nodo, []) )
            if nodo.prioridad_stp<=self.mejor_prioridad:
                self.nodo_raiz=nodo
                self.mejor_prioridad=nodo.prioridad_stp

    def get_aristas(self):
        return self.aristas

    def get_nodo_mejor_prioridad(self):
        return self.nodo_raiz

    def __str__(self) -> str:
        cad=""
        for nodo in self.nodos:
            cad+=str(nodo[0])+"\n"
        return cad
    
    def calcular_costo_minimo(self, nodo_origen, nodo_destino):
        print(self.nodos)
        if (nodo_origen, []) not in self.nodos or (nodo_destino, []) not in self.nodos:
            print("Fallo")
            return None

        distancia = {nodo: float('inf') for nodo, _ in self.nodos}
        distancia[nodo_origen] = 0

        cola_prioridad = [(0, nodo_origen)]  # (costo, nodo)

        while cola_prioridad:
            costo_actual, nodo_actual = heapq.heappop(cola_prioridad)

            if nodo_actual == nodo_destino:
                return costo_actual  # Hemos alcanzado el nodo de destino, devolvemos el costo mínimo

            for nodo, adyacentes in self.nodos:
                if nodo == nodo_actual:
                    for vecino in adyacentes:
                        costo_vecino = costo_actual + 1

                        if costo_vecino < distancia[vecino]:
                            distancia[vecino] = costo_vecino
                            heapq.heappush(cola_prioridad, (costo_vecino, vecino))
        print(distancia)
        return None

    @staticmethod
    def get_macs(num_macs=20):
        macs=[str(hex(num)[2:]).zfill(2) for num in range(0,255)]
        shuffle(macs)
        return macs[0:num_macs]
        
    @staticmethod
    def get_grafo_cuadrado():
        PRIORIDAD_MINIMA=0
        PRIORIDAD_MAXIMA=8

        grafo=Grafo()
        macs=Grafo.get_macs(8)
        
        nodo_norte=Nodo(randint(PRIORIDAD_MINIMA,PRIORIDAD_MAXIMA), 
                        macs[0:2], "Switch 0")
        nodo_sur=Nodo(randint(PRIORIDAD_MINIMA,PRIORIDAD_MAXIMA), 
                        macs[2:4], "Switch 1")
        nodo_este=Nodo(randint(PRIORIDAD_MINIMA,PRIORIDAD_MAXIMA), 
                        macs[4:6], "Switch 2")
        nodo_oeste=Nodo(randint(PRIORIDAD_MINIMA,PRIORIDAD_MAXIMA), 
                        macs[6:8], "Switch 3")
        grafo.agregar_nodo(nodo_norte)
        grafo.agregar_nodo(nodo_sur)
        grafo.agregar_nodo(nodo_este)
        grafo.agregar_nodo(nodo_oeste)
        
        arista_no=Arista(nodo_norte, nodo_oeste, 
                         nodo_norte.lista_macs[0],
                         nodo_oeste.lista_macs[0])
        arista_ne=Arista(nodo_norte, nodo_este,
                         nodo_norte.lista_macs[1],
                         nodo_este.lista_macs[1])
        arista_os=Arista(nodo_oeste, nodo_sur,
                         nodo_oeste.lista_macs[1],
                         nodo_sur.lista_macs[1])
        arista_se=Arista(nodo_sur, nodo_este,
                         nodo_sur.lista_macs[0],
                         nodo_este.lista_macs[0])
        grafo.agregar_arista(arista_no)
        grafo.agregar_arista(arista_ne)
        grafo.agregar_arista(arista_os)
        grafo.agregar_arista(arista_se)
        print(grafo.nodos)
        return grafo
        
        
        



class TestNodo(unittest.TestCase):
    def test_prioridad1(self):
        n=Nodo(10, ["0f", "0b", "0c", "0a"], "Switch 1")
        self.assertEqual(n.prioridad_stp, "10:0a")

    def test_grafo(self):
        g=Grafo.get_grafo_cuadrado()
        print("grafo")
        #print(str(g))
        #print(g.get_nodo_mejor_prioridad())
        coste_minimo=g.calcular_costo_minimo(g.nodos[0], g.nodos[2])
        print("Coste minimo")
        print("--------------")
        print(coste_minimo)

if __name__=="__main__":
    unittest.main()
