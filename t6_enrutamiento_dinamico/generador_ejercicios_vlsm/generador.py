#!/usr/bin/python3

from dataclasses import dataclass
from ipaddress import IPv4Network
from utilidades.ip.VLSM import VLSM, SolucionVLSM
from random import randint
from typing import List

PREFIJO="10.1.0.0/16"

ENCABEZADO="""
Anexo:Ejercicios VLSM
========================
En los ejercicios siguientes se plantean diversos problemas sobre VLSM. Para facilitar la operación todas los enunciados usan el mismo prefijo y se puede confiar en que todos los problemas tienen solución. Las soluciones a todos los ejercicios pueden encontrarse al final.

"""

SOLUCIONES_VLSM="""


Soluciones ejercicios VLSM
------------------------------
A continuación se pueden encontrar los enunciados VLSM propuestos junto con sus soluciones.

"""
PLANTILLA_ENUNCIADO_VLSM="""
Ejercicio VLSM {0}
-----------------------------
"""

PLANTILLA_SOLUCION_VLSM="""
Solución ejercicio  VLSM {0}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

@dataclass
class Ejercicio(object):
    lista_hosts:List[int]
    soluciones: List[SolucionVLSM]
    def get_enunciado(self):
        hosts=str(self.lista_hosts)
        enunciado="Se parte del prefijo {0} y de las siguientes subredes donde indicamos las cantidades de host: {1}. Se pide crear un esquema de direccionamiento VLSM que permita aprovechar al máximo las direcciones IP."
        return enunciado.format(PREFIJO, hosts)

    def get_solucion_rst(self):
        lista=[]
        for sol in self.soluciones:
            lista.append(sol.get_rst())
        return "\n".join(lista)

    

class GeneradorEjerciciosVLSM(object):
    @staticmethod
    def generar_lista_hosts():
        cantidad_subredes=randint(4, 6)
        cantidades_hosts=[]
        for subredes in range(0, cantidad_subredes):
            num_hosts_azar=randint(3, 95)
            cantidades_hosts.append(num_hosts_azar)
        #print (cantidades_hosts)
        return cantidades_hosts

    @staticmethod
    def generar_ejercicios(cantidad):
        ejercicios=[]
        for num_ejercicio in range(1, cantidad+1):
            lista_hosts=GeneradorEjerciciosVLSM.generar_lista_hosts()
            vlsm=VLSM(lista_hosts, IPv4Network(PREFIJO))
            ejercicio=Ejercicio(lista_hosts, vlsm.soluciones)
            ejercicios.append(ejercicio)
        return ejercicios

class FormateadorEjercicios(object):
    @staticmethod
    def formatear(ejercicios):
        archivo_texto=""
        textos=[]
        soluciones=[]
        for pos, valor in enumerate(ejercicios):
            encabezado=PLANTILLA_ENUNCIADO_VLSM.format(pos+1)
            enunciado=valor.get_enunciado()
            textos.append(encabezado+enunciado)
            encabezado_solucion=PLANTILLA_SOLUCION_VLSM.format(pos+1)
            soluciones.append(encabezado_solucion + "\n\n"+enunciado+"\n\n"+valor.get_solucion_rst())
        archivo_texto+=ENCABEZADO + "\n\n" + "\n\n".join(textos) + SOLUCIONES_VLSM + "\n\n" + "\n\n".join(soluciones)
        return archivo_texto

def guardar_texto_en_archivo(texto, nombre_archivo):
    with open(nombre_archivo, "w") as fich:
        fich.write(texto)
    
if __name__=="__main__":
    lista=GeneradorEjerciciosVLSM.generar_ejercicios(30)
    texto=FormateadorEjercicios.formatear(lista)
    guardar_texto_en_archivo(texto, "EjerciciosVLSM.rst")