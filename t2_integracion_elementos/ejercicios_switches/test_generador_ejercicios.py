import unittest

import generador_ejercicios

class TestSwitch(unittest.TestCase):
    def test_switch_conoce_primera_mac_de_puerto(self):
        switch_i=generador_ejercicios.Switch()
        switch_i.anadir_entrada(1, "c583")
        switch_i.anadir_entrada(5, "a636")
        switch_i.anadir_entrada(6, "94bd")

        switch_d=generador_ejercicios.Switch()
        switch_d.anadir_entrada(2, "94bd")
        switch_d.anadir_entrada(4, "c583")
        
        
        lo_conoce=switch_d.conoce_a_mac("94bd")
        self.assertTrue(lo_conoce)
    
    def test_switch_conoce_segunda_mac_de_puerto(self):
        switch_i=generador_ejercicios.Switch()
        switch_i.anadir_entrada(6, "5b8a")

        switch_d=generador_ejercicios.Switch()
        switch_d.anadir_entrada(1, "720f")
        switch_d.anadir_entrada(4, "5136")
        switch_d.anadir_entrada(5, "6866")
        
        lo_conoce=switch_d.conoce_a_mac("6866")
        self.assertTrue(lo_conoce)
    
    
    
        
if __name__=="__main__":
    unittest.main()