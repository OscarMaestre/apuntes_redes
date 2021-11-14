#!/usr/bin/python3

from random import randint, random, seed, choice
from dataclasses import dataclass
import ipaddress
from utilidades.ip.ipv4 import GeneradorIPV4Azar

class Generador(GeneradorIPV4Azar):


    def get_enunciado(self):
        plantilla="""
Ejercicio {0}
-----------------------------
Obtener el rango de direcciones posible para {1}
"""
        return plantilla.format(self.num_ejercicio, self.direccion)

    def get_solucion(self):
        direccion_red=self.direccion.network_address
        direccion_broadcast=self.direccion.broadcast_address
        hosts=list(self.direccion.hosts())
        plantilla="""
Solución al ejercicio {0}
-----------------------------
Para el enunciado *"Obtener el rango de direcciones posible para {1}"*, la solución sería:

1. La primera IP, que sería la IP de la red, sería {2}
2. La primera IP asignable sería la {3}
3. La última IP asignable sería la {4}
4. La última IP, que sería la de difusión, sería {5}
"""
        return plantilla.format(self.num_ejercicio, 
            self.direccion, direccion_red, hosts[0],
            hosts[-1], direccion_broadcast)



if __name__=="__main__":
    print("Anexo: ejercicios sobre rangos de direcciones")
    print("===================================================")
    MAX_EJERCICIOS=51
    ejercicios=[]
    for i in range(1, MAX_EJERCICIOS):
        ejercicio=Generador(i)
        ejercicios.append(ejercicio)

    for i in range(1, MAX_EJERCICIOS):
        print(ejercicios[i-1].get_enunciado())

    for i in range(1, MAX_EJERCICIOS):
        print(ejercicios[i-1].get_solucion())