#!/usr/bin/python3

from os import mkdir
from os.path import join
from utilidades.imagenes.CreadorImagenes import CreadorImagenes

TARJETA_1="enp0s3"
TARJETA_2="enp0s8"
TARJETA_3="enp0s9"

MAX_EQUIPOS=24
IP_RESERVADA="Reservada"

FICHERO_NETPLAN="""
network:
  version: 2 
  ethernets: 
{0}
"""

FICHERO_MAKE="""
all:
\trst2html5 Instrucciones.rst > Instrucciones.html

"""

INSTRUCCIONES="""
Instrucciones para el ordenador PC-{0}
=========================================

Junto con este documento se te ha dado una imagen con la topología de una red y una máquina virtual que puedes importar. Importa la máquina y haz 4 clones de manera que tengas en total 5 máquinas virtuales. Es muy recomendable que a cada máquina le pongas un nombre como vamos a ver a continuación. 

Obsérva la imagen con detenimiento porque vamos a construir una topologia de red con varios routers y con 
enrutamiento estático. 

.. figure:: Red.png

Como puedes ver tenemos 6 máquinas:

* Un cliente llamado "Cliente 1".
* Un cliente llamado "Cliente 2".
* Tres router que llamaremos "Izquierda", "Arriba" y "Abajo".


Cliente 1 y Cliente 2 solo van a usar **una tarjeta de red en modo puente**, la ``enp0s3``. Sin embargo  los router van a tener **tres tarjetas de red en modo puente**. Si estás usando máquinas virtuales clonadas o importadas recuerda **reiniciar las MAC de todas las tarjetas.** A continuación se te indican las direcciones IP y las tarjetas en las que hay que asignarlas.

* Cliente 1: {1}
* Cliente 2: {2}
* Izquierda: {3}
* Arriba: {4}
* Abajo: {5}




Ejercicio 1
--------------
Configurar las IP, máscaras, gateways y rutas en todas las máquinas de manera que Cliente1 pueda hacer ping a Cliente2 enviando los paquetes por abajo, es decir el camino directo.

Ejercicio 2
--------------
Modifica las rutas de manera que Cliente1 pueda hacer ping a Cliente2 enviando los paquetes por arriba, es decir el camino más largo.

Ejercicio 3
--------------
En el router de arriba hemos dejado una tarjeta sin usar. Intenta conectar con las redes de algún compañero. Para ello, tanto tu compañero como tú tendréis que hacer lo siguiente:

* Poneros de acuerdo en una red IP para ese segmento. Examinad vuestros números de puesto y usad la dirección de red 30.<numeromayor>.<numeromenor>.0/24. Es decir, si tenéis los números de puesto 7 y 24 deberíais usar la 30.24.7.0/24. 
* Pasáos el uno al otro las direcciones de red de vuestros respectivos "Cliente 1" y "Cliente 2"
* Poneros de acuerdo en qué IP usar cada uno en vuestro router de arriba.
* Reconfigura **todos tus router** para añadir en ellos rutas para llegar a las redes de los clientes de tu compañero.

Este ejercicio demuestra que la configuración estática de rutas solo es razonable para pequeñas redes y con pocos cambios. En el ejercicio siguiente verás como ahorrarte todo este trabajo.



Ejercicio 4
-------------
Reinicia todos los router, lo que borrará todas las rutas. En todos tus router tienes instalado un servicio que permite usar protocolos dinámicos de enrutamientos. Configúralos para que calculen todas las rutas automáticamente.

{7}


{8}


Solución al ejercicio 3
-------------------------
No se da

Solución al ejercicio 4
------------------------
En todos los router tendrás que hacer esto:

1. Editar el fichero de configuracion ``/etc/frr/daemons``
2. Activar OSPF poniendo ``yes``  en lugar de ``no`` en esta línea ``ospfd=no``
3. Reiniciar el servicio con ``sudo service frr restart``
4. Arranca la configuración del router con ``sudo vtysh``
5. Introduce los comandos correspondientes a cada router.

Router izquierda::

{9}

Router Arriba::

{10}

Router Abajo::

{11}
"""

