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
3. Cable auxiliar. Cada vez menos utilizado.


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
--------------------------------

El sistema operativo IOS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

IOS es el S.O de Cisco se maneja fundamentalmente por comandos. Sin embargo, cuando encendemos un switch/router por primera vez, no es posible acceder a ese sistema. Necesitamos proporcionar una configuración inicial. Y para ello, usaremos casi con toda seguridad el cable de consola.

El cable de consola es un cable propio de Cisco y por un lado usa una conexión propia de Cisco y en el otro extremos puede ser:

* USB (hoy en día lo más probable)
* RS-232 (aún muy utilizado, pero está cayendo en desuso)
* RJ-45 (depende del dispositivo)

Para acceder al sistema operativo necesitaremos un ordenador en el que haya algún programa de tipo "Terminal". Este programa enviará los datos directamente al dispositivo (sin direcciones de origen ni de destino ni nada). Es vital saber qué velocidades acepta el dispositivo al que nos conectamos. En el caso Cisco, es casi sin excepción:

* Velocidad: 9600 bits por segundo.
* Tamaño de los caracteres de datos: 8 bits.
* Paridad. Es un mecanismo de comprobación de comprobación de errores. Los dispositivos Cisco no usan paridad.
* Bits de stop. En Cisco se usa 1 bits de stop.
* Control de flujo/velocidad. No se usará ninguno.

En ocasiones se puede ver algo como 96008N1N. Esto significa "9600 bits/seg", "8 bits de datos", "No paridad", "1 bit de stop" y "No control de flujo".

Una vez que tenemos acceso al sistema operativo, debemos recordar que IOS es un sistema operativo modal.

1. El sistema operativo arranca en modo usuario. En ese modo lo único que se suele poder hacer es "visualizar", pero no "cambiar" ni "configurar". En suma, se usa el comando "show"
2. Para pasar al modo "privilegiado" se usa el comando ``enable``. Lo normal es que dicho modo tenga una clave. Para volver al modo usuario podemos usar ``disable``.
3. Para pasar al modo "configuración" se usa ``configure terminal`` desde el modo privilegiado.

La figura siguiente, tomada de Cisco, muestra los distintos modos:

.. figure:: 03-modos-cisco.png


El modo usuario
~~~~~~~~~~~~~~~~~

En este modo solo se pueden usar unos pocos comandos show. Por ejemplo:

* ``show interfaces`` muestra la información de todos los interfaces.
* ``show interfaces Fastethernet 0/1`` muestra solo la tarjeta 0/1

Modo privilegiado
~~~~~~~~~~~~~~~~~~

Comandos muy típicos:

* ``show running-config`` muestra la configuración en RAM.
* ``show startup-config`` muestra la configuración de arranque.
* ``show version``
* ``copy running-config startup-config``.

Modo de configuración global:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ``hostname <nombre>``

Configuración de contraseñas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Se puede poner contraseña a un montón de elementos:
* Contraseña al cable de consola.
* Contraseña de administrador para el modo privilegiado. 
* Contraseña al telnet.
* Contraseña SSH.
* Contraseña al puerto auxiliar.


Para poner contraseña a la conexión por cable de consola::

    Switch>enable
    Switch#configure terminal    
    Switch(config)#line console 0
    Switch(config-line)#password sesamo1234
    Switch(config-line)#login

Para poner una clave al modo de administrador::

    Switch>enable
    Switch#configure terminal
    Switch(config)#enable secret Admin1234!
    Switch(config)#exit
    Switch#copy running-config startup-config
    Switch#reload

.. WARNING::

   En muchos foros, manuales, tutoriales, vídeos se indica que el comando es "enable password" en lugar de "enable secret". Hace mucho tiempo que eso no es verdad. El comando Cisco fue durante mucho tiempo "enable password" y de hecho **el comando sigue funcionando**. Sin embargo, ``enable password`` guarda las claves en la memoria **SIN CIFRAR**.






Configuración estática y dinámica de la tabla de direcciones MAC.
Diagnóstico de incidencias del conmutador.
Las tormentas de "broadcast".
El protocolo Spanning-Tree.
