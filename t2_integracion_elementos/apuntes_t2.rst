Tema 2:Integración de elementos en una red
============================================

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
| 10010000 (144)| 11110001.01110011.10101011      (241.115.171)   |
+---------------+-------------------------------------------------+
| 11111111 (255)| 00000000.00000000.00000000.     (0.0.0.0)       |
+---------------+-------------------------------------------------+

Por desgracia en los comienzos de Internet las direcciones IP **se dividieron en bloques muy desiguales** lo que dió lugar a un tremendo desperdicio de direcciones. Estos bloques fueros llamados "clases de direcciones" y en los puntos siguientes desglosamos su composición:

+--------------------+----------+----------+----------+----------+-----------------+
| Patrón de clase A  | 0RRRRRRR | HHHHHHHH | HHHHHHHH | HHHHHHHH |                 |
+====================+==========+==========+==========+==========+=================+
| Primera            | 00000000 | 00000000 | 00000000 | 00000000 | 0.0.0.          |
| de clase A         |          |          |          |          |                 |
+--------------------+----------+----------+----------+----------+-----------------+
| Última de          | 01111111 | 11111111 | 11111111 | 11111111 | 127.255.255.255 |
| clase A            |          |          |          |          |                 |
+--------------------+----------+----------+----------+----------+-----------------+
| Máscara            | 11111111 | 00000000 | 00000000 | 00000000 | 255.0.0.0       |
| de clase A         |          |          |          |          |                 |
+--------------------+----------+----------+----------+----------+-----------------+
| Patrón clase B     | 10RRRRRR | RRRRRRRR | HHHHHHHH | HHHHHHHH |                 |
+--------------------+----------+----------+----------+----------+-----------------+
| Primera de clase B | 10000000 | 00000000 | 00000000 | 00000000 | 128.0.0.0       |
+--------------------+----------+----------+----------+----------+-----------------+
| Última de clase B  | 10111111 | 11111111 | 11111111 | 11111111 | 191.255.255.255 |
+--------------------+----------+----------+----------+----------+-----------------+
| Máscara de clase B | 11111111 | 11111111 | 00000000 | 00000000 | 255.255.0.0     |
+--------------------+----------+----------+----------+----------+-----------------+
| Patrón de clase C  | 110RRRRR | RRRRRRRR | RRRRRRRR | HHHHHHHH |                 |
+--------------------+----------+----------+----------+----------+-----------------+
| Primera de clase C | 11000000 | 00000000 | 00000000 | 00000000 | 192.0.0.0       |
+--------------------+----------+----------+----------+----------+-----------------+
| Última de clase C  | 11011111 | 11111111 | 11111111 | 11111111 | 223.255.255.255 |
+--------------------+----------+----------+----------+----------+-----------------+

Desperdicio y solución
------------------------
Debido a que el desperdicio era inasumible el IETF decidió lo siguiente:

1. Una solución para el corto plazo, ya que el ritmo de conexión a Internet crecía exponencialmente. Esta solución fue el NAT.
2. Por otro lado para resolver el problema a largo plazo el IETF diseñó IPv6.


Hablaremos de IPv6 en los apartados siguientes. En cuanto al NAT cabe destacar que actúa de la forma siguiente:

1.- Hay unos rangos de direcciones que **sí se pueden repetir en Internet**. Esto ocurre porque en realidad NUNCA SE USAN COMO DIRECCIONES DE DESTINO EN LA INTERNET PÚBLICA.
2. Todo router que use NAT en realidad cambia las IPs de origen de los paquetes que salen y pone en su lugar **su propia IP** (a la que llamamos pública). Cuando un paquete sale lo hará usando como IP de origen la IP del router.
3. El router anota en una tabla estas manipulaciones y cuando vengas las respuestas, el router volverá a manipular la IP para volver a poner la IP del equipo original que envió algo.



El NAT se caracteriza por:

1. Funcionó muy bien. Eso es una ventaja.
2. Perjudica al rendimiento. Los router están contínuamente quitando y poniendo direcciones de los paquetes que entran y salen.
3. Determinadas operaciones, como abrir servicios, pueden ser difíciles de conseguir para el usuario medio, que se ve obligado a "abrir puertos."

Los rangos de direcciones "privadas" o repetibles en Internet son los siguientes:

* La red 10.0.0.0/8
* La red 172.16.0.0/12
* La red 192.168.0.0/16

En estos rangos aparece el concepto de "máscara abreviada". En lugar de escribir la máscara en binario o en decimal (como 255.0.0.0 o 255.255.255.0) se ha escrito en estos rangos es **la cantidad de unos que hay dentro de la parte de red de la máscara**

Los rangos de direcciones aceptables en esos casos son entonces:

* Desde 10.0.0.0 hasta 10.255.255.255
* Desde 172.16.0.0 hasta 172.31.255.255
* Desde 192.168.0.0 hasta 192.168.255.255

¿Qué se podría decir entonces sobre la IP 161.43.118.31?

Convirtamos 161 a binario: 10100001

* La IP empieza por 10, es decir, parece de clase B.
* Dicha IP no está en el rango 172.16.0.0 a 172.31.255.255, así que es una **IP pública**
* Al ser de clase B es probable que su máscara sea /16, es decir, 255.255.0.0.


¿Qué se podría decir sobre la 172.25.0.13?
* Es privada. Está entre 172.16.0.0 y 172.31.255.255. En concreto es del segundo bloque, o sea que su máscara es /12 o más bits.
* Una máscara /12 sería 11111111.11110000.00000000.00000000, o en decimal 255.240.0.0
* Si se convierte a binario, 172 queda como 10101100, empieza por la pareja de bits 10, es decir, es de clase B.

Direcciones de red y de difusión
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
En las direcciones IP sabemos que tenemos dos partes

* Parte de red, también llamado **prefijo de red**.
* Parte de host, que es una secuencia binaria que cambia en cada equipo.


Supongamos que tenemos un conjunto de servidores y que queremos ubicarlos en una red. Supongamos que usamos un rango privado como 192.168.1.0 con máscara /24 (24 bits a uno). Esto significa que nuestros últimos 8 bits pueden ser estos.

+--------------+
| Últimos bits |
+==============+
| 00000000     |
+--------------+
| 00000001     |
+--------------+
| 00000010     |
+--------------+
| 00000011     |
+--------------+
| 00000100     |
+--------------+
| ...          |
+--------------+
| ...          |
+--------------+
| 11111111     |
+--------------+


En realidad, la combinación **todos los bits a 0** y la **todos los bits a uno** NO SON DIRECCIONES IP VÁLIDAS ASIGNABLES A NODOS. Esto significa que no podemos poner a un equipo ni la 192.168.1.0 ni la 192.168.1.255. **Estas direcciones tienen un significado especial**

* La **todo a ceros** se usa para "nombrar la red". Así, nuestra red digamos que "se llama 192.168.1.0/24"
* La **todo a unos** es la DIRECCIÓN DE DIFUSIÓN. Cuando un ordenador de nuestra red quiera enviar algo a todos usará como dirección de destino la 192.168.1.255

Por tanto, en realidad dentro de nuestra sala de servidores solo podemos poner direcciones entre 192.168.1.1 y 192.168.1.254


Enrutamiento
----------------

El enrutamiento es el proceso de configurar nodos y routers para conseguir llevar los paquetes hasta su destino:

* En los terminales (ordenadores, tablets, móviles...) esto implica configurar el "gateway", "puerta de enlace", "router por defecto". Es decir indicar la IP de algún dispositivo de enrutamiento en la red.

* En los routers implica rellenar las tablas de rutas. Es decir, indicar al router las direcciones de red (con las máscaras) e indicarles la IP del siguiente nodo para llegar a esa red.


Para el ejemplo visto en clase, repetir el proceso para estas redes:

1. Red 172.25.3.0/24 para la red izquierda, 16.2.0.0/16 para la red intermedia (la de los router) y red 61.24.3.0/24 para la red derecha.
2. * Red 41.0.0.0/24 para la red izquierda, 192.168.24.0/24 para la red intermedia (la de los router) y red 184.2.91.0/24 para la red derecha.

Subredes
-------------

Supongamos una red como 36.56.0.0/15. Si calculamos el rango de hosts nos salen 131.072 hosts con IPs comprendidas entre 36.56.0.1 y 36.57.255.254

Esta red está formada por un solo dominio de colisión muy grande, lo que es muy ineficiente y encima inseguro. Este proceso tiene que mejorar, y para ello tenemos una técnica llamada "subredes" o "subnetting".


