#!/usr/bin/python3


def generar_tabla(filas, columnas):
    tabla=[]
    salto=int(256/columnas)+1
    for num in range(0, salto):
        fila=[]
        for i in range(0, columnas):
            numero=(num*(i+1))
            binario=bin(numero)
            binario=binario[2:].zfill(8)
            fila=fila+[numero, binario]
        tabla.append(fila)
    for f in tabla:
        print(f)



if __name__=="__main__":
    generar_tabla(64, 4)
        
