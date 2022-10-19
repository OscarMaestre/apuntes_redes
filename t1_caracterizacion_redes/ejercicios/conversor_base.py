#!/usr/bin/env python3

from sre_compile import isstring
import pytablewriter
from random import choice, randint

class CambioRepresentacion(object):
    base16={
        0:("0","0000"),
        1:("1","0001"),
        2:("2","0010"),
        3:("3","0011"),
        4:("4","0100"),
        5:("5","0101"),
        6:("6","0110"),
        7:("7","0111"),
        8:("8","1000"),
        9:("9","1001"),
        10:("A","1010"),
        11:("B","1011"),
        12:("C","1100"),
        13:("D","1101"),
        14:("E","1110"),
        15:("F", "1111")
    }
    @staticmethod
    def get_valor_simbolo(simbolo):
        for i in range(0, 16):
            if CambioRepresentacion.base16[i][0]==simbolo:
                return i
        print("Error al convertir el simbolo "+i)
    @staticmethod
    def get_representacion(tupla, nuevabase):
      (cocientes, restos)=tupla
      #Es necesario invertir los restos
      restos.reverse()
      simbolos=[]
      simbolos.append(cocientes[-1])
      simbolos=simbolos+restos
      print("Los simbolos son:"+str(simbolos))
      if nuevabase==2 or nuevabase==8:
        resultado=list(map(str, simbolos))
        
        representacion="".join(resultado)
        return representacion
    @staticmethod
    def get_tabla_hexadecimal():
        filas=[]
        for num in range(0, 16):
            filas.append([num, CambioRepresentacion.base16[num][0]])
        return filas

    @staticmethod
    def get_tabla_binario():
        filas=[]
        for num in range(0, 16):
            filas.append([num, CambioRepresentacion.base16[num][1]])
        return filas
        
    @staticmethod
    def get_tabla_binariohexadecimal():
        filas=[]
        for num in range(0, 16):
            filas.append([CambioRepresentacion.base16[num][0], CambioRepresentacion.base16[num][1]])
        return filas
        
    @staticmethod
    def get_tabla_completa():
        filas=[]
        for num in range(0, 16):
            filas.append([num, CambioRepresentacion.base16[num][0], CambioRepresentacion.base16[num][1]])
        return filas

    @staticmethod
    def corregir_representacion( numero):
        if numero<10:
            return numero
        if numero>=10:
            plantilla="{0} (Símbolo {1})"
            return plantilla.format(numero, CambioRepresentacion.base16[numero][0])
        print("Error:"+str(numero))
        
    



class EjercicioDecimalABinario(object):
    def __init__(self, numero_decimal, num_ejercicio):
        self.numero_decimal=numero_decimal
        self.num_ejercicio=num_ejercicio
    
    def set_num_azar(self):
        self.numero_decimal=randint(512, 65500)
        
    def get_enunciado(self):
        plantilla="""
Ejercicio {0}
------------------
Convertir **{1}** (que está en decimal) a binario.
        """
        return plantilla.format(self.num_ejercicio, self.numero_decimal)

    def get_tabla_explicacion(self, numero_en_decimal, nuevabase):
        filas=[]
        numero=numero_en_decimal
        cocientes=[]
        restos=[]
        while numero>=nuevabase:
            resto=numero % nuevabase
            restos.append(resto)
            cociente=numero // nuevabase
            cocientes.append(cociente)
            filas.append([numero, nuevabase, cociente, resto])
            numero=cociente
        #Fin del while
        encabezados=["Dividendo", "Divisor", "Cociente", "Resto"]

        generadorTablas=pytablewriter.RstGridTableWriter()
        generadorTablas.headers=encabezados
        generadorTablas.value_matrix=filas
        return generadorTablas.dumps()

    def get_solucion(self):
        encabezado="""


Solución al ejercicio {0}
------------------------------
Convertir **{1}** (que está en decimal) a binario.
        
        """.format(self.num_ejercicio, self.numero_decimal)

        explicacion="""
El proceso consiste en dividir el número por 2 sucesivamente *hasta que no se pueda continuar*. Despues se coge **el último cociente y todos los restos en orden inverso** y se construye la secuencia binaria. Se ilustra en la tabla siguiente:

"""

        resultado="\n\nSi lo hacemos así, observaremos entonces que {0} en binario es **{1}**\n\n".format(self.numero_decimal, bin(self.numero_decimal)[2:])
        tabla=self.get_tabla_explicacion(self.numero_decimal, 2)
        return encabezado + explicacion + tabla + resultado



