import unittest
import heapq

class Nodo(object):
    def __init__(self, num_nodo=0, nombre="Nodo") -> None:
        self.num_nodo=num_nodo
        self.nombre=nombre
    
    def get_num(self):
        return self.num_nodo
    
    def __str__(self) -> str:
        return self.nombre

class Arista(object):
    def __init__(self, nodo1, nodo2, peso=1) -> None:
        self.nodo1=nodo1
        self.nodo2=nodo2
        self.peso=peso
    def __str__(self):
        cad_nodo1=str(self.nodo1)
        cad_nodo2=str(self.nodo2)
        cadena=f"Arista {cad_nodo1} a {cad_nodo2}"
        return cadena
    
class Grafo(object):
    def __init__(self, lista_nodos, lista_aristas) -> None:
        self.lista_nodos=lista_nodos
        #Asignamos a cada nodo una posicion
        for pos in range(0, len(lista_nodos)):
            self.lista_nodos[pos].num_nodo=pos

        self.matriz_adyacencia=[ [None for pos in range(0, len(self.lista_nodos))] for pos in range(0, len(self.lista_nodos))]

        for arista in lista_aristas:
            nodo_origen=arista.nodo1
            nodo_destino=arista.nodo2
            pos_origen=nodo_origen.get_num()
            pos_destino=nodo_destino.get_num()
            self.matriz_adyacencia[pos_origen][pos_destino]=arista
            self.matriz_adyacencia[pos_destino][pos_origen]=arista
    
    def get_pos_nodo(self, nodo):
        for pos in range(0, len(self.lista_nodos)):
            if nodo==self.lista_nodos[pos]:
                return pos
        return None
    
    def get_lista_aristas_adyacentes(self, nodo):
        pos_nodo=self.get_pos_nodo(nodo)
        lista_aristas=[]
        for pos in range(0, len(self.lista_nodos)):
            arista=self.matriz_adyacencia[pos_nodo][pos]
            if arista!=None:
                lista_aristas.append(arista)
        #Fin del for
        return lista_aristas
    
    def get_lista_tuplas_nodos_adyacentes(self, nodo):
        lista_adyacentes=self.get_lista_aristas_adyacentes(nodo)
        lista_tuplas=[]
        for arista in lista_adyacentes:
            if arista.nodo1==nodo:
                tupla=(arista.nodo2, arista.peso)
                lista_tuplas.append(tupla)
            if arista.nodo2==nodo:
                tupla=(arista.nodo1, arista.peso)
                lista_tuplas.append(tupla)
        #Fin del for
        return lista_tuplas
    
    def calcular_costo_minimo(self, nodo_origen, nodo_destino):
        
        distancia = {nodo: float('inf') for nodo in self.lista_nodos}
        distancia[nodo_origen] = 0

        cola_prioridad = [(0, nodo_origen)]  # (costo, nodo)

        while cola_prioridad:
            costo_actual, nodo_actual = heapq.heappop(cola_prioridad)

            if nodo_actual == nodo_destino:
                return distancia[nodo_actual]  # Hemos alcanzado el nodo de destino, devolvemos el costo mínimo

            for nodo in self.lista_nodos:
                adyacentes=self.get_lista_tuplas_nodos_adyacentes(nodo)
                if nodo == nodo_actual:
                    for adyacente in adyacentes:
                        vecino=adyacente[0]
                        costo_vecino = costo_actual + 1

                        if costo_vecino < distancia[vecino]:
                            distancia[vecino] = costo_vecino
                            heapq.heappush(cola_prioridad, (costo_vecino, vecino))

        return None  # No hay conexión entre el nodo de origen y el de destino
    
            

    
class TestGrafo(unittest.TestCase):
    def get_grafo_complejo(self):
        n1=Nodo()
        n2=Nodo()
        n3=Nodo()
        n4=Nodo()
        n5=Nodo()
        n6=Nodo()
        n7=Nodo()
        n8=Nodo()
        lista_nodos=[n1,n2,n3,n4,n5,n6,n7,n8]
        a1=Arista(n1,n2)
        a2=Arista(n1,n3)
        a3=Arista(n2,n3)
        a4=Arista(n3,n4)
        a5=Arista(n3,n5)
        a6=Arista(n4,n6)
        a7=Arista(n5,n6)
        a8=Arista(n5,n7)
        a9=Arista(n6,n8)
        lista_aristas=[a1,a2,a3,a4, a5, a6, a7, a8,a9]
        g=Grafo(lista_nodos, lista_aristas)
        return g
    
    def get_grafo_simple1(self):
            #     N
            #    / \
            #   /   \
            #  /     \
            # O-------E
            #  \     /
            #   \   /
            #    \ /
            #     S
        norte=Nodo(nombre="N")
        sur=Nodo(nombre="S")
        este=Nodo(nombre="E")
        oeste=Nodo(nombre="O")
        lista_nodos=[norte,sur,este,oeste]

        a1=Arista(norte,oeste)
        a2=Arista(norte,este)
        a3=Arista(sur,este)
        a4=Arista(sur,oeste)
        a5=Arista(este,oeste)
        lista_aristas=[a1,a2,a3,a4, a5]
        g=Grafo(lista_nodos, lista_aristas)
        return g

    def test_grafo(self):   
        g=self.get_grafo_complejo()
        print(g.matriz_adyacencia)
    
    def test_grafo_find_nodo(self):   
        g=self.get_grafo_complejo()
        nodo=g.lista_nodos[4]
        pos=g.get_pos_nodo(nodo)
        self.assertEqual(pos, 4)

    def test_grafo_find_lista_adyacentes(self):   
        g=self.get_grafo_simple1()
        #El 3 es el oeste y debería devolver 3
        #adyacentes, N, S y E
        nodo=g.lista_nodos[3]
        lista_aristas=g.get_lista_aristas_adyacentes(nodo)
        for a in lista_aristas:
            print(str(a))
    
    def test_grafo_find_nodos_adyacentes(self):   
        g=self.get_grafo_simple1()
        #El 3 es el oeste y debería devolver 3
        #adyacentes, N, S y E
        nodo=g.lista_nodos[3]
        lista_nodos_adyacentes=g.get_lista_tuplas_nodos_adyacentes(nodo)
        for a in lista_nodos_adyacentes:
            print(str(a[0]), str(a[1]) )

    def test_coste_minimo(self):
        g=self.get_grafo_simple1()
        #El 3 es el oeste y debería devolver 3
        #adyacentes, N, S y E
        nodo_norte=g.lista_nodos[0]
        nodo_sur=g.lista_nodos[1]
        nodo_este=g.lista_nodos[2]
        nodo_oeste=g.lista_nodos[3]
        coste=g.calcular_costo_minimo(nodo_norte, nodo_sur)
        print(coste)

if __name__=="__main__":
    unittest.main()