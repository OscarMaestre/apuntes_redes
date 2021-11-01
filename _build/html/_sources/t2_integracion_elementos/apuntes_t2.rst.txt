Integración de elementos en una red
=========================================

Los medios físicos.
---------------------------------------------------
Apartado 1.2.1.4 Página 29

Los cables metálicos (coaxial, STP y UTP).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Cable coaxial: apartado 4.2.1.5, página 168.
* Cable UTP: apartado 4.2.2.1, página 170.
* Cable STP: apartado 4.2.1.4, página 167.

Fibra óptica y tipos de fibra.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Apartado 4.2.3.3, página 176.

Ancho de banda y tasa de transferencia.
---------------------------------------------------
Apartado 4.1.3.2 página 162

En realidad antes de comprender el ancho de banda necesitamos comprender algunos conceptos básicos y que indicamos en los siguientes apartados

Analógico vs digital
~~~~~~~~~~~~~~~~~~~~~~~~
* Una señal analógica es una señal en la que aceptamos cualquier valor.
* Una señal digital es una en la que solo se aceptan ciertos valores.

Parámetros de una señal. 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Se llama amplitud a la altura de una onda. Cabe destacar que por altura nos referimos a la distancia entre el punto más alto y más bajo de una señal.
* Se llama longitud de onda a la distancia que recorre una señal entera. Se mide en metros (o mm, o hasta nanómetros)
* Se llama fase al punto donde empieza y acaba la onda, que no tiene por qué ser siempre el punto 0 o el punto más alto.

Modulación
~~~~~~~~~~~~~~

Modificar parámetros de una señal para enviar 0 y 1. Si combinamos la modificación de muchos parámetros conseguiremos enviar más bits por segundo, pero la recepción se vuelve algo muy complejo.

Medidas
~~~~~~~~~~~~~~
En informática, en general 1K=1024. Sin embargo, en redes, las medidas como 1=1000. Por tanto si nos hablan de una conexión de 300Mbps, se refieren a 300*10e6. Además se debe recordar que:

* "b" (en minúscula) se refiere a *bits*.
* "B" (en mayúscula) se refiere a *bytes*.

Pero ¿entonces qué es el ancho de banda? Se define como la diferencia entre la frecuencia máxima que se acepta y la frecuencia mínima. Cuanto más ancha sea esa banda, más datos podremos meter. No es lo mismo que la *velocidad*.

La diferencia entre el ancho de banda y la velocidad, es lo que llamamos *rendimiento*, que se mide en porcentaje y nunca es del 100%

* Si tenemos una fibra de 600Mbps, y perdemos el 8% en protocolos, ¿a qué velocidad nos descargaremos un archivo?

Si pierdo el 8%, conservamos el 92, es decir 0.92*600=552Mbps. Si un archivo ocupa 400MB, entonces ocupa 400*8Mb, es decir 3200Mb, que en realidad es 3200*1024 Kb, o lo que es lo mismo 3200*1024*1024 bits, o sea 3.355.443.200 bits. Si queremos descargar esos 3.355.443.200 bits en una fibra de 552Mbps, aún tendremos que convertir 552 "medidas estándar", es decir 552.000.000 bits por segundo.

Conclusión: si dividimos 3.355.443.200 bits por 552.000.000 obtenemos 6,078 segundos.







Factores físicos que afectan a la transmisión.
---------------------------------------------------

La conexión inalámbrica.
---------------------------------------------------

Se han popularizado mucho por ofrecer una ventaja inexistente en otros medios: la movilidad. Las redes Wifi usan el estándar 802.11, del cual ha habido muchas variantes:

* 802.11a), fue el primero, que ofrecía un máximo de 11Mbps, un alcance de unos pocos metros.
* 802.11n) ofrece mucha más velocidad y alcance.

Aparte de eso, las redes Wifi son más inseguras.

Un detalle muy sutil es que en ocasiones los usuarios usan la clave correcta en la red equivocada.



