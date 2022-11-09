Anexo: resolución entera de ejercicio IPv6
==========================================

Observa la figura siguiente. En ella se muestra un ejemplo típico de una interconexión entre dos redes que podrían ser incluso de dos empresas distintas.

.. figure:: ejercicio_entero_ipv6.png
   :width: 80%

Se desea tener **conectividad IPv6 entre todos los nodos**. Para ello hay que 

1. Asignar direcciones IPv6, máscaras y puertas de enlace a todos los nodos que lo necesiten.
2. Configurar correctamente las rutas entre ambas redes.

Boceto general de la solución
-------------------------------

En primer lugar necesitamos que las redes tengan un prefijo asignado. Por comodidad vamos a usar estos bloques:

* La empresa A usará direcciones 2001:aaaa::/64
* La empresa B usará direcciones 2001:bbbb::/64
* La interconexión entre routers usará direcciones 2001:aabb::64

Direccionamiento en la empresa A
---------------------------------

El router de la empresa A tendrá en su conexión izquierda (tarjeta GigabitEthernet 0/0) la dirección ``2001:aaaa::1/64``

El equipo PC0 (arriba a la izquierda) tendrá estos parámetros:

* Dirección IPv6: ``2001:aaaa::10/64``
* Gateway IPv6: ``2001:aaaa::1/64``

El equipo PC1 (abajo a la izquierda) tendrá estos parámetros:

* Dirección IPv6: ``2001:aaaa::11/64``
* Gateway IPv6: ``2001:aaaa::1/64``

Direccionamiento en la empresa B
---------------------------------

El router de la empresa B tendrá en su conexión derecha (tarjeta GigabitEthernet 0/1) la dirección ``2001:bbbb::1/64``

El equipo PC0 (arriba a la derecha) tendrá estos parámetros:

* Dirección IPv6: ``2001:bbbb::10/64``
* Gateway IPv6: ``2001:bbbb::1/64``

El equipo PC1 (abajo a la derecha) tendrá estos parámetros:

* Dirección IPv6: ``2001:bbbb::11/64``
* Gateway IPv6: ``2001:bbbb::1/64``

Direcciones en la interconexión de routers
-------------------------------------------

* El router de la empresa A tendrá en su tarjeta izquierda (GigabitEthernet0/1) la dirección ``2001:aabb::1/64``

* El router de la empresa B tendrá en su tarjeta derecha (GigabitEthernet0/0) la dirección ``2001:aabb::2/64``


Enrutamiento en el router A
----------------------------

En el router A hay que indicar de alguna manera que *para llegar a la red 2001:bbbb::/64 el siguiente salto que hay que dar es enviar a 2001:aabb::2*

Enrutamiento en el router B
--------------------------------
En el router B hay que indicar de alguna manera que *para llegar a la red 2001:aaaa::/64 el siguiente salto que hay que dar es enviar a 2001:aabb::1*


Comandos en el router A
------------------------

La secuencia completa en PacketTracer sería::

    enable
    configure terminal
    interface GigabitEthernet0/0
    ipv6 address 2001:aaaa::1/64
    no shutdown
    exit
    interface GigabitEthernet0/1
    ipv6 address 2001:aabb::1/64
    no shutdown
    exit
    ipv6 route 2001:bbbb::/64 2001:aabb::2


Comandos en el router B
-----------------------

La secuencia completa sería::

    enable
    configure terminal
    interface GigabitEthernet0/0
    ipv6 address 2001:aabb::2/64
    no shutdown
    exit
    interface GigabitEthernet0/1
    ipv6 address 2001:bbbb::1/64
    no shutdown
    exit
    ipv6 route 2001:aaa::/64 2001:aabb::1