La idea básica es que **vamos a hacer la máscara más ancha** de manera que vamos a perder bits de host pero vamos a poder tener unas entidades más pequeñas llamadas subredes, las cuales formarán parte de la red principal.

Veamos un esquema, si pasamos 36.56.0.0 a binario veremos algo como esto

+----------+----------+----------+----------+
| Byte 1   | Byte 2   | Byte 3   | Byte 4   |
+==========+==========+==========+==========+
| 00100100 | 00111000 | 00000000 | 00000000 |
+----------+----------+----------+----------+
| 36       | 56       | 0        | 0        |
+----------+----------+----------+----------+


Veamos como es el patrón.

* R significa que es un bit de red
* H significa que es un bit de host.

+----------+----------+----------+----------+
| Byte 1   | Byte 2   | Byte 3   | Byte 4   |
+==========+==========+==========+==========+
| 00100100 | 00111000 | 00000000 | 00000000 |
+----------+----------+----------+----------+
| RRRRRRRR | RRRRRRRH | HHHHHHHH | HHHHHHHH |
+----------+----------+----------+----------+
| 36       | 56       | 0        | 0        |
+----------+----------+----------+----------+

Vamos a analizar las necesidades de la empresa y vamos a usar solo tantos bits de host como requiera el departamento o sala más grande. Una vez hecha la asignación de bits de host al departamento más grande, los bits que nos queden se pueden usar como **identificación de subred**

+----------+----------+----------+----------+
| 00100100 | 00111000 | 00000000 | 00000000 |
+==========+==========+==========+==========+
| RRRRRRRR | RRRRRRRS | SSSSSSSS | SSHHHHHH |
+----------+----------+----------+----------+
| 11111111 | 11111111 | 11111111 | 11000000 |
+----------+----------+----------+----------+
| 255      | 255      | 255      | 192      |
+----------+----------+----------+----------+

Ahora hay que empezar a poner los números de subred.
¿Cual es nuestra primera subred? Recordemos que tenemos 11 bits, así que en teoría sería 11 bits a 0, pero por costumbre la combinación todo ceros y todo unos, nunca se usa.

+-----------------------------------+
|00100100.00111000.00000000.00000000|
+-----------------------------------+
|RRRRRRRR RRRRRRRS SSSSSSSS SSHHHHHH|
+-----------------------------------+

La primera subred sería algo como esto

+----------------+-------------+------+------------+
|00100100.0011100|0.00000000.00|000000|            |
+----------------+-------------+------+------------+
|RRRRRRRR RRRRRRR|S.SSSSSSSS.SS|HHHHHH|            |
+----------------+-------------+------+------------+
|00100100.0011100|0.00000000.01|000000|IP de subred|
|00100100.0011100|0.00000000.01|000001|Primera IP  |
|00100100.0011100|0.00000000.01|000010|Segunda IP  |
|00100100.0011100|0.00000000.01|111110|Última IP   |
|00100100.0011100|0.00000000.01|111111|IP difusión |
+----------------+-------------+------+------------+

Esto significa que la primera subred va así:

* 36.56.0.64/26 es la IP de la subred 1
* 36.56.0.65/26 es la primera IP asignable en esa subred 1
* 36.56.0.66/26 es la segunda IP
* 36.56.0.126/26 es la última IP asignable a un equipo.
* 36.56.0.127/26 es la IP de difusión en la subred 1.

Es decir, al ampliar la máscara y dejar solo los bits de host que necesitamos, ahora ocurre que en toda la empresa, la máscara en todos será 255.255.255.192

Protocolos de resolución de direcciones ARP, RARP.
---------------------------------------------------

Direcciones IPv6
---------------------------------------------------
Dadas las limitaciones en las direcciones IPv4 se diseñó un nuevo formato de direcciones en el que hubiera muchas más posibilidades: **IPv6** En IPv6 hay *128 bits para direcciones* lo que supone un espacio de direcciones de 2 elevado a 128, un número realmente grande. Las direcciones IPv6 se escriben como secuencias de 8 grupos de 4 hexadecimales separadas por dos puntos, a continuación vemos algunos ejemplos::

    fe80:a13d:d3d6:a190:31d2:a216:3261:1800
    3410:0000:0000:0000:0000:0000:0000:2900