class EjercicioDecimalAHexadecimal(object):
    def __init__(self, numero_decimal, num_ejercicio):
        self.numero_decimal=numero_decimal
        self.num_ejercicio=num_ejercicio
    def set_num_azar(self):
        self.numero_decimal=randint(512, 65500)

    def get_enunciado(self):
        plantilla="""
Ejercicio {0}
------------------
Convertir **{1}** (que está en decimal) a hexadecimal.
        """
        return plantilla.format(self.num_ejercicio, self.numero_decimal)

    def corregir_representacion(self, numero):
        if numero<10:
            return numero
        if numero>=10:
            plantilla="{0} (Símbolo {1}"
            return plantilla.format(numero, CambioRepresentacion.base16[numero][0])
        print("Error:"+str(numero))

    def get_tabla_explicacion(self, numero_en_decimal, nuevabase):
        filas=[]
        numero=numero_en_decimal
        cocientes=[]
        restos=[]
        while numero>=nuevabase:
            resto=numero % nuevabase
            restos.append(self.corregir_representacion(resto))
            cociente=numero // nuevabase
            cocientes.append(cociente)
            filas.append([numero, nuevabase, cociente, self.corregir_representacion(resto)])
            numero=cociente
        #Fin del while
        encabezados=["Dividendo", "Divisor", "Cociente", "Resto"]

        #Si el último cociente es 10 o más hay que corregir el símbolo
        ultima_fila=filas[-1]
        columna=2
        
        ultimo_cociente=ultima_fila[columna]
        if ultimo_cociente>=10:
            filas[-1][columna]=self.corregir_representacion(ultimo_cociente)
        generadorTablas=pytablewriter.RstGridTableWriter()
        generadorTablas.headers=encabezados
        generadorTablas.value_matrix=filas
        return generadorTablas.dumps()

    def get_solucion(self):
        encabezado="""


Solución al ejercicio {0}
------------------------------
Convertir **{1}** (que está en decimal) a hexadecimal.
        
        """.format(self.num_ejercicio, self.numero_decimal)

        explicacion="""
El proceso consiste en dividir el número por 16 sucesivamente *hasta que no se pueda continuar*. Despues se coge **el último cociente y todos los restos en orden inverso** y se construye la secuencia hexadecimal. Se ilustra en la tabla siguiente:

"""

        resultado="\n\nSi lo hacemos así, observaremos entonces que {0} en hexadecimal es **{1}**\n\n".format(self.numero_decimal, hex(self.numero_decimal)[2:].upper())
        tabla=self.get_tabla_explicacion(self.numero_decimal, 16)
        return encabezado + explicacion + tabla + resultado


class EjercicioHexadecimalADecimal(object):
    def __init__(self, cadena_hexadecimal, num_ejercicio):
        if not isstring(cadena_hexadecimal):
            self.set_num_azar()
        else:
            self.secuencia_hexadecimal=cadena_hexadecimal.upper()
            self.numero_en_decimal=int(self.secuencia_hexadecimal, base=16)
        self.num_ejercicio=num_ejercicio
    def set_num_azar(self):
        self.numero_en_decimal=randint(512, 65500)
        self.secuencia_hexadecimal=hex(self.numero_en_decimal)[2:].upper()

    def get_enunciado(self):
        plantilla="""
Ejercicio {0}
------------------
Convertir **{1}** (que está en hexadecimal) a decimal.
        """
        return plantilla.format(self.num_ejercicio, self.secuencia_hexadecimal)


    def get_tabla_explicacion(self):
        inicio="Iremos analizando el número {0} de izquierda a derecha. Iremos multiplicando cada cifra (o el valor del símbolo) por la potencia correspondiente y al final lo sumaremos todo.".format(self.secuencia_hexadecimal)
        cadena=self.secuencia_hexadecimal
        exponente=len(self.secuencia_hexadecimal)-1
        valores_intermedios=[]
        textos=[]
        #print(cadena)
        while cadena!="":
            simbolo=cadena[0]
            valor_simbolo=CambioRepresentacion.get_valor_simbolo(simbolo)
            texto_simbolo=CambioRepresentacion.corregir_representacion(valor_simbolo)
            valor_intermedio=valor_simbolo*(16**exponente)
            multiplicador=(16**exponente)
            valores_intermedios.append(valor_intermedio)
            #print(texto_simbolo, exponente, valor_intermedio)
            textos.append("* {0} * 16 elevado a {1} = {0} * {3} = {2}".format(texto_simbolo, exponente, valor_intermedio, multiplicador))
            cadena=cadena[1:]
            exponente=exponente-1
        cadenas_valores_intermedios=list(map(str, valores_intermedios))
        # print(cadenas_valores_intermedios)
        suma="+".join(cadenas_valores_intermedios)
        textos.append("* Sumando: {0} = {1}".format(suma, self.numero_en_decimal))
        return "\n".join(textos)



    def get_solucion(self):
        encabezado="""


Solución al ejercicio {0}
------------------------------
Convertir **{1}** (que está en hexadecimal) a decimal.
        
        """.format(self.num_ejercicio, self.secuencia_hexadecimal)

        explicacion="""
El proceso consiste en dividir el número por 16 sucesivamente *hasta que no se pueda continuar*. Despues se coge **el último cociente y todos los restos en orden inverso** y se construye la secuencia hexadecimal. Se ilustra en la tabla siguiente:

"""

        resultado="\n\nPor tanto {0} en hexadecimal es **{1}**\n\n".format(self.secuencia_hexadecimal, self.numero_en_decimal)
        tabla=self.get_tabla_explicacion()
        return encabezado + explicacion + tabla + resultado


class GeneradorEjercicios(object):
    def __init__(self, maximo=50):
        self.lista=[]
        self.elecciones=[
            EjercicioDecimalABinario, EjercicioDecimalAHexadecimal,
            EjercicioHexadecimalADecimal
        ]
        for num in range(1, maximo+1):
            ejercicio=choice(self.elecciones)(num, num)
            ejercicio.set_num_azar()
            self.lista.append(ejercicio)
        
    def get_enunciados(self):
        textos=[]
        for ejercicio in self.lista:
            textos.append(ejercicio.get_enunciado())
        return "\n\n".join(textos)
                

    def get_soluciones(self):
        textos=[]
        for ejercicio in self.lista:
            textos.append(ejercicio.get_solucion())
        return "\n\n".join(textos)
        

#e=EjercicioDecimalABinario(254, 1)
e=EjercicioDecimalAHexadecimal(65535, 1)
print(e.get_enunciado())
print(e.get_solucion())

g=GeneradorEjercicios()
print(g.get_enunciados())
print(g.get_soluciones())

# print(CambioRepresentacion.get_tabla_binario())
# print(CambioRepresentacion.get_tabla_hexadecimal())
# print(CambioRepresentacion.get_tabla_binariohexadecimal())
# print(CambioRepresentacion.get_tabla_completa())