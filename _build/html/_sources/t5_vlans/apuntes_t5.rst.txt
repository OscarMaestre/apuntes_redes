Tema 4: Configuración de redes virtuales VLAN
====================================================

Introducción
--------------------
Las VLAN intentan dar solución a un problema consistente en que a veces ordenadores de una misma sala no forman parte de la misma red.

Es decir, queremos una red virtual formada por ordenadores que están en sitios distintos. La solución a este problema son las VLANs (Virtual Local Area Network).


El diseño de redes locales a tres capas (núcleo, distribución y acceso).
----------------------------------------------------------------------------
En general, para diseñar redes grandes se utiliza una topología llamada de tres niveles. Cada nivel va a cumplir funciones distintas del anterior. Estos niveles son núcleo, distribución y acceso.

* Se llama "switches de acceso" a aquellos switches que dan servicio directo a terminales como PCs, impresoras o similares.

* Se llama "switches de distribución" a *switches que interconectan switches de acceso*.

* Se llama "switches de núcleo" a *switches que interconectan switches de distribución y que están más cerca del punto de salida (router)*

En la figura puede verse una organización típica con tres capas.

.. figure:: img/02-tres-capas.png


Implantación y configuración de redes virtuales.
----------------------------------------------------------------------------

Implantación
~~~~~~~~~~~~~~~~~~~~
En primer lugar es IMPRESCINDIBLE disponer de hardware que soporte VLANs y a ser posible usando el protocolo estándar 802.1q.

1) Se debe entrar en el switch y crear las distintas VLANs (con un número).

2) Se deben asignar puertos del switch a esas VLAN. Estos puertos se denominan "puertos de acceso". Es importante recordar que las VLAN están unidas a los puertos del switch. Si tiramos del cable y se conectar ese cable de ordenador a otro puertos, habremos sacado al ordenador de su VLAN.

3) A menudo las VLAN deben pasar por varios switches. Habrá puertos que transporten tráfico de varias VLANs. Estos puertos se denominan "troncos" o "puertos troncales". Se debe avisar al switch de los puertos que actuarán como troncales.

Configuración
~~~~~~~~~~~~~~~~~~~~~~~~
Al crear la arquitectura de redes es **fundamental** que los usuarios no tengan acceso al cableado del switch. Una vez se les asigne una VLAN, dicha VLAN quedará asociada a la interfaz del switch. Si alguien tira del cable del switch y lo conecta a otra interfaz *el usuario quedará fuera de la VLAN*.

Para configurar dispositivos Cisco se usan comandos como estos::

    #Permiten convertirse en 
    #administrador y pasar al modo
    #de configuración global.
    enable
    configure terminal 

Para poner una interfaz del switch en modo acceso solo tenemos que hacer cuatro cosas:

1. Entrar en la interfaz correcta (recuérdese que es **fundamental** tomar nota correcta de la interfaz a la que va conectado cada terminal)
2. Poner la interfaz en modo acceso.
3. Asignar una ID de VLAN a ese interfaz.
4. Activar la conexión. En realidad no tiene por qué ser necesario pero debe recordarse que podríamos tener dispositivos en los que las interfaces no se encienden por defecto.

Así, los comandos necesarios serían estos::

    #Entramos en la interfaz
    interface fastethernet 0/1
    #Activamos el modo acceso
    switchport mode access
    #Indicamos la VLAN
    switchport access vlan 10
    #Activamos la tarjeta.
    no shutdown 
    #Salimos de esta tarjeta
    exit 
    #Entramos en la siguiente 
    #y configuramos el resto de
    #interfaces...
    interface fastethernet .. 

Definición de enlaces troncales en los conmutadores y routers.
----------------------------------------------------------------------------

Para configurar el acceso troncal, el proceso es parecido.

1. Entrar en la tarjeta
2. Activar el modo "trunk".
3. Indicar las VLANs que se autorizan
4. Encender la tarjeta
5. Hacer lo mismo en los dos lados del cable.

