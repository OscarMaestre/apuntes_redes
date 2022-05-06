#!/usr/bin/python3


def generar_tabla(filas, columnas):
    tabla=[]
    salto=int(256/columnas)+1
    for num in range(0, salto):
        fila=[]
        for i in range(0, columnas):
            numero=(num*(i+1))
            cad_numero=str(numero).rjust(4, " ")
            binario=bin(numero)
            binario=binario[2:].zfill(8)
            fila=fila+[cad_numero, binario]
        tabla.append(fila)

    return tabla

def mostrar_ascii(tabla):
    texto=""
    separador="---"
    for fila in tabla:
        for pos in range(0, len(fila), 2):
            num=fila[pos]
            binario=fila[pos+1]
            texto_fila="{0}{1}{2}".format(num, separador, binario)
            texto=texto+texto_fila
        texto=texto+"\n"
    return texto
        



if __name__=="__main__":
    tabla=generar_tabla(64, 4)
    
    texto=mostrar_ascii(tabla)
    print(texto)
        
