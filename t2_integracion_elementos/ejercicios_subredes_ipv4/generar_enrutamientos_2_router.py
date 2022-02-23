#!/usr/bin/python3
from generar_subredes_ipv4 import Generador
from generar_enrutamientos import GeneradorEjercicioEnrutamiento


class GeneradorEjercicioTresRouter(GeneradorEjercicioEnrutamiento):
    def __init__(self, num_ejercicio) -> None:
        self.num_ejercicio=num_ejercicio

        self.num_redes=5
        self.redes=[]
        for i in range(0, self.num_redes):
            self.redes.append(Generador(num_ejercicio))
        self.direcciones=[generador.direccion for generador in self.redes]
        
        (self.ip_ri, self.ip_rdi)=self.get_primera_y_ultima_up(self.redes[1])
        (self.ip_rdd, self.ip_rc)=self.get_primera_y_ultima_up(self.redes[3])

    def get_explicacion_par_routers(self, nombre_r1, nombre_r2, ip1, ip2, red):
        plantilla="""
* Dentro de la red {0}:

    * El router {1} tiene la IP {2} y la máscara {3}
    * El router {4} tiene la IP {5} y la máscara {3}
"""
        mascara=red.get_mascara_en_decimal()
        return plantilla.format(
            red.direccion,
            nombre_r1, ip1, mascara, nombre_r2, ip2, mascara
        )
    
    def get_tabla_ri(self):
        entrada1=[self.direcciones[2], self.redes[2].get_mascara_en_decimal(), self.ip_rdi]
        entrada2=[self.direcciones[4], self.redes[4].get_mascara_en_decimal(), self.ip_rdi]
        entradas=[entrada1, entrada2]
        return self.get_tabla_rutas("RI", entradas)


    def get_tabla_rd(self):
        entrada1=[self.direcciones[0], self.redes[0].get_mascara_en_decimal(), self.ip_ri]
        entrada2=[self.direcciones[4], self.redes[4].get_mascara_en_decimal(), self.ip_rc]
        entradas=[entrada1, entrada2]
        return self.get_tabla_rutas("RD", entradas)

    def get_tabla_rc(self):
        entrada1=[self.direcciones[2], self.redes[2].get_mascara_en_decimal(), self.ip_rdd]
        entrada2=[self.direcciones[0], self.redes[0].get_mascara_en_decimal(), self.ip_rdd]
        entradas=[entrada1, entrada2]
        return self.get_tabla_rutas("RC", entradas)

            

    def get_enunciado(self):
        plantilla="""
Ejercicio {0}
------------------------------
Dada la arquitectura de la red de la figura, asignar direcciones IP, máscaras, puertas de enlace y tablas de rutas de manera que haya conectividad entre todos
los nodos de la red. Se desean utilizar las siguientes redes:

.. figure:: RedTresRouters.png


* Red {1} en el área izquierda.
* Red {2} en el área RI-RD
* Red {3} en el área derecha
* Red {4} en el área RD-RC
* Red {5} en el área superior.



Aparte de eso, se desean respetar unos ciertos estándares:

* Los routers de acceso a red deben tener siempre la última IP de la red.
* Los ordenadores se empezarán a numerar por la primera IP de la red.
* Los routers deberán tener la primera IP en el punto izquierdo y la última en el derecho.

        """

        
        enunciado=plantilla.format(
            self.num_ejercicio, 
            *self.direcciones
            
        )
        return enunciado


    def get_solucion(self):
        plantilla="""

        
Solución al ejercicio {0} de enrutamiento
----------------------------------------------

Enunciado
~~~~~~~~~~~~~~
{1}

Solución
~~~~~~~~~~~~~~~~

La solución sería:

{2}
{3}
{4}
{5}
{6}
{7}
{8}
{9}
        """

        solucion_red_izq=self.get_solucion_red(self.redes[0], "1I", "2I", "RI")
        solucion_red_der=self.get_solucion_red(self.redes[2], "1D", "2D", "RD")
        solucion_red_sup=self.get_solucion_red(self.redes[4], "1C", "2C", "RC")

        solucion_red_ri_rd=self.get_explicacion_par_routers(
            "RI", "RD", self.ip_ri, self.ip_rdi, self.redes[1])

        solucion_red_rd_rc=self.get_explicacion_par_routers(
            "RD", "RC", self.ip_rdd, self.ip_rc, self.redes[3])

        tabla_ri=self.get_tabla_ri()
        tabla_rd=self.get_tabla_rd()
        tabla_rc=self.get_tabla_rc()
        solucion=plantilla.format(
            self.num_ejercicio, self.get_enunciado(),
            solucion_red_izq,
            solucion_red_der,
            solucion_red_sup,
            solucion_red_ri_rd,
            solucion_red_rd_rc,
            tabla_ri,
            tabla_rd,
            tabla_rc
            )
        return solucion




if __name__=="__main__":

    print ("Anexo: ejercicios de enrutamiento con 3 routers (caso 1)")
    print ("============================================================")

    print("Para todos estos casos se puede asumir una arquitectura como la siguiente:")
    NUM_EJERCICIOS_CON_DOS_ROUTER=20

    # ej=GeneradorEjercicioTresRouter(1)
    # print(ej.get_solucion())

    ejercicios_dos_router=[]
    for i in range(0, NUM_EJERCICIOS_CON_DOS_ROUTER):
        ej=GeneradorEjercicioTresRouter(i+1)
        ejercicios_dos_router.append(ej)

    for i in range(0, NUM_EJERCICIOS_CON_DOS_ROUTER):
        print(ejercicios_dos_router[i].get_enunciado())

    for i in range(0, NUM_EJERCICIOS_CON_DOS_ROUTER):
        print(ejercicios_dos_router[i].get_solucion())