Si nuestro portátil tiene una tarjeta WiFi 802.11n) y nuestro router wifi resulta ser 802.11 a) ambos dispositivos cambian automáticamente al protocolo más compatible, que será el más lento.

Toda red Wifi tiene un identificador llamado SSID. La costumbre es que los nodos difundan el nombre. Sin embargo no es obligatorio, puede activarse una opción con un nombre parecido a este "Not broadcast SSID"


Hay muchos tipos de conexiones:

* Wifi: conexión doméstica, con alcance alto y una velocidad alta.
* Bluetooth:  punto a punto, velocidad baja y un alcance bajo, consume muy poca energía.
* 4G, 5G. 


Los espectros de onda de microondas y radio.
---------------------------------------------------

Apartado....

Topologías.
---------------------------------------------------
* Bus: los equipos forman una línea y cada equipo tiene que averiguar al principio qué ordenadores están a su izquierda y cuales a su derecha. **Obsoleto**

* Anillo: antiguo,  los equipos se conectaban en círculo y había un sentido de giro en el envío de paquetes, el sistema era un poco mejor, pero los cortes en el cable producían errores en toda la red. **Muy improbable que sigan usándose.**

* Estrella: la conexión de los cables implica conectar todos los dispositivos a un punto central que retransmite los datos el equipo correcto. **Es prácticamente el único sistema que queda en uso**





Asociación y autenticación en la WLAN.
---------------------------------------------------

Se llama "autenticación" al proceso seguido por un punto de acceso para ver si un equipo va a tener permiso para enviar y recibir datos a través de ese punto de acceso.

Se llama "asociación" al proceso por el cual un dispositivo utiliza el permiso concedido en el punto anterior para enviar y recibir datos. 


Dentro de los sistemas de autenticación:

* Deshabilitado: cualquier puede asociarse al punto de acceso y transmitir y recibir.

* WEP (Wire Equivalent Privacy) usa un sistema de cifrado y un sistema de claves. Quien proporcione la clave correcta podrá asociarse al punto de acceso y enviar y recibir datos cifrados con una clave del router.

* WPA: usa un cifrado más potente y mucho más difícil de romper que WEP. 

* WPA2: va aún más lejos y ofrece una seguridad mucho mayor.

WEP, WPA y WPA2 suelen basarse un sistema llamado PSK (Pre-Shared Key o clave pre-compartida). En estos casos ponemos una clave en los router/puntos de acceso que luego también pondremos en los ordenadores. Estos sistemas suelen llamarse WPA-PSK y WPA2-PSK.


Existe una variante: WPA,WPA2 usan un tercer equipo que actúa de servidor de autenticación.

En todos los sistemas de autenticación ocurre lo siguiente:
* Los sistemas de cifrado pueden ser más potentes o más débiles. Los más potentes implican velocidades más lentas al gastar más tiempo en el cifrado y descifrado.
* Una vez que un dispositivo envía una petición de conexión el router/punto de acceso envía una petición de clave.
* Si el dispositivo envía una clave correcta, el router envía una clave de cifrado que se usará durante toda la sesión.

Dispositivos hardware en redes: hubs, APs, switches y routers
--------------------------------------------------------------


Dispositivos hay muchos, pero no todos ellos trabajan en la misma capa de red.

Hub
~~~~~~~~~

Un hub o concentrador es un dispositivo "tonto", cualquier paquete que reciba lo difunde por todos los puertos Ethernet. Por lo tanto es un dispositivo de capa de enlace.

Switch
~~~~~~~~~~~
Un switch es un dispositivo con un software incorporado que ejecuta un programa que apoyándose en una memoria RAM interna consigue enviar los paquetes **solo al destinatario correcto**. En un pequeño número sí generará colisiones, pero su número es muchísimo menor que el de un hub.

Ejemplo de simulación con switch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Supongamos que tenemos un switch. Supongamos que tenemos tres ordenadores:

* Ordenador con IP 192.168.1.20 con MAC 0A conectado al puerto 2 del switch.
* Ordenador con IP 192.168.1.21 con MAC 0B conectado al puerto 5 del switch.
* Ordenador con IP 192.168.1.22 con MAC 0C conectado al puerto 9 del switch.

Al principio la tabla del switch está en este estado:

+--------+-----+
| Puerto | Mac |
+--------+-----+
| 0      |     |
+--------+-----+
| 1      |     |
+--------+-----+
| 2      |     |
+--------+-----+
| 3      |     |
+--------+-----+
| 4      |     |
+--------+-----+
| 5      |     |
+--------+-----+
| 6      |     |
+--------+-----+
| 7      |     |
+--------+-----+
| 8      |     |
+--------+-----+
| 9      |     |
+--------+-----+

Ahora supongamos que en el 192.168.1.20 envía un ping al 192.168.1.22. El 192.168.1.20 mete el mensaje (que llevará la MAC de origen 0A dentro) en su cable que llega al switch.

El switch se encuentra con dos cosas:

1. No sabe en qué puerto está el ordenador 0C que es el destinatario final: **no tendrá más remedio que enviar ese paquete por todos los puertos menos por donde vino**

2. El switch acaba de aprender y apuntar en su tabla que el ordenador con la MAC 0A está en el puerto 2, así que ahora la tabla del switch queda como sigue:

+--------+-----+
| Puerto | Mac |
+--------+-----+
| 0      |     |
+--------+-----+
| 1      |     |
+--------+-----+
| 2      | 0A  |
+--------+-----+
| 3      |     |
+--------+-----+
| 4      |     |
+--------+-----+
| 5      |     |
+--------+-----+
| 6      |     |
+--------+-----+
| 7      |     |
+--------+-----+
| 8      |     |
+--------+-----+
| 9      |     |
+--------+-----+

El mensaje llegará a todos los ordenadores y casi todos lo descartarán pero el "ping" llegará correctamente al 0C el cual enviará un mensaje de respuesta usando como MAC de origen 0C. Ese mensaje llega al switch que ahora se encuentra con dos cosas:

1. El ordenador con la MAC 0C está conectado al puerto 9, así que ese conocimiento nuevo se apunta en la tabla quedará como sigue:

+--------+-----+
| Puerto | Mac |
+--------+-----+
| 0      |     |
+--------+-----+
| 1      |     |
+--------+-----+
| 2      | 0A  |
+--------+-----+
| 3      |     |
+--------+-----+
| 4      |     |
+--------+-----+
| 5      |     |
+--------+-----+
| 6      |     |
+--------+-----+
| 7      |     |
+--------+-----+
| 8      |     |
+--------+-----+
| 9      | 0C  |
+--------+-----+

2. El switch sabe que tiene que enviar un paquete al 0A así que analiza su tabla de direcciones. Al analizar su tabla y observar que tiene apunta que ese destinatario 0A está en el puerto 2 **EL PAQUETE SE ENVÍA SOLO POR EL PUERTO CORRECTO** sin generar colisiones en otros puntos de la red.

Direccionamiento. 
---------------------------------------------------

Hasta ahora hemos visto que hay muchas capas de red: enlace, red, transporte, aplicación. Cada capa tiene su propio sistema de direcciones:

* En Ethernet hemos aprendido que las direcciones son de 48 bits, que se escriben como parejas de números hexadecimales, por ejemplo 3a:d1:f3:55:a8:10. Se debe recordar que hay una dirección Ethernet especial llamada "dirección de broadcast" o "dirección de difusión". Cuando un dispositivo quiere enviar un mensaje a toda la red, pone la dirección ff:ff:ff:ff:ff:ff como dirección de destino. Esto se hace por ejemplo en ARP cuando un ordenador quiere averiguar la MAC teniendo solo su IP. Los switches SIEMPRE OBEDECEN ESAS DIFUSIONES.

