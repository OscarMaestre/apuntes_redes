#!/usr/bin/python3

from random import randint, random, seed, choice
from dataclasses import dataclass
import ipaddress

class Generador(object):

    def __init__(self, num_ejercicio) -> None:
        self.primer_byte=randint(8, 52)
        self.bits_mascara=randint(10, 30)
        #print("Mascara:/"+str(self.bits_mascara))
        self.bits_host=32-self.bits_mascara
        self.secuencia_binaria=self.generar()
        #print(self.secuencia_binaria)
        bytes_ip=[]
        for i in range(0, 4):
            #print("Trozo:"+str(i))
            li=i*8
            ls=li+8
            trozo=int(self.secuencia_binaria[li:ls], 2)
            bytes_ip.append(str(trozo))
        #print(bytes_ip)
        self.cadena=".".join(bytes_ip)
        #print(self.cadena)
        self.direccion=ipaddress.IPv4Network(
            self.cadena+"/"+str(self.bits_mascara)
        )
        self.num_ejercicio=num_ejercicio
        #print (self.direccion)

    def generar(self):
        
        posibles_generadores=[]
        bits_host="0"*self.bits_host
        if self.bits_mascara>=24:
            posibles_generadores=[
                self.generar_clase_a, self.generar_clase_b,self.generar_clase_c]
            generador=choice(posibles_generadores)
            return generador(self.bits_mascara)+bits_host
        if self.bits_mascara>=16:
            posibles_generadores=[
                self.generar_clase_a, self.generar_clase_b]
            generador=choice(posibles_generadores)
            return generador(self.bits_mascara)+bits_host
        if self.bits_mascara>=8:
            posibles_generadores=[
                self.generar_clase_a]
            generador=choice(posibles_generadores)
            return generador(self.bits_mascara)+bits_host
            
    def generar_clase_a(self, num_bits):
        return "0"+self.get_secuencia_azar_bits(num_bits-1)
    def generar_clase_b(self, num_bits):
        return "10"+self.get_secuencia_azar_bits(num_bits-2)
    def generar_clase_c(self, num_bits):
        return "110"+self.get_secuencia_azar_bits(num_bits-3)
    
    def get_bit(self):
        return choice(["0", "1"])

    def get_secuencia_azar_bits(self, num_bits):
        cadena=""
        for i in range(0, num_bits):
            cadena=cadena+self.get_bit()
        return cadena   
 
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