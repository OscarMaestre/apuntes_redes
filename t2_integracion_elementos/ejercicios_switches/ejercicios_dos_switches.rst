Anexo: ejercicios con tablas MAC de switches
================================================


Ejercicio 1 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 1 que va al puerto 2 del switch 2. Se pretende enviar desde ``ec0c`` a ``a548`` sabiendo lo siguiente:


.. figure:: Switches3-2.png

* Ordenador 1I tiene la MAC ``a548``.
* Ordenador 2I tiene la MAC ``cc63``.
* Ordenador 3I tiene la MAC ``4e42``.
* Ordenador 1D tiene la MAC ``ec0c``.
* Ordenador 2D tiene la MAC ``a4c8``.

.. table:: Tabla MAC de Switch 1

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  ``cc63``
                   2  --      
                   3  --      
                   4  --      
                   5  --      
                   6  --      
                   7  --      
    ================  ========


.. table:: Tabla MAC de Switch 2

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  --      
                   2  ``cc63``
                   3  --      
                   4  --      
                   5  --      
                   6  --      
                   7  --      
    ================  ========


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``ec0c``.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 2 envía el mensaje por el puerto 4.
* El Switch 1 envía el mensaje por el puerto 6.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``ec0c``.


Ejercicio 2 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 5 que va al puerto 7 del switch 2. Se pretende enviar desde ``dd84`` a ``9e68`` sabiendo lo siguiente:


.. figure:: Switches2-4.png

* Ordenador 1I tiene la MAC ``7e2e``.
* Ordenador 2I tiene la MAC ``9e68``.
* Ordenador 1D tiene la MAC ``5bb1``.
* Ordenador 2D tiene la MAC ``c383``.
* Ordenador 3D tiene la MAC ``dd84``.
* Ordenador 4D tiene la MAC ``413c``.

.. table:: Tabla MAC de Switch 1

    ================  =============
    Numero de puerto       MAC     
    ================  =============
                   0  --           
                   1  ``9e68``     
                   2  --           
                   3  --           
                   4  --           
                   5  ``5bb1,c383``
                   6  --           
                   7  --           
    ================  =============


.. table:: Tabla MAC de Switch 2

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  --      
                   2  --      
                   3  --      
                   4  --      
                   5  ``dd84``
                   6  --      
                   7  ``5bb1``
    ================  ========


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 2 envía el mensaje por el puerto 4.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``dd84``.
* El Switch 1 envía el mensaje por el puerto 1.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``dd84``.


Ejercicio 3 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 4 que va al puerto 1 del switch 2. Se pretende enviar desde ``de08`` a ``8413`` sabiendo lo siguiente:


.. figure:: Switches3-4.png

* Ordenador 1I tiene la MAC ``de08``.
* Ordenador 2I tiene la MAC ``9fb0``.
* Ordenador 3I tiene la MAC ``8a24``.
* Ordenador 1D tiene la MAC ``68de``.
* Ordenador 2D tiene la MAC ``c12f``.
* Ordenador 3D tiene la MAC ``4c35``.
* Ordenador 4D tiene la MAC ``8413``.

.. table:: Tabla MAC de Switch 1

    ================  ==================
    Numero de puerto         MAC        
    ================  ==================
                   0  --                
                   1  --                
                   2  --                
                   3  --                
                   4  ``68de,4c35,8413``
                   5  --                
                   6  --                
                   7  --                
    ================  ==================


.. table:: Tabla MAC de Switch 2

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  ``c12f``
                   1  ``8a24``
                   2  --      
                   3  --      
                   4  --      
                   5  --      
                   6  --      
                   7  --      
    ================  ========


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``de08``.
* El Switch 1 envía el mensaje por el puerto 4.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``de08``.
* El Switch 2 envía el mensaje por el puerto 5.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.


Ejercicio 4 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 7 que va al puerto 3 del switch 2. Se pretende enviar desde ``50d2`` a ``e9b5`` sabiendo lo siguiente:


.. figure:: Switches4-3.png

* Ordenador 1I tiene la MAC ``ece5``.
* Ordenador 2I tiene la MAC ``50d2``.
* Ordenador 3I tiene la MAC ``bb19``.
* Ordenador 4I tiene la MAC ``60c2``.
* Ordenador 1D tiene la MAC ``aa99``.
* Ordenador 2D tiene la MAC ``e863``.
* Ordenador 3D tiene la MAC ``e9b5``.

.. table:: Tabla MAC de Switch 1

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  ``bb19``
                   1  ``50d2``
                   2  --      
                   3  --      
                   4  --      
                   5  --      
                   6  --      
                   7  --      
    ================  ========


.. table:: Tabla MAC de Switch 2

    ================  =============
    Numero de puerto       MAC     
    ================  =============
                   0  ``aa99``     
                   1  ``e863``     
                   2  --           
                   3  ``bb19,60c2``
                   4  --           
                   5  --           
                   6  --           
                   7  --           
    ================  =============


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``50d2``.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 2 envía el mensaje por el puerto 5.
* El Switch 1 envía el mensaje por el puerto 4.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``50d2``.


Ejercicio 5 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 2 que va al puerto 1 del switch 2. Se pretende enviar desde ``d973`` a ``9a1a`` sabiendo lo siguiente:


.. figure:: Switches3-2.png

* Ordenador 1I tiene la MAC ``c194``.
* Ordenador 2I tiene la MAC ``9a1a``.
* Ordenador 3I tiene la MAC ``6072``.
* Ordenador 1D tiene la MAC ``d973``.
* Ordenador 2D tiene la MAC ``a947``.

.. table:: Tabla MAC de Switch 1

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  --      
                   2  ``a947``
                   3  --      
                   4  --      
                   5  --      
                   6  --      
                   7  --      
    ================  ========


.. table:: Tabla MAC de Switch 2

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  ``d973``
                   1  --      
                   2  --      
                   3  --      
                   4  --      
                   5  ``a947``
                   6  --      
                   7  --      
    ================  ========


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``d973``.
* El Switch 1 envía el mensaje por el puerto 3.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 2 envía el mensaje por el puerto 3.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``d973``.


Ejercicio 6 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 7 que va al puerto 0 del switch 2. Se pretende enviar desde ``cf0f`` a ``d421`` sabiendo lo siguiente:


.. figure:: Switches3-2.png

* Ordenador 1I tiene la MAC ``533b``.
* Ordenador 2I tiene la MAC ``d421``.
* Ordenador 3I tiene la MAC ``8b59``.
* Ordenador 1D tiene la MAC ``a1f7``.
* Ordenador 2D tiene la MAC ``cf0f``.

