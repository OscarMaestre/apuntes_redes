#!/usr/bin/python3


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
    def asignar_ip_tarjeta(self, ip, tarjeta):
        self.tarjetas[ip]=tarjeta
    def get_ip_tarjeta(self, tarjeta):
        nombre_tarjeta="    {0}:\n".format(tarjeta)
        ip            ="      addresses: [{0}]\n".format(self.tarjetas[tarjeta])
        return nombre_tarjeta + ip

    def get_todas_tarjetas(self):
        ips=[]
        for clave in self.tarjetas:
            ips.append(self.get_ip_tarjeta(clave))
        return "".join(ips)
    def get_fichero_netplan(self):
        ips=self.get_todas_tarjetas()
        return FICHERO_NETPLAN.format(ips)
    def get_ips_csv(self):
        ips=[]
        for clave in self.tarjetas:
            ips.append(self.tarjetas[clave])
        return ",".join(ips)

def generar_lista_routers(num_equipo):
    T3="enp0s3"
    T8="enp0s8"
    T9="enp0s9"
    red_base=100+num_equipo
    cad_red_base=str(red_base)
    r1=Router()
    r2=Router()
    r3=Router()
    
    r1.asignar_ip_tarjeta(T3, "1."+cad_red_base+".0.1/16")
    r1.asignar_ip_tarjeta(T8, "2."+cad_red_base+".0.1/16")
    r1.asignar_ip_tarjeta(T9, "3."+cad_red_base+".0.1/16")


    r2.asignar_ip_tarjeta(T3, "4."+cad_red_base+".0.1/16")
    r2.asignar_ip_tarjeta(T8, "2."+cad_red_base+".0.2/16")
    r2.asignar_ip_tarjeta(T9, "5."+cad_red_base+".0.1/16")

    r3.asignar_ip_tarjeta(T3, "6."+cad_red_base+".0.1/16")
    r3.asignar_ip_tarjeta(T8, "3."+cad_red_base+".0.2/16")
    r3.asignar_ip_tarjeta(T9, "5."+cad_red_base+".0.2/16")


    # print(r1.get_fichero_netplan())    
    # print(r2.get_fichero_netplan())    
    # print(r3.get_fichero_netplan())    
    
    return (r1,r2,r3)

def generar_para_equipo(num_equipo):
    routers=generar_lista_routers(num_equipo)
    ip1="1."+str(num_equipo)+".101.10"
    ip2="6."+str(num_equipo)+".101.10"
    return (ip1, routers, ip2)

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