class Router(object):
    def __init__(self):
        self.tarjetas=dict()
        self.gateways=dict()
        self.rutas=[]
        self.redes_conectadas=[]
    def asignar_ip_tarjeta(self, tarjeta, ip):
        self.tarjetas[tarjeta]=ip
    def asignar_gateway(self, tarjeta, ip_gateway):
        self.gateways[tarjeta]=ip_gateway
    def anadir_red(self, red):
        self.redes_conectadas.append(red)
    def anadir_ruta(self, ip_red, siguiente_salto):
        self.rutas.append( (ip_red, siguiente_salto))
    def limpiar_rutas(self):
        self.rutas=[]

    def get_comandos_ospf(self):
        comandos=[]
        plantilla="\tnetwork {0} area 1"
        for red in self.redes_conectadas:
            comandos.append(plantilla.format(red))
        texto= "\n".join(comandos)
        return texto
        #print(texto)

    def get_comandos_rutas(self, con_tabulador=True):
        comandos=[]
        if con_tabulador:
            plantilla="\tsudo ip route add {0} via {1}"
        else:
            plantilla="sudo ip route add {0} via {1}"

        for ruta in self.rutas:
            texto=plantilla.format(ruta[0], ruta[1])
            comandos.append(texto)
        return "\n".join(comandos)

    def get_ip_tarjeta(self, tarjeta):
        if self.tarjetas[tarjeta]==IP_RESERVADA:
            return ""
        nombre_tarjeta="    {0}:\n".format(tarjeta)
        ip            ="      addresses: [{0}]\n".format(self.tarjetas[tarjeta])
        gw=""
        try:
            gateway=self.gateways[tarjeta]
            gw="      gateway4:  {0}".format(gateway)
            #print("He puesto esto:"+gw)
        except KeyError:
            gw=""
        return nombre_tarjeta + ip + gw

    def get_todas_tarjetas(self):
        ips=[]
        for clave in self.tarjetas:
            ips.append(self.get_ip_tarjeta(clave))
        return "".join(ips)

    def get_lista_ips(self):
        ips=[self.tarjetas[TARJETA_1], self.tarjetas[TARJETA_2], self.tarjetas[TARJETA_3]]
        
        return ips

    def get_fichero_netplan(self):
        ips=self.get_todas_tarjetas()
        return FICHERO_NETPLAN.format(ips)
    def get_ips_csv(self):
        ips=[]
        for clave in self.tarjetas:
            ips.append(self.tarjetas[clave])
        return ",".join(ips)
    def get_puntos_informacion_ips(self):
        lineas=[]
        for clave in self.tarjetas:
            linea="la tarjeta {0} tiene la IP **{1}**".format(clave, self.tarjetas[clave])
            lineas.append(linea)
        return ",".join(lineas)

def tabular_texto(texto):
    trozos=texto.split("\n")
    nuevo=[]
    for t in trozos:
        nuevo.append("\t"+t)
    return "\n".join(nuevo)

def poner_texto_en_fichero(ruta, texto):
    with open(ruta, "w") as fich:
        fich.write(texto)

def poner_netplan_en_fichero(ruta, maquina):
    texto=maquina.get_fichero_netplan()
    poner_texto_en_fichero(ruta, texto)

def get_comando_ruta(ip_red, siguiente_salto):
    comando="sudo ip route add {0} via {1}"
    texto=comando.format(ip_red, siguiente_salto)
    return texto