.. table:: Tabla MAC de Switch 1

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  --      
                   2  --      
                   3  --      
                   4  --      
                   5  --      
                   6  --      
                   7  ``a1f7``
    ================  ========


.. table:: Tabla MAC de Switch 2

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  --      
                   2  --      
                   3  ``a1f7``
                   4  --      
                   5  --      
                   6  --      
                   7  --      
    ================  ========


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``cf0f``.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 2 envía el mensaje por el puerto 1.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``cf0f``.
* El Switch 1 envía el mensaje por el puerto 3.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.


Ejercicio 7 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 3 que va al puerto 2 del switch 2. Se pretende enviar desde ``d5e8`` a ``889f`` sabiendo lo siguiente:


.. figure:: Switches2-3.png

* Ordenador 1I tiene la MAC ``f6f5``.
* Ordenador 2I tiene la MAC ``889f``.
* Ordenador 1D tiene la MAC ``d822``.
* Ordenador 2D tiene la MAC ``9e8a``.
* Ordenador 3D tiene la MAC ``d5e8``.

.. table:: Tabla MAC de Switch 1

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  --      
                   2  --      
                   3  --      
                   4  --      
                   5  ``889f``
                   6  --      
                   7  ``f6f5``
    ================  ========


.. table:: Tabla MAC de Switch 2

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  --      
                   2  --      
                   3  --      
                   4  --      
                   5  --      
                   6  ``d5e8``
                   7  --      
    ================  ========


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``d5e8``.
* El Switch 2 envía el mensaje por el puerto 2.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 envía el mensaje por el puerto 5.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``d5e8``.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.


Ejercicio 8 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 0 que va al puerto 6 del switch 2. Se pretende enviar desde ``42fd`` a ``6e03`` sabiendo lo siguiente:


.. figure:: Switches2-4.png

* Ordenador 1I tiene la MAC ``e2e4``.
* Ordenador 2I tiene la MAC ``6e03``.
* Ordenador 1D tiene la MAC ``9c02``.
* Ordenador 2D tiene la MAC ``65ae``.
* Ordenador 3D tiene la MAC ``42fd``.
* Ordenador 4D tiene la MAC ``c8ee``.

.. table:: Tabla MAC de Switch 1

    ================  =============
    Numero de puerto       MAC     
    ================  =============
                   0  ``42fd,c8ee``
                   1  --           
                   2  ``6e03``     
                   3  --           
                   4  --           
                   5  ``e2e4``     
                   6  --           
                   7  --           
    ================  =============


.. table:: Tabla MAC de Switch 2

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  --      
                   2  --      
                   3  --      
                   4  ``65ae``
                   5  --      
                   6  ``6e03``
                   7  --      
    ================  ========


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 1 envía el mensaje por el puerto 2.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``42fd``.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``42fd``.
* El Switch 2 envía el mensaje por el puerto 6.


Ejercicio 9 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 5 que va al puerto 0 del switch 2. Se pretende enviar desde ``94bb`` a ``cb23`` sabiendo lo siguiente:


.. figure:: Switches2-2.png

* Ordenador 1I tiene la MAC ``f093``.
* Ordenador 2I tiene la MAC ``cb23``.
* Ordenador 1D tiene la MAC ``640c``.
* Ordenador 2D tiene la MAC ``94bb``.

.. table:: Tabla MAC de Switch 1

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  ``cb23``
                   2  --      
                   3  --      
                   4  --      
                   5  --      
                   6  --      
                   7  --      
    ================  ========


.. table:: Tabla MAC de Switch 2

    ================  ===
    Numero de puerto  MAC
    ================  ===
                   0  -- 
                   1  -- 
                   2  -- 
                   3  -- 
                   4  -- 
                   5  -- 
                   6  -- 
                   7  -- 
    ================  ===


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``94bb``.
* El Switch 2 envía el mensaje por el puerto 7.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 1 envía el mensaje por el puerto 1.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``94bb``.


Ejercicio 10 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 3 que va al puerto 2 del switch 2. Se pretende enviar desde ``7026`` a ``a423`` sabiendo lo siguiente:


.. figure:: Switches4-4.png

* Ordenador 1I tiene la MAC ``895a``.
* Ordenador 2I tiene la MAC ``7c6d``.
* Ordenador 3I tiene la MAC ``a423``.
* Ordenador 4I tiene la MAC ``c4ed``.
* Ordenador 1D tiene la MAC ``63e4``.
* Ordenador 2D tiene la MAC ``7026``.
* Ordenador 3D tiene la MAC ``87e7``.
* Ordenador 4D tiene la MAC ``466a``.

.. table:: Tabla MAC de Switch 1

    ================  =============
    Numero de puerto       MAC     
    ================  =============
                   0  --           
                   1  ``895a``     
                   2  ``a423``     
                   3  ``63e4,7026``
                   4  ``c4ed``     
                   5  ``7c6d``     
                   6  --           
                   7  --           
    ================  =============


.. table:: Tabla MAC de Switch 2

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  ``7026``
                   2  ``7c6d``
                   3  --      
                   4  --      
                   5  --      
                   6  --      
                   7  --      
    ================  ========


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``7026``.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 1 envía el mensaje por el puerto 2.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 2 envía el mensaje por el puerto 5.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``7026``.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.


Ejercicio 11 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 0 que va al puerto 7 del switch 2. Se pretende enviar desde ``ee1f`` a ``5f4c`` sabiendo lo siguiente:


.. figure:: Switches2-3.png

* Ordenador 1I tiene la MAC ``ee1f``.
* Ordenador 2I tiene la MAC ``c7cc``.
* Ordenador 1D tiene la MAC ``926d``.
* Ordenador 2D tiene la MAC ``5f4c``.
* Ordenador 3D tiene la MAC ``78fa``.

.. table:: Tabla MAC de Switch 1

    ================  ===
    Numero de puerto  MAC
    ================  ===
                   0  -- 
                   1  -- 
                   2  -- 
                   3  -- 
                   4  -- 
                   5  -- 
                   6  -- 
                   7  -- 
    ================  ===


.. table:: Tabla MAC de Switch 2

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  --      
                   2  --      
                   3  --      
                   4  --      
                   5  --      
                   6  --      
                   7  ``ee1f``
    ================  ========


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 1 envía el mensaje por el puerto 0.
* El Switch 2 envía el mensaje por el puerto 1.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``ee1f``.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``ee1f``.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.


Ejercicio 12 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 2 que va al puerto 0 del switch 2. Se pretende enviar desde ``418d`` a ``79d5`` sabiendo lo siguiente:


.. figure:: Switches2-3.png

* Ordenador 1I tiene la MAC ``79d5``.
* Ordenador 2I tiene la MAC ``8d79``.
* Ordenador 1D tiene la MAC ``418d``.
* Ordenador 2D tiene la MAC ``f8f5``.
* Ordenador 3D tiene la MAC ``9c7b``.

.. table:: Tabla MAC de Switch 1

    ================  =============
    Numero de puerto       MAC     
    ================  =============
                   0  --           
                   1  --           
                   2  ``418d,9c7b``
                   3  --           
                   4  --           
                   5  --           
                   6  --           
                   7  --           
    ================  =============


.. table:: Tabla MAC de Switch 2

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  --      
                   2  ``418d``
                   3  --      
                   4  --      
                   5  --      
                   6  ``f8f5``
                   7  --      
    ================  ========


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 1 envía el mensaje por el puerto 7.
* El Switch 2 envía el mensaje por el puerto 1.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``418d``.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``418d``.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.


Ejercicio 13 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 1 que va al puerto 3 del switch 2. Se pretende enviar desde ``920f`` a ``cc20`` sabiendo lo siguiente:


.. figure:: Switches2-4.png

* Ordenador 1I tiene la MAC ``920f``.
* Ordenador 2I tiene la MAC ``ca67``.
* Ordenador 1D tiene la MAC ``95c2``.
* Ordenador 2D tiene la MAC ``7d24``.
* Ordenador 3D tiene la MAC ``5833``.
* Ordenador 4D tiene la MAC ``cc20``.

.. table:: Tabla MAC de Switch 1

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  ``cc20``
                   2  --      
                   3  --      
                   4  --      
                   5  --      
                   6  --      
                   7  --      
    ================  ========


.. table:: Tabla MAC de Switch 2

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  ``5833``
                   2  --      
                   3  --      
                   4  --      
                   5  --      
                   6  --      
                   7  --      
    ================  ========


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``920f``.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``920f``.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 envía el mensaje por el puerto 1.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 2 envía el mensaje por el puerto 5.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.


Ejercicio 14 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 3 que va al puerto 2 del switch 2. Se pretende enviar desde ``6301`` a ``d6de`` sabiendo lo siguiente:


.. figure:: Switches3-2.png

* Ordenador 1I tiene la MAC ``f7fa``.
* Ordenador 2I tiene la MAC ``f8d3``.
* Ordenador 3I tiene la MAC ``6301``.
* Ordenador 1D tiene la MAC ``5e95``.
* Ordenador 2D tiene la MAC ``d6de``.

.. table:: Tabla MAC de Switch 1

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  ``f8d3``
                   1  --      
                   2  --      
                   3  ``5e95``
                   4  --      
                   5  --      
                   6  ``f7fa``
                   7  --      
    ================  ========


.. table:: Tabla MAC de Switch 2

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  --      
                   2  --      
                   3  --      
                   4  --      
                   5  --      
                   6  ``5e95``
                   7  --      
    ================  ========


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``6301``.
* El Switch 2 envía el mensaje por el puerto 2.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``6301``.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 envía el mensaje por el puerto 5.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.


Ejercicio 15 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 4 que va al puerto 7 del switch 2. Se pretende enviar desde ``94f5`` a ``9b89`` sabiendo lo siguiente:


.. figure:: Switches3-4.png

* Ordenador 1I tiene la MAC ``90a0``.
* Ordenador 2I tiene la MAC ``b3d6``.
* Ordenador 3I tiene la MAC ``9b89``.
* Ordenador 1D tiene la MAC ``94f5``.
* Ordenador 2D tiene la MAC ``ea4a``.
* Ordenador 3D tiene la MAC ``61ae``.
* Ordenador 4D tiene la MAC ``a6c7``.

.. table:: Tabla MAC de Switch 1

    ================  =============
    Numero de puerto       MAC     
    ================  =============
                   0  --           
                   1  ``b3d6``     
                   2  --           
                   3  --           
                   4  ``ea4a,a6c7``
                   5  --           
                   6  --           
                   7  --           
    ================  =============


.. table:: Tabla MAC de Switch 2

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  ``94f5``
                   1  --      
                   2  --      
                   3  --      
                   4  ``a6c7``
                   5  --      
                   6  --      
                   7  ``9b89``
    ================  ========


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``94f5``.
* El Switch 2 envía el mensaje por el puerto 7.
* El Switch 1 envía el mensaje por el puerto 3.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``94f5``.


Ejercicio 16 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 2 que va al puerto 7 del switch 2. Se pretende enviar desde ``699a`` a ``86d6`` sabiendo lo siguiente:


.. figure:: Switches3-4.png

* Ordenador 1I tiene la MAC ``5026``.
* Ordenador 2I tiene la MAC ``526b``.
* Ordenador 3I tiene la MAC ``86d6``.
* Ordenador 1D tiene la MAC ``d454``.
* Ordenador 2D tiene la MAC ``699a``.
* Ordenador 3D tiene la MAC ``d464``.
* Ordenador 4D tiene la MAC ``f172``.

.. table:: Tabla MAC de Switch 1

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  --      
                   2  ``d454``
                   3  --      
                   4  --      
                   5  --      
                   6  --      
                   7  ``86d6``
    ================  ========


.. table:: Tabla MAC de Switch 2

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  --      
                   2  ``699a``
                   3  --      
                   4  ``d454``
                   5  --      
                   6  --      
                   7  --      
    ================  ========


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``699a``.
* El Switch 2 envía el mensaje por el puerto 1.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``699a``.
* El Switch 1 envía el mensaje por el puerto 7.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.


Ejercicio 17 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 3 que va al puerto 0 del switch 2. Se pretende enviar desde ``b578`` a ``4c29`` sabiendo lo siguiente:


.. figure:: Switches3-3.png

* Ordenador 1I tiene la MAC ``f92b``.
* Ordenador 2I tiene la MAC ``b578``.
* Ordenador 3I tiene la MAC ``46dd``.
* Ordenador 1D tiene la MAC ``6daf``.
* Ordenador 2D tiene la MAC ``83bb``.
* Ordenador 3D tiene la MAC ``4c29``.

.. table:: Tabla MAC de Switch 1

    ================  =============
    Numero de puerto       MAC     
    ================  =============
                   0  ``b578``     
                   1  --           
                   2  --           
                   3  ``83bb,4c29``
                   4  --           
                   5  --           
                   6  ``46dd``     
                   7  --           
    ================  =============


