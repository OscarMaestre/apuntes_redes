#!/usr/bin/python3

from random import randint, random, seed, shuffle, choices, choice, sample
from dataclasses import dataclass
from pytablewriter import RstSimpleTableWriter

class GeneradorMACS(object):
    def __init__(self) -> None:
        self.lista_macs_generadas=[]
    def generar_mac(self):
        num_mac=hex(randint(16384,65535))
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
    def __str__(self) -> str:
        return "PC con MAC {0} en puerto {1}".format(self.mac,self.puerto)



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
                if mac.find(mac_buscada)!=-1:
                    return num_puerto
            num_puerto=num_puerto+1
        return -1

    def conoce_a_mac(self, mac_buscada):
        if self.get_puerto_asociado(mac_buscada)==-1:
            return False
        return True

    def get_tabla_rst(self):
        tipos_cabeceras=["Numero de puerto", "MAC"]
        valores=[]
        num_puerto=0
        for p in self.tabla_mac:
            if p==[]:
                fila=[num_puerto, "--"]
            else:
                fila=[num_puerto, "``"+",".join(p)+"``"]

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

def formatear_pcs(lista_pcs, sufijo):
    lineas=[]
    plantilla="* Ordenador {0} tiene la MAC ``{1}``."
    pos=1
    for pc in lista_pcs:
        linea=plantilla.format(str(pos)+sufijo, pc.mac)
        lineas.append(linea)
        pos=pos+1
    return "\n".join(lineas)