def generar_lista_routers(num_equipo):
    T3=TARJETA_1
    T8=TARJETA_2
    T9=TARJETA_3
    red_base=100+num_equipo
    PRIMER_BYTE=1
    ULTIMO_BYTE=2
    RED_1="1.{0}.0.{1}/16"
    RED_2="2.{0}.0.{1}/16"
    RED_3="3.{0}.0.{1}/16"
    RED_4="4.{0}.0.{1}/16"
    RED_5="5.{0}.0.{1}/16"
    RED_6="6.{0}.0.{1}/16"

    cad_red_base=str(red_base)
    r1=Router()
    r2=Router()
    r3=Router()
    
    r1.asignar_ip_tarjeta(T3, RED_1.format(cad_red_base, PRIMER_BYTE))
    r1.asignar_ip_tarjeta(T8, RED_2.format(cad_red_base, PRIMER_BYTE))
    r1.asignar_ip_tarjeta(T9, RED_3.format(cad_red_base, PRIMER_BYTE))
    
    r1.anadir_red(RED_1.format(cad_red_base, "0"))
    r1.anadir_red(RED_2.format(cad_red_base, "0"))
    r1.anadir_red(RED_3.format(cad_red_base, "0"))

    #r2.asignar_ip_tarjeta(T3, "4."+cad_red_base+".0.1/16")
    r2.asignar_ip_tarjeta(T3, IP_RESERVADA)
    #r2.asignar_ip_tarjeta(T8, "2."+cad_red_base+".0.2/16")
    r2.asignar_ip_tarjeta(T8, RED_2.format(cad_red_base, ULTIMO_BYTE))
    #r2.asignar_ip_tarjeta(T9, "5."+cad_red_base+".0.1/16")
    r2.asignar_ip_tarjeta(T9, RED_5.format(cad_red_base, PRIMER_BYTE))
    r2.anadir_red(RED_2.format(cad_red_base, "0"))
    r2.anadir_red(RED_5.format(cad_red_base, "0"))

    # r3.asignar_ip_tarjeta(T3, "6."+cad_red_base+".0.1/16")
    # r3.asignar_ip_tarjeta(T8, "3."+cad_red_base+".0.2/16")
    # r3.asignar_ip_tarjeta(T9, "5."+cad_red_base+".0.2/16")

    r3.asignar_ip_tarjeta(T3, RED_6.format(cad_red_base, PRIMER_BYTE))
    r3.asignar_ip_tarjeta(T8, RED_3.format(cad_red_base, ULTIMO_BYTE))
    r3.asignar_ip_tarjeta(T9, RED_5.format(cad_red_base, ULTIMO_BYTE))
    
    r3.anadir_red(RED_6.format(cad_red_base, "0"))
    r3.anadir_red(RED_3.format(cad_red_base, "0"))
    r3.anadir_red(RED_5.format(cad_red_base, "0"))

    # print(r1.get_fichero_netplan())    
    # print(r2.get_fichero_netplan())    
    # print(r3.get_fichero_netplan())    
    
    return (r1,r2,r3)


def generar_make_global():
    lineas=[]
    for i in range(1, MAX_EQUIPOS):
        subdir=get_nombre_subdirectorio(i)
        linea="cd {0};make;cd ..; cd ..".format(subdir)
        lineas.append(linea)
    texto=";".join(lineas)
    fichero="all:\n\t{0}".format(texto)
    with open("Makefile", "w") as fich:
        fich.write(fichero)

def get_nombre_subdirectorio(num_equipo):
    nombre_subdirectorio="PC-"+str(num_equipo).zfill(2)
    directorio=join("Documentos", nombre_subdirectorio)
    return directorio

def get_solucion_1(equipo, datos_ips):
    (cliente1, routers, cliente2)=datos_ips
    (izquierda, arriba, abajo) = routers

    nombres=["Cliente 1", "Izquierda", "Arriba", "Abajo"]
    maquinas=[cliente1, izquierda, arriba, abajo, cliente2]

    SOLUCION="""
Solución al ejercicio 1
------------------------

Direccionamiento
~~~~~~~~~~~~~~~~~~~~~
{0}

Una vez configuradas todas las direcciones IP repasalo todo ejecutando ``ip addr`` **en todas las máquinas** y comprueba que **todo el mundo puede hacer ping a su vecino inmediato**. Si no es así repasa las direcciones y tarjetas y si no ves el error llama al profesor.

Enrutamiento
~~~~~~~~~~~~~~~~~~~~~~~~~
Antes de empezar, en Linux se debe habilitar el enrutamiento.

1. Escribe ``sudo nano /etc/sysctl.conf``.
2. Busca una línea con el texto ``net.ipv4.ip_forward=1``.
3. Si tiene una almohadilla delante es porque esa línea está comentada y no está activada. Borra el símbolo #, **guarda los cambios** y despues ejecuta ``sudo sysctl -p`` que forzará la recarga del fichero y activará el enrutamiento.

En todos los router debemos recordar poner tanto las rutas de ida *como las rutas de vuelta*, así, los comandos a ejecutar serían algo como esto:

En Izquierda podemos ejecutar esto::

{1}

En Abajo podemos ejecutar esto::

{2}
"""
    #Aquí resolvemos el direccionamiento
    lineas=[]
    for nombre, maquina in zip(nombres, maquinas):
        plantilla="{0} tendría un fichero de ``netplan`` como este::\n{1}"
        fich_netplan=tabular_texto(maquina.get_fichero_netplan())
        texto=plantilla.format(nombre, fich_netplan)
        lineas.append(texto)
    texto_solucion_encaminamiento="\n\n".join(lineas)
    #Aquí resolvemos el enrutamiento

    red_cliente_1=get_red_cliente_1(equipo) 
    red_cliente_2=get_red_cliente_2(equipo)
    izquierda.anadir_ruta(red_cliente_2,abajo.tarjetas[TARJETA_2])
    abajo.anadir_ruta(red_cliente_1,izquierda.tarjetas[TARJETA_3])
    
    enrutamiento_r1=izquierda.get_comandos_rutas()
    enrutamiento_r2=abajo.get_comandos_rutas() 

    texto= SOLUCION.format(texto_solucion_encaminamiento, enrutamiento_r1, enrutamiento_r2)
    return texto
    

