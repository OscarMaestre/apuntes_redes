
Instrucciones para el ordenador PC-13
=========================================

Junto con este documento se te ha dado una imagen con la topolog�a de una red y una m�quina virtual que puedes importar. Importa la m�quina y haz 4 clones de manera que tengas en total 5 m�quinas virtuales. Es muy recomendable que a cada m�quina le pongas un nombre como vamos a ver a continuaci�n. 

Obs�rva la imagen con detenimiento porque vamos a construir una topologia de red con varios routers y con 
enrutamiento est�tico. 

.. figure:: Red.png

Como puedes ver tenemos 6 m�quinas:

* Un cliente llamado "Cliente 1".
* Un cliente llamado "Cliente 2".
* Tres router que llamaremos "Izquierda", "Arriba" y "Abajo".


Cliente 1 y Cliente 2 solo van a usar **una tarjeta de red en modo puente**, la ``enp0s3``. Sin embargo  los router van a tener **tres tarjetas de red en modo puente**. Si est�s usando m�quinas virtuales clonadas o importadas recuerda **reiniciar las MAC de todas las tarjetas.** A continuaci�n se te indican las direcciones IP y las tarjetas en las que hay que asignarlas.

* Cliente 1: la tarjeta enp0s3 tiene la IP **1.113.101.10/16**
* Cliente 2: la tarjeta enp0s3 tiene la IP **6.113.101.10/16**
* Izquierda: la tarjeta enp0s3 tiene la IP **1.113.0.1/16**,la tarjeta enp0s8 tiene la IP **2.113.0.1/16**,la tarjeta enp0s9 tiene la IP **3.113.0.1/16**
* Arriba: la tarjeta enp0s3 tiene la IP **Reservada**,la tarjeta enp0s8 tiene la IP **2.113.0.2/16**,la tarjeta enp0s9 tiene la IP **5.113.0.1/16**
* Abajo: la tarjeta enp0s3 tiene la IP **6.113.0.1/16**,la tarjeta enp0s8 tiene la IP **3.113.0.2/16**,la tarjeta enp0s9 tiene la IP **5.113.0.2/16**




Ejercicio 1
--------------
Configurar las IP, m�scaras, gateways y rutas en todas las m�quinas de manera que Cliente1 pueda hacer ping a Cliente2 enviando los paquetes por abajo, es decir el camino directo.

Ejercicio 2
--------------
Modifica las rutas de manera que Cliente1 pueda hacer ping a Cliente2 enviando los paquetes por arriba, es decir el camino m�s largo.

Ejercicio 3
--------------
En el router de arriba hemos dejado una tarjeta sin usar. Intenta conectar con las redes de alg�n compa�ero. Para ello, tanto tu compa�ero como t� tendr�is que hacer lo siguiente:

* Poneros de acuerdo en una red IP para ese segmento. Examinad vuestros n�meros de puesto y usad la direcci�n de red 30.<numeromayor>.<numeromenor>.0/24. Es decir, si ten�is los n�meros de puesto 7 y 24 deber�ais usar la 30.24.7.0/24. 
* Pas�os el uno al otro las direcciones de red de vuestros respectivos "Cliente 1" y "Cliente 2"
* Poneros de acuerdo en qu� IP usar cada uno en vuestro router de arriba.
* Reconfigura **todos tus router** para a�adir en ellos rutas para llegar a las redes de los clientes de tu compa�ero.

Este ejercicio demuestra que la configuraci�n est�tica de rutas solo es razonable para peque�as redes y con pocos cambios. En el ejercicio siguiente ver�s como ahorrarte todo este trabajo.



Ejercicio 4
-------------
Reinicia todos los router, lo que borrar� todas las rutas. En todos tus router tienes instalado un servicio que permite usar protocolos din�micos de enrutamientos. Config�ralos para que calculen todas las rutas autom�ticamente.


Soluci�n al ejercicio 1
------------------------

Direccionamiento
~~~~~~~~~~~~~~~~~~~~~
Cliente 1 tendr�a un fichero de ``netplan`` como este::
	
	network:
	  version: 2 
	  ethernets: 
	    enp0s3:
	      addresses: [1.113.101.10/16]
	      gateway4:  1.113.0.1/16
	

