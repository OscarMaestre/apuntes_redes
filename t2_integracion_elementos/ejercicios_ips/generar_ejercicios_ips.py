#!/usr/bin/python3

from random import randint, random, seed, choice
from dataclasses import dataclass
from pytablewriter import RstSimpleTableWriter
import ipaddress

class DireccionIP(object):

    def get_enunciado(self):
        pass
    def get_enunciado_con_respuesta(self):
        pass

class DireccionIPv4(DireccionIP):
    def __init__(self):
        super().__init__()

@dataclass
class BloqueIPv6(object):
    nombre:str
    primer_hexteto:int
    ultimo_hexteto:int
    bits_prefijo:int
    @staticmethod
    def get_bloques():
        bloques=[]
        #Unicast global
        bloque1=BloqueIPv6(nombre="Unicast global", 
                        primer_hexteto=0x2000, 
                        ultimo_hexteto=0x3fff, 
                        bits_prefijo=3)
        bloque2=BloqueIPv6(nombre="Unicast local único", 
                        primer_hexteto=0xfc00, 
                        ultimo_hexteto=0xfdff, 
                        bits_prefijo=7)
        bloque3=BloqueIPv6(nombre="Unicast local en enlace", 
                        primer_hexteto=0xfe80, 
                        ultimo_hexteto=0xfebf, 
                        bits_prefijo=10)
        bloque4=BloqueIPv6(nombre="Multicast", 
                        primer_hexteto=0xff00, 
                        ultimo_hexteto=0xffff, 
                        bits_prefijo=8)
        bloques.append(bloque1)
        bloques.append(bloque2)
        bloques.append(bloque3)
        bloques.append(bloque4)
        return bloques
                
class DireccionIPv6(DireccionIP):
    def __init__(self):
        super().__init__()
        self.ip=""
        self.bloque_asociado=None
        ipv6=self.generar_ipv6()
        self.ip=self.comprimir_ipv6(ipv6)

    def formatear_bloque(self, bloque):
        cadena_hex_python="{0:04x}".format(bloque)
        return cadena_hex_python

    def generar_bloque_hexadecimal(self):
        #Decidimos si sacamos un bloque de ceros o no
        #En principio sacamos un cero
        numero_sacado=0
        if randint(0,1)==0:
            #Y si el azar dice otra cosa, cambiamos el numero
            numero_sacado=randint(0,65535)
        return self.formatear_bloque(numero_sacado)

    def generar_bloque_hexadecimal_dentro_de_rango(self, minimo, maximo):
        numero=randint(minimo, maximo)
        
        return self.formatear_bloque(numero)

    def generar_primer_bloque(self):
        bloques=BloqueIPv6.get_bloques()
        bloque_al_azar=choice(bloques)
        self.bloque_asociado=bloque_al_azar
        primer_bloque=self.generar_bloque_hexadecimal_dentro_de_rango(
            bloque_al_azar.primer_hexteto, bloque_al_azar.ultimo_hexteto
        )
        return primer_bloque


    def generar_ipv6(self):
        lista_bloques=[]
        primer_bloque=self.generar_primer_bloque()
        lista_bloques.append(primer_bloque)

        for i in range(1, 8):
            bloque=self.generar_bloque_hexadecimal()
            lista_bloques.append(bloque)
        ip=":".join(lista_bloques)
        return ip
    def comprimir_ipv6(self, ipv6):
        objeto_ip=ipaddress.ip_address(ipv6)
        return objeto_ip.compressed

    def get_enunciado(self, num_enunciado):
        formato="{1}. ``{0}``"
        return formato.format(self.ip, num_enunciado)

    def get_enunciado_con_respuesta(self, num_enunciado):
        formato="{2}. ``{0}`` es de tipo {1}"
        nombre_bloque=self.bloque_asociado.nombre.lower()
        return formato.format(self.ip, nombre_bloque, num_enunciado)

MAX_EJERCICIOS=50
ips=[]
texto_enunciados=[]
texto_enunciados_con_respuesta=[]
num_enunciado=1
for i in range(0, MAX_EJERCICIOS):    
    ipv6=DireccionIPv6()
    ips.append(ipv6)
    texto_enunciados.append(ipv6.get_enunciado(num_enunciado))
    texto_enunciados_con_respuesta.append(ipv6.get_enunciado_con_respuesta(num_enunciado))
    num_enunciado=num_enunciado+1

texto_anexo="""
Anexo: ejercicios sobre clasificación de direcciones IPv6
------------------------------------------------------------

Dadas las siguientes direcciones IPv6 indica de qué tipo son:

{0}

Soluciones a la clasificaciones de direcciones IPv6
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

{1}
"""

anexo=texto_anexo.format(
    "\n".join(texto_enunciados),
    "\n".join(texto_enunciados_con_respuesta)
)

print(anexo)