def get_solucion_2(equipo, datos_ips):
    (cliente1, routers, cliente2)=datos_ips
    (izquierda, arriba, abajo) = routers

    nombres=["Cliente 1", "Izquierda", "Arriba", "Abajo"]
    maquinas=[cliente1, izquierda, arriba, abajo, cliente2]

    SOLUCION="""
Solución al ejercicio 2
------------------------

Direccionamiento
~~~~~~~~~~~~~~~~~~~~~
Los ficheros de ``netplan`` **NO CAMBIAN**

Enrutamiento
~~~~~~~~~~~~~~~~~~~~~~~~~
Si ya tienes el enrutamiento activa (ver más arriba) **no hace falta que vuelvas a hacerlo**.

En primer lugar **debemos borrar las rutas anteriores en los router Izquierda y Abajo**. Ademas, de nuevo en todos los router debemos recordar poner tanto las rutas de ida *como las rutas de vuelta*. 

En Izquierda podemos ejecutar esto::

{0}

En Arriba podemos ejecutar esto::

{1}

En Abajo podemos ejecutar esto::

{2}

"""
    
    #Aquí resolvemos el enrutamiento
    izquierda.limpiar_rutas()
    abajo.limpiar_rutas()
    arriba.limpiar_rutas()

    red_cliente_1=get_red_cliente_1(equipo) 
    red_cliente_2=get_red_cliente_2(equipo)

    izquierda.anadir_ruta(red_cliente_2,arriba.tarjetas[TARJETA_2])
    abajo.anadir_ruta(red_cliente_1,arriba.tarjetas[TARJETA_3])

    arriba.anadir_ruta(red_cliente_1, izquierda.tarjetas[TARJETA_2])
    arriba.anadir_ruta(red_cliente_2, abajo.tarjetas[TARJETA_3])
    
    enrutamiento_izq=izquierda.get_comandos_rutas()
    enrutamiento_arriba=arriba.get_comandos_rutas()
    enrutamiento_abajo=abajo.get_comandos_rutas() 
    

    texto= SOLUCION.format( enrutamiento_izq, enrutamiento_arriba, enrutamiento_abajo)
    return texto
    

def get_lista_ips(datos_ips):
    ips=[]
    (ip1, tupla_routers,ip2)=datos_ips
    (r1, r2, r3)=tupla_routers
    ips.append(ip1)
    lista2=r1.get_lista_ips()+r2.get_lista_ips()+r3.get_lista_ips()
    ips=ips+lista2
    ips.append(ip2)

    return ips

def generar_imagen(num_equipo, datos_ips):
    IMG_ORIGINAL="Router3.png"
    SUBDIRECTORIO=get_nombre_subdirectorio(num_equipo)
    IMG_FINAL=join(SUBDIRECTORIO,"Red.png")
    ips=get_lista_ips(datos_ips)

    coordenadas=[
        #IP1
        (15,166),
        #R1 enp0s3    enp0s8     enp0s9
        (89,262), (161,134), (155,291),
        #R2 enp0s3    enp0s8     enp0s9
        (536,42), (305,37), (482, 107),
        #R3 enp0s3    enp0s8     enp0s9
        (396,370), (298,338),(475,230),
        #IP2
        (553,315)
    ]
    creador=CreadorImagenes(IMG_ORIGINAL, IMG_FINAL, tamano_fuente=14)
    creador.poner_textos(ips, coordenadas)
    creador.guardar()