class GeneradorEjercicios(object):
    def __init__(self, num_ejercicio) -> None:
        self.num_ejercicio=num_ejercicio

    def get_tuplas_respuestas_switch(self, switch, mac_origen, mac_destino):
        vector_tuplas_respuestas=[]
        nombre_switch1=switch.nombre
        
        

        #Caso 1 ¿El switch 1 conoce al destinatario?
        puerto_asociado_en_switch1=switch.get_puerto_asociado(mac_destino)
        txt_respuesta1="El {0} envía el mensaje por el puerto {1}."
        txt_respuesta2="El {0} envía el mensaje por todos los puertos menos por donde vino."
        if switch.conoce_a_mac(mac_destino):
            tupla1=(txt_respuesta1.format(nombre_switch1, puerto_asociado_en_switch1), 
                    True,
                    ", ``{0}`` está en esa posición en la tabla de MACs".format(mac_destino))
            tupla2=(txt_respuesta2.format(nombre_switch1), False,
                    " no necesita hacer difusión, tiene la MAC de destino ``{0}`` en su tabla, en el puerto {1}.".format(mac_destino, puerto_asociado_en_switch1))
            vector_tuplas_respuestas.append(tupla1)
            vector_tuplas_respuestas.append(tupla2)
        else:
            otro_puerto=switch.get_num_puerto_libre_azar()
            tupla1=(txt_respuesta1.format(nombre_switch1, otro_puerto), False,
            ", no conoce a la MAC de destino ``{0}``, así que necesita difundir.".format(mac_destino))
            tupla2=(txt_respuesta2.format(nombre_switch1), True,
            ", necesita hacerlo porque no tiene la MAC de destino ``{0}`` en su tabla".format(mac_destino))
            vector_tuplas_respuestas.append(tupla1)
            vector_tuplas_respuestas.append(tupla2)

        #Caso 2 ¿El switch 1 conoce al emisor?
        puerto_asociado_en_switch1=switch.get_puerto_asociado(mac_origen)
        txt_respuesta1="El {0} apunta en su tabla de MACS  la MAC de origen ``{1}``."
        txt_respuesta2="El {0} no modifica su tabla de MACS, no aprende nada nuevo."
        if switch.conoce_a_mac(mac_origen):
            tupla1=(txt_respuesta1.format(nombre_switch1, mac_origen), False,
            ", ya tenía esa MAC")
            tupla2=(txt_respuesta2.format(nombre_switch1), False,
            ", sí la modifica, no tenía la MAC de origen ``{0}``.".format(mac_origen))
            vector_tuplas_respuestas.append(tupla1)
            vector_tuplas_respuestas.append(tupla2)
        else:
            otro_puerto=switch.get_num_puerto_libre_azar()
            tupla1=(txt_respuesta1.format(nombre_switch1, mac_origen, otro_puerto), True,
            ", antes no lo conocía, así que sí anota la MAC de origen ``{0}``.".format(mac_origen))
            tupla2=(txt_respuesta2.format(nombre_switch1), False,
            ", no conocía la MAC de origen ``{0}``, así que la anota.".format(mac_origen))
            vector_tuplas_respuestas.append(tupla1)
            vector_tuplas_respuestas.append(tupla2)

        #Fin de la generacion
        shuffle(vector_tuplas_respuestas)
     
        return vector_tuplas_respuestas

    def generar_vector_respuestas(self, mac_origen, mac_destino, switch1, switch2):
        
        vector1=self.get_tuplas_respuestas_switch(switch1, mac_origen, mac_destino)
        vector2=self.get_tuplas_respuestas_switch(switch2, mac_origen, mac_destino)
        vector_respuestas=vector1+vector2
        self.vector_respuestas=vector_respuestas
        shuffle(self.vector_respuestas)
        
        return self.vector_respuestas

            
    def get_respuestas_sin_solucion(self):
        vector_con_numero_de_orden=[]
        for pos in range(0, len(self.vector_respuestas)):
            (txt, respuesta, causa)=self.vector_respuestas[pos]
            vector_con_numero_de_orden.append(
                (str(pos+1)+". "+txt, respuesta, causa)
            )
        lineas=[texto for texto,respuesta, causa in vector_con_numero_de_orden]
        return "\n".join(lineas)

    def get_respuestas_con_solucion(self):
        vector_con_numero_de_orden=[]
        for pos in range(0, len(self.vector_respuestas)):
            (txt, respuesta, causa)=self.vector_respuestas[pos]
            vector_con_numero_de_orden.append(
                (str(pos+1)+". "+txt, respuesta, causa)
            )
        lineas=[]
        for texto,respuesta, causa in vector_con_numero_de_orden:
            if respuesta==True:
                lineas.append(texto+" **Verdadera**"+causa)
            else:
                lineas.append(texto+" **Falsa**"+causa)
        return "\n".join(lineas)

    def generar_ejercicio_dos_switches(self, solucion=False):
        
        generador=GeneradorMACS()
        switch1=Switch()
        switch2=Switch()
        
        switch1.set_nombre("Switch 1")
        switch2.set_nombre("Switch 2")
        #Generamos un grupo de equipos
        num_equipos1=randint(2, 3)
        macs=[]
        pcs1=[]
        
        puerto_switch1=switch1.get_num_puerto_libre_azar()
        puerto_switch2=switch2.get_num_puerto_libre_azar()
        switch1.anadir_entrada_a_puerto_libre("Switch 2", puerto_switch1)
        switch2.anadir_entrada_a_puerto_libre("Switch 1", puerto_switch2)
        mensaje_union="Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto {0} que va al puerto {1} del switch 2".format(puerto_switch1, puerto_switch2)
        
        
        #Esta es la red izquierda
        for i in range(0, num_equipos1):
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
        num_equipos2=randint(2, 4)
        macs=[]
        pcs2=[]
        
        for i in range(0, num_equipos2):
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
        #Fin del for

        nombre_de_fichero="Switches{0}-{1}.png".format(num_equipos1, num_equipos2)

        if solucion==False:
            plantilla_cabecera="""
Ejercicio {0} de switches
----------------------------------
"""
        else:
            plantilla_cabecera="""
Solución al ejercicio {0} de switches
------------------------------------------
"""
                        
        mensaje=mensaje_union+". Se pretende enviar desde ``{0}`` a ``{1}`` sabiendo lo siguiente:\n".format(origen, destino)
        datos_ordenadores_izq=formatear_pcs(pcs1, "I")
        datos_ordenadores_der=formatear_pcs(pcs2, "D")

        plantilla_enunciado="""
{0}
{1}

.. figure:: {6}

{2}
{3}

{4}

{5}

"""
        self.enunciado=plantilla_enunciado.format(
            plantilla_cabecera.format(self.num_ejercicio),
            mensaje,
            datos_ordenadores_izq,
            datos_ordenadores_der,
            switch1.get_tabla_rst(),
            switch2.get_tabla_rst(), nombre_de_fichero
        )
        
        self.generar_vector_respuestas(origen, destino,switch1, switch2)
        #print(self.vector_respuestas)