Los comandos serían::

    #Para entrar en la tarjeta
    interface fastethernet 0/1
    #Activar el modo troncal
    switchport mode trunk
    #Autorizamos la 10 y la 20
    switchport trunk allowed vlan 10,20
    
    #Activamos la conexión 
    no shutdown


En algunos dispositivos se pueden configurar muchas interfaces a la vez, haciendo esto::

    interface fastethernet 0/1-12
    switchport mode access
    switchport access vlan 30
    no shutdown


.. WARNING:: 
   Al construir VLANs y enlaces troncales se debe tener cuidado al "copiar y pegar configuraciones" de unos switches a otros. Podría ocurrir que sin querer autorizásemos VLANs en enlaces troncales que no debían permitir ese paso.

Reflexión sobre ciclos en switches con VLANs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Observa la figura siguiente

.. figure:: img/03-stp-ciclos.png

¿Por qué no se han deshabilitado puertos? En realidad sí se deshabilitan, pero cuando tenemos ciclos en switches que forman parte de VLANs puede ocurrir que **un puerto esté bloqueado dentro de una VLAN, pero esté activo dentro de otra VLAN distinta**. En realidad lo que ejecutan los switches modernos es PVST (Per-VLAN Spanning Tree)


    
Protocolos para la administración centralizada de redes virtuales; el protocolo VTP
----------------------------------------------------------------------------------------
En realidad **las VLAN no se crean "sobre la marcha" a medida que definimos los interfaces**. En redes grandes se establecen muy claramente dos cosas:

* El identificador de VLAN al que van a pertenecer un grupo de usuarios. 
* El *nombre de dicha VLAN*. Aunque los nombres no son estrictamente obligatorios **sí son muy recomendables**. En redes grandes pueden ser fundamentales para no perdernos en la asignación de interfaces a VLANs.

Este último punto es el que nos interesa. Para crear una VLAN y asociarle un nombre tenemos que dar estos pasos:

.. code-block: bash

    Switch1>enable
    Switch1#configure terminal
    Switch1(config)#vlan 10
    Switch1(config-vlan)#name Contabilidad
    Switch1(config-vlan)#exit
    Switch1(config)#vlan 20
    Switch1(config-vlan)#name Investigación
    Switch1(config-vlan)#exit
    

¿Qué ocurre si tenemos una red grande con varias decenas de VLANs? ¿Y si además de vez en cuando algunos nombres cambian o se crean otros nuevos? Evidentemente, conectarse a tantos switches tecleando una y otra vez los mismos comandos y/o cambiar los números o nombres correspondientes no solo es muy tedioso, sino propenso a errores. Para evitar esto tenemos un protocolo llamado VTP (VLAN Trunking Protocol) que nos va a facilitar la operativa.

Modos VTP
~~~~~~~~~

1. Servidor.
2. Cliente.
3. Transparente

Proceso básico
~~~~~~~~~~~~~~~
En el modo de configuración global tenemos que hacer esto:

1. Configurar dominio con el comando ``vtp domain acme.com``.
2. Configurar la clave con ``vtp password abcd1234``.
3. Configurar el modo con ``vtp mode client`` o ``vtp mode server``
4. Habilitar los interfaces troncales correspondientes.

Ejercicio completo con VLANs y VTP
--------------------------------------

Observa la red de la figura:

.. figure:: img/04-vlans-y-vtp.png

Las conexiones son las siguientes:

* Puerto 0/1 de Nucleo con puerto 0/1 de Distribucion1.
* Puerto 0/2 de Nucleo con puerto 0/2 de Distribucion2.
* Puerto 0/3 de Nucleo con puerto 0/1 de Distribucion3.
* Puerto 0/4 de Distribucion1 con puerto 0/4 de Acceso1.
* Puerto 0/5 de Distribucion1 con puerto 0/5 de Acceso2.
* Puerto 0/6 de Distribucion2 con puerto 0/6 de Acceso3.
* Puerto 0/7 de Distribucion2 con puerto 0/7 de Acceso4.
* Puerto 0/8 de Distribucion1 con puerto 0/8 de Acceso5.
* Puerto 0/9 de Distribucion1 con puerto 0/9 de Acceso6.
* PC 0 va conectado a puerto 0/1 de Acceso1.
* PC 1 va conectado a puerto 0/2 de Acceso1.
* PC 2 va conectado a puerto 0/1 de Acceso2.
* PC 3 va conectado a puerto 0/2 de Acceso2.
* PC 4 va conectado a puerto 0/1 de Acceso3.
* PC 5 va conectado a puerto 0/2 de Acceso3.
* PC 6 va conectado a puerto 0/1 de Acceso4.
* PC 7 va conectado a puerto 0/2 de Acceso4.
* PC 8 va conectado a puerto 0/1 de Acceso5.
* PC 9 va conectado a puerto 0/2 de Acceso5.
* PC 10 va conectado a puerto 0/1 de Acceso6.
* PC 11 va conectado a puerto 0/2 de Acceso6.
* Puerto 0/11 de Acceso1 va conectado a puerto 0/11 de Acceso2.
* Puerto 0/12 de Acceso2 va conectado a puerto 0/12 de Acceso3.
* Puerto 0/12 de Acceso1 va conectado a puerto 0/12 de Acceso5.
* Puerto 0/12 de Acceso5 va conectado a puerto 0/13 de Acceso6.

En esta red se desea lo siguiente:

1. Usando VTP se desea tener centralizada la información sobre VLANs en un único switch, en este caso el switch Nucleo. El dominio de la empresa es ``empresa.com`` y la clave que se va a usar es ``vtpadmin1234``.
2. La empresa va a tener estas VLANS con estos nombres: 10 (GESTIONVTP), 100 (USUARIOS), 200 (TECNICOS), 300 (GERENCIA)
3. El switch Acceso2 va a ser gestionado por sus propios técnicos y se desea que IGNORE por completo toda la información sobre VLANS.
4. Dentro de la VLAN USUARIOS están los ordenadores 0 y 2.
5. Dentro de la VLAN TECNICOS están los ordenadores 1 y 5.
6. Dentro de la VLAN GERENCIA están los ordenadores 6 y 8.
7. La empresa dispone de la red 10.0.0.0/8 para configurar direcciones IP y se desea que la VLAN USUARIOS esté en la red 10.1.0.0/16, que la VLAN TECNICOS esté en la 10.2.0.0/16 y que la VLAN GERENCIA esté en la 10.3.0.0/16

Configurar las direcciones IP, máscaras, enlaces de acceso, enlaces troncales y modos VTP para conseguir que la conectividad funcione según los requisitos pedidos.

Solución
~~~~~~~~~~~~~

Empecemos por las direcciones IP.

* Las direcciones de USUARIOS deben ser algo como 10.1.xxx.xxx con máscara 255.255.0.0. Usaremos las IP 10.1.0.1 y la 10.1.0.2 para los dos ordenadores de esta VLAN.
* Para TECNICOS usaremos las IP 10.2.0.1 y 10.2.0.2. También llevarán la máscara 255.255.0.0
* Para GERENCIA usaremos las IP 10.3.0.1 y 10.3.0.2 con máscara 255.255.0.0

Una vez hecho esto, los distintos ordenadores se pueden hacer ping solo con los de su subred. En este punto cabe preguntarse **¿para qué queremos entonces las VLAN?**.

Recordemos que al formar VLANs los distintos grupos de ordenadores quedan *totalmente aislados*. Esto significa que 

* Los de la VLAN USUARIOS **no reciben las difusiones Ethernet de ninguna otra VLAN** con lo que el rendimiento mejora. Recordemos que hemos dividido un dominio de colisiones grande en varios dominios de colisión pequeños.
* La seguridad también mejora porque nadie puede recibir tramas ni mensajes IP de ningún otra VLAN. 

Con solo una cualquiera de estas ventajas ya tendríamos suficiente para justificar la implantación de las VLANs, pero el hecho de obtener las dos hace que esta tecnología sea mucho más interesante aún.

Analicemos ahora las VLANs y los enlaces.

El protocolo IEEE802.1Q
----------------------------------------------------------------------------


Diagnóstico de incidencias en redes virtuales.
----------------------------------------------------------------------------