.. table:: Tabla MAC de Switch 2

    ================  =============
    Numero de puerto       MAC     
    ================  =============
                   0  ``f92b,46dd``
                   1  --           
                   2  --           
                   3  ``83bb``     
                   4  --           
                   5  --           
                   6  ``4c29``     
                   7  --           
    ================  =============


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 2 envía el mensaje por el puerto 6.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 1 envía el mensaje por el puerto 3.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``b578``.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``b578``.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.


Ejercicio 18 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 3 que va al puerto 7 del switch 2. Se pretende enviar desde ``8e69`` a ``ffaf`` sabiendo lo siguiente:


.. figure:: Switches4-2.png

* Ordenador 1I tiene la MAC ``ed2d``.
* Ordenador 2I tiene la MAC ``8e69``.
* Ordenador 3I tiene la MAC ``cf58``.
* Ordenador 4I tiene la MAC ``faa0``.
* Ordenador 1D tiene la MAC ``a359``.
* Ordenador 2D tiene la MAC ``ffaf``.

.. table:: Tabla MAC de Switch 1

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  ``faa0``
                   1  --      
                   2  --      
                   3  ``ffaf``
                   4  --      
                   5  --      
                   6  --      
                   7  --      
    ================  ========


.. table:: Tabla MAC de Switch 2

    ================  =============
    Numero de puerto       MAC     
    ================  =============
                   0  --           
                   1  --           
                   2  --           
                   3  --           
                   4  --           
                   5  ``a359``     
                   6  --           
                   7  ``ed2d,cf58``
    ================  =============


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``8e69``.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``8e69``.
* El Switch 2 envía el mensaje por el puerto 1.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 1 envía el mensaje por el puerto 3.


Ejercicio 19 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 2 que va al puerto 3 del switch 2. Se pretende enviar desde ``ceda`` a ``ad8a`` sabiendo lo siguiente:


.. figure:: Switches3-2.png

* Ordenador 1I tiene la MAC ``d7fc``.
* Ordenador 2I tiene la MAC ``ad8a``.
* Ordenador 3I tiene la MAC ``f745``.
* Ordenador 1D tiene la MAC ``ceda``.
* Ordenador 2D tiene la MAC ``6045``.

.. table:: Tabla MAC de Switch 1

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  --      
                   2  --      
                   3  ``f745``
                   4  --      
                   5  --      
                   6  --      
                   7  --      
    ================  ========


.. table:: Tabla MAC de Switch 2

    ================  =============
    Numero de puerto       MAC     
    ================  =============
                   0  ``6045``     
                   1  --           
                   2  --           
                   3  ``d7fc,f745``
                   4  --           
                   5  --           
                   6  --           
                   7  --           
    ================  =============


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``ceda``.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 1 envía el mensaje por el puerto 2.
* El Switch 2 envía el mensaje por el puerto 1.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``ceda``.


Ejercicio 20 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 2 que va al puerto 5 del switch 2. Se pretende enviar desde ``c8f4`` a ``9359`` sabiendo lo siguiente:


.. figure:: Switches4-3.png

* Ordenador 1I tiene la MAC ``c8f4``.
* Ordenador 2I tiene la MAC ``52bf``.
* Ordenador 3I tiene la MAC ``ff7f``.
* Ordenador 4I tiene la MAC ``bda6``.
* Ordenador 1D tiene la MAC ``9359``.
* Ordenador 2D tiene la MAC ``8b7b``.
* Ordenador 3D tiene la MAC ``abb3``.

.. table:: Tabla MAC de Switch 1

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  --      
                   2  ``abb3``
                   3  --      
                   4  --      
                   5  ``ff7f``
                   6  --      
                   7  --      
    ================  ========


.. table:: Tabla MAC de Switch 2

    ================  =============
    Numero de puerto       MAC     
    ================  =============
                   0  ``9359``     
                   1  --           
                   2  --           
                   3  --           
                   4  ``abb3``     
                   5  ``ff7f,bda6``
                   6  --           
                   7  --           
    ================  =============


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 1 envía el mensaje por el puerto 6.
* El Switch 2 envía el mensaje por el puerto 0.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``c8f4``.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``c8f4``.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.


Ejercicio 21 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 4 que va al puerto 2 del switch 2. Se pretende enviar desde ``6bcf`` a ``becb`` sabiendo lo siguiente:


.. figure:: Switches3-3.png

* Ordenador 1I tiene la MAC ``fb54``.
* Ordenador 2I tiene la MAC ``becb``.
* Ordenador 3I tiene la MAC ``e68f``.
* Ordenador 1D tiene la MAC ``6bcf``.
* Ordenador 2D tiene la MAC ``b1db``.
* Ordenador 3D tiene la MAC ``854b``.

.. table:: Tabla MAC de Switch 1

    ================  =============
    Numero de puerto       MAC     
    ================  =============
                   0  --           
                   1  --           
                   2  ``e68f``     
                   3  --           
                   4  ``6bcf,b1db``
                   5  --           
                   6  --           
                   7  --           
    ================  =============


.. table:: Tabla MAC de Switch 2

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  ``b1db``
                   2  ``fb54``
                   3  --      
                   4  --      
                   5  ``6bcf``
                   6  --      
                   7  --      
    ================  ========


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``6bcf``.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``6bcf``.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 envía el mensaje por el puerto 1.
* El Switch 2 envía el mensaje por el puerto 7.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.


Ejercicio 22 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 3 que va al puerto 1 del switch 2. Se pretende enviar desde ``d02c`` a ``9d00`` sabiendo lo siguiente:


.. figure:: Switches2-4.png

* Ordenador 1I tiene la MAC ``9d00``.
* Ordenador 2I tiene la MAC ``fbaa``.
* Ordenador 1D tiene la MAC ``da15``.
* Ordenador 2D tiene la MAC ``8fa4``.
* Ordenador 3D tiene la MAC ``bed1``.
* Ordenador 4D tiene la MAC ``d02c``.

.. table:: Tabla MAC de Switch 1

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  ``9d00``
                   2  --      
                   3  --      
                   4  --      
                   5  --      
                   6  --      
                   7  --      
    ================  ========


.. table:: Tabla MAC de Switch 2

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  ``fbaa``
                   2  --      
                   3  --      
                   4  --      
                   5  --      
                   6  --      
                   7  --      
    ================  ========


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 2 envía el mensaje por el puerto 2.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``d02c``.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``d02c``.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 1 envía el mensaje por el puerto 1.


Ejercicio 23 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 0 que va al puerto 1 del switch 2. Se pretende enviar desde ``6f12`` a ``9af0`` sabiendo lo siguiente:


.. figure:: Switches2-2.png

* Ordenador 1I tiene la MAC ``9af0``.
* Ordenador 2I tiene la MAC ``faba``.
* Ordenador 1D tiene la MAC ``6f12``.
* Ordenador 2D tiene la MAC ``5fbf``.

.. table:: Tabla MAC de Switch 1

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  ``faba``
                   1  --      
                   2  --      
                   3  --      
                   4  --      
                   5  --      
                   6  --      
                   7  ``9af0``
    ================  ========


.. table:: Tabla MAC de Switch 2

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  ``faba``
                   2  --      
                   3  --      
                   4  --      
                   5  --      
                   6  --      
                   7  --      
    ================  ========


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``6f12``.
* El Switch 1 envía el mensaje por el puerto 7.
* El Switch 2 envía el mensaje por el puerto 3.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``6f12``.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.


Ejercicio 24 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 1 que va al puerto 2 del switch 2. Se pretende enviar desde ``44a8`` a ``f7ee`` sabiendo lo siguiente:


.. figure:: Switches4-2.png

* Ordenador 1I tiene la MAC ``44a8``.
* Ordenador 2I tiene la MAC ``47fc``.
* Ordenador 3I tiene la MAC ``a511``.
* Ordenador 4I tiene la MAC ``c6da``.
* Ordenador 1D tiene la MAC ``662b``.
* Ordenador 2D tiene la MAC ``f7ee``.

.. table:: Tabla MAC de Switch 1

    ================  ===
    Numero de puerto  MAC
    ================  ===
                   0  -- 
                   1  -- 
                   2  -- 
                   3  -- 
                   4  -- 
                   5  -- 
                   6  -- 
                   7  -- 
    ================  ===


.. table:: Tabla MAC de Switch 2

    ================  ===
    Numero de puerto  MAC
    ================  ===
                   0  -- 
                   1  -- 
                   2  -- 
                   3  -- 
                   4  -- 
                   5  -- 
                   6  -- 
                   7  -- 
    ================  ===


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 1 envía el mensaje por el puerto 6.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``44a8``.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 2 envía el mensaje por el puerto 0.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``44a8``.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.


Ejercicio 25 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 4 que va al puerto 7 del switch 2. Se pretende enviar desde ``d6d4`` a ``f493`` sabiendo lo siguiente:


.. figure:: Switches4-2.png

* Ordenador 1I tiene la MAC ``e6db``.
* Ordenador 2I tiene la MAC ``ee07``.
* Ordenador 3I tiene la MAC ``b3d7``.
* Ordenador 4I tiene la MAC ``d6d4``.
* Ordenador 1D tiene la MAC ``4fe5``.
* Ordenador 2D tiene la MAC ``f493``.

.. table:: Tabla MAC de Switch 1

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  --      
                   2  --      
                   3  --      
                   4  ``4fe5``
                   5  --      
                   6  ``b3d7``
                   7  --      
    ================  ========


.. table:: Tabla MAC de Switch 2

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  --      
                   2  ``4fe5``
                   3  --      
                   4  --      
                   5  --      
                   6  --      
                   7  ``ee07``
    ================  ========


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 1 envía el mensaje por el puerto 1.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``d6d4``.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``d6d4``.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 2 envía el mensaje por el puerto 3.


Ejercicio 26 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 0 que va al puerto 0 del switch 2. Se pretende enviar desde ``5bfc`` a ``d9cd`` sabiendo lo siguiente:


.. figure:: Switches3-3.png

* Ordenador 1I tiene la MAC ``7ed9``.
* Ordenador 2I tiene la MAC ``da84``.
* Ordenador 3I tiene la MAC ``5bfc``.
* Ordenador 1D tiene la MAC ``d9cd``.
* Ordenador 2D tiene la MAC ``b96e``.
* Ordenador 3D tiene la MAC ``cd38``.

.. table:: Tabla MAC de Switch 1

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  --      
                   2  --      
                   3  --      
                   4  ``7ed9``
                   5  --      
                   6  --      
                   7  ``5bfc``
    ================  ========


.. table:: Tabla MAC de Switch 2

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  --      
                   2  --      
                   3  --      
                   4  --      
                   5  --      
                   6  --      
                   7  ``b96e``
    ================  ========


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``5bfc``.
* El Switch 2 envía el mensaje por el puerto 6.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 1 envía el mensaje por el puerto 2.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``5bfc``.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.


Ejercicio 27 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 6 que va al puerto 2 del switch 2. Se pretende enviar desde ``9616`` a ``63e9`` sabiendo lo siguiente:


.. figure:: Switches2-4.png

* Ordenador 1I tiene la MAC ``63e9``.
* Ordenador 2I tiene la MAC ``5b26``.
* Ordenador 1D tiene la MAC ``be88``.
* Ordenador 2D tiene la MAC ``9616``.
* Ordenador 3D tiene la MAC ``fda4``.
* Ordenador 4D tiene la MAC ``6703``.

.. table:: Tabla MAC de Switch 1

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  ``63e9``
                   1  --      
                   2  --      
                   3  --      
                   4  --      
                   5  --      
                   6  --      
                   7  --      
    ================  ========


.. table:: Tabla MAC de Switch 2

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  --      
                   2  ``63e9``
                   3  --      
                   4  --      
                   5  --      
                   6  ``be88``
                   7  --      
    ================  ========


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 2 envía el mensaje por el puerto 2.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``9616``.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``9616``.
* El Switch 1 envía el mensaje por el puerto 0.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.


Ejercicio 28 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 7 que va al puerto 3 del switch 2. Se pretende enviar desde ``7a56`` a ``abae`` sabiendo lo siguiente:


.. figure:: Switches4-4.png

* Ordenador 1I tiene la MAC ``7f54``.
* Ordenador 2I tiene la MAC ``d7cd``.
* Ordenador 3I tiene la MAC ``ce9a``.
* Ordenador 4I tiene la MAC ``7a56``.
* Ordenador 1D tiene la MAC ``b8a6``.
* Ordenador 2D tiene la MAC ``eb2e``.
* Ordenador 3D tiene la MAC ``424a``.
* Ordenador 4D tiene la MAC ``abae``.

.. table:: Tabla MAC de Switch 1

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  --      
                   2  --      
                   3  ``7f54``
                   4  --      
                   5  --      
                   6  --      
                   7  --      
    ================  ========


.. table:: Tabla MAC de Switch 2

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  ``abae``
                   1  --      
                   2  ``424a``
                   3  ``d7cd``
                   4  --      
                   5  --      
                   6  --      
                   7  --      
    ================  ========


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 envía el mensaje por el puerto 2.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``7a56``.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``7a56``.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 2 envía el mensaje por el puerto 0.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.


