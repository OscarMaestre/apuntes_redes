#!/usr/bin/python3
from utilidades.ip.ipv4 import GeneradorIPV4Azar
import ipaddress

from random import randint


class GeneradorEjercicioMascaras(object):
    def __init__(self, num_ejercicio) -> None:
        self.num_ejercicio=num_ejercicio
        byte1=randint(10,125)
        byte2=randint(3,254)
        bits_mascara=randint(16,30)
        cad_red="{0}.{1}.0.0/{2}".format(byte1, byte2, bits_mascara)
        red_azar=ipaddress.ip_network(cad_red)
        todos_hosts=red_azar.hosts()
        #El tipo de ejercicio 0 es en el que están
        #en la misma red. El tipo 1 es en distinta red
        self.tipo_ejercicio=randint(0, 1)
        self.primera_ip=list(todos_hosts)[0]
        self.mascara1=red_azar.netmask
        if self.tipo_ejercicio==0:
            todos_hosts=red_azar.hosts()
            self.segunda_ip=list(todos_hosts)[-1]
        if self.tipo_ejercicio==1:
            todos_hosts=red_azar.hosts()
            self.segunda_ip=list(todos_hosts)[-1]+3
    def get_cantidades_hosts_azar(self):
        pass
    def get_enunciado(self):
        texto="""
Ejercicio {4}
-------------------

Se dispone de dos máquinas:

* Una de ellas, que llamaremos máquina A, tiene la IP {0} con la máscara {1}.
* La otra, que llamaremos máquina B tiene la IP {2} con la máscara {3}.

En la máquina A alguien escribe el comando ``ping {2}``. ¿Funcionará dicho comando o no? 

"""

        enunciado=texto.format(
            self.primera_ip,self.mascara1, self.segunda_ip,self.mascara1,
            self.num_ejercicio
        )
        return enunciado

    def get_descripcion_maquina(self, direccion, mascara):
        generador=GeneradorIPV4Azar(self.num_ejercicio)
        direccion_binario=generador.get_direccion_en_binario(direccion)
        mascara_binaria=generador.get_direccion_en_binario(mascara)

    
    def get_solucion(self):
        plantilla="""
Solución al ejercicio {0}
----------------------------------------
Recordemos:

* La máquina A tiene la IP {1} con la máscara {2}.
* La máquina B tiene la IP {3} con la máscara {4}.

En la máquina A alguien escribe el comando ``ping {3}`` y nos preguntan si funcionará.

{5}

        """
        if self.tipo_ejercicio==0:
            self.solucion="La respuesta es que ``ping {3}`` **sí funciona porque ambos están en la misma red."
        if self.tipo_ejercicio==1:
            self.solucion="La respuesta es que ``ping {3}`` **no funciona porque las máquinas están en una red distinta."
        return plantilla.format(self.num_ejercicio,
                    self.primera_ip,self.mascara1, self.segunda_ip,self.mascara1,
                    self.solucion)

    def convertir_a_binario(self, numentero, anchura_bits):
        binario=bin(numentero)
        resultado=binario[2:].zfill(anchura_bits)
        #print("El resultado es:<"+resultado+">")
        return resultado
    
    def entrecomillar(self, cadena):
        return "``"+str(cadena)+"``"

    

    

if __name__=="__main__":
    ejercicios=[]
    
    MAX_EJERCICIOS=51


    encabezamiento="""
Anexo: ejercicios con máscaras
================================
"""
    print(encabezamiento)
    for i in range(1, MAX_EJERCICIOS):
        g=GeneradorEjercicioMascaras(i)
        ejercicios.append(g)
    for i in range(1, MAX_EJERCICIOS):
        g=ejercicios[i-1]
        print (g.get_enunciado())
        
    for i in range(1, MAX_EJERCICIOS):
        g=ejercicios[i-1]
        print (g.get_solucion())
        
