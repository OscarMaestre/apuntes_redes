#!/usr/bin/python3

from random import randint, random, seed, choice
from dataclasses import dataclass
import ipaddress

class Generador(object):
    def __init__(self, num_ejercicio) -> None:
        self.primer_byte=randint(8, 52)
        self.bits_mascara=randint(10, 30)
        self.direccion=ipaddress.IPv4Network(
            str(self.primer_byte)+".0.0.0/"+str(self.bits_mascara)
        )
        self.num_ejercicio=num_ejercicio
        #print (self.direccion)
    
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
Ejercicio {0}
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