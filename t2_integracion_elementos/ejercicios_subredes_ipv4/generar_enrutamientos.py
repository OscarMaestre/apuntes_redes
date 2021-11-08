from generar_subredes_ipv4 import Generador


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

    def get_primera_y_ultima_up(self, generador):
        hosts=list(generador.direccion.hosts())
        tupla=(hosts[0], hosts[-1])
        return tupla
    


class GeneradorEjercicioTresRouter(GeneradorEjercicioEnrutamiento):
    def __init__(self, num_ejercicio) -> None:
        self.num_ejercicio=num_ejercicio

        self.generador_izq=Generador(num_ejercicio)
        self.red_izquierda=self.generador_izq.direccion


        self.generador_der=Generador(num_ejercicio)
        self.red_derecha=self.generador_der.direccion


        self.generador_centro_izq=Generador(num_ejercicio)
        self.red_centro_izq=self.generador_centro_izq.direccion

        self.generador_centro_der=Generador(num_ejercicio)
        self.red_centro_der=self.generador_centro_der.direccion

    def get_enunciado(self):
        plantilla="""
Ejercicio {0}
------------------------------
Dada la arquitectura de la red de la figura, asignar direcciones IP, máscaras, puertas de enlace y tablas de rutas de manera que haya conectividad entre todos
los nodos de la red. Se desean utilizar las siguientes redes:

* Red {1} en el área izquierda.
* Red {2} en el área derecha
* Red {3} en el área RI-RC.
* Red {4} en el área RC-RD



Aparte de eso, se desean respetar unos ciertos estándares:
* Los routers de acceso a red deben tener siempre la primera IP de la red.
* Los distintos ordenadores deben tener direcciones de 10 en adelante.
* Los routers deberán tener la primera IP en el punto izquierdo y la última en el derecho.

        """

        enunciado=plantilla.format(
            self.num_ejercicio,
            self.red_izquierda,
            self.red_derecha,
            self.red_centro_izq,
            self.red_centro_der,
            
        )
        return enunciado

    def get_solucion(self):
        plantilla="""
Solución al ejercicio {0} de enrutamiento
----------------------------------------------

Las direcciones serían estas:
* PC 1I: IP {1}, máscara {3}, gateway {4}
* PC 2I: IP {2}, máscara {3}, gateway {4}
* Router I, interfaz izquierda: IP {4}, máscara {3}
* Router C, interfaz izquierda: IP {9}
* PC 1D: IP {5}, máscara {7}, gateway {8}
* PC 2D: IP {6}, máscara {7}, gateway {8}
* Router D, interfaz derecha: IP {8}, máscara {7}
        """
        POS_PC1=0
        POS_PC2=1
        POS_GW =2
        POS_MASCARA=3

        datos_red_izq=self.get_datos_ordenadores(self.generador_izq, self.red_izquierda)
        
        datos_red_der=self.get_datos_ordenadores(self.generador_der, self.red_derecha)
        

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


            
        )
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

Aparte de eso, se desean respetar unos ciertos estándares:

* Los routers de acceso a red deben tener siempre la primera IP de la red.
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

La tabla de rutas del Router I contiene la entrada siguiente:

* Red {9}, máscara {10}, siguiente salto: {11}

La tabla de rutas del Router D contiene la entrada siguiente:

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

print("Anexo: ejercicios de enrutamiento")
print("=========================================")

print ("Ejercicios con dos router")
print ("-----------------------------------")

print("Para todos estos casos se puede asumir una arquitectura como la siguiente")
NUM_EJERCICIOS_CON_DOS_ROUTER=21
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