Experimentos con switches
==============================

Para esta práctica se ha proporcionado un switch Cisco a cada mesa de trabajo (3-4 equipos). Comprueba lo siguiente:

* Debes tener 3 máquinas virtuales que puedan ejecutar Windows y que tengan instalado Putty y TftpServer. Todas las máquinas deben tener una carpeta compartida con el anfitrión. Si es posible lo ideal es tener cada máquina en un equipo distintos.
* Durante el ejercicio llamaremos a estas máquinas "administrador", "oficinista1" y "oficinista2". La máquina donde ejecutas Putty conectado al switch será "administrador".
* Las tres máquinas virtuales deben tener la tarjeta de red en modo puente y conectada al cable de red del aula. Si estás usando portátiles recuerda que en general los drivers no permiten conectar la tarjeta puente de la máquina virtual con la tarjeta inalámbrica del equipo. 
* Conecta los cables desde los ordenadores al switch. Esto significa que tendrás que sacar los cables de las rosetas y conectarlos de los ordenadores al switch.
* En la práctica a veces habrá que contactar con el switch por Telnet y otras por SSH. Asegúrate de que en Putty eliges el modo correcto.
* Si algo no te funciona, *intenta resolverlo o al menos averiguar la causa del problema.* No te limites a "como no me funcionaba me he puesto a hacer otra cosa/leer el Marca/charlar". No pasa nada si algo no sale, pero por favor 

Práctica
===========
En los puntos siguientes se te pide que pongas en práctica tareas básicas con el switch. **No te limites a copiar y pegar comandos** Lo importante no es conseguir hacer todo sino experimentar con un switch real y familiarizarse con el método de trabajo. Todo lo que tienes que hacer debe hacerse dentro de la máquina virtual. Apunta el nombre del switch que se te ha entregado por si se puede continuar el trabajo otro día.

No se debe ejecutar ``copy running-config startup-config`` en ninguno de los ejercicios. Si crees que lo has hecho por error, por favor comunícalo al profesor.

Conectividad básica
--------------------------
Configura las 3 máquinas virtuales para que usen direcciones como 192.168.xxx.0/24. **No** se necesita poner puerta de enlace ni servidores DNS. Comprueba que las máquinas pueden "verse" entre ellas usando ``ping``.

Establecimiento de sesión
-----------------------------
Accede al switch que se te ha dado usando Telnet. Navega por los distintos modos y comprueba que todo funciona igual que en el simulador. Muestra la configuración de ejecución. Si no lo consigues comprueba que tu máquina virtual con Putty tiene una IP que esté en el mismo prefijo de red que tiene el switch. ¿Pueden hacerse ping entre ellas las máquinas 192.168.xxx.0/?

Copia de seguridad de la configuración
----------------------------------------------
Haz una copia de seguridad de la configuración transfiriéndola a alguna de las máquinas virtuales que ejecute el servidor TFTP. Guarda bien el archivo de copia, se usará despues.


Cambio de IP
---------------------
Modifica la IP del switch a una 172.16.xxx.0/24. ¿Qué ocurre cuando lo haces?

Clave al modo enable
--------------------------
1. Asigna al modo administrador la clave "cisco". Por favor **no uses otra contraseña**, usa exactamente la clave "cisco" (sin comillas, en minúsculas). 
2. Comprueba que efectivamente se pide clave al pasar de modo "usuario" a modo administrador. 
3. Quita la clave al terminar y comprueba que efectivamente ya no la pide.


Clave al acceso por telnet
------------------------------
1. Pon la clave "cisco" al modo Telnet (en algunas versiones de Cisco IOS el comando "login" es a veces "login local".
2. Cierra la sesión y vuelve a abrirla. Comprueba que ahora te pide una clave y que efectivamente al ponerla puedes entrar. 
3. Despues de comprobarlo quita la clave, cierra la sesión y comprueba que efectivamente ya no la pide.


Clave al modo SSH
-----------------------
1. Configura SSH en el switch para que tenga el usuario ``admin`` y la clave ``cisco``. Puedes elegir el nombre de dominio ``practicaswitches.com``.
2. Cierra la sesión  Putty e inicia una sesión SSH con el switch y comprueba que funciona.
3. Quita todo lo relativo a SSH. Cierra la sesión y comprueba que ahora ya no es posible acceder por SSH

Cambio de IP (II)
---------------------
Vuelve a dejar la IP y máscara que tenía el switch. Recuerda que /24 significa 255.255.255.0 y que /16 significa 255.255.0.0

VLANs
-----------------------------------
1. Fíjate bien en los puertos donde están conectados los ordenadores "oficinista1" y "oficinista2". 
2. Comprueba que ambas máquinas pueden hacerse ping.
3. Crea las VLAN 100 y 200 con los respectivos nombres CONTABLES y GERENTES.
4. Asigna al puerto de "oficinista1" la VLAN 100 y a "oficinista2" la VLAN 200. Comprueba que ``ping`` ha dejado de funcionar.
5. Asigna a "oficinista1" la VLAN 200 y comprueba que los ``ping`` vuelven a funcionar.

Enlaces troncales
-----------------------------------
1. Utiliza un cable para conectar tu switch al switch de otro grupo. 
2. Poned en las máquinas de vuestros oficinistas las IP 172.25.xxx.xxx/24. Comprobad que todos pueden hacer ping a todos.
3. Cada grupo debe poner a su "oficinista1" en la VLAN 100 y a "oficinista2" en la VLAN 200. 
4. Cada grupo debe configurar el puerto correcto con el modo correcto "trunk" y permitiendo las VLAN 100 y 200
5. Comprueba que ahora solo funcionan los ping entre ambos "oficinista1" y entre ambos "oficinista2" pero ningun "oficinista1" puede hacer "ping" a "oficinista2"

VTP
--------------

1. Uno de los grupos pondrá su switch modo ``vtp server``. Podéis usar como clave ``vtp1234``
2. El otro grupo debe poner su switch en modo ``vtp client``
3. Comprobad que cuando el servidor crea una VLAN nueva el cliente la recibe
4. Desactivad los modos vtp en ambos switches y dejadlo todo como estaba.

Al terminar
===============
Por favor, asegúrate de que el switch que has recibido:

* No tiene puesta ninguna clave.
* Tiene puesta la misma IP que aparece en la etiqueta.
* No está activo nada de lo que hemos practicado en clase. Solo debería estar la IP de gestión que aparece en la etiqueta y con la misma máscara. Gracias por tu colaboración

Vuelve a dejar los cables como estaban y comprueba que el equipo en el que estabas sentado tiene Internet.
