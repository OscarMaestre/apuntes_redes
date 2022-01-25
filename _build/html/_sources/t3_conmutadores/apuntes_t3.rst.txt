Configuración y administración de conmutadores
===================================================

Segmentación de la red.
----------------------------
En primer lugar analicemos una red grande.

.. figure:: 01-red-grande.png

En una red como la que mostramos, puede haber muchos enviando y recibiendo a la vez. ¿Qué ocurre si un nodo genera una difusión? En redes tan grandes, la cantidad de "perjudicados" por una difusión, aumenta mucho. De hecho aumenta más cuanto más ordenadores hay en un switch.



Ventajas que presenta.
============================

En este sentido, los switches pueden ayudar a aliviar problemas de congestión usandolos como divisores de redes. Una red grande se puede dividir en dos redes más pequeñas y mejorar el rendimiento. Por desgracia esto implica dos cosas:

* Coste. Donde antes había un switch ahora hay dos.
* Trabajo. Recablear toda una sala es algo lento.


Conmutadores y dominios de colisión y "broadcast".
======================================================
Se denomina "dominio de colisión" al conjunto de máquinas que pertenecen a un mismo enlace o red local y en el que una de esas máquinas puede perjudicar a las demás sin querer.

Se denomina "dominio de broadcast" al conjunto de máquinas en las que UNA DIFUSIÓN IP (es decir, un paquete en el que la IP de destino es algo como 192.168.1.255) puede perjudicar a las demás sin querer. Un dominio de broadcast puede abarcar muchas redes Ethernet, o lo que es lo mismo, un dominio de broadcast puede abarcar muchos dominios de colisión. En la imagen siguiente puede verse una red muy grande compuesta por varias redes más pequeñas. Una difusión IP generada por una máquina cualquiera *podría ser recibida por todos los equipos de esa red*

.. figure:: 02-dominio-broadcast.png

Formas de conexión al conmutador para su configuración.
---------------------------------------------------------------

Cables 
~~~~~~~~~~~~~~
Los switches Cisco aceptan varios tipos de cable para conectar un PC con ellos y enviarles comandos:

1. Cable de red típico. Muchos switches por defecto **traen deshabilitado el acceso por medio de este tipo de cable**.
2. Cable de consola.


Protocolos
~~~~~~~~~~~~~~~

* Telnet: un protocolo muy simple que **no cifra los datos**
* SSH: es el que debería usarse siempre porque entre otras ventajas SSH **cifra datos**.



Práctica: intercepción de contraseñas.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Descarga Putty en tu Windows e instala los siguientes páquetes en tu máquina virtual Ubuntu::

    sudo apt-get update -y
    sudo apt-get install wireshark openssh-server telnetd

Ve a tu máquina Ubuntu y crea un usuario para él que además pertenezca al grupo administrador (grupo ``sudo``). Usa estos comandos::

    sudo adduser pepe
    sudo usermod -a -G sudo pepe

Asegúrate de tener la tarjeta de tu máquina virtual en modo puente, arranca Wireshark y despues pide a tu compañero que use tanto Telnet como SSH para conectar con tu máquina. Intenta ver como envía la contraseña.


Configuración del conmutador.
Configuración estática y dinámica de la tabla de direcciones MAC.
Diagnóstico de incidencias del conmutador.
Las tormentas de "broadcast".
El protocolo Spanning-Tree.