El segundo ejemplo muestra algo interesante y además muy habitual: **la mayor parte de las veces una dirección IPv6 tendrá muchos ceros consecutivos**. En ese caso, se puede abreviar esa dirección eliminando las secuencias de ceros **pero dejando un "doble dos puntos"** para indicar que hemos recortado una IPv6, así tendríamos que la última dirección la podemos escribir así::

    3410:0000:0000:0000:0000:0000:0000:2900 (sin abreviar)
    3410::2900 (abreviada)

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


Uso de direcciones
------------------------
En IPv6 va a ocurrir que TODOS LOS NODOS van a tener siempre al menos una IPv6 de enlace local. Después aparte de esa, pueden tener una o varias unicast y una o varias multicast. Como norma general, lo habitual será tener esto

* Direcciones local link: UNA POR TARJETA y SIEMPRE.
* Direcciones unicast: NORMALMENTE UNA POR TARJETA, aunque puede haber varias.
* Direcciones multicast: puede haber una o varias, dependiendo de a cuantos grupos se pertenezca.



Ampliación: encaminamiento dinámico
---------------------------------------

En apartados anteriores hemos construido tablas de rutas pequeñas para rutas pequeñas. Pero en grandes redes pasan dos cosas:

1. Averiguar los mejores caminos es largo y difícil.
2. Aunque los calculemos las redes fluctúan mucho y un buen camino hoy puede ser una mala ruta dentro de 5 minutos.

Se pueden hacer dos cosas:

1. Construir las tablas de rutas a mano.
2. Dejar que los routers construyan las tablas automáticamente.

Supongamos una red como la de la figura:

.. figure:: Red_compleja_routers.png

¿Cual sería el mejor camino para ir de la izquierda a la derecha? Podríamos pensar en que el mejor camino es el más corto pero en redes eso no tiene por qué ser así. Un camino podría ser "muy largo en longitud" pero cruzar enlaces de 1Gb/s y resultar ser más rápido que otro camino con menos cables pero más lentos. Por desgracia este camino bueno podría empeorar el día de mañana y volver a mejorar al siguiente. En suma, las redes son a veces demasiado aleatorias y construir los caminos a mano puede ser muy ineficiente.

Por suerte, existen protocolos de enrutamiento en los que los router construyen ellos solos todas las tablas. Para ello se basan en ciertas premisas:

1. Todos los router anuncian periódicamente todo lo que saben.
2. Todos los router reciben periódicamente información de otros router. Pueden y deben usar esa información para actualizar su propio conocimiento y así encontrar caminos mejores.
3. No hemos mencionado hasta ahora que en realidad en las tablas de rutas hay una columna llamada "métrica". Una métrica indica el coste de seguir una ruta. Así, si en una tabla de rutas tenemos algo como esto y llega un paquete con destino a la red 10.0.0.0, el router elegirá enviarlo por la IP 65.133.8.71.

+----------+-----------+---------------+---------+
| Red      | Máscara   | Sig. salto    | Métrica |
+==========+===========+===============+=========+
| 10.0.0.0 | 255.0.0.0 | 10.43.2.1     | 13      |
+----------+-----------+---------------+---------+
| 20.0.0.0 | 255.0.0.0 | 161.51.91.103 | 7       |
+----------+-----------+---------------+---------+
| 10.0.0.0 | 255.0.0.0 | 65.133.8.71   | 10      |
+----------+-----------+---------------+---------+


Enrutamiento "interior" y "exterior"
-------------------------------------
Un protocolo de enrutamiento (dinámico) interior es un protocolo pensado para una organización con muchas redes y routers que desea que dentro de su empresa el enrutamiento sea dinámico. A todos estos protocolos se les llama IGP (Protocolos para Gateway interiores). Dentro de este conjunto tenemos RIP y OSPF.

Un protocolo de enrutamiento (dinámico) exterior es un protocolo pensado para intercambiar información con una red externa, de fuera de nuestra empresa. Aquí el único protocolo existente es BGP (Border Gateway Protocol)

En grandes redes es obligatorio disponer de un número que usará BGP. Este número se llama "número de sistema autónomo o AS number".

Dado que Internet es una red demasiado grande, la administración de direcciones IP, números AS se delega en lo que se llama "Registros", y hay más o menos uno por continente.

* "RIPE" es el registro para Europa.
* "APNIC" es el registro para Asia y Pacífico.


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