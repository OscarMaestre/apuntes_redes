from utilidades.ip.ipv4 import GeneradorIPV4Azar
from random import randint

class GeneradorEjercicio(object):
    def __init__(self, num_ejercicio, tuplas) -> None:
        super().__init__()
        self.bits_para_los_host=randint(3,6)
        self.bits_para_las_subredes=randint(3,6)
        self.total_bits_necesarios_para_ejercicio= self.bits_para_las_subredes+self.bits_para_los_host
        self.bits_mascara=32-self.total_bits_necesarios_para_ejercicio
        self.generador_ips=GeneradorIPV4Azar(
            num_ejercicio, cantidad_bits_mascara=self.bits_mascara)
        self.num_ejercicio=num_ejercicio

    def get_cantidades_hosts_azar(self):
        print(self.generador_ips.direccion)

    def get_enunciado(self):
        texto="""
Ejercicio {3}
-------------------

Se dispone del siguiente prefijo de red {0}, pero despues de analizar las necesidades se ha observado que se necesitan {1} subredes en las que como
máximo habrá {2} host.
        """

        enunciado=texto.format(
            self.generador_ips.direccion,
            (2**self.bits_para_las_subredes-2),
            (2**self.bits_para_los_host)-2,
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
        return (hosts[0], hosts[1], hosts[-2], hosts[-1])

    def get_cadena_formato_red(self, subred, encabezado):
        (ip_de_red, primera_ip, ultima_ip, ip_difusion)=self.get_direcciones(subred)
        solucion=f'\n{encabezado} subred\n~~~~~~~~~~~~~~\n\n'  \
            f'* IP  de red: ``{ip_de_red}``\n'\
            f'* Primera IP asignable: ``{primera_ip}``\n'\
            f'* Última IP asignable: ``{ultima_ip}``\n' \
            f'* IP de difusión:{ip_difusion}\n'
        return solucion

    def get_solucion(self):
        inicio=f'Ejercicio {self.num_ejercicio}\n--------------------------------\n'\
            f'Nos piden {self.'
        #print("Diferencia:"+str(self.bits_para_las_subredes))
        subredes=self.get_lista_subredes()
        #print(subredes)
        encabezamiento=f'Usaremos {self.bits_para_las_subredes} bits de subred ' \
        f' y {self.bits_para_los_host} bits de host. El desglose sería este:\n\n' 
        primera_subred=subredes[1]
        segunda_subred=subredes[2]
        ultima_subred=subredes[-2]
        txt_primera_subred=self.get_cadena_formato_red(primera_subred, "Primera")
        txt_segunda_subred=self.get_cadena_formato_red(segunda_subred, "Segunda")
        txt_ultima_subred=self.get_cadena_formato_red(ultima_subred, "Última")
        
        return inicio+encabezamiento + txt_primera_subred + txt_segunda_subred + txt_ultima_subred        

if __name__=="__main__":
    ejercicios=[]
    MAX_EJERCICIOS=4
    for i in range(1, MAX_EJERCICIOS):
        g=GeneradorEjercicio(i, None)
        ejercicios.append(g)
    for i in range(1, MAX_EJERCICIOS):
        print (g.get_enunciado())
    for i in range(1, MAX_EJERCICIOS):
        print (g.get_solucion())