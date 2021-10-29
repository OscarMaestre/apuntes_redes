import ipaddress
from random import randint
from pytablewriter import RstSimpleTableWriter
def generar_bloque_hexadecimal():
    #Decidimos si sacamos un bloque de ceros o no
    #En principio sacamos un cero
    numero_sacado=0
    if randint(0,1)==0:
        #Y si el azar dice otra cosa, cambiamos el numero
        numero_sacado=randint(0,65535)
    
    #Ahora formateamos el numero
    cadena_hex_python="{0:04x}".format(numero_sacado)
    return cadena_hex_python

def generar_ipv6():
    lista_bloques=[]
    for i in range(0, 8):
        bloque=generar_bloque_hexadecimal()
        lista_bloques.append(bloque)
    ip=":".join(lista_bloques)
    return ip

def comprimir_ipv6(ipv6):
    objeto_ip=ipaddress.ip_address(ipv6)
    return objeto_ip.compressed


def generar_parejas():
    num_ips=100
    lista_ips=[]
    for i in range(0, num_ips):
        ipv6=generar_ipv6()
        ipv6comprimida=comprimir_ipv6(ipv6)
        pareja=(ipv6, ipv6comprimida)
        lista_ips.append(pareja)
    return lista_ips



def generar_ejercicio():
    CADENA_TITULO="""
Anexo: Ejercicios sobre compresión de direcciones IPv6
-----------------------------------------------------------------------

Comprimir las direcciones IPv6 siguientes según las reglas de compresión del protocolo (las soluciones aparecen al final):

    """
    print (CADENA_TITULO)
    parejas=generar_parejas()
    num_ejercicio=1
    tipos_cabeceras=["Num ejercicio", "IPv6"]
    valores=[]
    for p in parejas:
        ip=p[0]
        cadena="``{0}``".format(ip)
        
        fila=[num_ejercicio, cadena]
        valores.append(fila)
        num_ejercicio=num_ejercicio+1
     #Fin del for 
    escritor_tablas=RstSimpleTableWriter(table_name="Ejercicios propuestos IPv6",
     headers=tipos_cabeceras, value_matrix=valores)
    
    escritor_tablas.write_table()


    CADENA_TITULO="""
Soluciones a compresión de direcciones IPv6
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


A continuación se muestran las soluciones a los ejercicios propuestos:

    """
    print (CADENA_TITULO)

    
    tipos_cabeceras=["Num ejercicio", "IPv6", "Comprimida"]
    valores=[]
    num_ejercicio=1
    for p in parejas:
        fila=[]
        ip=p[0]
        ip_comprimida=p[1]
        cadena_ip="``{0}``".format(ip)
        cadena_ip_comp="``{0}``".format(ip_comprimida)
        fila=[num_ejercicio, cadena_ip, cadena_ip_comp]
        valores.append(fila)
        num_ejercicio=num_ejercicio+1

    escritor_tablas=RstSimpleTableWriter(table_name="Ejercicios resueltos IPv6",
     headers=tipos_cabeceras, value_matrix=valores)
    
    escritor_tablas.write_table()
generar_ejercicio()