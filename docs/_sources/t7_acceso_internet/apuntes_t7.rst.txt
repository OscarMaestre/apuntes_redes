Tema 7: Configuración del acceso a Internet desde una LAN
==============================================================

Direccionamiento interno y direccionamiento externo.
----------------------------------------------------------------------------

Desde el punto de vista del administrador de redes, estos términos se refieren a lo siguiente:

* Direccionamiento interno: es el conjunto de direcciones de la red que administramos.
* Direccionamiento externo: al conjunto del resto de direcciones.

La mayor parte de las veces, el direccionamiento interno usa direcciones privadas, que ocupaban este rango:

* 10.0.0.0/8
* 172.16.0.0/12 (es decir desde 172.16.0.0 hasta 172.31.255.255)
* 192.168.0.0/16 (es decir desde 192.168.0.0 hasta 192.168.255.255)

NAT origen y NAT destino.NAT estático, dinámico, de sobrecarga (PAT) e inverso.
---------------------------------------------------------------------------------
Ocurre que como muchas redes usan direcciones privadas, es necesario hacer algo para conseguir que los paquetes vayan correctamente del origen al destino incluso aunque ambos "tengan la misma IP".

El proceso que consigue esto se denomina NAT, que consiste básicamente en que los router modifican las IP de origen y de destino. Para ello se apoyan en que los propios router tienen una dirección pública, es decir, una que no tiene nadie más. 

NAT viene de Network Address Translation (traducción de direcciones de red). Este proceso se puede hacer de muchas maneras (muchas son obsoletas).

NAT origen
~~~~~~~~~~~~~~~
Esto significa que el router modifica la IP de origen cuando un paquete intenta salir desde una red interna que usa direcciones privadas.

NAT destino
~~~~~~~~~~~~~~~
Esto significa que el router al cual llega un paquete modifica la IP de destino.

NAT estático
~~~~~~~~~~~~~~~~~
Consiste en que el administrador asigna a cada IP de la red interna una traducción con una IP y un puerto FIJOS. Obsoleto, los router efectúan este proceso de manera automática y desde hace bastante tiempo.

NAT dinámico
~~~~~~~~~~~~~~~~
Lo contrario de lo anterior, el administrador define un conjunto de traducciones y el router las hace de manera automática o incluso el administrador no necesita definir nada y todas las "traducciones" las hace el router de manera automática.


NAT de sobrecarga (PAT)
~~~~~~~~~~~~~~~~~~~~~~~~
En realidad PAT es lo que hacen los router desde hace mucho tiempo, no NAT. PAT viene de Port Address Translation y lo que implica es que los router modifican los paquetes de salida "apuntando" el puerto por el que salen y asignando una IP de origen fija que es la pública del router.

Por costumbre, seguimos llamando NAT al proceso que se hace en nuestras casas. Algunas personas llaman también a este proceso "NPAT" (Network Port & Address Translation) o incluso "NAT de sobrecarga" (en realidad solo Cisco llama "de sobrecarga" a este proceso)

NAT inverso
~~~~~~~~~~~~~~~~~~
Se denomina así al proceso por el cual un router recibe un paquete entrante y modifica la IP de destino para redirigirlo a otra IP del interior de la red.


Configuración de NAT de sobrecarga o PAT.
----------------------------------------------------------------------------

El proceso básico es el siguiente:

1. Indicar las direcciones que se traducirán con ``access-list <número> permit <origen> <wildcard>``
2. Permitir la traducción metiendo esa lista y la tarjeta interna correspondiente con ``ip nat inside source list <número ACL> interface <interfaz> overload``.
3. Identificar la interfaz interna con ``ip nat inside``.
4. Identificar la interfaz externa con ``ip nat outside``.

Diagnostico de incidencias de NAT.
----------------------------------------------------------------------------
En router Cisco solo requiere usar el comando "show logging", ya se ha mencionado.


Configuración de PAT.
----------------------------------------------------------------------------
Se vió como hacer el NAT en el tema 5.


Diagnóstico de fallos de PAT.
----------------------------------------------------------------------------
En router Cisco solo requiere usar el comando "show logging", ya se ha mencionado.


Introducción a las tecnologías WAN: Frame Relay, RDSI, ADSL y 5G
----------------------------------------------------------------------------
En el examen no se preguntará ADSL, ni RDSI ni Frame Relay.

Conceptos básicos sobre telefonía móvil
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Los teléfonos móviles basan la conectividad en "células" de conectividad. Las compañías distribuyen antenas que ofrecen "cobertura" en distintas áreas de manera que el territorios esté lo más "cubierto" posible usando el mínimo número de antenas.

.. figure:: img/Red-alta-densidad.png


Para establecer una llamada, los teléfonos difunden señales de establecimiento de llamada que obligan a las antenas a coordinarse de manera que se establezca un circuito entre el origen y el destino.

.. figure:: img/red_movil.png

5G usa frecuencias cuya longitud de onda sitúa estas señales en el rango de los milímetros. A estas señales se les conoce como mmWave. Como la frecuencia es muy alta, la velocidad también puede serlo, pero hay un problema muy importante: la facilidad de propagación. 5G apenas consigue cruzar muros o puertas, por lo que no se prevee que a corto plazo reemplace las conexiones de cable/fibra que hay en los hogares.




.. figure:: img/5g-puerta-abierta.png
   :scale: 50%
   :align: center
   :alt: Propagación de mmWave sin obstáculos

   Propagación de mmWave sin obstáculos





.. figure:: img/5g-puerta-cerrada.png
   :scale: 50%
   :align: center
   :alt: Propagación de mmWave con obstáculos, incluso de baja densidad.

   Propagación de mmWave con obstáculos, incluso de baja densidad.



Tres bandas con distintas velocidades:

* 5G Low-Band: velocidades de 30 a 250 Mbits/s
* 5G Mid-band: 100 a 900 Mbits/s
* 5G High-band: mínimo 1 Gbits/s y hasta 4 Gbits/s




Aplicaciones 5G
~~~~~~~~~~~~~~~~~~~~~

5G pretende ofrecer estos tipos de servicio:

* eMBB: Enhanced Mobile BroadBand: "Banda ancha móvil mejorada" o "Internet rápido en el móvil"
* URLLC: Ultra Reliable Low-Latency Communications: "Comunicaciones ultra-fiables con una baja latencia" Como 5G ofrece tiempos de respuesta muy cortos puede utilizarse para monitorizar máquinas/dispositivos en tiempo real. Aún no está desplegado.
* mMTC: massive Machine Type Communications "Comunicaciones masivas entre máquinas". 





Las tecnologías Wifi y Wimax.
----------------------------------------------------------------------------

Las tecnologías UMTS y HSDPA.
----------------------------------------------------------------------------

Tecnologías emergentes basadas en cable e inalámbricas.
----------------------------------------------------------------------------

