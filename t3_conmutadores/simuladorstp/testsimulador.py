#!/usr/bin/python3 
from tkinter import SW
import simulador
import unittest



class TestBPDU(unittest.TestCase):
    def testDistintosCostes1(self):
        paquete1=simulador.BPDU(1, 0, 1, "03")
        paquete2=simulador.BPDU(2, 1, 3, "04")
        #A nivel interno las raíces y todo se manejan como cadenas
        #El paquete 1 es mejor BPDU que el 2 (o eso debería salir)
        resultado=paquete1.recalcular(paquete2)
        self.assertEqual(paquete1, resultado)

    def testDistintosCostes1(self):
        paquete1=simulador.BPDU(1, 0, 1, "03")
        paquete2=simulador.BPDU(2, 1, 3, "04")
        #El paquete 2 es PEOR BPDU que el 1
        #Para el 2 debería devolverse esto
        bpdu_esperada_para_paquete2=simulador.BPDU(1, 1, 3, "04")
        resultado=paquete2.recalcular(paquete1)
        # print("Resultado obtenido:"+str(resultado))
        # print("Resultado obtenido:"+str(bpdu_esperada_para_paquete2))
        self.assertEqual(bpdu_esperada_para_paquete2, resultado)

    def testIgualesCostes(self):
        paquete1=simulador.BPDU(1, 1, 3, "03")
        paquete2=simulador.BPDU(1, 1, 4, "04")
        #El 3 y el 4 tiene el mismo coste, que es 1
        resultado=paquete1.recalcular(paquete2)
        self.assertEqual(paquete1, resultado)
    

class TestSwitch(unittest.TestCase) :
    def setUp(self) -> None:
        self.puerto_01=simulador.Puerto("01")
        self.puerto_02=simulador.Puerto("02")

        self.puerto_0a=simulador.Puerto("0a")
        self.puerto_0b=simulador.Puerto("0b")

        self.puerto_1a=simulador.Puerto("1a")
        self.puerto_1b=simulador.Puerto("1b")
        
        self.lista_todos_puertos=[self.puerto_01, self.puerto_02,
                                    self.puerto_0a, self.puerto_0b,
                                    self.puerto_1a, self.puerto_1b,]
        self.lista_grupo_1=[self.puerto_01, self.puerto_02]

        self.lista_grupo_3=[self.puerto_1a, self.puerto_1b]


        return super().setUp()

    def test_menor_mac_en_segmento(self):
        puerto_01=simulador.Puerto("01")
        puerto_02=simulador.Puerto("02")
        puerto_01.asociar_puerto(puerto_02)
        puerto_02.asociar_puerto(puerto_01)

        esto_debe_ser_true=puerto_01.tiene_menor_mac_que_puerto_enfrente()
        self.assertEqual(esto_debe_ser_true, True)

        esto_debe_ser_false=puerto_02.tiene_menor_mac_que_puerto_enfrente()
        self.assertEqual(esto_debe_ser_false, False)
        
    def get_red_dos_switches(self):
        constructor_redes=simulador.ConstructorCuadradoCuatroLados()

        switch1=simulador.Switch("13", self.lista_grupo_1, [])
        switch2=simulador.Switch("5", self.lista_grupo_3, [])

        constructor_redes.asociar_puertos(self.puerto_01, self.puerto_1a)
        iteraciones=[simulador.Iteracion(switch1, self.puerto_01), 
                    simulador.Iteracion(switch2, self.puerto_1a)]
        
        constructor_redes.switches=[switch1, switch2]
        constructor_redes.iteraciones=iteraciones

    def test_menor_mac_1(self):
        switch=simulador.Switch("13", self.lista_todos_puertos, [])
        menor_mac=switch.get_menor_mac()
        self.assertEqual("01", menor_mac)
    
    def test_menor_mac_2(self):
        switch=simulador.Switch("13", self.lista_grupo_3, [])
        menor_mac=switch.get_menor_mac()
        self.assertEqual("1a", menor_mac)
    
    def test_prioridad_1(self):
        switch=simulador.Switch("13", self.lista_todos_puertos, [])
        prioridad=switch.identificador_yo
        self.assertEqual("13:01", prioridad)
    
    def test_ha_terminado_1(self):
        switch=simulador.Switch("13", self.lista_todos_puertos, [])
        estado=switch.ha_terminado()
        self.assertEqual(False, estado)

    def test_ha_terminado_2(self):
        switch=simulador.Switch("13", self.lista_todos_puertos, [])
        for p in switch.puertos:
            p.poner_bloqueado()

        estado=switch.ha_terminado()
        self.assertEqual(True, estado)
    
    def test_ha_terminado_3(self):
        switch=simulador.Switch("13", self.lista_todos_puertos, [])
        switch.puertos[0].poner_bloqueado()

        estado=switch.ha_terminado()
        self.assertEqual(False, estado)
    
class TestRed(unittest.TestCase):

    def setUp(self):
        self.puerto_01=simulador.Puerto("01")
        self.puerto_02=simulador.Puerto("02")

        self.puerto_0a=simulador.Puerto("0a")
        self.puerto_0b=simulador.Puerto("0b")

        self.puerto_1a=simulador.Puerto("1a")
        self.puerto_1b=simulador.Puerto("1b")
        
        self.lista_todos_puertos=[self.puerto_01, self.puerto_02,
                                    self.puerto_0a, self.puerto_0b,
                                    self.puerto_1a, self.puerto_1b,]
        self.lista_grupo_1=[self.puerto_01, self.puerto_02]

        self.lista_grupo_3=[self.puerto_1a, self.puerto_1b]

        return super().setUp()

    
    
    def testEnvio1(self):
        switch1=simulador.Switch("13", self.lista_grupo_1, [])
        switch2=simulador.Switch("5", self.lista_grupo_3, [])


class TestPuerto(unittest.TestCase):
    def setUp(self) -> None:
        self.puerto1=simulador.Puerto()
        self.puerto2=simulador.Puerto()
        return super().setUp()



if __name__=="__main__":
    unittest.main()