#!/usr/bin/python3


from utilidades.cisco.GeneradorEjerciciosVLAN import GeneradorEjerciciosVLAN


def main():
    enunciados=[]
    soluciones=[]
    for num_ejercicio in range(1, 19):
        encabezado="\n\nEjercicio VLANS/VTP {0}".format(num_ejercicio)
        encabezado+="\n---------------------------------------\n"
        g=GeneradorEjerciciosVLAN()
        g.generar_ejercicio()
        texto=g.get_enunciado()
        enunciados.append(encabezado+texto)

        solucion="\n\nSolución al ejercicio de VLANs {0}".format(num_ejercicio)
        solucion+="\n---------------------------------------\n"
        solucion+=g.get_solucion()

        soluciones.append(solucion)
    
    archivo="""
Ejercicios con VLANS y VTP
============================

{0}

{1}
"""
    textos_enunciados="\n\n".join(enunciados)

    textos_soluciones="\n\n".join(soluciones)

    with open("ejercicios_vlans.rst", "w") as fich:
        fich.write(archivo.format(textos_enunciados, textos_soluciones))

    
if __name__=="__main__":
    main()