#!/usr/bin/python3

def generar_tabla(filas, columnas):
    tabla=[]
    for fila in range(0, filas):
        vector_fila=[]
        for columna in range(0, columnas):
            numero=fila+(filas*columna)
            cad_numero=str(numero).rjust(4, " ")
            binario=bin(numero)
            binario=binario[2:].zfill(8)
            binario=binario[0:4]+"."+binario[4:]
            vector_fila=vector_fila+[cad_numero, binario]
        tabla.append(vector_fila)
    return tabla


def mostrar_ascii(tabla):
    texto=""
    separador_interno="---"
    for fila in tabla:
        for pos in range(0, len(fila), 2):
            num=fila[pos]
            binario=fila[pos+1]
            texto_fila="|  {0}{1}{2}   ".format(num, separador_interno, binario)
            texto=texto+texto_fila
        texto=texto+"  |\n"
    return texto
        



if __name__=="__main__":
    tabla=generar_tabla(64, 4)
    
    texto=mostrar_ascii(tabla)
    print(texto)
        
