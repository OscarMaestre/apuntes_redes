#!/usr/bin/python3
from generar_subredes_ipv4 import Generador
from pytablewriter import RstSimpleTableWriter

class GeneradorEjercicioEnrutamiento(object):
    def get_enunciado(self):
        pass
    def get_datos_ordenadores(self, generador, red):
        ip_red              = red
        hosts               = list(ip_red.hosts())
        return [
            hosts[0],   #PC 1
            hosts[1],   #PC 2
            hosts[-1],  #Gateway
            generador.get_mascara_en_decimal() #Mascara
        ]
    def get_solucion(self):
        pass

    def get_tabla_rutas(self, nombre_router, entradas):
        plantilla="""
* Para el router {0} la tabla de rutas sería:

{1}
"""
        tabla=self.get_tabla_enrutamiento(entradas)

        return plantilla.format(nombre_router, tabla)

    def get_tabla_enrutamiento(self, entradas_tabla_rutas):
        encabezamientos=["IP de red", "Máscara", "Siguiente salto"]
        escritor_tablas=RstSimpleTableWriter(headers=encabezamientos, 
        value_matrix=entradas_tabla_rutas)
        return escritor_tablas.dumps()

    def get_cadena_ordenador(self, nombre, ip, mascara, gateway):
        plantilla="* PC {0}: IP {1}, máscara {2}, gateway {3}"
        return plantilla.format(
            nombre, ip, mascara, gateway
        )
    
    def get_primera_y_ultima_up(self, generador):
        hosts=list(generador.direccion.hosts())
        tupla=(hosts[0], hosts[-1])
        return tupla

    def get_primera_segunda_y_ultima_up(self, generador):
        hosts=list(generador.direccion.hosts())
        tupla=(hosts[0], hosts[1], hosts[-1])
        return tupla

    def get_solucion_red(self, generador, nombre_pc1, nombre_pc2, nombre_router):
        mascara=generador.get_mascara_en_decimal()
        (ip1, ip2, ip_router)=self.get_primera_segunda_y_ultima_up(generador)
        cadena_pc1=self.get_cadena_ordenador(nombre_pc1, ip1, mascara, ip_router)
        cadena_pc2=self.get_cadena_ordenador(nombre_pc1, ip2, mascara, ip_router)
        cadena_router="* Router {0}: IP:{1}".format(nombre_router, ip_router)
        solucion="\n".join([cadena_pc1, cadena_pc2, cadena_router])
        return solucion
    



class GeneradorEjercicioDosRouter(GeneradorEjercicioEnrutamiento):
    def __init__(self, num_ejercicio) -> None:
        self.num_ejercicio=num_ejercicio

        self.generador_izq=Generador(num_ejercicio)
        self.red_izquierda=self.generador_izq.direccion


        self.generador_der=Generador(num_ejercicio)
        self.red_derecha=self.generador_der.direccion


        self.generador_centro=Generador(num_ejercicio)
        self.red_centro=self.generador_centro.direccion
    
    def get_encabezamiento(self):
        plantilla="""
Ejercicio {0}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
        return plantilla.format(self.num_ejercicio)
    def get_enunciado(self):
        encabezamiento=self.get_encabezamiento()
        texto=self.get_texto()
        return "\n".join([encabezamiento, texto])

    def get_texto(self):
        plantilla="""

Dada la arquitectura de la red de la figura, asignar direcciones IP, máscaras, puertas de enlace y tablas de rutas de manera que haya conectividad entre todos
los nodos de la red. Se desean utilizar las siguientes redes:

* Red {1} en el área izquierda.
* Red {2} en el área central.
* Red {3} en el área derecha

.. figure:: RedDosRouters.png

Aparte de eso, se desean respetar unos ciertos estándares:


* Los routers de acceso a red deben tener siempre la última IP de la red.
* Los ordenadores se empezarán a númerar por la primera IP de la red.
* Los routers de distribución (los centrales) deberán tener la primera IP en el punto izquierdo y la última en el derecho.

        """

        enunciado=plantilla.format(
            self.num_ejercicio,
            self.red_izquierda,
            self.red_centro,
            self.red_derecha
        )
        return enunciado

    def get_solucion(self):
        plantilla="""
Solución al ejercicio {0} de enrutamiento
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

{16}


Las direcciones serían estas:

* PC 1I: IP {1}, máscara {3}, gateway {4}
* PC 2I: IP {2}, máscara {3}, gateway {4}
* Router I, interfaz izquierda: IP {4}, máscara {3}
* Router I, interfaz derecha: IP {12}, máscara {13}
* PC 1D: IP {5}, máscara {7}, gateway {8}
* PC 2D: IP {6}, máscara {7}, gateway {8}
* Router D, interfaz derecha: IP {8}, máscara {7}
* Router D, interfaz izquierda: IP {11}, máscara {13}

La tabla de rutas del Router I debería tener la entrada siguiente:

* Red {9}, máscara {10}, siguiente salto: {11}

La tabla de rutas del Router D debería tener la entrada siguiente:

* Red {14}, máscara {15}, siguiente salto {12}
        """
        POS_PC1=0
        POS_PC2=1
        POS_GW =2
        POS_MASCARA=3

        datos_red_izq=self.get_datos_ordenadores(self.generador_izq, self.red_izquierda)
        
        datos_red_der=self.get_datos_ordenadores(self.generador_der, self.red_derecha)
        

        (ip_router_izq_en_red_central, ip_router_der_en_red_central)=self.get_primera_y_ultima_up(self.generador_centro)

        solucion=plantilla.format(
            self.num_ejercicio,
            datos_red_izq[POS_PC1], 
            datos_red_izq[POS_PC2], 
            datos_red_izq[POS_MASCARA],
            datos_red_izq[POS_GW],

            datos_red_der[POS_PC1], 
            datos_red_der[POS_PC2], 
            datos_red_der[POS_MASCARA],
            datos_red_der[POS_GW],
            
            self.generador_der.direccion,
            self.generador_der.get_mascara_en_decimal(),
            ip_router_der_en_red_central,
            ip_router_izq_en_red_central,
            self.generador_centro.get_mascara_en_decimal(), 

            self.generador_izq.direccion,
            self.generador_izq.get_mascara_en_decimal(),

            self.get_texto()
        )
        return solucion



if __name__=="__main__":
    print("Anexo: ejercicios de enrutamiento")
    print("=========================================")

    print ("Ejercicios con dos router")
    print ("-----------------------------------")

    print("Para todos estos casos se puede asumir una arquitectura como la siguiente:")
    NUM_EJERCICIOS_CON_DOS_ROUTER=20
    ejercicios_dos_router=[]
    for i in range(0, NUM_EJERCICIOS_CON_DOS_ROUTER):
        ej=GeneradorEjercicioDosRouter(i+1)
        ejercicios_dos_router.append(ej)

    for i in range(0, NUM_EJERCICIOS_CON_DOS_ROUTER):
        print(ejercicios_dos_router[i].get_enunciado())

    for i in range(0, NUM_EJERCICIOS_CON_DOS_ROUTER):
        print(ejercicios_dos_router[i].get_solucion())


# ej1=GeneradorEjercicioTresRouter(1)
# print(ej1.get_enunciado())
# print(ej1.get_solucion())