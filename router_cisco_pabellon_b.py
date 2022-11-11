
NOMBRE_TARJETAS = "GigabitEthernet"
TARJETA_PABELLON_B=NOMBRE_TARJETAS+"0/0"
TARJETA_ESCUELAS_CONECTADAS=NOMBRE_TARJETAS+"0/1"
AULAS=[
    8,9,10,11,12,13,14,15
]

MASCARA_PABELLON_B="255.255.0.0"
MASCARA_ESCUELAS_CONECTADAS="255.255.255.128"

IP_ROUTER_CONECTADA_A_ESCUELAS_CONECTADAS="10.204.9.99"
GATEWAY_SALIDA_ESCUELAS_CONECTADAS="10.204.9.1"

COMANDOS_INICIO="""
enable
configure terminal
"""
EL_ROUTER_USA_IP_FIJA=False


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

def poner_ip_con_dhcp_en_tarjeta_de_salida():
    COMANDOS=[]
    COMANDOS.append("interface "+TARJETA_ESCUELAS_CONECTADAS)
    COMANDOS.append("ip address dhcp");
    COMANDOS.append("ip nat outside")
    COMANDOS.append("exit")
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
                IP_ROUTER_CONECTADA_A_ESCUELAS_CONECTADAS, MASCARA_ESCUELAS_CONECTADAS)
        )
        COMANDOS.append(
            "ip route 0.0.0.0 0.0.0.0 {0}".format(GATEWAY_SALIDA_ESCUELAS_CONECTADAS)
        )
    else:
         COMANDOS.append("ip address dhcp" )   
    #Marcamos la tarjeta como NAT de salida
    COMANDOS.append("ip nat outside")
    #Y salimos
    COMANDOS.append("exit")
    return COMANDOS


if __name__=="__main__":
    print(COMANDOS_INICIO)
    lista=generar_comandos_subinterfaces()
    print("\n".join(lista))
    config_tarjeta_salida=poner_ip_en_tarjeta_de_salida()
    print("\n".join(config_tarjeta_salida))