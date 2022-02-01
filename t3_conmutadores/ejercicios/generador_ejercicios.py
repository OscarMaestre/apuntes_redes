#!/usr/bin/python3
 
from utilidades.ip.ipv4 import GeneradorIPV4Azar

generador=GeneradorIPV4Azar(num_ejercicio=1)
direccion=generador.generar()
print(generador.convertir_a_decimal(direccion))
print(dir(generador.direccion))