#!/usr/bin/python3


from utilidades.ip.ipv4 import GeneradorIPV4Azar
from random import randint
from pytablewriter import RstSimpleTableWriter

class GeneradorEjercicioMascaras(object):
    def __init__(self, num_ejercicio, tuplas) -> None:
        super().__init__()
        self.bits_para_los_host=randint(3,6)
        self.bits_para_las_subredes=randint(3,6)
        self.total_subredes=(2**self.bits_para_las_subredes)-2
        self.total_hosts=(2**self.bits_para_los_host)-2
        self.total_bits_necesarios_para_ejercicio= self.bits_para_las_subredes+self.bits_para_los_host
        self.bits_mascara=32-self.bits_para_los_host
        self.generador_ips=GeneradorIPV4Azar(
            num_ejercicio, cantidad_bits_mascara=32-self.total_bits_necesarios_para_ejercicio)
        self.mascara_vieja_en_decimal=self.generador_ips.get_mascara_en_decimal()
        self.mascara_en_decimal=self.mascara_vieja_en_decimal
        self.num_ejercicio=num_ejercicio

    def get_cantidades_hosts_azar(self):
        print(self.generador_ips.direccion)

    def get_enunciado(self):
        texto="""
Ejercicio {3}
-------------------

Se dispone del siguiente prefijo de red ``{0}``, pero despues de analizar las necesidades se ha observado que se necesitan {1} subredes en las que como
máximo habrá {2} host. Desglosar para cada subred las direcciones IP de subred, la primera IP asignable, la última IP asignable
y la dirección de broadcast. Ignorar las subredes con todos los bits a 0 y las subredes con todos los bits a 1.
        """

        enunciado=texto.format(
            self.generador_ips.direccion,
            self.total_subredes,
            self.total_hosts,
            self.num_ejercicio
        )
        return enunciado

    

    def get_lista_subredes(self):
        subredes=self.generador_ips.direccion.subnets(prefixlen_diff=self.bits_para_las_subredes)
        return list(subredes)
    
    def get_primera_y_ultima_ip(self, subred):
        hosts=list(subred.hosts())
        return (hosts[0], hosts[1])

    def get_direcciones(self, subred):
        hosts=list(subred.hosts())
        return (subred.network_address, hosts[0], hosts[-1], subred.broadcast_address)

    def get_cadena_formato_red(self, subred, encabezado):
        (ip_de_red, primera_ip, ultima_ip, ip_difusion)=self.get_direcciones(subred)
        solucion=f'\n{encabezado} subred\n~~~~~~~~~~~~~~\n\n'  \
            f'* IP  de red: ``{ip_de_red}``\n'\
            f'* Primera IP asignable: ``{primera_ip}``\n'\
            f'* Última IP asignable: ``{ultima_ip}``\n' \
            f'* IP de difusión:``{ip_difusion}``\n'
        return solucion

    def get_filas_subred(self, prefijo, bits_red, num_subred, bits_subred):
        pass


    def get_solucion(self):
        inicio=f'Solución al ejercicio {self.num_ejercicio} de subredes\n----------------------------------------------------------------\n'\
            f'Nos dan el prefijo {self.generador_ips.direccion} (o poniendo la máscara vieja en decimal {self.mascara_vieja_en_decimal}) '\
            f'Nos piden {self.total_subredes} subredes con {self.total_hosts} hosts cada una. '
        #print("Diferencia:"+str(self.bits_para_las_subredes))
        subredes=self.get_lista_subredes()
        #print(subredes)
        encabezamiento=f'Para conseguir esta estructura usaremos {self.bits_para_las_subredes} bits de subred ' \
        f' y {self.bits_para_los_host} bits de host. La máscara nueva será {self.mascara_en_decimal} (en formato CIDR un prefijo/{self.bits_mascara})'\
            f' y el desglose de direcciones sería este:\n\n' 
        primera_subred=subredes[1]
        segunda_subred=subredes[2]
        ultima_subred=subredes[-2]
        txt_primera_subred=self.get_cadena_formato_red(primera_subred, "Primera")
        txt_segunda_subred=self.get_cadena_formato_red(segunda_subred, "Segunda")
        txt_ultima_subred=self.get_cadena_formato_red(ultima_subred, "Última")
        
        return inicio+encabezamiento + txt_primera_subred + txt_segunda_subred + txt_ultima_subred        

    def convertir_a_binario(self, numentero, anchura_bits):
        binario=bin(numentero)
        resultado=binario[2:].zfill(anchura_bits)
        #print("El resultado es:<"+resultado+">")
        return resultado
    
    def entrecomillar(self, cadena):
        return "``"+str(cadena)+"``"

    def get_filas(self, prefijo, subred_en_binario, objeto_subred):

        id_host_difusion=(2**self.bits_para_los_host)-1
        id_ultimo_host=id_host_difusion-1

        host_0_en_binario=self.convertir_a_binario(0, self.bits_para_los_host)
        host_1_en_binario=self.convertir_a_binario(1, self.bits_para_los_host)
        ultimo_host      =self.convertir_a_binario(id_ultimo_host, self.bits_para_los_host)
        host_difusion    =self.convertir_a_binario(id_host_difusion, self.bits_para_los_host)

        (ip_de_red, primera_ip, ultima_ip, ip_difusion)=self.get_direcciones(objeto_subred)
        
        filas=[]
        
        fila1=[prefijo, subred_en_binario, host_0_en_binario, ip_de_red, "Dirección de red"]
        fila1=list(map(self.entrecomillar, fila1))
        filas.append(fila1)

        fila2=[prefijo, subred_en_binario, host_1_en_binario, primera_ip, "Primera IP asignable"]
        fila2=list(map(self.entrecomillar, fila2))
        filas.append(fila2)

        fila3=[prefijo, subred_en_binario, ultimo_host, ultima_ip, "Última IP asignable"]
        fila3=list(map(self.entrecomillar, fila3))
        filas.append(fila3)

        fila4=[prefijo, subred_en_binario, host_difusion, ip_difusion, "IP de broadcast"]
        fila4=list(map(self.entrecomillar, fila4))
        filas.append(fila4)

        return filas



    def get_desglose(self):
        subredes=self.get_lista_subredes()
        primera_subred=subredes[1]
        segunda_subred=subredes[2]
        ultima_subred=subredes[-2]
        texto=f"El prefijo de red es {self.generador_ips.prefijo}\n"
        subredes=[  (1,primera_subred) ,
                    (2,segunda_subred),
                    (self.total_subredes-1, ultima_subred)]
        resultado=[]
        for subred, objeto_subred in subredes:
            subred_en_binario=self.convertir_a_binario(subred, self.bits_para_las_subredes)
            filas=self.get_filas(self.generador_ips.prefijo, subred_en_binario, objeto_subred)
            resultado=resultado+filas
        return resultado

    def get_desglose_subred(self, id_subred, objeto_subred):
        prefijo=self.generador_ips.secuencia_binaria[0:self.generador_ips.bits_mascara]
        subred_en_binario=self.convertir_a_binario(id_subred, self.bits_para_las_subredes)
        filas=self.get_filas(prefijo, subred_en_binario, objeto_subred)
        return filas

    def get_tabla(self, id_subred, objeto_subred):
        valores=self.get_desglose_subred(id_subred, objeto_subred)
        tipos_cabeceras=[   "Prefijo de red", "ID de subred", 
                            "ID de host", "IP", "Concepto"]
        escritor_tablas=RstSimpleTableWriter(table_name=f'Subred {id_subred}', headers=tipos_cabeceras, value_matrix=valores)
        return str(escritor_tablas)

    def get_tablas(self):
        subredes=self.get_lista_subredes()
        primera_subred=subredes[1]
        segunda_subred=subredes[2]
        ultima_subred=subredes[-2]
        subredes=[  (1,primera_subred) ,
                    (2,segunda_subred),
                    (self.total_subredes-1, ultima_subred)]
        texto_tablas=""
        for subred, objeto_subred in subredes:
            tabla=self.get_tabla(subred, objeto_subred)
            texto_tablas+="\n\n"+tabla
        return texto_tablas

if __name__=="__main__":
    ejercicios=[]
    
    MAX_EJERCICIOS=50


    encabezamiento="""
Anexo: cálculo de subredes
==========================
"""
    print(encabezamiento)
    for i in range(1, MAX_EJERCICIOS):
        g=GeneradorEjercicioMascaras(i)
        ejercicios.append(g)
    for i in range(1, MAX_EJERCICIOS):
        g=ejercicios[i-1]
        print (g.get_enunciado())
        
    for i in range(1, MAX_EJERCICIOS):
        g=ejercicios[i-1]
        print (g.get_solucion())
        print (g.get_tablas())
