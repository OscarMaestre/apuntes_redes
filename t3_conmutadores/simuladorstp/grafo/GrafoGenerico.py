import unittest

class Nodo(object):
    def __init__(self, num_nodo=0) -> None:
        self.num_nodo=num_nodo
    
    def get_num(self):
        return self.num_nodo

class Arista(object):
    def __init__(self, nodo1, nodo2, peso=1) -> None:
        self.nodo1=nodo1
        self.nodo2=nodo2
        self.peso=peso

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
    
class TestGrafo(unittest.TestCase):
    def get_grafo(self):
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
    
    def test_grafo(self):   
        g=self.get_grafo()
        print(g.matriz_adyacencia)
    
    def test_grafo_find_nodo(self):   
        g=self.get_grafo()
        nodo=g.lista_nodos[4]
        pos=g.get_pos_nodo(nodo)
        self.assertEqual(pos, 4)

    def test_grafo_find_adyacentes(self):   
        g=self.get_grafo()
        nodo=g.lista_nodos[4]
        lista_aristas=g.get_lista_aristas_adyacentes(nodo)
        print(lista_aristas)
    
        
if __name__=="__main__":
    unittest.main()