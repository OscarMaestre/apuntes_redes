#!/usr/bin/python3 
 

from creadorimagenes import CreadorImagen 
from simulador import ConstructorRedes, ListaEventos, Puerto, Switch, Iteracion, ConstructorCuadradoCuatroLados, Red

from random import randint
from os.path import basename, join
from os import mkdir



class ConstructorCuadradoCuatroLadosConDiagonal1(ConstructorCuadradoCuatroLados):
        

    def __init__(self) -> None:
        super().__init__()
        self.lista_eventos=ListaEventos()
        macs=self.generar_macs_azar(10)
        self.puerto_01=Puerto(macs[0])
        self.puerto_02=Puerto(macs[1])
        self.puerto_09=Puerto(macs[8])        
        self.Switch1=Switch(randint(1,6), [self.puerto_01, self.puerto_02, self.puerto_09], self.lista_eventos)

        self.puerto_03=Puerto(macs[2])
        self.puerto_04=Puerto(macs[3])
        self.Switch2=Switch(randint(1,6), [self.puerto_03, self.puerto_04], self.lista_eventos)

        self.puerto_05=Puerto(macs[4])
        self.puerto_06=Puerto(macs[5])
        self.puerto_10=Puerto(macs[9])        
        self.Switch3=Switch(randint(1,6), [self.puerto_05, self.puerto_06, self.puerto_10], self.lista_eventos)
        
        self.puerto_07=Puerto(macs[6])
        self.puerto_08=Puerto(macs[7])
        self.Switch4=Switch(randint(1,6), [self.puerto_07, self.puerto_08], self.lista_eventos)


        self.asociar_puertos(self.puerto_01, self.puerto_08)
        self.asociar_puertos(self.puerto_02, self.puerto_03)
        self.asociar_puertos(self.puerto_04, self.puerto_05)
        self.asociar_puertos(self.puerto_06, self.puerto_07)
        self.asociar_puertos(self.puerto_10, self.puerto_09)

        self.iteraciones=[]
        self.iteraciones.append(Iteracion(self.Switch1, self.puerto_01))
        self.iteraciones.append(Iteracion(self.Switch1, self.puerto_02))
        self.iteraciones.append(Iteracion(self.Switch1, self.puerto_09))

        self.iteraciones.append(Iteracion(self.Switch2, self.puerto_03))
        self.iteraciones.append(Iteracion(self.Switch2, self.puerto_04))

        self.iteraciones.append(Iteracion(self.Switch3, self.puerto_05))
        self.iteraciones.append(Iteracion(self.Switch3, self.puerto_06))
        self.iteraciones.append(Iteracion(self.Switch3, self.puerto_10))

        self.iteraciones.append(Iteracion(self.Switch4, self.puerto_07))
        self.iteraciones.append(Iteracion(self.Switch4, self.puerto_08))

        self.switches=[self.Switch1, self.Switch2, self.Switch3, self.Switch4]
        self.puertos=[self.puerto_01, self.puerto_02, self.puerto_03, self.puerto_04,
                self.puerto_05, self.puerto_06, self.puerto_07, self.puerto_08,
                self.puerto_09, self.puerto_10]

        
        self.red=Red(self.switches, self.puertos, self.iteraciones, self.lista_eventos)
        
    def set_valores_prueba(self):
        """Establece valores de prueba conocidos para los test de unidad"""
        #La red de prueba es asi
        #         1a               0b    
        #   1:1a--------------------- 3:0a
        #  1b |\                       | 0a
        #     | ----3a----\            |
        #     | 1c         \-----2c    | 2b
        #    2:1c-------------------- 1:2a
        #         1d                2a
        self.puerto_01.mac="1a"
        self.puerto_02.mac="1b"
        self.puerto_03.mac="1c"
        self.puerto_04.mac="1d"
        self.puerto_05.mac="2a"
        self.puerto_06.mac="2b"
        self.puerto_07.mac="0a"
        self.puerto_08.mac="0b"
        self.puerto_09.mac="3a"
        self.puerto_10.mac="2d"
        self.Switch1.set_mi_prioridad(1)
        self.Switch2.set_mi_prioridad(2)
        self.Switch3.set_mi_prioridad(1)
        self.Switch4.set_mi_prioridad(3)
        

    def set_valores_prueba_2(self):
        """Establece valores de prueba conocidos para los test de unidad"""
        #La red de prueba es asi
        #         7f               7a    
        #   5:1a--------------------- 3:0a
        #     | 1b                     | 0a
        #     |                        |
        #     | 1c                2a   | 2b
        #    2:1c-------------------- 1:2a
        #         1d
        self.puerto_01.mac="7f"
        self.puerto_02.mac="1b"
        self.puerto_03.mac="1c"
        self.puerto_04.mac="1d"
        self.puerto_05.mac="2a"
        self.puerto_06.mac="2b"
        self.puerto_07.mac="0a"
        self.puerto_08.mac="7a"
        self.Switch1.set_mi_prioridad(5)
        self.Switch2.set_mi_prioridad(2)
        self.Switch3.set_mi_prioridad(1)
        self.Switch4.set_mi_prioridad(3)
        
    def __str__(self) -> str:
        PLANTILLA="""
        
                 {1}               {11}    
           {0}--------------------- {9}
             | {2}                    | {10}
             |                       |
             |      {12}               |
             | {4}             {13}     | {8}
            {3}-------------------- {6}
                 {5}            {7}
"""
        return PLANTILLA.format(self.Switch1.identificador_yo, 
            self.puerto_01, self.puerto_02, 
            self.Switch2.identificador_yo, self.puerto_03, self.puerto_04,
            self.Switch3.identificador_yo, self.puerto_05, self.puerto_06,
            self.Switch4.identificador_yo, self.puerto_07, self.puerto_08,
            self.puerto_09, self.puerto_10)
        
    def generar_texto_ejercicio(self, num_ejercicio):
        
        PLANTILLA="""
STP Ejercicio {0}, dificultad 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Dada la red de switches que se muestra en la figura:

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej{0}/ejercicio{0}.png

Indicar el estado final en que quedarán todos los puertos de todos los switches.

Empezando por los eventos de envío, recepción y determinación de cual es el switch raíz la lista de sucesos sería esta:

{1}


Una vez decidido el switch raíz, los switches toman las siguientes decisiones (volvemos a indicar la figura por comodidad):

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej{0}/ejercicio{0}.png

{2}

        """
        textos_eventos=str(self.lista_eventos)
        decisiones=[]
        #print(c.red.switches)
        for s in self.red.switches:
            decisiones.append(s.get_decisiones_formateadas())
            
        textos_decisiones="\n".join(decisiones)

        texto_ejercicio=PLANTILLA.format(num_ejercicio, textos_eventos, textos_decisiones)
        return texto_ejercicio

    
    def formatear_lista_decisiones(self):
        texto=""
        # print(self.red.switches[0].lista_decisiones)
        # print(self.red.switches[1].lista_decisiones)
        # print(self.red.switches[2].lista_decisiones)
        # print(self.red.switches[3].lista_decisiones)
        
        
        for s in self.red.switches:
            texto+=s.get_decisiones_formateadas()+"\n"
        return texto+"\n"
    

    def generar_imagen(self, num_ejercicio):
        DIRECTORIO_BASE="tipo2"
        
        DIRECTORIO_EJ=join(DIRECTORIO_BASE, "ej"+str(num_ejercicio)+sep)
        FICHERO_TEXTO="ejercicio"+str(num_ejercicio)+".rst"
        RUTA_TEXTO=join(DIRECTORIO_EJ, FICHERO_TEXTO)
        FICHERO_IMAGEN_BASE="base1.png"
        FICHERO_IMAGEN_FINAL="ejercicio"+str(num_ejercicio)+".png"
        print("Fabricando:"+DIRECTORIO_EJ)
        mkdir(DIRECTORIO_EJ)
        RUTA_IMAGEN=join(DIRECTORIO_EJ, FICHERO_IMAGEN_FINAL)
        FICHERO_TTF=basename("Roboto.ttf")
        macs=[
            self.switches[0].puertos[0].mac, self.switches[0].puertos[1].mac, 
            self.switches[1].puertos[0].mac, self.switches[1].puertos[1].mac, 
            self.switches[2].puertos[0].mac, self.switches[2].puertos[1].mac, 
            self.switches[3].puertos[0].mac, self.switches[3].puertos[1].mac, 
        ]
        c=CreadorRoutersCuadrados(FICHERO_IMAGEN_BASE, RUTA_IMAGEN, FICHERO_TTF)
        c.poner_macs(macs)
        c.poner_prioridades(self.switches)
        c.get_resultado()
        with open(RUTA_TEXTO, "w") as fich:
            texto=self.generar_texto_ejercicio(num_ejercicio)
            fich.write(texto)

    def generar_ejercicio(self, num_ejercicio):
        self.simular()
        self.generar_imagen(num_ejercicio)
    def simular(self):
        self.red.hacer_envios()
        self.red.evaluar_switches()

        self.red.hacer_envios()
        self.red.evaluar_switches()

        self.red.hacer_envios()
        self.red.evaluar_switches()
        
        self.red.evaluar_estado_raiz_en_switches()


