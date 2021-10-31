#!/usr/bin/python3

from random import randint, random, seed
from dataclasses import dataclass
from pytablewriter import RstSimpleTableWriter
import subprocess

MAX_PUERTOS_SWITCH=8
UMBRAL_PROBABILIDAD_RELLENO_MACS=0.3

class GeneradorMACS(object):
    def __init__(self) -> None:
        self.lista_macs_generadas=[]
        seed()
    def generar_mac(self):
        num_mac=hex(randint(16,255))
        mac=str(num_mac)[2:].strip()
        while mac  in self.lista_macs_generadas:
            num_mac=hex(randint(16,255))
            mac=str(num_mac)[2:]
        self.lista_macs_generadas.append(mac)
        return mac

class Ordenador(object):
    def __init__(self):
        self.mac=GeneradorMACS().generar_mac()
    def __str__(self):
        return self.mac
    
class ListaMACS(object):
    def __init__(self):
        self.macs=[]
    def anadir_mac(self, mac):
        self.macs.append(mac)
    def es_vacia(self):
        if len(self.macs)==0:
            return True
        return False

    def __str__(self):
        lista=[" "+mac for mac in self.macs]
        return ",".join(lista)

class Switch(object):

    def __init__(self, nombre):
        self.puertos_fisicos=[]
        self.tabla_macs=[]
        self.nombre=nombre
        for i in range(0, MAX_PUERTOS_SWITCH):
            self.puertos_fisicos.append(None)
            self.tabla_macs.append(ListaMACS())
        self.generar_red()

    def get_lista_pcs(self):
        lista_pcs=[]
        for i in range(0, MAX_PUERTOS_SWITCH):
            elemento=self.puertos_fisicos[i]
            if elemento!=None:
                if isinstance(elemento, Ordenador):
                    lista_pcs.append(elemento)
        return lista_pcs

    def generar_aristas_grafo(self):
        aristas=[]
        formato_aristas="\"{0}\"--\"{1}\" [taillabel=\"{2}\"]"
        for i in range(0, MAX_PUERTOS_SWITCH):
            elemento=self.puertos_fisicos[i]
            if elemento!=None:
                if isinstance(elemento, Ordenador):
                    arista=formato_aristas.format(str(elemento), self.nombre, i)
                    aristas.append(arista)
        return aristas

    def get_num_puerto_fisico_libre_al_azar(self):
        encontrado_puerto_libre=False
        while not encontrado_puerto_libre:
            puerto=randint(0, MAX_PUERTOS_SWITCH-1)
            if self.puertos_fisicos[puerto]==None:
                encontrado_puerto_libre=True
                return puerto
    
    def get_puerto_pc_al_azar(self):
        while True:
            puerto=randint(0, MAX_PUERTOS_SWITCH-1)
            if self.puertos_fisicos[puerto]!=None:
                if isinstance(self.puertos_fisicos[puerto], Ordenador):
                    return puerto


    def get_pc_conectado_en_puerto(self, num_puerto):
        return self.puertos_fisicos[num_puerto]
    
    def get_mac_conectada_en_puerto(self, num_puerto):
        pc=self.get_pc_conectado_en_puerto(num_puerto)
        return pc.mac

    def get_mac_pc_al_azar(self):
        pc_al_azar=self.get_pc_al_azar
        return pc_al_azar.mac

    def get_pc_al_azar(self):
        pc_al_azar=self.get_puerto_pc_al_azar()
        return self.puertos_fisicos[pc_al_azar]

    def conectar_ordenador(self, pc):
        num_puerto_fisico=self.get_num_puerto_fisico_libre_al_azar()
        self.puertos_fisicos[num_puerto_fisico]=pc
        if random()>UMBRAL_PROBABILIDAD_RELLENO_MACS:
            #print("Añadiendo MAC")
            self.tabla_macs[num_puerto_fisico].anadir_mac(pc.mac)


    def generar_red(self, min_equipos=2, max_equipos=4):
        num_equipos=randint(min_equipos, max_equipos)
        for i in range(0, num_equipos):
            pc=Ordenador()
            self.conectar_ordenador(pc)
    
    def get_cad_pcs(self):
        pcs=[pc.mac for pc in self.puertos_fisicos if pc!=None and isinstance(pc, Ordenador)]
        texto=",".join(pcs)
        return "PCS:"+texto 
    
    def get_macs_str(self):
        lista=[]
        for num in range(0, MAX_PUERTOS_SWITCH-1):
            if not self.tabla_macs[num].es_vacia():
                lista.append("Puerto {0}: MAC {1}".format(num, str(self.tabla_macs[num])))
        texto=",".join(lista)
        return texto
    
    def conectar_switch(self, switch):
        puerto_libre=self.get_num_puerto_fisico_libre_al_azar()
        self.puertos_fisicos[puerto_libre]=switch
        #Miramos todos los PCs del switch conectado para ver si añadimos sus macs
        #a la lista de macs de este puerto
        pcs_nuevo_switch=switch.puertos_fisicos
        #print(pcs_nuevo_switch)
        for pc in pcs_nuevo_switch:
            if pc!=None and isinstance(pc, Ordenador) and random()>UMBRAL_PROBABILIDAD_RELLENO_MACS:
                #print("Añadiendo MAC de otro switch")
                self.tabla_macs[puerto_libre].anadir_mac(pc.mac)
        return puerto_libre

    def get_tabla_rst(self):
        tipos_cabeceras=["Numero de puerto", "Entradas MAC asociadas"]
        valores=[]
        num_puerto=0
        for lista_macs in self.tabla_macs:
            fila=[num_puerto, str(lista_macs)]
            valores.append(fila)
            num_puerto=num_puerto+1
        #print(valores)
        escritor_tablas=RstSimpleTableWriter(table_name="Tabla MAC de "+self.nombre,
        headers=tipos_cabeceras, value_matrix=valores)
        return str(escritor_tablas)

    
    def get_grafo_pcs(self):
        textos=[]
        lista_pcs=self.get_lista_pcs()
        formato_arista="\"{0}\" [shape=box]"
        for pc in lista_pcs:
            arista=formato_arista.format(pc.mac,)
            textos.append(arista)
        plantilla_grafo="""
    subgraph{{
        rankdir="LR"
    {0}
    }}
        """
        return plantilla_grafo.format("\n".join(textos))

    def get_grafo_pcs2(self):
        textos=[]
        formato_arista="\"{0}\"--\"{1}\" [taillabel=\"{2}\"]"
        for num_puerto in range(0, MAX_PUERTOS_SWITCH-1):
            nodo=self.puertos_fisicos[num_puerto]
            if nodo!=None:
                if isinstance(nodo, Ordenador):
                    arista=formato_arista.format(nodo.mac, self.nombre, num_puerto)
                    textos.append(arista)
        plantilla_grafo="""
    subgraph{{
        rankdir="LR"
    {0}
    }}
        """
        return plantilla_grafo.format("\n".join(textos))

    def __str__(self):
        return self.get_cad_pcs()+"\n"+self.get_macs_str()


