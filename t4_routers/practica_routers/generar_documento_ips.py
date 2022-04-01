#!/usr/bin/python3

from os import mkdir
from os.path import join
from utilidades.imagenes.CreadorImagenes import CreadorImagenes

TARJETA_1="enp0s3"
TARJETA_2="enp0s8"
TARJETA_3="enp0s9"


FICHERO_NETPLAN="""
network:
  version: 2 
  ethernets: 
{0}
"""

class Router(object):
    def __init__(self):
        self.tarjetas=dict()
    def asignar_ip_tarjeta(self, tarjeta, ip):
        self.tarjetas[tarjeta]=ip
    def get_ip_tarjeta(self, tarjeta):
        nombre_tarjeta="    {0}:\n".format(tarjeta)
        ip            ="      addresses: [{0}]\n".format(self.tarjetas[tarjeta])
        return nombre_tarjeta + ip

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

def generar_lista_routers(num_equipo):
    T3=TARJETA_1
    T8=TARJETA_2
    T9=TARJETA_3
    red_base=100+num_equipo
    cad_red_base=str(red_base)
    r1=Router()
    r2=Router()
    r3=Router()
    
    r1.asignar_ip_tarjeta(T3, "1."+cad_red_base+".0.1/16")
    r1.asignar_ip_tarjeta(T8, "2."+cad_red_base+".0.1/16")
    r1.asignar_ip_tarjeta(T9, "3."+cad_red_base+".0.1/16")


    #r2.asignar_ip_tarjeta(T3, "4."+cad_red_base+".0.1/16")
    r2.asignar_ip_tarjeta(T3, "Reservada")
    r2.asignar_ip_tarjeta(T8, "2."+cad_red_base+".0.2/16")
    r2.asignar_ip_tarjeta(T9, "5."+cad_red_base+".0.1/16")

    r3.asignar_ip_tarjeta(T3, "6."+cad_red_base+".0.1/16")
    r3.asignar_ip_tarjeta(T8, "3."+cad_red_base+".0.2/16")
    r3.asignar_ip_tarjeta(T9, "5."+cad_red_base+".0.2/16")


    # print(r1.get_fichero_netplan())    
    # print(r2.get_fichero_netplan())    
    # print(r3.get_fichero_netplan())    
    
    return (r1,r2,r3)


def get_nombre_subdirectorio(num_equipo):
    nombre_subdirectorio="PC-"+str(num_equipo).zfill(2)
    directorio=join("Documentos", nombre_subdirectorio)
    return directorio

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

def generar_para_equipo(num_equipo):
    routers=generar_lista_routers(num_equipo)
    ip1="1."+str(num_equipo)+".101.10"
    ip2="6."+str(num_equipo)+".101.10"
    
    #Fabricamos el subdirectorio
    try:
        mkdir(get_nombre_subdirectorio(num_equipo))
    except FileExistsError:
        pass
    datos_ips=(ip1, routers, ip2)
    generar_imagen(num_equipo, datos_ips)

    return datos_ips

def generar_documento():
    texto=""
    NUM_EQUIPOS=range(1, 33)
    configuraciones=[]
    for num_equipo in NUM_EQUIPOS:
        NUM_RED=100+num_equipo
        configuraciones.append(generar_para_equipo(num_equipo))

    lineas_csv=[]
    num=1
    for c in configuraciones:
        linea="Equipo {5},{0},{1},{2},{3},{4};".format(c[0], c[1][0].get_ips_csv(), c[1][1].get_ips_csv(),c[1][2].get_ips_csv(), c[2], num )
        num=num+1           
        lineas_csv.append(linea)
    cabeceras='Equipo,Cliente1,R13,R18,R19,R23,R28,R29,R33,R38,R39,Cliente2;\n'
    texto="\n".join(lineas_csv)
    with open("datos.csv", "w") as fich:
        fich.write(cabeceras+texto)

if __name__=="__main__":
    generar_documento()