class GeneradorEjerciciosV2(GeneradorEjercicios):
    def __init__(self, num_ejercicio) -> None:
        super().__init__(num_ejercicio)
    
    def generar_lista_pcs_azar(self):
        generador=GeneradorMACS()
        pcs=[]
        num_equipos=randint(2, 4)
        for i in range(0, num_equipos):
            mac_azar=generador.generar_mac()
            pc=Ordenador(mac=mac_azar)
            pcs.append(pc)
        return pcs

    def asignar_pcs_remotos_en_puerto_switch_al_azar(self, switch, lista_pcs_remotos, puerto):
        for pc in lista_pcs_remotos:
            if random()<0.3:
                switch.anadir_entrada(puerto,pc.mac)

    def asignar_pcs_locales_en_switch(self, switch, lista_pcs):
        for pc in lista_pcs:
            if random()<0.4:
                switch.anadir_entrada_azar(pc.mac)

    def get_origen_y_destino(self, listas_pcs):
        lista_origen_y_destino=sample(listas_pcs, k=2)
        pc_origen=choice(lista_origen_y_destino[0])
        pc_destino=choice(lista_origen_y_destino[1])
        return (pc_origen.mac, pc_destino.mac)

    def generar_ejercicio_dos_switches(self, solucion=False):
        
        generador=GeneradorMACS()
        switch1=Switch()
        switch2=Switch()
        
        switch1.set_nombre("Switch 1")
        switch2.set_nombre("Switch 2")
        #Generamos un grupo de equipos
        
        pcs1=self.generar_lista_pcs_azar()
        pcs2=self.generar_lista_pcs_azar()
        
        puerto_switch1=switch1.get_num_puerto_libre_azar()
        puerto_switch2=switch2.get_num_puerto_libre_azar()
        #switch1.anadir_entrada_a_puerto_libre("Switch 2", puerto_switch1)
        #switch2.anadir_entrada_a_puerto_libre("Switch 1", puerto_switch2)
        mensaje_union="Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto {0} que va al puerto {1} del switch 2".format(puerto_switch1, puerto_switch2)
        
        self.asignar_pcs_remotos_en_puerto_switch_al_azar(
            switch1, pcs2, puerto_switch1
        )
        self.asignar_pcs_remotos_en_puerto_switch_al_azar(
            switch2, pcs1, puerto_switch2
        )
        self.asignar_pcs_locales_en_switch(switch1, pcs1)
        self.asignar_pcs_locales_en_switch(switch2, pcs2)

        num_equipos1=len(pcs1)
        num_equipos2=len(pcs2)
        nombre_de_fichero="Switches{0}-{1}.png".format(num_equipos1, num_equipos2)
        (origen, destino)=self.get_origen_y_destino([pcs1, pcs2])
        if solucion==False:
            plantilla_cabecera="""
Ejercicio {0} de switches
----------------------------------
"""
        else:
            plantilla_cabecera="""
Solución al ejercicio {0} de switches
------------------------------------------
"""
                        
        mensaje=mensaje_union+". Se pretende enviar desde ``{0}`` a ``{1}`` sabiendo lo siguiente:\n".format(origen, destino)
        datos_ordenadores_izq=formatear_pcs(pcs1, "I")
        datos_ordenadores_der=formatear_pcs(pcs2, "D")

        plantilla_enunciado="""
{0}
{1}

.. figure:: {6}

{2}
{3}

{4}

{5}
"""
        self.enunciado=plantilla_enunciado.format(
            plantilla_cabecera.format(self.num_ejercicio),
            mensaje,
            datos_ordenadores_izq,
            datos_ordenadores_der,
            switch1.get_tabla_rst(),
            switch2.get_tabla_rst(), nombre_de_fichero
        )
        
        self.generar_vector_respuestas(origen, destino,switch1, switch2)
        #print(self.vector_respuestas)




def ejecutar_script():
    seed()
    MAX_EJERCICIOS=1
    print("Anexo: ejercicios con tablas MAC de switches")
    print("================================================")
    vector_ejercicios=[]
    for i in range(0, 30):
        ejercicio=GeneradorEjerciciosV2(i+1)
        ejercicio.generar_ejercicio_dos_switches()
        vector_ejercicios.append(ejercicio)


    for ej in vector_ejercicios:
        print(ej.enunciado)
        print("Indica si las siguientes afirmaciones son verdaderas o falsas:\n")
        print(ej.get_respuestas_sin_solucion())

    pos=1
    for ej in vector_ejercicios:
        print()
        print("Solucion al ejercicio {0} de switches".format(pos))
        print("-----------------------------------------")
        print("Las respuestas son:")
        print()
        pos=pos+1
        print(ej.get_respuestas_con_solucion())
    #generar_ejercicio_dos_switches("P1.png")

if __name__=="__main__":
    ejecutar_script()