* Si hay muchos sistemas de direcciones siempre va a ser necesario "traducir entre ellos". Y por ejemplo ya conocemos ARP (Address Resolution Protocol), el cual dada una IP usa difusiones para averiguar la MAC de dicho ordenador con esa IP.

Ethernet en realidad divide la MAC en dos partes: los tres primeros pares son el código de fabricante. Los tres últimos son el número de la tarjeta.

Dominios de colisión y de "broadcast".
---------------------------------------------------
* Se llama "dominio de colisión" al conjunto de equipos que son susceptibles de provocarse colisiones mutuamente. En general es mucho mejor para el rendimiento el tener muchos dominios pequeños en lugar de uno grande.

* Dominio de broadcast o dominio de difusión es el conjunto de ordenadores que reciben las difusiones de un ordenador.

Un dominio de difusón **NO TIENE POR QUÉ COINCIDIR** con el dominio de colisiones en una red.

Direcciones IPv4 y máscaras de red.
---------------------------------------------------
Las direcciones IP son las direcciones de la capa software de red más extendida. La capa de red va a ser capaz de enviar datos a sitios remotos. Las direcciones IP están pensadas para poder distinguir un dispositivo cualquiera de cualquier otro del mundo.

Las direcciones IP son software, son un parámetro de configuración. La capa de red sirve como "abstracción" de la capa de enlace Ethernet.

En esencia una dirección IP es una secuencia binaria de 32 bits, como esta:

10010000.11110001.01110011.10101011


Como son muy poco prácticas de manejar y recordar, se suele permitir el escribirlas como números en decimal separados por un punto.


* El primer byte de la dirección dada es 10010000, que en decimal es 144.
* El segundo byte es 11110001, que en decimal es 241.
* El tercer byte es 01110011, que en decimal es 115.
* El cuarto byte es 10101011, que en decimal es 171.

Por tanto esa IP era 144.241.115.171.



La idea original era que con 32 bits se podrían tener 2 a la 32 equipos, es decir 4.294.967.296 ordenadores.

Como aparentemente había direcciones de sobra, se decidió asignarlas en bloques. Como una IP debe servir para poner número a las redes, y dentro de las redes poner número a cada equipo de esa red, se decidió utilizar siempre una secuencia llamada máscara para poder distinguir cual es el número de red y cual es el número de host.


Supongamos que en un cierto sitio se tiene una red. Si en un ordenador nos han dado una secuencia de bits como la de arriba 10010000.11110001.01110011.10101011 (que en decimal era 144.241.115.171 ) ¿como saber cual es la parte de red y la parte de host. La clave es mirar ese parámetro llamado máscara. Supongamos que esa máscara es 255.0.0.0. Si la pasamos a binario sale que la máscara es 11111111.00000000.00000000.00000000.

+---------------+-------------------------------------------------+
| Num de red    |      Número de host                             |
+---------------+-------------------------------------------------+
| 10010000      | 11110001.01110011.10101011                      |
+---------------+-------------------------------------------------+


Protocolos de resolución de direcciones ARP, RARP.
---------------------------------------------------

Direcciones IPv6
---------------------------------------------------

Representación de direcciones
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dadas las limitaciones en las direcciones IPv4 se diseñó un nuevo formato de direcciones en el que hubiera muchas más posibilidades: **IPv6** En IPv6 hay *128 bits para direcciones* lo que supone un espacio de direcciones de 2 elevado a 128, un número realmente grande. Las direcciones IPv6 se escriben como secuencias de 8 grupos de 4 hexadecimales separadas por dos puntos, a continuación vemos algunos ejemplos::

    fe80:a13d:d3d6:a190:31d2:a216:3261:1800
    3410:0000:0000:0000:0000:0000:0000:2900

El segundo ejemplo muestra algo interesante y además muy habitual: **la mayor parte de las veces una dirección IPv6 tendrá muchos ceros consecutivos**. En ese caso, se puede abreviar esa dirección eliminando las secuencias de ceros **pero dejando un "doble dos puntos"** para indicar que hemos recortado una IPv6, así tendríamos que la última dirección la podemos escribir así::

    3410:0000:0000:0000:0000:0000:0000:2900 (sin abreviar)
    3410::2900 (abreviada)


