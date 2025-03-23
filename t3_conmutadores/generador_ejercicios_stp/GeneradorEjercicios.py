from Generador import *
import subprocess

FIGURA="""
.. figure:: Grafo{0}.png
   :alt: Ejercicio {0} de STP

   Ejercicio {0} de STP

"""
def generar_ejercicio(num_ejercicio, num_nodos):
    g=Grafo(num_nodos)
    encabezado=f"\nEjercicio STP {num_ejercicio}\n"
    encabezado+="-----------------------------------------------"

    texto=[]
    texto.append(encabezado)
    texto.append("Indicar el estado final en que quedará una red de switches que ejecutan STP. Ten en cuenta que el número de un switch es *irrelevante.* Lo que importa son las prioridades y las MAC más pequeñas. Las prioridades de los switches son:\n")
    texto.append(g.get_nodos_punteados())
    texto.append("\nLas conexiones entre switches son:\n\n")
    texto.append(g.get_aristas_punteadas())
    texto.append("\n")
    texto.append(FIGURA.format(num_ejercicio))
    texto.append("\n")
    texto.append(f"\nSolución al ejercicio STP {num_ejercicio}")
    texto.append("-----------------------------------------------")
    g.resolver_stp()
    nombre_archivo_dot=f"Grafo{num_ejercicio}.dot"
    nombre_archivo_png=f"Grafo{num_ejercicio}.png"
    g.guardar_grafo_dot(nombre_archivo_dot)
    texto.append("\n")
    raiz=g.averiguar_switch_raiz()
    texto.append(f"Switch raíz {raiz.get_prioridad()}\n\n")
    texto.append("A continuación se indica cada switch con el formato prioridad:mac-mas-baja junto al estado de sus puertos.\n")
    texto.append(g.get_estado_puertos())
    comando=f"dot -Tpng {nombre_archivo_dot} > {nombre_archivo_png}"
    subprocess.run(comando, shell=True)

    return "\n".join(texto)

def generar_archivo_ejercicios(nombre_archivo):
    ejercicios=[]
    ejercicios.append("Ejercicios de STP")
    ejercicios.append("==========================")
    for num_ejercicio in range(1,10):
        texto_ejercicio=generar_ejercicio(num_ejercicio, 5)
        ejercicios.append(texto_ejercicio)
    
    for num_ejercicio in range(11,20):
        texto_ejercicio=generar_ejercicio(num_ejercicio, 6)
        ejercicios.append(texto_ejercicio)
    
    for num_ejercicio in range(21,30):
        texto_ejercicio=generar_ejercicio(num_ejercicio, 7)
        ejercicios.append(texto_ejercicio)

    for num_ejercicio in range(31,40):
        texto_ejercicio=generar_ejercicio(num_ejercicio, 8)
        ejercicios.append(texto_ejercicio)
    
    texto_final="\n".join(ejercicios)
    with open(nombre_archivo, "w") as fich:
        fich.write(texto_final)
    
if __name__=="__main__":
    generar_archivo_ejercicios("Ejercicios_stp.rst")