Tema 5: Configuración y administración básica de routers
================================================================

La capa de transporte
--------------------------------

Recordemos la arquitectura de las redes:

.. figure:: img/01-osi.png

En el dibujo vemos las distintas capas y sabemos que:

* Las direcciones Ethernet son fijas. Hay una dirección por tarjeta de red.
* Las direcciones IP son configurables. Por cada tarjeta puede haber una IP (o más).

Tradicionalmente pensamos en el movimiento de datos como si fuera una transacción entre dos máquinas y habrá un paquete que tiene una IP de origen y una de destino.

Supongamos que en un ordenador hay dos servicios. Un servidor Web y un servidor de bases de datos por ejemplo Oracle. Supongamos ahora que otro ordenador quiere conectarse y ver la página web. Supongamos que el cliente tiene la IP 192.168.1.1 y que el servidor tiene la IP 192.168.1.10.

¿Qué ocurre cuando la conexión del 192.168.1.1 (cliente) llega al servidor 192.168.1.10? Con lo que sabemos hasta ahora ¿quien recibe la conexión? ¿El proceso Oracle o el proceso Apache web?

Como en un ordenador puede haber muchos programas enviando y recibiendo datos, ocurre que a cada programa se le asigna un número llamado **PUERTO**. Esto significa que cuando un cliente quiere conectar con un servidor **DEBE PROPORCIONAR UN NÚMERO DE PUERTO**. Los números de puerto y la gestión de esas múltiples conexiones se hace en la capa de transporte.

Ocurre por tanto, que cualquier bloque de trama que envíamos tiene en realidad *al menos* cuatro elementos:

1. IP de origen
2. Puerto de origen
3. IP de destino.
4. Puerto de destino

Tenemos que tener presente que a partir de ahora, la estructura de cualquier paquete es algo como esto:


.. figure:: img/02-puertos.png


Un puerto, en realidad es un número. El sistema operativo usa ese número para saber a qué programa tiene que darle un paquete entrante. Cuando un programa servidor (como Apache) arranca intenta que el sistema operativo le dé un puerto fijo. Si ningún otro programa lo usa, el sistema operativo se lo dará y a partir de ese momento, los paquetes entrantes cuyo puerto de destino sea ese se entregarán al software de Apache.

* Los servidores que aceptan conexiones **siempre escuchan en el mismo puerto**. De hecho hay algunos números de puerto estandarizados. Por ejemplo el 80 TCP es de HTTP y el 443 TCP es de HTTPS.
* Los clientes no siempre usan el mismo número. De hecho los eligen al azar con valores entre 49152 y 65535.

¿Qué es eso de TCP? Resulta que en realidad hay dos protocolos de transporte bastante conocidos (en realidad más pero no los mencionaremos)

* TCP es un protocolo fiable. Para conseguir fiabilidad envia confirmaciones de recepción de mensajes. El problema es que TCP es más lento que su alternativa.
* UDP es no confiable. Algunas aplicaciones (como video conferencia) necesitan la velocidad extra a toda costa y no importa si se pierden algunos datos.

Se debe tener también presente algunas cosas sobre los protocolos:


* Cada programador elige el protocolo de su programa: **no lo podemos cambiar**
* Aparte de las IP, los puertos y los orígenes y destino, **el sentido del tráfico importa**. 
* En las redes, los estándares son públicos, abiertos y gratuitos. Estos estándares se denominan RFCs (Request For Comments)

Componentes del router.
----------------------------------------------------------------------------
Los router modernos son verdaderos ordenadores en sí mismos:


* Microprocesador: Los Cisco llevan MPC (PowerPC). En los domésticos se ve procesadores embebidos en muchos casos MIPS.
* Sistema operativo: En Cisco está IOS. En los domésticos los sistemas son propietarios.
* RAM: los router/switch modernos almacenan datos temporales como por ejemplo la tabla de MACs.
* ROM: en realidad hoy en día suelen ser EEPROM. Alojan un programa llamado comúnmente el firmware.
* NVRAM: en ella se almacena información como la VLANs. Solo en dispositivos de gama media/alta.
* E/S: normalmente solo a través de los puertos de red.


En la figura siguiente podemos ver un router doméstico abierto:

.. figure:: img/03-router-abierto.jpg


