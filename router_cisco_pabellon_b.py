
NOMBRE_TARJETAS                         = "GigabitEthernet"
TARJETA_PABELLON_B                      = NOMBRE_TARJETAS+"0/0"
TARJETA_ESCUELAS_CONECTADAS             = NOMBRE_TARJETAS+"0/1"
AULAS                                   = [8,9,10,11,12,13,14,15]

MASCARA_PABELLON_B                      ="255.255.0.0"
MASCARA_ESCUELAS_CONECTADAS             ="255.255.255.0"
IP_HACIA_ESCUELAS_CONECTADAS            ="172.16.0.254"
GATEWAY_SALIDA_ESCUELAS_CONECTADAS      ="172.16.0.1"
IP_DENTRO_PABELLON_B                    ="192.168.1.1"
MASCARA_TARJETA_EN_PABELLON_B           ="255.255.255.0"

COMANDOS_INICIO="""
enable
configure terminal
"""
EL_ROUTER_USA_IP_FIJA=True


def generar_comandos_subinterfaces():
    COMANDOS_SUBINTERFACES=[]

    for numero_de_aula in AULAS:
        COMANDOS_SUBINTERFAZ=[]

        NUMERO_VLAN     =   numero_de_aula * 10
        DIRECCION_IP    =   "10.{0}.0.254".format(numero_de_aula)

        COMANDO_CREACION_SUBINTERFAZ    =   "interface {0}.{1}".format(TARJETA_PABELLON_B, NUMERO_VLAN)
        COMANDO_ENCAPSULACION           =   "encapsulation dot1q {0}".format(NUMERO_VLAN)
        COMANDO_ASIGNACION_IP           =   "ip address {0} {1}".format(DIRECCION_IP, MASCARA_PABELLON_B)
        ENCENDIDO_INTERFAZ              =   "no shutdown"
        COMANDO_NAT_INSIDE              =   "ip nat inside"
        COMANDO_SALIDA                  =   "exit"
        

        COMANDOS_SUBINTERFAZ.append(    COMANDO_CREACION_SUBINTERFAZ    )
        COMANDOS_SUBINTERFAZ.append(    COMANDO_ENCAPSULACION           )
        COMANDOS_SUBINTERFAZ.append(    COMANDO_ASIGNACION_IP           )
        COMANDOS_SUBINTERFAZ.append(    COMANDO_NAT_INSIDE              )
        COMANDOS_SUBINTERFAZ.append(    ENCENDIDO_INTERFAZ              )
        COMANDOS_SUBINTERFAZ.append(    COMANDO_SALIDA                  )

        #Y finalmente añadimos este grupo de comandos a la lista
        COMANDOS_SUBINTERFACES.append("\n".join(COMANDOS_SUBINTERFAZ))
    
    return COMANDOS_SUBINTERFACES


def get_acl():
    comandos=[]
    comandos.append("access-list 100 permit ip 10.0.0.0 0.255.255.255 any")
    comandos.append("ip nat inside source list 100 interface {0} overload".format(
        TARJETA_ESCUELAS_CONECTADAS
    ))
    return comandos

def poner_ip_con_dhcp_en_tarjeta_de_salida():
    COMANDOS=[]
    COMANDOS.append("interface "+TARJETA_ESCUELAS_CONECTADAS)
    COMANDOS.append("ip address dhcp");
    COMANDOS.append("ip nat outside")
    COMANDOS.append("exit")
    return COMANDOS



def get_ruta(ip, mascara, tarjeta_de_salida):
    comando="ip route {0} {1} {2}".format(ip, mascara, tarjeta_de_salida)
    return comando

def get_comandos_rutas_aulas():
    comandos=[]
    for aula in AULAS:
        red="10.{0}.0.0".format(aula)
        comando_ruta=get_ruta(red, MASCARA_PABELLON_B, TARJETA_PABELLON_B)
        comandos.append(comando_ruta)
    return comandos


def poner_ip_en_tarjeta(nombre_tarjeta, ip, mascara, tipo_nat):
    COMANDOS=[]
    #Entramos en la tarjeta del escuelas conectadas
    COMANDOS.append("interface {0}".format(nombre_tarjeta))
    COMANDOS.append(
            "ip address {0} {1}".format(
                ip, mascara)
        )
    COMANDOS.append("ip nat {0}".format(tipo_nat))
    COMANDOS.append("exit")
    return COMANDOS

def poner_dhcp_en_tarjeta(nombre_tarjeta, tipo_nat):
    COMANDOS=[]
    #Entramos en la tarjeta del escuelas conectadas
    COMANDOS.append("interface {0}".format(nombre_tarjeta))
    COMANDOS.append("ip address dhcp")
    COMANDOS.append("ip nat {0}".format(tipo_nat))
    COMANDOS.append("exit")


def poner_ruta_por_defecto(gateway):
    COMANDOS=[]
    COMANDOS.append("ip route 0.0.0.0 0.0.0.0 {0}".format(gateway))
    return COMANDOS

def poner_ip_en_tarjeta_de_salida():
    COMANDOS=[]
    
    #Entramos en la tarjeta del escuelas conectadas
    COMANDOS.append("interface {0}".format(TARJETA_ESCUELAS_CONECTADAS))
    #Si usamos IP FIJA
    if EL_ROUTER_USA_IP_FIJA:
        #Asignamos la IP
        COMANDOS.append(
            "ip address {0} {1}".format(
                IP_HACIA_ESCUELAS_CONECTADAS, MASCARA_ESCUELAS_CONECTADAS)
        )
        
    else:
         COMANDOS.append("ip address dhcp" )   
    #Marcamos la tarjeta como NAT de salida
    COMANDOS.append("ip nat outside")
    COMANDOS.append("exit")
    COMANDOS.append(
            "ip route 0.0.0.0 0.0.0.0 {0}".format(GATEWAY_SALIDA_ESCUELAS_CONECTADAS)
        )
    #Y salimos

    #Establecemos las rutas hacia el interior del pabellón B
    
    COMANDOS=COMANDOS+rutas

    #Establecemos la ACL para hacer el nat de salida
    acls=get_acl()
    COMANDOS=COMANDOS+acls
    COMANDOS.append("exit")
    return COMANDOS


if __name__=="__main__":
    print(COMANDOS_INICIO)
    # lista=generar_comandos_subinterfaces()
    # print("\n".join(lista))
    
    rutas=get_comandos_rutas_aulas()
    print("\n".join(rutas))

    ruta_por_defecto=poner_ruta_por_defecto(GATEWAY_SALIDA_ESCUELAS_CONECTADAS)
    
    config_tarjeta_hacia_pabellon_b=poner_ip_en_tarjeta(TARJETA_PABELLON_B, IP_DENTRO_PABELLON_B, MASCARA_PABELLON_B, "inside")
    print("\n".join(config_tarjeta_hacia_pabellon_b))
    
    config_tarjeta_salida=poner_ip_en_tarjeta(TARJETA_ESCUELAS_CONECTADAS, IP_HACIA_ESCUELAS_CONECTADAS, MASCARA_ESCUELAS_CONECTADAS, "outside")
    print("\n".join(config_tarjeta_salida))

    acls=get_acl()
    print("\n".join(acls))
    