Izquierda tendr�a un fichero de ``netplan`` como este::
	
	network:
	  version: 2 
	  ethernets: 
	    enp0s3:
	      addresses: [1.113.0.1/16]
	    enp0s8:
	      addresses: [2.113.0.1/16]
	    enp0s9:
	      addresses: [3.113.0.1/16]
	
	

Arriba tendr�a un fichero de ``netplan`` como este::
	
	network:
	  version: 2 
	  ethernets: 
	    enp0s8:
	      addresses: [2.113.0.2/16]
	    enp0s9:
	      addresses: [5.113.0.1/16]
	
	

Abajo tendr�a un fichero de ``netplan`` como este::
	
	network:
	  version: 2 
	  ethernets: 
	    enp0s3:
	      addresses: [6.113.0.1/16]
	    enp0s8:
	      addresses: [3.113.0.2/16]
	    enp0s9:
	      addresses: [5.113.0.2/16]
	
	

Una vez configuradas todas las direcciones IP repasalo todo ejecutando ``ip addr`` **en todas las m�quinas** y comprueba que **todo el mundo puede hacer ping a su vecino inmediato**. Si no es as� repasa las direcciones y tarjetas y si no ves el error llama al profesor.

Enrutamiento
~~~~~~~~~~~~~~~~~~~~~~~~~
Antes de empezar, en Linux se debe habilitar el enrutamiento.

1. Escribe ``sudo nano /etc/sysctl.conf``.
2. Busca una l�nea con el texto ``net.ipv4.ip_forward=1``.
3. Si tiene una almohadilla delante es porque esa l�nea est� comentada y no est� activada. Borra el s�mbolo #, **guarda los cambios** y despues ejecuta ``sudo sysctl -p`` que forzar� la recarga del fichero y activar� el enrutamiento.

En todos los router debemos recordar poner tanto las rutas de ida *como las rutas de vuelta*, as�, los comandos a ejecutar ser�an algo como esto:

En Izquierda podemos ejecutar esto::

	sudo ip route add 6.13.101.0/16 via 3.113.0.2/16

En Abajo podemos ejecutar esto::

	sudo ip route add 1.13.101.0/16 via 3.113.0.1/16




Soluci�n al ejercicio 2
------------------------

Direccionamiento
~~~~~~~~~~~~~~~~~~~~~
Los ficheros de ``netplan`` **NO CAMBIAN**

Enrutamiento
~~~~~~~~~~~~~~~~~~~~~~~~~
Si ya tienes el enrutamiento activa (ver m�s arriba) **no hace falta que vuelvas a hacerlo**.

En primer lugar **debemos borrar las rutas anteriores en los router Izquierda y Abajo**. Ademas, de nuevo en todos los router debemos recordar poner tanto las rutas de ida *como las rutas de vuelta*. 

En Izquierda podemos ejecutar esto::

	sudo ip route add 6.13.101.0/16 via 2.113.0.2/16

En Arriba podemos ejecutar esto::

	sudo ip route add 1.13.101.0/16 via 2.113.0.1/16
	sudo ip route add 6.13.101.0/16 via 5.113.0.2/16

En Abajo podemos ejecutar esto::

	sudo ip route add 1.13.101.0/16 via 5.113.0.1/16




Soluci�n al ejercicio 3
-------------------------
No se da

Soluci�n al ejercicio 4
------------------------
En todos los router tendr�s que hacer esto:

1. Editar el fichero de configuracion ``/etc/frr/daemons``
2. Activar OSPF poniendo ``yes``  en lugar de ``no`` en esta l�nea ``ospfd=no``
3. Reiniciar el servicio con ``sudo service frr restart``
4. Arranca la configuraci�n del router con ``sudo vtysh``
5. Introduce los comandos correspondientes a cada router.

Router izquierda::

	network 1.113.0.0/16 area 1
	network 2.113.0.0/16 area 1
	network 3.113.0.0/16 area 1

Router Arriba::

	network 2.113.0.0/16 area 1
	network 5.113.0.0/16 area 1

Router Abajo::

	network 6.113.0.0/16 area 1
	network 3.113.0.0/16 area 1
	network 5.113.0.0/16 area 1