Ejercicio 29 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 7 que va al puerto 6 del switch 2. Se pretende enviar desde ``f9a6`` a ``8380`` sabiendo lo siguiente:


.. figure:: Switches3-2.png

* Ordenador 1I tiene la MAC ``56b2``.
* Ordenador 2I tiene la MAC ``b0f1``.
* Ordenador 3I tiene la MAC ``f9a6``.
* Ordenador 1D tiene la MAC ``8682``.
* Ordenador 2D tiene la MAC ``8380``.

.. table:: Tabla MAC de Switch 1

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  ``b0f1``
                   2  --      
                   3  --      
                   4  --      
                   5  ``56b2``
                   6  --      
                   7  --      
    ================  ========


.. table:: Tabla MAC de Switch 2

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  ``8682``
                   2  --      
                   3  --      
                   4  ``8380``
                   5  --      
                   6  --      
                   7  --      
    ================  ========


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 2 envía el mensaje por el puerto 4.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``f9a6``.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``f9a6``.
* El Switch 1 envía el mensaje por el puerto 6.


Ejercicio 30 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 0 que va al puerto 2 del switch 2. Se pretende enviar desde ``613e`` a ``6947`` sabiendo lo siguiente:


.. figure:: Switches4-3.png

* Ordenador 1I tiene la MAC ``511d``.
* Ordenador 2I tiene la MAC ``c00a``.
* Ordenador 3I tiene la MAC ``6947``.
* Ordenador 4I tiene la MAC ``7c5f``.
* Ordenador 1D tiene la MAC ``613e``.
* Ordenador 2D tiene la MAC ``aa57``.
* Ordenador 3D tiene la MAC ``a7a7``.

.. table:: Tabla MAC de Switch 1

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  ``a7a7``
                   1  --      
                   2  --      
                   3  ``c00a``
                   4  --      
                   5  --      
                   6  --      
                   7  ``511d``
    ================  ========


.. table:: Tabla MAC de Switch 2

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  --      
                   2  ``7c5f``
                   3  ``613e``
                   4  --      
                   5  --      
                   6  ``a7a7``
                   7  --      
    ================  ========


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``613e``.
* El Switch 2 envía el mensaje por el puerto 1.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 1 envía el mensaje por el puerto 4.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``613e``.

Solucion al ejercicio 1 de switches
-----------------------------------------
Las respuestas son:

* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``ec0c``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen ec0c.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen ec0c, así que la anota.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino a548 en su tabla
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino a548 en su tabla
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen ec0c, así que la anota.
* El Switch 2 envía el mensaje por el puerto 4. **Falsa**, no conoce a la MAC de destino a548, así que necesita difundir.
* El Switch 1 envía el mensaje por el puerto 6. **Falsa**, no conoce a la MAC de destino a548, así que necesita difundir.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``ec0c``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen ec0c.

Solucion al ejercicio 2 de switches
-----------------------------------------
Las respuestas son:

* El Switch 2 envía el mensaje por el puerto 4. **Falsa**, no conoce a la MAC de destino 9e68, así que necesita difundir.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen dd84, así que la anota.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino 9e68 en su tabla
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen dd84.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino 9e68 en su tabla, en el puerto 1.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``dd84``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen dd84.
* El Switch 1 envía el mensaje por el puerto 1. **Verdadera**, 9e68 está en esa posición en la tabla de MACs
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``dd84``. **Falsa**, ya tenía esa MAC

Solucion al ejercicio 3 de switches
-----------------------------------------
Las respuestas son:

* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``de08``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen de08.
* El Switch 1 envía el mensaje por el puerto 4. **Verdadera**, 8413 está en esa posición en la tabla de MACs
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino 8413 en su tabla, en el puerto 4.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``de08``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen de08.
* El Switch 2 envía el mensaje por el puerto 5. **Falsa**, no conoce a la MAC de destino 8413, así que necesita difundir.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen de08, así que la anota.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen de08, así que la anota.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino 8413 en su tabla

Solucion al ejercicio 4 de switches
-----------------------------------------
Las respuestas son:

* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino e9b5 en su tabla
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``50d2``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen 50d2.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen 50d2.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen 50d2, así que la anota.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino e9b5 en su tabla
* El Switch 2 envía el mensaje por el puerto 5. **Falsa**, no conoce a la MAC de destino e9b5, así que necesita difundir.
* El Switch 1 envía el mensaje por el puerto 4. **Falsa**, no conoce a la MAC de destino e9b5, así que necesita difundir.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``50d2``. **Falsa**, ya tenía esa MAC

Solucion al ejercicio 5 de switches
-----------------------------------------
Las respuestas son:

* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino 9a1a en su tabla
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen d973, así que la anota.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``d973``. **Falsa**, ya tenía esa MAC
* El Switch 1 envía el mensaje por el puerto 3. **Falsa**, no conoce a la MAC de destino 9a1a, así que necesita difundir.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino 9a1a en su tabla
* El Switch 2 envía el mensaje por el puerto 3. **Falsa**, no conoce a la MAC de destino 9a1a, así que necesita difundir.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen d973.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``d973``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen d973.

Solucion al ejercicio 6 de switches
-----------------------------------------
Las respuestas son:

* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``cf0f``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen cf0f.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino d421 en su tabla
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen cf0f, así que la anota.
* El Switch 2 envía el mensaje por el puerto 1. **Falsa**, no conoce a la MAC de destino d421, así que necesita difundir.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``cf0f``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen cf0f.
* El Switch 1 envía el mensaje por el puerto 3. **Falsa**, no conoce a la MAC de destino d421, así que necesita difundir.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino d421 en su tabla
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen cf0f, así que la anota.

Solucion al ejercicio 7 de switches
-----------------------------------------
Las respuestas son:

* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``d5e8``. **Falsa**, ya tenía esa MAC
* El Switch 2 envía el mensaje por el puerto 2. **Falsa**, no conoce a la MAC de destino 889f, así que necesita difundir.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino 889f en su tabla, en el puerto 5.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen d5e8, así que la anota.
* El Switch 1 envía el mensaje por el puerto 5. **Verdadera**, 889f está en esa posición en la tabla de MACs
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``d5e8``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen d5e8.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino 889f en su tabla
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen d5e8.

Solucion al ejercicio 8 de switches
-----------------------------------------
Las respuestas son:

* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen 42fd, así que la anota.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino 6e03 en su tabla, en el puerto 2.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino 6e03 en su tabla, en el puerto 6.
* El Switch 1 envía el mensaje por el puerto 2. **Verdadera**, 6e03 está en esa posición en la tabla de MACs
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``42fd``. **Falsa**, ya tenía esa MAC
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen 42fd.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``42fd``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen 42fd.
* El Switch 2 envía el mensaje por el puerto 6. **Verdadera**, 6e03 está en esa posición en la tabla de MACs

Solucion al ejercicio 9 de switches
-----------------------------------------
Las respuestas son:

* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``94bb``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen 94bb.
* El Switch 2 envía el mensaje por el puerto 7. **Falsa**, no conoce a la MAC de destino cb23, así que necesita difundir.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen 94bb, así que la anota.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen 94bb, así que la anota.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino cb23 en su tabla
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino cb23 en su tabla, en el puerto 1.
* El Switch 1 envía el mensaje por el puerto 1. **Verdadera**, cb23 está en esa posición en la tabla de MACs
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``94bb``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen 94bb.

Solucion al ejercicio 10 de switches
-----------------------------------------
Las respuestas son:

* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``7026``. **Falsa**, ya tenía esa MAC
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino a423 en su tabla, en el puerto 2.
* El Switch 1 envía el mensaje por el puerto 2. **Verdadera**, a423 está en esa posición en la tabla de MACs
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino a423 en su tabla
* El Switch 2 envía el mensaje por el puerto 5. **Falsa**, no conoce a la MAC de destino a423, así que necesita difundir.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen 7026.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``7026``. **Falsa**, ya tenía esa MAC
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen 7026.

Solucion al ejercicio 11 de switches
-----------------------------------------
Las respuestas son:

* El Switch 1 envía el mensaje por el puerto 0. **Falsa**, no conoce a la MAC de destino 5f4c, así que necesita difundir.
* El Switch 2 envía el mensaje por el puerto 1. **Falsa**, no conoce a la MAC de destino 5f4c, así que necesita difundir.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``ee1f``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen ee1f.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino 5f4c en su tabla
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen ee1f, así que la anota.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen ee1f.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``ee1f``. **Falsa**, ya tenía esa MAC
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino 5f4c en su tabla

Solucion al ejercicio 12 de switches
-----------------------------------------
Las respuestas son:

* El Switch 1 envía el mensaje por el puerto 7. **Falsa**, no conoce a la MAC de destino 79d5, así que necesita difundir.
* El Switch 2 envía el mensaje por el puerto 1. **Falsa**, no conoce a la MAC de destino 79d5, así que necesita difundir.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen 418d.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``418d``. **Falsa**, ya tenía esa MAC
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino 79d5 en su tabla
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``418d``. **Falsa**, ya tenía esa MAC
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen 418d.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino 79d5 en su tabla

Solucion al ejercicio 13 de switches
-----------------------------------------
Las respuestas son:

* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``920f``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen 920f.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``920f``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen 920f.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen 920f, así que la anota.
* El Switch 1 envía el mensaje por el puerto 1. **Verdadera**, cc20 está en esa posición en la tabla de MACs
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino cc20 en su tabla
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino cc20 en su tabla, en el puerto 1.
* El Switch 2 envía el mensaje por el puerto 5. **Falsa**, no conoce a la MAC de destino cc20, así que necesita difundir.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen 920f, así que la anota.

Solucion al ejercicio 14 de switches
-----------------------------------------
Las respuestas son:

* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``6301``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen 6301.
* El Switch 2 envía el mensaje por el puerto 2. **Falsa**, no conoce a la MAC de destino d6de, así que necesita difundir.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``6301``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen 6301.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino d6de en su tabla
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino d6de en su tabla
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen 6301, así que la anota.
* El Switch 1 envía el mensaje por el puerto 5. **Falsa**, no conoce a la MAC de destino d6de, así que necesita difundir.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen 6301, así que la anota.

Solucion al ejercicio 15 de switches
-----------------------------------------
Las respuestas son:

* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``94f5``. **Falsa**, ya tenía esa MAC
* El Switch 2 envía el mensaje por el puerto 7. **Verdadera**, 9b89 está en esa posición en la tabla de MACs
* El Switch 1 envía el mensaje por el puerto 3. **Falsa**, no conoce a la MAC de destino 9b89, así que necesita difundir.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen 94f5.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino 9b89 en su tabla
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino 9b89 en su tabla, en el puerto 7.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen 94f5, así que la anota.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``94f5``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen 94f5.

Solucion al ejercicio 16 de switches
-----------------------------------------
Las respuestas son:

* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen 699a.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``699a``. **Falsa**, ya tenía esa MAC
* El Switch 2 envía el mensaje por el puerto 1. **Falsa**, no conoce a la MAC de destino 86d6, así que necesita difundir.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino 86d6 en su tabla, en el puerto 7.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen 699a, así que la anota.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``699a``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen 699a.
* El Switch 1 envía el mensaje por el puerto 7. **Verdadera**, 86d6 está en esa posición en la tabla de MACs
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino 86d6 en su tabla

Solucion al ejercicio 17 de switches
-----------------------------------------
Las respuestas son:

* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen b578, así que la anota.
* El Switch 2 envía el mensaje por el puerto 6. **Verdadera**, 4c29 está en esa posición en la tabla de MACs
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen b578.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino 4c29 en su tabla, en el puerto 6.
* El Switch 1 envía el mensaje por el puerto 3. **Verdadera**, 4c29 está en esa posición en la tabla de MACs
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``b578``. **Falsa**, ya tenía esa MAC
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``b578``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen b578.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino 4c29 en su tabla, en el puerto 3.

Solucion al ejercicio 18 de switches
-----------------------------------------
Las respuestas son:

* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen 8e69, así que la anota.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen 8e69, así que la anota.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``8e69``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen 8e69.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino ffaf en su tabla
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``8e69``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen 8e69.
* El Switch 2 envía el mensaje por el puerto 1. **Falsa**, no conoce a la MAC de destino ffaf, así que necesita difundir.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino ffaf en su tabla, en el puerto 3.
* El Switch 1 envía el mensaje por el puerto 3. **Verdadera**, ffaf está en esa posición en la tabla de MACs

Solucion al ejercicio 19 de switches
-----------------------------------------
Las respuestas son:

* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen ceda, así que la anota.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``ceda``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen ceda.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino ad8a en su tabla
* El Switch 1 envía el mensaje por el puerto 2. **Falsa**, no conoce a la MAC de destino ad8a, así que necesita difundir.
* El Switch 2 envía el mensaje por el puerto 1. **Falsa**, no conoce a la MAC de destino ad8a, así que necesita difundir.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen ceda, así que la anota.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino ad8a en su tabla
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``ceda``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen ceda.

Solucion al ejercicio 20 de switches
-----------------------------------------
Las respuestas son:

* El Switch 1 envía el mensaje por el puerto 6. **Falsa**, no conoce a la MAC de destino 9359, así que necesita difundir.
* El Switch 2 envía el mensaje por el puerto 0. **Verdadera**, 9359 está en esa posición en la tabla de MACs
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``c8f4``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen c8f4.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen c8f4, así que la anota.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen c8f4, así que la anota.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino 9359 en su tabla
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``c8f4``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen c8f4.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino 9359 en su tabla, en el puerto 0.

Solucion al ejercicio 21 de switches
-----------------------------------------
Las respuestas son:

* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino becb en su tabla
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``6bcf``. **Falsa**, ya tenía esa MAC
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen 6bcf.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``6bcf``. **Falsa**, ya tenía esa MAC
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen 6bcf.
* El Switch 1 envía el mensaje por el puerto 1. **Falsa**, no conoce a la MAC de destino becb, así que necesita difundir.
* El Switch 2 envía el mensaje por el puerto 7. **Falsa**, no conoce a la MAC de destino becb, así que necesita difundir.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino becb en su tabla

Solucion al ejercicio 22 de switches
-----------------------------------------
Las respuestas son:

* El Switch 2 envía el mensaje por el puerto 2. **Falsa**, no conoce a la MAC de destino 9d00, así que necesita difundir.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``d02c``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen d02c.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen d02c, así que la anota.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino 9d00 en su tabla
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen d02c, así que la anota.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``d02c``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen d02c.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino 9d00 en su tabla, en el puerto 1.
* El Switch 1 envía el mensaje por el puerto 1. **Verdadera**, 9d00 está en esa posición en la tabla de MACs

Solucion al ejercicio 23 de switches
-----------------------------------------
Las respuestas son:

* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen 6f12, así que la anota.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino 9af0 en su tabla, en el puerto 7.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``6f12``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen 6f12.
* El Switch 1 envía el mensaje por el puerto 7. **Verdadera**, 9af0 está en esa posición en la tabla de MACs
* El Switch 2 envía el mensaje por el puerto 3. **Falsa**, no conoce a la MAC de destino 9af0, así que necesita difundir.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen 6f12, así que la anota.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``6f12``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen 6f12.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino 9af0 en su tabla

Solucion al ejercicio 24 de switches
-----------------------------------------
Las respuestas son:

* El Switch 1 envía el mensaje por el puerto 6. **Falsa**, no conoce a la MAC de destino f7ee, así que necesita difundir.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen 44a8, así que la anota.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``44a8``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen 44a8.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen 44a8, así que la anota.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino f7ee en su tabla
* El Switch 2 envía el mensaje por el puerto 0. **Falsa**, no conoce a la MAC de destino f7ee, así que necesita difundir.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``44a8``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen 44a8.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino f7ee en su tabla

Solucion al ejercicio 25 de switches
-----------------------------------------
Las respuestas son:

* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino f493 en su tabla
* El Switch 1 envía el mensaje por el puerto 1. **Falsa**, no conoce a la MAC de destino f493, así que necesita difundir.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen d6d4, así que la anota.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``d6d4``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen d6d4.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen d6d4, así que la anota.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``d6d4``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen d6d4.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino f493 en su tabla
* El Switch 2 envía el mensaje por el puerto 3. **Falsa**, no conoce a la MAC de destino f493, así que necesita difundir.

Solucion al ejercicio 26 de switches
-----------------------------------------
Las respuestas son:

* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``5bfc``. **Falsa**, ya tenía esa MAC
* El Switch 2 envía el mensaje por el puerto 6. **Falsa**, no conoce a la MAC de destino d9cd, así que necesita difundir.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino d9cd en su tabla
* El Switch 1 envía el mensaje por el puerto 2. **Falsa**, no conoce a la MAC de destino d9cd, así que necesita difundir.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino d9cd en su tabla
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen 5bfc.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``5bfc``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen 5bfc.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen 5bfc, así que la anota.

Solucion al ejercicio 27 de switches
-----------------------------------------
Las respuestas son:

* El Switch 2 envía el mensaje por el puerto 2. **Verdadera**, 63e9 está en esa posición en la tabla de MACs
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen 9616, así que la anota.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino 63e9 en su tabla, en el puerto 0.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``9616``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen 9616.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen 9616, así que la anota.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``9616``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen 9616.
* El Switch 1 envía el mensaje por el puerto 0. **Verdadera**, 63e9 está en esa posición en la tabla de MACs
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino 63e9 en su tabla, en el puerto 2.

Solucion al ejercicio 28 de switches
-----------------------------------------
Las respuestas son:

* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen 7a56, así que la anota.
* El Switch 1 envía el mensaje por el puerto 2. **Falsa**, no conoce a la MAC de destino abae, así que necesita difundir.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``7a56``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen 7a56.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen 7a56, así que la anota.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``7a56``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen 7a56.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino abae en su tabla, en el puerto 0.
* El Switch 2 envía el mensaje por el puerto 0. **Verdadera**, abae está en esa posición en la tabla de MACs
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino abae en su tabla

Solucion al ejercicio 29 de switches
-----------------------------------------
Las respuestas son:

* El Switch 2 envía el mensaje por el puerto 4. **Verdadera**, 8380 está en esa posición en la tabla de MACs
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino 8380 en su tabla
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino 8380 en su tabla, en el puerto 4.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``f9a6``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen f9a6.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen f9a6, así que la anota.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen f9a6, así que la anota.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``f9a6``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen f9a6.
* El Switch 1 envía el mensaje por el puerto 6. **Falsa**, no conoce a la MAC de destino 8380, así que necesita difundir.

Solucion al ejercicio 30 de switches
-----------------------------------------
Las respuestas son:

* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen 613e.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``613e``. **Falsa**, ya tenía esa MAC
* El Switch 2 envía el mensaje por el puerto 1. **Falsa**, no conoce a la MAC de destino 6947, así que necesita difundir.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino 6947 en su tabla
* El Switch 1 envía el mensaje por el puerto 4. **Falsa**, no conoce a la MAC de destino 6947, así que necesita difundir.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino 6947 en su tabla
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen 613e, así que la anota.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``613e``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen 613e.