class RedDosSwitches(object):
    def __init__(self):
        self.switch1=Switch("Switch 1")
        self.switch2=Switch("Switch 2")
        puerto_en_switch1=self.switch1.conectar_switch(self.switch2)
        puerto_en_switch1=self.switch2.conectar_switch(self.switch1)   
    
   

    def generar_aristas(self):
        aristas=[]
        formato_arista_switches="\"{0}\"--\"{1}\""
        arista_switches=formato_arista_switches.format(self.switch1.nombre,self.switch2.nombre)
        aristas.append(arista_switches)
        aristas=aristas+self.switch1.generar_aristas_grafo()
        aristas=aristas+self.switch2.generar_aristas_grafo()
        return aristas
        
        
    def generar_envio(self):
        if randint(0, 1)==0:
            self.switch_origen=1
            self.switch_destino=2
            self.emisor=self.switch1.get_puerto_pc_al_azar()
            self.receptor=self.switch2.get_puerto_pc_al_azar()
            self.mac_emisor=self.switch1.get_mac_conectada_en_puerto(self.emisor)
            self.mac_receptor=self.switch2.get_mac_conectada_en_puerto(self.receptor)
        else:
            self.switch_origen=2
            self.switch_destino=1
            self.emisor=self.switch2.get_puerto_pc_al_azar()
            self.receptor=self.switch1.get_puerto_pc_al_azar()
            self.mac_emisor=self.switch2.get_mac_conectada_en_puerto(self.emisor)
            self.mac_receptor=self.switch1.get_mac_conectada_en_puerto(self.receptor)

    def generar_imagen_grafo_red(self, num_ejercicio):
        grafo_pcs1=self.switch1.get_grafo_pcs()
        grafo_pcs2=self.switch2.get_grafo_pcs()
        lista_aristas   =self.generar_aristas()
        aristas="\n".join(lista_aristas)
        plantilla_grafo="""
graph Red{{
    size="18,21"
    rankdir="LR"
   
    {0}
    {1}
    {2}    
}}
"""
        grafo=plantilla_grafo.format(grafo_pcs1, grafo_pcs2, aristas)
        return grafo

    def generar_archivos_grafos(self, num_ejercicio):
        texto_grafo=self.generar_imagen_grafo_red(num_ejercicio)
        nombre_archivo="Grafo-{0:04}.dot".format(num_ejercicio)
        nombre_png="Grafo-{0:04}.png".format(num_ejercicio)
        with open(nombre_archivo, "w") as fich:
            fich.write(texto_grafo)
        with open(nombre_png, "w") as salida:
            ejecutar_dot=["dot", nombre_archivo, "-Tpng"]
            print("ejecutando..."+str(ejecutar_dot))
            subprocess.run(ejecutar_dot, stdout=salida)
        return nombre_png

    def get_enunciado(self, num_ejercicio):
        self.generar_envio()
        nombre_png=self.generar_archivos_grafos(num_ejercicio)
        plantilla="""
Ejercicio {0} de switches
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Dada la configuración que muestra la figura siguiente, en la que se muestran dos switches con ordenadores conectados a ciertos puertos y dadas las tablas MAC que se adjuntan indicar qué cosas pasarán si el ordenador con la MAC {1} intenta enviar un paquete al ordenador con la MAC {2}:

{3}

{4}

Posibilidades:

1. El switch {7} difunde el envío.
2. El switch {7} envía el mensaje solo por el puerto {5}
3. El switch {8} difunde el envío.
4. El switch {8} envía el mensaje solo por el puerto {6}

"""

        return plantilla.format(num_ejercicio, 
                    self.mac_emisor, 
                    self.mac_receptor,
                    self.switch1.get_tabla_rst(),
                    self.switch2.get_tabla_rst(),
                    self.emisor, self. receptor,
                    self.switch_origen, self.switch_destino
                    )

red=RedDosSwitches()
print(red.get_enunciado(1))