Pero ¡cuidado! esta abreviatura debe hacerse con cuidado. Supongamos una IPv6 como esta::

    5199:0000:0000:1767:0000:0000:0000:00a5

Obsérvese que tenemos dos secuencias de ceros. Una de 8 ceros y otra de 12 ceros. La pregunta típica es ¿puedo abreviar ambos bloques? La respuesta es **NO**. Si escribiéramos la IPv6 así::

    5199::1767::00a5

entonces ocurriría que **la máquina no podría nunca saber cuantos ceros hay en cada bloque abreviado**. Por ello haremos lo siguiente:

1. El bloque más grande de ceros, lo eliminaremos y pondremos el "doble dos puntos".
2. El bloque de ceros más pequeño se "recorta" dejándolo con un solo cero por bloque.
3. Si algun bloque tiene ceros por la izquierda se pueden eliminar (igual que en la vida real da igual escribir 15 que 0015)

Así la dirección IPv6 5199:0000:0000:1767:0000:0000:0000:00a5

1. Se recorta primero por el bloque de ceros de la derecha y queda 5199:0000:0000:1767::00a5
2. Y el 5199:0000:0000:1767::00a5 se recorta de nuevo en los ceros de la izquierda para quedar como 5199:0:0:1767::00a5
3. Por último observamos que en el bloque final hay un 00a5 que se puede escribir como a5, así que nuestra dirección queda finalmente como *5199:0:0:1767::a5*


Tipos de direcciones
~~~~~~~~~~~~~~~~~~~~~~~~~~

Hay tres tipos básicos de direcciones IPv6: unicast, anycast y multicast.

* Las direcciones unicast son direcciones que indican una única conexión en todo Internet. Son las direcciones más comunes
* Las direcciones anycast se usan por lo administradores para "formar grupos". En anycast habrá muchas máquinas con la mismo IPv6 anycast pero cuando se envíe algo a esa dirección anycast **solo se enviará a uno de ellos**. Los router se encargarán de entregarlo a la máquina más cerca que tenga esa dirección anycast.
* Las direcciones multicast se usan en casos en los que varios nodos van a tener una misma IPv6 y cuando se envíe algo a esa IPv6 **todos la recibirán**.

Las direcciones reservadas por el IETF son las siguientes:


+----------------+-----------+--------------+-------------+--------------------+
| Uso            | Prefijo   | Primera IPv6 | Última IPv6 | Fracción que ocupa |
+================+===========+==============+=============+====================+
| Unicast global | 2000::/3  | 2000::/3     | 3fff::/3    | 1/8                |
+----------------+-----------+--------------+-------------+--------------------+
| Unicast local  | fc00::/7  | fc00::/7     | fdff::/7    | 1/128              |
| único          |           |              |             |                    |
+----------------+-----------+--------------+-------------+--------------------+
| Unicast local  | fe80::/10 | fe80::/10    | febf::/10   | 1/1024             |
| en enlace      |           |              |             |                    |
+----------------+-----------+--------------+-------------+--------------------+
| Multicast      | ff00::/8  | ff00:/8      | ffff:/8     | 1/256              |
+----------------+-----------+--------------+-------------+--------------------+

Conjuntos de protocolos IPv6
---------------------------------------------------

Túneles IPv6
---------------------------------------------------

Direccionamiento dinámico (DHCP).
---------------------------------------------------

Adaptadores.
---------------------------------------------------

Adaptadores alámbricos: instalación y configuración.Adaptadores inalámbricos: instalación y configuración.
-------------------------------------------------------------------------------------------------------------

Monitorización de la red mediante aplicaciones que usan el protocolo SNMP.
---------------------------------------------------------------------------------




.. include:: ejerciciosipv6/ejercicios_ipv6.rst

.. include:: ejercicios_ips/clasificacion_ipv6.rst