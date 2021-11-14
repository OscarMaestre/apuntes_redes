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

    def get_cantidades_hosts_azar(self):
        print(self.generador_ips.direccion)

    def get_enunciado(self):
        texto="""
Se dispone del siguiente prefijo de red {0}, pero despues de analizar las necesidades se ha observado que se necesitan {1} subredes en las que como
máximo habrá {2} host.
        """

        enunciado=texto.format(
            self.generador_ips.direccion,
            (2**self.bits_para_las_subredes-2),
            (2**self.bits_para_los_host)-2
        )
        return enunciado

    def get_lista_subredes(self):
        subredes=self.generador_ips.direccion.subnets(prefixlen_diff=self.bits_para_las_subredes)
        return list(subredes)
    
    def get_primera_y_ultima_ip(self, subred):
        hosts=list(subred.hosts())
        return (hosts[0], hosts[1])

    def get_solucion(self):
        print("Diferencia:"+str(self.bits_para_las_subredes))
        subredes=self.get_lista_subredes()
        print(subredes)
        primera_subred=subredes[1]
        ultima_subred=subredes[-2]
        print(primera_subred)
        print(ultima_subred)
        

if __name__=="__main__":
    g=GeneradorEjercicio(1, None)
    print (g.get_enunciado())
    print (g.get_solucion())