def prueba_depuracion():
        
    c=ConstructorCuadradoCuatroLadosConDiagonal1()
    
    c.simular()
    print(c.red.get_cadena_situacion_actual_raices())
    lista_eventos=c.lista_eventos
    for e in lista_eventos.lista:
        print(e)

    
    red=c.red
    print("-----------------------RED------------------------")
    print(str(c))
    print("-----------------------FIN RED------------------------")

    print("----------------------------DECISIONES--------------")
    print(red.get_lista_decisiones())
    print("----------------------------FIN DECISIONES--------------")

    #print (c.switches[0].get_menor_mac())
    

    for s in c.switches:
        print(s.get_decisiones_formateadas())

    print (c.red.get_lista_decisiones())



def main():
    
    PLANTILLA="""
Anexo al tema 3:Ejercicios STP 
--------------------------------

{0}

"""
    texto=""
    NUM_EJERCICIOS=20
    for i in range(1, NUM_EJERCICIOS+1):
        c=ConstructorCuadradoCuatroLados()
        print("Generando:"+str(i))
        plantilla=".. include:: tipo2/ej{0}/ejercicio{0}.rst\n\n"
        texto=texto+plantilla.format(str(i))
        c.generar_ejercicio(i)

    with open("stp1.rst", "w") as fich:
        fich.write(PLANTILLA.format(texto))

if __name__=="__main__":
    prueba_depuracion()
    #main()