El diagrama de bloques sería más o menos así:

.. figure:: img/04-descomposicion.png


Los router domésticos a nivel interno no solamente tienen un sistema operativo sino también algunos parámetros configurables:

* IP y máscara. Por defecto, en muchos hogares es la 192.168.1.1 con máscara 255.255.255.0
* Rango de direcciones DHCP. DHCP se explicará en profundidad en segundo curso, en el módulo "Servicios de red".




Los routers en las LAN y en las WAN.
----------------------------------------------------------------------------

En las redes LAN el router toma decisiones sencillas. En líneas generales solo deciden "¿se envía este paquete al otro lado o no?".

En redes WAN, los routers tienen conexión con muchas otras redes. Al tener muchas redes, estos routers tienen que "intentar averiguar todas las conexiones y decidir cuales son los mejores caminos".


El proceso de NAT paso a paso
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Paso 1: un usuario quiere iniciar una conexión y conectarse a un servidor en otro lugar remoto.

.. figure:: img/nat01.png

Paso 2: el usuario pide al servidor la IP pública de su router y usando su programa intenta conectarse a la IP pública del otro router y al puerto del juego o servicio. El puerto de origen se elige al azar.


.. figure:: img/nat02.png

Paso 3: el paquete llega al router. El router observa que el paquete va al exterior. Como no se pueden usar IPs privadas en el exterior, el router **CAMBIA LA IP DE ORIGEN Y TOMA NOTA DE ESA TRADUCCIÓN POR SI EN EL FUTURO SE NECESITA ESA INFORMACIÓN**.

.. figure:: img/nat03.png

Paso 4: el paquete (con la IP de origen cambiada) viaja por la red y llega al router de destino. Como los router **por defecto no aceptan conexiones entrantes, en principio el paquete no entraría** Es necesario que primero el router derecho tenga *el puerto 6003 abierto.* Abrir un puerto consiste en poner una regla que indique que si llega una conexión entrante iniciada en el exterior se va a dejar pasar enviando el paquete a una cierta IP.

.. figure:: img/nat04.png

Paso 5: si hubiera la regla correcta, el paquete entrará pero con la IP de destino modificada.
.. figure:: img/nat05.png    

Paso 6: el paquete que intentaba iniciar la conexión **llega correctamente a su destino**.
.. figure:: img/nat06.png    

Paso 7: el servidor va a responder y genera un paquete de respuesta.

.. figure:: img/nat07.png    

Paso 8: el paquete llega al router **que vuelve a modificar la IP de origen porque no se aceptan IPs privadas en Internet.** Por supuesto, el router vuelve a apuntar esa traducción.

.. figure:: img/nat08.png    


Paso 9: el paquete intenta entrar. Lo primero que podríamos pensar es que el paquete no entrará, sin embargo **SÍ VA A CONSEGUIR ENTRAR**

.. figure:: img/nat09.png    

Paso 10: el router observa que el paquete **coincide perfectamente** con la información de una traducción que se hizo en el pasado. Es decir **el paquete puede pasar**. De nuevo, se vuelve a cambiar la IP de destino y el paquete se inyecta en la red izquierda.
.. figure:: img/nat10.png    

Paso 10b: se modifica la IP y se envía al interior.

.. figure:: img/nat11.png    

Paso 11: el paquete **llega a su destino**

.. figure:: img/nat12.png    


Formas de conexión al router para su configuración inicial.
----------------------------------------------------------------------------

Routers domésticos
~~~~~~~~~~~~~~~~~~~~

Routers de gama alta
~~~~~~~~~~~~~~~~~~~~~~

Comandos para configuración del router.
----------------------------------------------------------------------------

Poner clave al modo administrador
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Poner clave al acceso por telnet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Poner clave al acceso por cable de consola
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Quitar una clave o valor de configuración
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Comandos para administración del router.
----------------------------------------------------------------------------

Poner una IP a una interfaz
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configurar DHCP
~~~~~~~~~~~~~~~~~~~~~~~~

Excluir direcciones de la asignación DHCP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Activar NAT en un router
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configuración del enrutamiento estático.
----------------------------------------------------------------------------

Definición y ubicación de listas de control de acceso (ACLs).
----------------------------------------------------------------------------

