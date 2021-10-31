#!/usr/bin/python3

from random import randint, random, seed
from dataclasses import dataclass
from pytablewriter import RstSimpleTableWriter

class GeneradorMACS(object):
    def __init__(self) -> None:
        self.lista_macs_generadas=[]
    def generar_mac(self):
        num_mac=hex(randint(16,255))
        mac=str(num_mac)[2:].strip()
        while mac  in self.lista_macs_generadas:
            num_mac=hex(randint(16,255))
            mac=str(num_mac)[2:]
        self.lista_macs_generadas.append(mac)
        return mac

@dataclass
class Ordenador(object):
    mac:str
    def set_puerto_switch(self, puerto):
        self.puerto=puerto

    

class Switch(object):
    def __init__(self) -> None:
        super().__init__()
        self.tabla_mac=[]
        self.MAX_PUERTOS=8
        for i in range(0, self.MAX_PUERTOS):
            self.tabla_mac.append([])

    def get_num_puerto_azar(self):
        num=randint(0, self.MAX_PUERTOS-1)
        return num
    def set_nombre(self, nombre):
        self.nombre=nombre

    def anadir_entrada(self, puerto, mac):
        self.tabla_mac[puerto].append(mac)

    

    def anadir_entrada_azar(self, mac):
        puerto=self.get_num_puerto_libre_azar()
        self.anadir_entrada(puerto, mac)

    def get_num_puerto_libre_azar(self):
        encontrado_puerto_libre=False
        while not encontrado_puerto_libre:
            puerto=randint(0, self.MAX_PUERTOS-1)
            if self.tabla_mac[puerto]==[]:
                encontrado_puerto_libre=True
                return puerto

    def anadir_entrada_a_puerto_libre(self, mac, puerto_a_excluir):
        puerto=self.get_num_puerto_azar()
        while puerto==puerto_a_excluir:
            puerto=self.get_num_puerto_azar()
        self.anadir_entrada(puerto, mac)

    def __str__(self) -> str:
        aux=""
        for i in self.tabla_mac:
            aux=aux+"Entrada:"+i
        return aux
    
    def get_puerto_asociado(self, mac_buscada):
        num_puerto=0
        for entrada in self.tabla_mac:
            for mac in entrada:
                if mac_buscada==mac:
                    return num_puerto
            num_puerto=num_puerto+1
        return -1

    def get_tabla_rst(self):
        tipos_cabeceras=["Numero de puerto", "MAC"]
        valores=[]
        num_puerto=0
        for p in self.tabla_mac:
            if p==[]:
                fila=[num_puerto, ""]
            else:
                fila=[num_puerto, ",".join(p)]

            valores.append(fila)
            num_puerto=num_puerto+1
        escritor_tablas=RstSimpleTableWriter(table_name="Tabla MAC de "+self.nombre,
        headers=tipos_cabeceras, value_matrix=valores)
        return str(escritor_tablas)

def get_aristas_switch_izq():
    pass
def get_grafo_dos_switches():
    grafo="""
    subgraph {
        rankdir="LR";
        switch1 [shape=box]
        switch2 [shape=box]  
    }
    """
    return grafo

def get_grafo_pcs(vector_pcs):
    lista_nodos=["\t\"{0}\" [shape=box]".format(pc.mac) for pc in vector_pcs]
    nodos_pcs="\n".join(lista_nodos)
    plantilla_grafo="""
    subgraph{{
        rankdir="LR"
{0}
    }}
    """
    return plantilla_grafo.format(nodos_pcs)


def get_mac_azar_vector_pcs(vector_pcs):
    pos_azar=randint(0, len(vector_pcs)-1)
    pc=vector_pcs[pos_azar]
    return pc.mac

def generar_ejercicio_dos_switches(nombre_archivo):
    seed()
    generador=GeneradorMACS()
    switch1=Switch()
    switch2=Switch()
    
    switch1.set_nombre("Switch 1")
    switch2.set_nombre("Switch 2")
    #Generamos un grupo de equipos
    num_equipos=randint(2, 4)
    macs=[]
    pcs1=[]
    
    puerto_switch1=switch1.get_num_puerto_libre_azar()
    puerto_switch2=switch2.get_num_puerto_libre_azar()
    mensaje_union="El switch 1 tiene un cable en el puerto {0} que va al puerto {1} del switch 2".format(puerto_switch1, puerto_switch2)
    print (mensaje_union)
    
    for i in range(0, num_equipos):
        mac_azar=generador.generar_mac()
        macs.append(mac_azar)
        pc=Ordenador("")
        pc.mac=mac_azar
        pcs1.append(pc)
        #Decidimos al azar si añadimos la MAC de ese PC al switch1
        if random()>0.30:
            switch1.anadir_entrada_a_puerto_libre(mac_azar, puerto_switch1)
            #print("Añadiendo {0} al switch 1".format(mac_azar))
        else:
            #print("NO añadiendo {0} al switch 1".format(mac_azar))
            pass
        #Y hacemos lo mismo con el switch 2
        if randint(0, 1)==0:
            switch2.anadir_entrada(puerto_switch2, mac_azar)
            #print("Añadiendo {0} al switch 2".format(mac_azar))
        else:
            pass
            #print("NO añadiendo {0} al switch 2".format(mac_azar))

    #Generamos un grupo de equipos
    num_equipos=randint(2, 4)
    macs=[]
    pcs2=[]
    
    for i in range(0, num_equipos):
        mac_azar=generador.generar_mac()
        macs.append(mac_azar)
        pc=Ordenador("")
        pc.mac=mac_azar
        pcs2.append(pc)
        #Decidimos al azar si añadimos la MAC de ese PC al switch1
        if randint(0, 1)==0:
            switch1.anadir_entrada(puerto_switch1, mac_azar)
        #Y hacemos lo mismo con el switch 2
        if random()>0.3:
            switch2.anadir_entrada_a_puerto_libre(mac_azar, puerto_switch2)


   


    #Elegimos un sentido de envío
    origen=""
    destino=""
    if randint(0, 1)==0:
        origen=get_mac_azar_vector_pcs(pcs1)
        destino=get_mac_azar_vector_pcs(pcs2)
    else:
        origen=get_mac_azar_vector_pcs(pcs2)
        destino=get_mac_azar_vector_pcs(pcs1)
    mensaje="Enviar desde {0} a {1}".format(origen, destino)
    
    print(pcs1)
    print(switch1.get_tabla_rst())
    print(pcs2)
    print(switch2.get_tabla_rst())

    print(mensaje)

    nodos_pcs1=get_grafo_pcs(pcs1)
    print(nodos_pcs1)
    nodos_pcs2=get_grafo_pcs(pcs2)
    print(nodos_pcs2)
    

generar_ejercicio_dos_switches("P1.png")