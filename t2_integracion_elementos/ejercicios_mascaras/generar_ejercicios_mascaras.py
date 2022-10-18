#!/usr/bin/python3
from utilidades.ip.ipv4 import GeneradorIPV4Azar

from random import randint


class GeneradorEjercicioMascaras(object):
    def __init__(self, num_ejercicio, tuplas) -> None:
        pass

    def get_cantidades_hosts_azar(self):
    
    def get_enunciado(self):
        texto="""
Ejercicio {3}
-------------------

Se dispone de dos máquinas:

* Una de ellas, que llamaremos máquina A, tiene la IP {0} con la máscara {1}.
* La otra, que llamaremos máquina B tiene la IP {2} con la máscara {3}.

En la máquina A alguien escribe el comando ``ping {3}``. ¿Funcionará dicho comando o no? 

"""

        enunciado=texto.format(
            self.generador_ips.direccion,
            self.total_subredes,
            self.total_hosts,
            self.num_ejercicio
        )
        return enunciado

    

    
    def get_solucion(self):
        inicio=f'Solución al ejercicio {self.num_ejercicio} de subredes\n----------------------------------------------------------------\n'\
            f'Nos dan el prefijo {self.generador_ips.direccion} (o poniendo la máscara vieja en decimal {self.mascara_vieja_en_decimal}) '\
            f'Nos piden {self.total_subredes} subredes con {self.total_hosts} hosts cada una. '
        #print("Diferencia:"+str(self.bits_para_las_subredes))
        subredes=self.get_lista_subredes()
        #print(subredes)
        encabezamiento=f'Para conseguir esta estructura usaremos {self.bits_para_las_subredes} bits de subred ' \
        f' y {self.bits_para_los_host} bits de host. La máscara nueva será {self.mascara_en_decimal} (en formato CIDR un prefijo/{self.bits_mascara})'\
            f' y el desglose de direcciones sería este:\n\n' 
        primera_subred=subredes[1]
        segunda_subred=subredes[2]
        ultima_subred=subredes[-2]
        txt_primera_subred=self.get_cadena_formato_red(primera_subred, "Primera")
        txt_segunda_subred=self.get_cadena_formato_red(segunda_subred, "Segunda")
        txt_ultima_subred=self.get_cadena_formato_red(ultima_subred, "Última")
        
        return inicio+encabezamiento + txt_primera_subred + txt_segunda_subred + txt_ultima_subred        

    def convertir_a_binario(self, numentero, anchura_bits):
        binario=bin(numentero)
        resultado=binario[2:].zfill(anchura_bits)
        #print("El resultado es:<"+resultado+">")
        return resultado
    
    def entrecomillar(self, cadena):
        return "``"+str(cadena)+"``"

    

    

if __name__=="__main__":
    ejercicios=[]
    
    MAX_EJERCICIOS=50


    encabezamiento="""
Anexo: ejercicios con máscaras
================================
"""
    print(encabezamiento)
    for i in range(1, MAX_EJERCICIOS):
        g=GeneradorEjercicio(i)
        ejercicios.append(g)
    for i in range(1, MAX_EJERCICIOS):
        g=ejercicios[i-1]
        print (g.get_enunciado())
        
    for i in range(1, MAX_EJERCICIOS):
        g=ejercicios[i-1]
        print (g.get_solucion())
        print (g.get_tablas())
