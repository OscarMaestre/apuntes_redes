from Generador import Nodo, Grafo
import unittest


class TestNodo(unittest.TestCase):
    def testBasico(self):
        g=Grafo(0)
        NUM_NODO_1=3
        PRIORIDAD_NODO_1=5
        NUM_NODO_2=4
        PRIORIDAD_NODO_2=2
        
        n1=Nodo(NUM_NODO_1, PRIORIDAD_NODO_1)
        n2=Nodo(NUM_NODO_2, PRIORIDAD_NODO_2)
        g.anadir_nodo(n1)
        g.anadir_nodo(n2)
        g.anadir_arista_con_macs(n1, n2,"N1","N2")
        prioridad_leida_n1=n1.get_prioridad()
        prioridad_leida_n2=n2.get_prioridad()
        self.assertEqual(prioridad_leida_n1, str(NUM_NODO_1)+":N1")
        self.assertEqual(prioridad_leida_n2, str(NUM_NODO_2)+":N2")

        nodo_raiz=g.averiguar_switch_raiz()
        self.assertEqual(nodo_raiz.get_prioridad(),str(NUM_NODO_1)+":N1")

        g.establecer_distancias_al_raiz(nodo_raiz)
        distancia_al_raiz_de_n1=n1.get_distancia_a_raiz()
        distancia_al_raiz_de_n2=n2.get_distancia_a_raiz()
        self.assertEqual(distancia_al_raiz_de_n1, 0)
        self.assertEqual(distancia_al_raiz_de_n2, 1)
        g.resolver_stp()

    def testBasico2(self):
        g=Grafo(0)
        NUM_NODO_1=3
        PRIORIDAD_NODO_1=5
        NUM_NODO_2=4
        PRIORIDAD_NODO_2=2
        NUM_NODO_3=8
        PRIORIDAD_NODO_3=9
        
        n1=Nodo(NUM_NODO_1, PRIORIDAD_NODO_1)
        n2=Nodo(NUM_NODO_2, PRIORIDAD_NODO_2)
        n3=Nodo(NUM_NODO_3, PRIORIDAD_NODO_3)
        g.anadir_nodo(n1)
        g.anadir_nodo(n2)
        g.anadir_nodo(n3)
        g.anadir_arista_con_macs(n1, n2,"N1","N2")
        g.anadir_arista_con_macs(n2, n3,"N22","N3")
        prioridad_leida_n1=n1.get_prioridad()
        prioridad_leida_n2=n2.get_prioridad()
        prioridad_leida_n3=n3.get_prioridad()
        self.assertEqual(prioridad_leida_n1, str(NUM_NODO_1)+":N1")
        self.assertEqual(prioridad_leida_n2, str(NUM_NODO_2)+":N2")
        self.assertEqual(prioridad_leida_n3, str(NUM_NODO_3)+":N3")

        nodo_raiz=g.averiguar_switch_raiz()
        self.assertEqual(nodo_raiz.get_prioridad(),str(NUM_NODO_1)+":N1")

        g.establecer_distancias_al_raiz(nodo_raiz)
        distancia_al_raiz_de_n1=n1.get_distancia_a_raiz()
        distancia_al_raiz_de_n2=n2.get_distancia_a_raiz()
        distancia_al_raiz_de_n3=n3.get_distancia_a_raiz()
        self.assertEqual(distancia_al_raiz_de_n1, 0)
        self.assertEqual(distancia_al_raiz_de_n2, 1)
        self.assertEqual(distancia_al_raiz_de_n3, 2)
        g.resolver_stp()

    def testBasico3(self):
        g=Grafo(0)
        NUM_NODO_1=3
        PRIORIDAD_NODO_1=5
        NUM_NODO_2=4
        PRIORIDAD_NODO_2=2
        NUM_NODO_3=8
        PRIORIDAD_NODO_3=9
        NUM_NODO_4=5
        PRIORIDAD_NODO_4=7
        
        n1=Nodo(NUM_NODO_1, PRIORIDAD_NODO_1)
        n2=Nodo(NUM_NODO_2, PRIORIDAD_NODO_2)
        n3=Nodo(NUM_NODO_3, PRIORIDAD_NODO_3)
        n4=Nodo(NUM_NODO_4, PRIORIDAD_NODO_4)

        g.anadir_nodo(n1)
        g.anadir_nodo(n2)
        g.anadir_nodo(n3)
        g.anadir_nodo(n4)
        g.anadir_arista_con_macs(n1, n2,"N1","N2")
        g.anadir_arista_con_macs(n1, n4,"N11","N4")
        g.anadir_arista_con_macs(n2, n3,"N22","N3")
        prioridad_leida_n1=n1.get_prioridad()
        prioridad_leida_n2=n2.get_prioridad()
        prioridad_leida_n3=n3.get_prioridad()
        self.assertEqual(prioridad_leida_n1, str(NUM_NODO_1)+":N1")
        self.assertEqual(prioridad_leida_n2, str(NUM_NODO_2)+":N2")
        self.assertEqual(prioridad_leida_n3, str(NUM_NODO_3)+":N3")

        nodo_raiz=g.averiguar_switch_raiz()
        self.assertEqual(nodo_raiz.get_prioridad(),str(NUM_NODO_1)+":N1")

        g.establecer_distancias_al_raiz(nodo_raiz)
        distancia_al_raiz_de_n1=n1.get_distancia_a_raiz()
        distancia_al_raiz_de_n2=n2.get_distancia_a_raiz()
        distancia_al_raiz_de_n3=n3.get_distancia_a_raiz()
        distancia_al_raiz_de_n4=n4.get_distancia_a_raiz()
        self.assertEqual(distancia_al_raiz_de_n1, 0)
        self.assertEqual(distancia_al_raiz_de_n2, 1)
        self.assertEqual(distancia_al_raiz_de_n3, 2)
        self.assertEqual(distancia_al_raiz_de_n4, 1)
        g.resolver_stp()
    
    def testBasico4(self):
        g=Grafo(0)
        NODOS=[(1,8), (2,5), (3,3), (4,7), (5,7)]
        lista_nodos=[]
        for tupla in NODOS:
            num=tupla[0]
            prioridad=tupla[1]
            nodo=Nodo(prioridad, num)
            g.anadir_nodo(nodo)
            lista_nodos.append(nodo)
        # * Conexion desde el Switch 1, prioridad 8 con MAC 1e a la MAC b3 de Switch 4, prioridad 7 
        g.anadir_arista_con_macs(lista_nodos[0], lista_nodos[3], "1e", "b3")
        # * Conexion desde el Switch 4, prioridad 7 con MAC f5 a la MAC 43 de Switch 2, prioridad 5 
        g.anadir_arista_con_macs(lista_nodos[3], lista_nodos[1], "f5", "43")
        # * Conexion desde el Switch 2, prioridad 5 con MAC 30 a la MAC 5c de Switch 5, prioridad 7 
        g.anadir_arista_con_macs(lista_nodos[1], lista_nodos[4], "30", "5c")
        # * Conexion desde el Switch 5, prioridad 7 con MAC 54 a la MAC 52 de Switch 3, prioridad 3 
        g.anadir_arista_con_macs(lista_nodos[4], lista_nodos[2], "54", "52")
        # * Conexion desde el Switch 1, prioridad 8 con MAC ce a la MAC 64 de Switch 3, prioridad 3 
        g.anadir_arista_con_macs(lista_nodos[0], lista_nodos[2], "ce", "64")
        # * Conexion desde el Switch 2, prioridad 5 con MAC a4 a la MAC 12 de Switch 3, prioridad 3 
        g.anadir_arista_con_macs(lista_nodos[1], lista_nodos[2], "a4", "12")
        
        g.guardar_grafo_dot("test.dot")
        nodo_raiz=g.averiguar_switch_raiz()
        
        self.assertEqual(nodo_raiz.get_prioridad(), "3:12")
        g.establecer_distancias_al_raiz(nodo_raiz)
        
        g.resolver_stp()
        print(g.get_estado_puertos())

        

if __name__=="__main__":
    unittest.main()