def generar_instrucciones(num_equipo, datos_ips):
    TARJETA_EN_CLIENTES="enp0s3"
    (cliente1, routers, cliente2)=datos_ips
    (r1, r2, r3) = routers

    directorio=get_nombre_subdirectorio(num_equipo)
    router_cliente_1=Router()
    router_cliente_1.asignar_ip_tarjeta(TARJETA_EN_CLIENTES, get_ip_cliente_1(num_equipo))
    router_cliente_1.asignar_gateway(TARJETA_EN_CLIENTES, r1.tarjetas[TARJETA_EN_CLIENTES])
    router_cliente_2=Router()
    router_cliente_2.asignar_ip_tarjeta(TARJETA_EN_CLIENTES, get_ip_cliente_2(num_equipo))
    router_cliente_2.asignar_gateway(TARJETA_EN_CLIENTES, r2.tarjetas[TARJETA_EN_CLIENTES])

    IP_SALIDA_CLASE="10.9.0.{0}/24".format(str(200+num_equipo))

    tupla_maquinas=(router_cliente_1, (r1,r2,r3), router_cliente_2)
    solucion1=get_solucion_1(num_equipo, tupla_maquinas)
    solucion2=get_solucion_2(num_equipo, tupla_maquinas)

    comandos_ospf_router1=r1.get_comandos_ospf()
    comandos_ospf_router2=r2.get_comandos_ospf()
    comandos_ospf_router3=r3.get_comandos_ospf()

    texto=INSTRUCCIONES.format(num_equipo, 
        router_cliente_1.get_puntos_informacion_ips(),
        router_cliente_2.get_puntos_informacion_ips(),
        r1.get_puntos_informacion_ips(),
        r2.get_puntos_informacion_ips(),
        r3.get_puntos_informacion_ips(),
        IP_SALIDA_CLASE,
        solucion1,
        solucion2, 
        comandos_ospf_router1, comandos_ospf_router2, comandos_ospf_router3
    )
    with open(join(directorio, "Instrucciones.rst"), "w") as fich:
        fich.write(texto)

        
def generar_make(num_equipo):
    directorio=get_nombre_subdirectorio(num_equipo)
    with open ( join (directorio, "Makefile"), "w") as fich:
        fich.write(FICHERO_MAKE)

def get_ip_cliente_1(num_equipo):
    nuevo_num=100+num_equipo
    
    ip="1."+str(nuevo_num)+".101.10/16"
    return ip
def get_red_cliente_1(num_equipo):
    ip="1."+str(num_equipo)+".101.0/16"
    return ip

def get_ip_cliente_2(num_equipo):
    nuevo_num=100+num_equipo
    ip="6."+str(nuevo_num)+".101.10/16"
    return ip

def get_red_cliente_2(num_equipo):
    ip="6."+str(num_equipo)+".101.0/16"
    return ip

def generar_para_equipo(num_equipo):
    
    routers=generar_lista_routers(num_equipo)
    ip1=get_ip_cliente_1(num_equipo)
    ip2=get_ip_cliente_2(num_equipo)
    
    #Fabricamos el subdirectorio
    try:
        mkdir(get_nombre_subdirectorio(num_equipo))
    except FileExistsError:
        pass
    #Generamos las IPs que debe usar este equipo
    datos_ips=(ip1, routers, ip2)
    #Generamos la imagen que debe ver
    generar_imagen(num_equipo, datos_ips)

    #Generamos las instrucciones para ese equipo
    generar_instrucciones(num_equipo, datos_ips)

    generar_make(num_equipo)
    return datos_ips

def generar_csv(configuraciones):
    lineas_csv=[]
    num=1
    for c in configuraciones:
        linea="Equipo {5},{0},{1},{2},{3},{4};".format(c[0], c[1][0].get_ips_csv(), c[1][1].get_ips_csv(),c[1][2].get_ips_csv(), c[2], num )
        num=num+1           
        lineas_csv.append(linea)
    #Fin del for

    generar_make_global()
    cabeceras='Equipo,Cliente1,R13,R18,R19,R23,R28,R29,R33,R38,R39,Cliente2;\n'
    texto="\n".join(lineas_csv)
    with open("datos.csv", "w") as fich:
        fich.write(cabeceras+texto)


def generar_todos_los_documentos():
    texto=""
    NUM_EQUIPOS=range(1, MAX_EQUIPOS)
    configuraciones=[]
    #Para cada equipo
    for num_equipo in NUM_EQUIPOS:
        NUM_RED=100+num_equipo
        configuraciones.append(generar_para_equipo(num_equipo))
    
    generar_csv(configuraciones)
    

if __name__=="__main__":
    generar_todos_los_documentos()