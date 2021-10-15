Caracterización de redes
==============================


Terminología: redes LAN, MAN y WAN, topologías, arquitecturas, protocolos.
-----------------------------------------------------------------------------
Apartados 1.2.2.2 hasta 1.2.3.2


Sistemas de numeración decimal, binario y hexadecimal.
-----------------------------------------------------------------------------
Apartado 8.1.1.5

Ejercicio: convertir a binario
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Convertir a binario:

* 43
* 67
* 95
* 121
* 193
* 217
* 675


Ejercicio: convertir a hexadecimal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* 5191
* 2193
* 21430
* 39810
* 46712




Conversión entre sistemas.
-----------------------------------------------------------------------------
Apartado 8.1.1.5


Arquitectura de redes.
-----------------------------------------------------------------------------
Apartados 1.3.1.1 hasta 1.3.2.4

Encapsulamiento de la información.
-----------------------------------------------------------------------------
Apartado 3.1.14

El modelo OSI.El modelo TCP/IP.
-----------------------------------------------------------------------------
Apartado 3.2.4.2

Las tecnologías "Ethernet".
-----------------------------------------------------------------------------
Apartados 5.1.1.1 hasta 5.3.1.2
Apartados 3.3.2.3

El protocolo ARP
-----------------------------------------------------------------------------
Tenemos esta situación:
* Un ordenador tiene la IP 192.168.1.10
* Otro ordenador tiene la IP 192.168.1.11
* Se desea enviar un bloque de datos desde el 192.168.1.10 hacia el  192.168.1.11

Los bloques de datos **NO SE PUEDEN ENVIAR DIRECTAMENTE DE UNA IP A OTRA IP**. El ordenador 192.168.1.10 no puede enviar directamente a ese ordenador que le han dicho. PRIMERO HAY QUE AVERIGUAR LA DIRECCIÓN ETHERNET DEL 192.168.1.11.

Podrían pasar dos cosas
1. El ordenador 192.168.1.10 ya sabía de alguna manera la MAC del 192.168.1.11
2. Si no la sabe TIENE QUE PREGUNTAR.

Al protocolo que hace preguntas y respuestas traduciendo de direcciones IP a MACs se le llama **protocolo ARP (Address Resolution Protocol)**

ARP funciona así:

1. El ordenador 192.168.1.10 envia los datos a su capa Ethernet. Esta capa no sabe cual es la MAC de ese destinatario 192.168.1.11, así que GENERA UN PAQUETE CON UNA PREGUNTA EN LA QUE PONE ESTO

        Dirección origen: La MAC del 192.168.1.10 (por ejemplo  00-01-96-cc-59-43)
        Dirección destino: FF-FF-FF-FF-FF-FF

2. El paquete llega a todo el mundo, y por supuesto también al 192.168.1.11, que lo abre, ve la pregunta y por tanto construye la respuesta:
    
        Dirección de origen: La MAC del 192.168.1.11 (por ejemplo 00.30.f2.d.6e.34)
        Dirección de destino: La MAC del 192.168.1.10 (00-01-96-cc-59-43)

3. El paquete de respuesta llega al que preguntó, el cual ya puede enviar los datos a la dirección Ethernet correcta.


El modelo OSI y "Ethernet".
-----------------------------------------------------------------------------
Apartado 3.2.4.4 página 142

Tipos de cableado "Ethernet".
-----------------------------------------------------------------------------
Cable UTP: apartado 4.2.1.3
Cable STP: apartado 4.2.1.4

Cableado estructurado: subsistemas troncales y horizontales.
-----------------------------------------------------------------------------

Algoritmo de acceso al medio CSMA/CD.
-----------------------------------------------------------------------------
Apartado 4.4.3.3 página 198

Estructura de la trama "Ethernet".
---------------------------------------------------------------------------
Apartado 4.4.4.6