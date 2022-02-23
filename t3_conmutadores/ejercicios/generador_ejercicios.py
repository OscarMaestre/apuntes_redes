#!/usr/bin/python3

from utilidades.cisco.GeneradorEjercicioSwitches import GeneradorEjercicioSwitches    

ejercicios=[]

for i in range(1, 7):
    for j in range(1, 5):
        g=GeneradorEjercicioSwitches ()
        g.generar_ejercicio(i)
        ejercicios.append(g)

contador=1

encabezado="""
Anexo al tema 3: Ejercicios sobre comandos Cisco en switches
--------------------------------------------------------------------
"""



print (encabezado)
for e in ejercicios:
    print("\nEjercicio {0} de switches".format(contador))
    print(50*"~")
    print(e.get_enunciado())
    contador+=1

contador=1
for e in ejercicios:
    print("\nSolución al ejercicio {0} de switches".format(contador))
    print(50*"~")
    print(e.get_solucion())
    contador+=1