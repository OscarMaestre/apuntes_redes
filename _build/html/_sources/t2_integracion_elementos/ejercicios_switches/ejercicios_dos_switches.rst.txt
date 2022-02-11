Anexo: ejercicios con tablas MAC de switches
================================================


Ejercicio 1 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 1 que va al puerto 2 del switch 2. Se pretende enviar desde ``65fc`` a ``a15e`` sabiendo lo siguiente:


.. figure:: Switches3-2.png

* Ordenador 1I tiene la MAC ``ea9b``.
* Ordenador 2I tiene la MAC ``65fc``.
* Ordenador 3I tiene la MAC ``9e6f``.
* Ordenador 1D tiene la MAC ``eb9a``.
* Ordenador 2D tiene la MAC ``a15e``.

.. table:: Tabla MAC de Switch 1

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  ``65fc``
                   2  ``9e6f``
                   3  --      
                   4  ``ea9b``
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

1. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
2. El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
3. El Switch 2 envía el mensaje por el puerto 7.
4. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``65fc``.
5. El Switch 1 envía el mensaje por el puerto 6.
6. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``65fc``.
7. El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
8. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.


Ejercicio 2 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 1 que va al puerto 4 del switch 2. Se pretende enviar desde ``b039`` a ``c50e`` sabiendo lo siguiente:


.. figure:: Switches2-2.png

* Ordenador 1I tiene la MAC ``b039``.
* Ordenador 2I tiene la MAC ``a6e8``.
* Ordenador 1D tiene la MAC ``c50e``.
* Ordenador 2D tiene la MAC ``b490``.

.. table:: Tabla MAC de Switch 1

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  ``b490``
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
                   2  --      
                   3  ``b490``
                   4  --      
                   5  --      
                   6  --      
                   7  --      
    ================  ========


Indica si las siguientes afirmaciones son verdaderas o falsas:

1. El Switch 2 envía el mensaje por el puerto 2.
2. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``b039``.
3. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
4. El Switch 1 envía el mensaje por el puerto 0.
5. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``b039``.
6. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
7. El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
8. El Switch 2 envía el mensaje por todos los puertos menos por donde vino.


Ejercicio 3 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 6 que va al puerto 4 del switch 2. Se pretende enviar desde ``a636`` a ``8fc8`` sabiendo lo siguiente:


.. figure:: Switches2-3.png

* Ordenador 1I tiene la MAC ``c583``.
* Ordenador 2I tiene la MAC ``a636``.
* Ordenador 1D tiene la MAC ``98a8``.
* Ordenador 2D tiene la MAC ``94bd``.
* Ordenador 3D tiene la MAC ``8fc8``.

.. table:: Tabla MAC de Switch 1

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  ``c583``
                   2  --      
                   3  --      
                   4  --      
                   5  ``a636``
                   6  ``94bd``
                   7  --      
    ================  ========


.. table:: Tabla MAC de Switch 2

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  --      
                   2  ``94bd``
                   3  --      
                   4  ``c583``
                   5  --      
                   6  --      
                   7  --      
    ================  ========


Indica si las siguientes afirmaciones son verdaderas o falsas:

1. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
2. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``a636``.
3. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``a636``.
4. El Switch 2 envía el mensaje por el puerto 3.
5. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
6. El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
7. El Switch 1 envía el mensaje por el puerto 3.
8. El Switch 1 envía el mensaje por todos los puertos menos por donde vino.


Ejercicio 4 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 6 que va al puerto 4 del switch 2. Se pretende enviar desde ``b4f3`` a ``7a3c`` sabiendo lo siguiente:


.. figure:: Switches3-4.png

* Ordenador 1I tiene la MAC ``e607``.
* Ordenador 2I tiene la MAC ``5a70``.
* Ordenador 3I tiene la MAC ``b4f3``.
* Ordenador 1D tiene la MAC ``7a3c``.
* Ordenador 2D tiene la MAC ``fd70``.
* Ordenador 3D tiene la MAC ``b54d``.
* Ordenador 4D tiene la MAC ``c4a2``.

.. table:: Tabla MAC de Switch 1

    ================  =============
    Numero de puerto       MAC     
    ================  =============
                   0  --           
                   1  --           
                   2  --           
                   3  --           
                   4  --           
                   5  --           
                   6  ``7a3c,b54d``
                   7  --           
    ================  =============


.. table:: Tabla MAC de Switch 2

    ================  =============
    Numero de puerto       MAC     
    ================  =============
                   0  ``b54d``     
                   1  ``7a3c``     
                   2  --           
                   3  --           
                   4  ``e607,b4f3``
                   5  --           
                   6  --           
                   7  --           
    ================  =============


Indica si las siguientes afirmaciones son verdaderas o falsas:

1. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``b4f3``.
2. El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
3. El Switch 1 envía el mensaje por el puerto 6.
4. El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
5. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
6. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
7. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``b4f3``.
8. El Switch 2 envía el mensaje por el puerto 1.


Ejercicio 5 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 5 que va al puerto 3 del switch 2. Se pretende enviar desde ``bf67`` a ``bf66`` sabiendo lo siguiente:


.. figure:: Switches3-3.png

* Ordenador 1I tiene la MAC ``6a0f``.
* Ordenador 2I tiene la MAC ``4bd8``.
* Ordenador 3I tiene la MAC ``bf67``.
* Ordenador 1D tiene la MAC ``bf66``.
* Ordenador 2D tiene la MAC ``8ac4``.
* Ordenador 3D tiene la MAC ``482a``.

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
                   2  ``482a``
                   3  --      
                   4  --      
                   5  --      
                   6  --      
                   7  --      
    ================  ========


Indica si las siguientes afirmaciones son verdaderas o falsas:

1. El Switch 2 envía el mensaje por el puerto 4.
2. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``bf67``.
3. El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
4. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
5. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``bf67``.
6. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
7. El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
8. El Switch 1 envía el mensaje por el puerto 3.


Ejercicio 6 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 7 que va al puerto 7 del switch 2. Se pretende enviar desde ``61a4`` a ``b5f1`` sabiendo lo siguiente:


.. figure:: Switches4-4.png

* Ordenador 1I tiene la MAC ``f6bf``.
* Ordenador 2I tiene la MAC ``fcf5``.
* Ordenador 3I tiene la MAC ``61a4``.
* Ordenador 4I tiene la MAC ``96e2``.
* Ordenador 1D tiene la MAC ``c153``.
* Ordenador 2D tiene la MAC ``9c0b``.
* Ordenador 3D tiene la MAC ``b5f1``.
* Ordenador 4D tiene la MAC ``a32d``.

.. table:: Tabla MAC de Switch 1

    ================  =============
    Numero de puerto       MAC     
    ================  =============
                   0  --           
                   1  ``61a4``     
                   2  --           
                   3  ``fcf5``     
                   4  --           
                   5  --           
                   6  --           
                   7  ``c153,a32d``
    ================  =============


.. table:: Tabla MAC de Switch 2

    ================  ==================
    Numero de puerto         MAC        
    ================  ==================
                   0  --                
                   1  --                
                   2  --                
                   3  --                
                   4  --                
                   5  ``c153``          
                   6  --                
                   7  ``fcf5,61a4,96e2``
    ================  ==================


Indica si las siguientes afirmaciones son verdaderas o falsas:

1. El Switch 1 envía el mensaje por el puerto 4.
2. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``61a4``.
3. El Switch 2 envía el mensaje por el puerto 3.
4. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
5. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
6. El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
7. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``61a4``.
8. El Switch 2 envía el mensaje por todos los puertos menos por donde vino.


Ejercicio 7 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 2 que va al puerto 0 del switch 2. Se pretende enviar desde ``6d8d`` a ``5fa6`` sabiendo lo siguiente:


.. figure:: Switches3-4.png

* Ordenador 1I tiene la MAC ``95c5``.
* Ordenador 2I tiene la MAC ``7dac``.
* Ordenador 3I tiene la MAC ``6d8d``.
* Ordenador 1D tiene la MAC ``e387``.
* Ordenador 2D tiene la MAC ``6198``.
* Ordenador 3D tiene la MAC ``4099``.
* Ordenador 4D tiene la MAC ``5fa6``.

.. table:: Tabla MAC de Switch 1

    ================  =============
    Numero de puerto       MAC     
    ================  =============
                   0  --           
                   1  --           
                   2  ``e387,6198``
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
                   0  ``6d8d``
                   1  --      
                   2  --      
                   3  ``e387``
                   4  --      
                   5  --      
                   6  --      
                   7  --      
    ================  ========


Indica si las siguientes afirmaciones son verdaderas o falsas:

1. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
2. El Switch 2 envía el mensaje por el puerto 7.
3. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
4. El Switch 1 envía el mensaje por el puerto 1.
5. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``6d8d``.
6. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``6d8d``.
7. El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
8. El Switch 1 envía el mensaje por todos los puertos menos por donde vino.


Ejercicio 8 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 6 que va al puerto 1 del switch 2. Se pretende enviar desde ``958c`` a ``bb84`` sabiendo lo siguiente:


.. figure:: Switches3-2.png

* Ordenador 1I tiene la MAC ``958c``.
* Ordenador 2I tiene la MAC ``94ce``.
* Ordenador 3I tiene la MAC ``80e7``.
* Ordenador 1D tiene la MAC ``9690``.
* Ordenador 2D tiene la MAC ``bb84``.

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
                   1  ``94ce``
                   2  --      
                   3  --      
                   4  --      
                   5  --      
                   6  ``9690``
                   7  --      
    ================  ========


Indica si las siguientes afirmaciones son verdaderas o falsas:

1. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
2. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
3. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``958c``.
4. El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
5. El Switch 2 envía el mensaje por el puerto 2.
6. El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
7. El Switch 1 envía el mensaje por el puerto 4.
8. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``958c``.


Ejercicio 9 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 4 que va al puerto 7 del switch 2. Se pretende enviar desde ``cb76`` a ``bee9`` sabiendo lo siguiente:


.. figure:: Switches4-2.png

* Ordenador 1I tiene la MAC ``bee9``.
* Ordenador 2I tiene la MAC ``8c88``.
* Ordenador 3I tiene la MAC ``457c``.
* Ordenador 4I tiene la MAC ``beea``.
* Ordenador 1D tiene la MAC ``cb76``.
* Ordenador 2D tiene la MAC ``abf2``.

.. table:: Tabla MAC de Switch 1

    ================  =============
    Numero de puerto       MAC     
    ================  =============
                   0  ``8c88``     
                   1  --           
                   2  ``457c``     
                   3  --           
                   4  ``cb76,abf2``
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
                   2  --      
                   3  --      
                   4  ``cb76``
                   5  --      
                   6  --      
                   7  ``beea``
    ================  ========


Indica si las siguientes afirmaciones son verdaderas o falsas:

1. El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
2. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
3. El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
4. El Switch 1 envía el mensaje por el puerto 6.
5. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
6. El Switch 2 envía el mensaje por el puerto 0.
7. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``cb76``.
8. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``cb76``.


Ejercicio 10 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 0 que va al puerto 7 del switch 2. Se pretende enviar desde ``5a09`` a ``c525`` sabiendo lo siguiente:


.. figure:: Switches2-3.png

* Ordenador 1I tiene la MAC ``95c3``.
* Ordenador 2I tiene la MAC ``5a09``.
* Ordenador 1D tiene la MAC ``c525``.
* Ordenador 2D tiene la MAC ``d0bd``.
* Ordenador 3D tiene la MAC ``7083``.

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
                   0  ``7083``
                   1  --      
                   2  --      
                   3  --      
                   4  --      
                   5  ``c525``
                   6  --      
                   7  ``5a09``
    ================  ========


Indica si las siguientes afirmaciones son verdaderas o falsas:

1. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``5a09``.
2. El Switch 1 envía el mensaje por el puerto 0.
3. El Switch 2 envía el mensaje por el puerto 5.
4. El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
5. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
6. El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
7. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
8. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``5a09``.


Ejercicio 11 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 6 que va al puerto 3 del switch 2. Se pretende enviar desde ``cc6a`` a ``7019`` sabiendo lo siguiente:


.. figure:: Switches3-3.png

* Ordenador 1I tiene la MAC ``60b2``.
* Ordenador 2I tiene la MAC ``7019``.
* Ordenador 3I tiene la MAC ``9b6f``.
* Ordenador 1D tiene la MAC ``6275``.
* Ordenador 2D tiene la MAC ``cc6a``.
* Ordenador 3D tiene la MAC ``9f99``.

.. table:: Tabla MAC de Switch 1

    ================  =============
    Numero de puerto       MAC     
    ================  =============
                   0  --           
                   1  --           
                   2  ``7019``     
                   3  --           
                   4  --           
                   5  --           
                   6  ``6275,cc6a``
                   7  --           
    ================  =============


.. table:: Tabla MAC de Switch 2

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  --      
                   2  --      
                   3  ``9b6f``
                   4  --      
                   5  --      
                   6  --      
                   7  --      
    ================  ========


Indica si las siguientes afirmaciones son verdaderas o falsas:

1. El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
2. El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
3. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
4. El Switch 1 envía el mensaje por el puerto 2.
5. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``cc6a``.
6. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``cc6a``.
7. El Switch 2 envía el mensaje por el puerto 1.
8. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.


Ejercicio 12 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 6 que va al puerto 1 del switch 2. Se pretende enviar desde ``a96c`` a ``500d`` sabiendo lo siguiente:


.. figure:: Switches3-4.png

* Ordenador 1I tiene la MAC ``500d``.
* Ordenador 2I tiene la MAC ``f182``.
* Ordenador 3I tiene la MAC ``8c75``.
* Ordenador 1D tiene la MAC ``471e``.
* Ordenador 2D tiene la MAC ``a07c``.
* Ordenador 3D tiene la MAC ``a96c``.
* Ordenador 4D tiene la MAC ``4c6b``.

.. table:: Tabla MAC de Switch 1

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  ``500d``
                   2  --      
                   3  --      
                   4  --      
                   5  ``8c75``
                   6  ``4c6b``
                   7  --      
    ================  ========


.. table:: Tabla MAC de Switch 2

    ================  ==================
    Numero de puerto         MAC        
    ================  ==================
                   0  --                
                   1  ``500d,f182,8c75``
                   2  ``471e``          
                   3  ``4c6b``          
                   4  --                
                   5  --                
                   6  --                
                   7  --                
    ================  ==================


Indica si las siguientes afirmaciones son verdaderas o falsas:

1. El Switch 2 envía el mensaje por el puerto 1.
2. El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
3. El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
4. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
5. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``a96c``.
6. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
7. El Switch 1 envía el mensaje por el puerto 1.
8. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``a96c``.


Ejercicio 13 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 6 que va al puerto 7 del switch 2. Se pretende enviar desde ``8ce0`` a ``9b8c`` sabiendo lo siguiente:


.. figure:: Switches2-4.png

* Ordenador 1I tiene la MAC ``8ce0``.
* Ordenador 2I tiene la MAC ``6a4b``.
* Ordenador 1D tiene la MAC ``c5c3``.
* Ordenador 2D tiene la MAC ``be66``.
* Ordenador 3D tiene la MAC ``9b8c``.
* Ordenador 4D tiene la MAC ``6ff1``.

.. table:: Tabla MAC de Switch 1

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  ``8ce0``
                   1  --      
                   2  --      
                   3  --      
                   4  --      
                   5  --      
                   6  ``9b8c``
                   7  --      
    ================  ========


.. table:: Tabla MAC de Switch 2

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  --      
                   2  --      
                   3  ``be66``
                   4  ``c5c3``
                   5  --      
                   6  --      
                   7  ``6a4b``
    ================  ========


Indica si las siguientes afirmaciones son verdaderas o falsas:

1. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``8ce0``.
2. El Switch 2 envía el mensaje por el puerto 2.
3. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
4. El Switch 1 envía el mensaje por el puerto 6.
5. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``8ce0``.
6. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
7. El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
8. El Switch 2 envía el mensaje por todos los puertos menos por donde vino.


Ejercicio 14 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 2 que va al puerto 4 del switch 2. Se pretende enviar desde ``af07`` a ``bafc`` sabiendo lo siguiente:


.. figure:: Switches2-2.png

* Ordenador 1I tiene la MAC ``bafc``.
* Ordenador 2I tiene la MAC ``7c04``.
* Ordenador 1D tiene la MAC ``af07``.
* Ordenador 2D tiene la MAC ``cca8``.

.. table:: Tabla MAC de Switch 1

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  ``7c04``
                   1  --      
                   2  --      
                   3  --      
                   4  --      
                   5  --      
                   6  --      
                   7  ``bafc``
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

1. El Switch 1 envía el mensaje por el puerto 7.
2. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``af07``.
3. El Switch 2 envía el mensaje por el puerto 4.
4. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
5. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``af07``.
6. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
7. El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
8. El Switch 2 envía el mensaje por todos los puertos menos por donde vino.


Ejercicio 15 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 0 que va al puerto 4 del switch 2. Se pretende enviar desde ``c85b`` a ``ac7b`` sabiendo lo siguiente:


.. figure:: Switches3-2.png

* Ordenador 1I tiene la MAC ``c85b``.
* Ordenador 2I tiene la MAC ``f0b6``.
* Ordenador 3I tiene la MAC ``d3b0``.
* Ordenador 1D tiene la MAC ``55af``.
* Ordenador 2D tiene la MAC ``ac7b``.

.. table:: Tabla MAC de Switch 1

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  ``c85b``
                   1  --      
                   2  --      
                   3  --      
                   4  --      
                   5  --      
                   6  --      
                   7  ``f0b6``
    ================  ========


.. table:: Tabla MAC de Switch 2

    ================  ==================
    Numero de puerto         MAC        
    ================  ==================
                   0  --                
                   1  --                
                   2  --                
                   3  --                
                   4  ``c85b,f0b6,d3b0``
                   5  --                
                   6  --                
                   7  --                
    ================  ==================


Indica si las siguientes afirmaciones son verdaderas o falsas:

1. El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
2. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
3. El Switch 2 envía el mensaje por el puerto 1.
4. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``c85b``.
5. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``c85b``.
6. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
7. El Switch 1 envía el mensaje por el puerto 3.
8. El Switch 1 envía el mensaje por todos los puertos menos por donde vino.


Ejercicio 16 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 3 que va al puerto 0 del switch 2. Se pretende enviar desde ``6bdc`` a ``e281`` sabiendo lo siguiente:


.. figure:: Switches3-3.png

* Ordenador 1I tiene la MAC ``94a5``.
* Ordenador 2I tiene la MAC ``e281``.
* Ordenador 3I tiene la MAC ``e902``.
* Ordenador 1D tiene la MAC ``7395``.
* Ordenador 2D tiene la MAC ``945e``.
* Ordenador 3D tiene la MAC ``6bdc``.

.. table:: Tabla MAC de Switch 1

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  --      
                   2  --      
                   3  ``6bdc``
                   4  --      
                   5  --      
                   6  ``e281``
                   7  ``e902``
    ================  ========


.. table:: Tabla MAC de Switch 2

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  ``e281``
                   1  --      
                   2  --      
                   3  --      
                   4  ``945e``
                   5  --      
                   6  --      
                   7  --      
    ================  ========


Indica si las siguientes afirmaciones son verdaderas o falsas:

1. El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
2. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
3. El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
4. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``6bdc``.
5. El Switch 1 envía el mensaje por el puerto 6.
6. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``6bdc``.
7. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
8. El Switch 2 envía el mensaje por el puerto 0.


Ejercicio 17 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 5 que va al puerto 0 del switch 2. Se pretende enviar desde ``c21f`` a ``6c3f`` sabiendo lo siguiente:


.. figure:: Switches2-2.png

* Ordenador 1I tiene la MAC ``6c3f``.
* Ordenador 2I tiene la MAC ``b141``.
* Ordenador 1D tiene la MAC ``55b0``.
* Ordenador 2D tiene la MAC ``c21f``.

.. table:: Tabla MAC de Switch 1

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  --      
                   2  --      
                   3  ``6c3f``
                   4  --      
                   5  ``55b0``
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

1. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
2. El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
3. El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
4. El Switch 1 envía el mensaje por el puerto 3.
5. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``c21f``.
6. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
7. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``c21f``.
8. El Switch 2 envía el mensaje por el puerto 1.


Ejercicio 18 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 7 que va al puerto 5 del switch 2. Se pretende enviar desde ``aeaf`` a ``8913`` sabiendo lo siguiente:


.. figure:: Switches3-2.png

* Ordenador 1I tiene la MAC ``ecd9``.
* Ordenador 2I tiene la MAC ``aeaf``.
* Ordenador 3I tiene la MAC ``460c``.
* Ordenador 1D tiene la MAC ``ab77``.
* Ordenador 2D tiene la MAC ``8913``.

.. table:: Tabla MAC de Switch 1

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  --      
                   2  --      
                   3  --      
                   4  --      
                   5  ``aeaf``
                   6  --      
                   7  ``ab77``
    ================  ========


.. table:: Tabla MAC de Switch 2

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  ``ab77``
                   2  --      
                   3  --      
                   4  --      
                   5  --      
                   6  --      
                   7  --      
    ================  ========


Indica si las siguientes afirmaciones son verdaderas o falsas:

1. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
2. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
3. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``aeaf``.
4. El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
5. El Switch 2 envía el mensaje por el puerto 0.
6. El Switch 1 envía el mensaje por el puerto 4.
7. El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
8. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``aeaf``.


Ejercicio 19 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 4 que va al puerto 0 del switch 2. Se pretende enviar desde ``523d`` a ``eea3`` sabiendo lo siguiente:


.. figure:: Switches2-3.png

* Ordenador 1I tiene la MAC ``523d``.
* Ordenador 2I tiene la MAC ``52cd``.
* Ordenador 1D tiene la MAC ``cb88``.
* Ordenador 2D tiene la MAC ``eea3``.
* Ordenador 3D tiene la MAC ``54cd``.

.. table:: Tabla MAC de Switch 1

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  --      
                   2  --      
                   3  ``52cd``
                   4  ``54cd``
                   5  --      
                   6  ``523d``
                   7  --      
    ================  ========


.. table:: Tabla MAC de Switch 2

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  --      
                   2  --      
                   3  ``cb88``
                   4  --      
                   5  --      
                   6  --      
                   7  --      
    ================  ========


Indica si las siguientes afirmaciones son verdaderas o falsas:

1. El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
2. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``523d``.
3. El Switch 1 envía el mensaje por el puerto 0.
4. El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
5. El Switch 2 envía el mensaje por el puerto 7.
6. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``523d``.
7. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
8. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.


Ejercicio 20 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 5 que va al puerto 1 del switch 2. Se pretende enviar desde ``f4c2`` a ``c600`` sabiendo lo siguiente:


.. figure:: Switches3-3.png

* Ordenador 1I tiene la MAC ``b41d``.
* Ordenador 2I tiene la MAC ``d212``.
* Ordenador 3I tiene la MAC ``f4c2``.
* Ordenador 1D tiene la MAC ``5e3e``.
* Ordenador 2D tiene la MAC ``40d7``.
* Ordenador 3D tiene la MAC ``c600``.

.. table:: Tabla MAC de Switch 1

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  --      
                   2  ``d212``
                   3  --      
                   4  ``b41d``
                   5  ``5e3e``
                   6  --      
                   7  --      
    ================  ========


.. table:: Tabla MAC de Switch 2

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  ``f4c2``
                   2  ``c600``
                   3  --      
                   4  --      
                   5  --      
                   6  --      
                   7  --      
    ================  ========


Indica si las siguientes afirmaciones son verdaderas o falsas:

1. El Switch 1 envía el mensaje por el puerto 6.
2. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``f4c2``.
3. El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
4. El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
5. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``f4c2``.
6. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
7. El Switch 2 envía el mensaje por el puerto 2.
8. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.


Ejercicio 21 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 5 que va al puerto 2 del switch 2. Se pretende enviar desde ``d008`` a ``da71`` sabiendo lo siguiente:


.. figure:: Switches4-3.png

* Ordenador 1I tiene la MAC ``da71``.
* Ordenador 2I tiene la MAC ``9bd6``.
* Ordenador 3I tiene la MAC ``5fe4``.
* Ordenador 4I tiene la MAC ``72c6``.
* Ordenador 1D tiene la MAC ``d008``.
* Ordenador 2D tiene la MAC ``80c4``.
* Ordenador 3D tiene la MAC ``ae72``.

.. table:: Tabla MAC de Switch 1

    ================  =============
    Numero de puerto       MAC     
    ================  =============
                   0  ``5fe4``     
                   1  ``9bd6``     
                   2  --           
                   3  --           
                   4  ``da71``     
                   5  ``80c4,ae72``
                   6  --           
                   7  --           
    ================  =============


.. table:: Tabla MAC de Switch 2

    ================  =============
    Numero de puerto       MAC     
    ================  =============
                   0  --           
                   1  --           
                   2  ``9bd6,72c6``
                   3  --           
                   4  --           
                   5  --           
                   6  --           
                   7  --           
    ================  =============


Indica si las siguientes afirmaciones son verdaderas o falsas:

1. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``d008``.
2. El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
3. El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
4. El Switch 2 envía el mensaje por el puerto 1.
5. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``d008``.
6. El Switch 1 envía el mensaje por el puerto 4.
7. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
8. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.


Ejercicio 22 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 5 que va al puerto 1 del switch 2. Se pretende enviar desde ``a4a0`` a ``bd89`` sabiendo lo siguiente:


.. figure:: Switches3-3.png

* Ordenador 1I tiene la MAC ``c38c``.
* Ordenador 2I tiene la MAC ``7249``.
* Ordenador 3I tiene la MAC ``bd89``.
* Ordenador 1D tiene la MAC ``a13d``.
* Ordenador 2D tiene la MAC ``a4a0``.
* Ordenador 3D tiene la MAC ``7fe2``.

.. table:: Tabla MAC de Switch 1

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  --      
                   2  ``7249``
                   3  --      
                   4  --      
                   5  ``a4a0``
                   6  --      
                   7  ``c38c``
    ================  ========


.. table:: Tabla MAC de Switch 2

    ================  =============
    Numero de puerto       MAC     
    ================  =============
                   0  --           
                   1  ``7249,bd89``
                   2  --           
                   3  --           
                   4  --           
                   5  --           
                   6  --           
                   7  --           
    ================  =============


Indica si las siguientes afirmaciones son verdaderas o falsas:

1. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``a4a0``.
2. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
3. El Switch 2 envía el mensaje por el puerto 1.
4. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``a4a0``.
5. El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
6. El Switch 1 envía el mensaje por el puerto 6.
7. El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
8. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.


Ejercicio 23 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 5 que va al puerto 6 del switch 2. Se pretende enviar desde ``cf1a`` a ``ff22`` sabiendo lo siguiente:


.. figure:: Switches2-4.png

* Ordenador 1I tiene la MAC ``cf1a``.
* Ordenador 2I tiene la MAC ``f8bf``.
* Ordenador 1D tiene la MAC ``7bbb``.
* Ordenador 2D tiene la MAC ``f16d``.
* Ordenador 3D tiene la MAC ``ff22``.
* Ordenador 4D tiene la MAC ``ca96``.

.. table:: Tabla MAC de Switch 1

    ================  =============
    Numero de puerto       MAC     
    ================  =============
                   0  ``f8bf``     
                   1  --           
                   2  --           
                   3  --           
                   4  --           
                   5  ``7bbb,ca96``
                   6  --           
                   7  --           
    ================  =============


.. table:: Tabla MAC de Switch 2

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  ``ff22``
                   2  --      
                   3  --      
                   4  --      
                   5  ``f16d``
                   6  ``f8bf``
                   7  --      
    ================  ========


Indica si las siguientes afirmaciones son verdaderas o falsas:

1. El Switch 1 envía el mensaje por el puerto 6.
2. El Switch 2 envía el mensaje por el puerto 1.
3. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
4. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``cf1a``.
5. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``cf1a``.
6. El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
7. El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
8. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.


Ejercicio 24 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 3 que va al puerto 6 del switch 2. Se pretende enviar desde ``aad0`` a ``f384`` sabiendo lo siguiente:


.. figure:: Switches4-4.png

* Ordenador 1I tiene la MAC ``fc79``.
* Ordenador 2I tiene la MAC ``8e17``.
* Ordenador 3I tiene la MAC ``f384``.
* Ordenador 4I tiene la MAC ``dd0e``.
* Ordenador 1D tiene la MAC ``6ebe``.
* Ordenador 2D tiene la MAC ``6b67``.
* Ordenador 3D tiene la MAC ``685e``.
* Ordenador 4D tiene la MAC ``aad0``.

.. table:: Tabla MAC de Switch 1

    ================  =============
    Numero de puerto       MAC     
    ================  =============
                   0  ``fc79``     
                   1  ``8e17``     
                   2  --           
                   3  ``6ebe,685e``
                   4  --           
                   5  ``f384``     
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
                   3  ``6b67``
                   4  --      
                   5  --      
                   6  ``f384``
                   7  ``6ebe``
    ================  ========


Indica si las siguientes afirmaciones son verdaderas o falsas:

1. El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
2. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``aad0``.
3. El Switch 1 envía el mensaje por el puerto 5.
4. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
5. El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
6. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``aad0``.
7. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
8. El Switch 2 envía el mensaje por el puerto 6.


Ejercicio 25 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 0 que va al puerto 3 del switch 2. Se pretende enviar desde ``e75d`` a ``abe5`` sabiendo lo siguiente:


.. figure:: Switches2-3.png

* Ordenador 1I tiene la MAC ``e75d``.
* Ordenador 2I tiene la MAC ``5e30``.
* Ordenador 1D tiene la MAC ``9a8e``.
* Ordenador 2D tiene la MAC ``8656``.
* Ordenador 3D tiene la MAC ``abe5``.

.. table:: Tabla MAC de Switch 1

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  ``9a8e``
                   1  --      
                   2  --      
                   3  --      
                   4  --      
                   5  --      
                   6  --      
                   7  ``e75d``
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

1. El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
2. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``e75d``.
3. El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
4. El Switch 1 envía el mensaje por el puerto 4.
5. El Switch 2 envía el mensaje por el puerto 3.
6. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
7. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
8. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``e75d``.


Ejercicio 26 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 4 que va al puerto 5 del switch 2. Se pretende enviar desde ``6dfe`` a ``b530`` sabiendo lo siguiente:


.. figure:: Switches2-2.png

* Ordenador 1I tiene la MAC ``c32e``.
* Ordenador 2I tiene la MAC ``6dfe``.
* Ordenador 1D tiene la MAC ``b530``.
* Ordenador 2D tiene la MAC ``9e8a``.

.. table:: Tabla MAC de Switch 1

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  --      
                   2  ``6dfe``
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

1. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
2. El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
3. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
4. El Switch 1 envía el mensaje por el puerto 4.
5. El Switch 2 envía el mensaje por el puerto 0.
6. El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
7. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``6dfe``.
8. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``6dfe``.


Ejercicio 27 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 7 que va al puerto 3 del switch 2. Se pretende enviar desde ``5fef`` a ``81b9`` sabiendo lo siguiente:


.. figure:: Switches3-4.png

* Ordenador 1I tiene la MAC ``abff``.
* Ordenador 2I tiene la MAC ``5fef``.
* Ordenador 3I tiene la MAC ``6026``.
* Ordenador 1D tiene la MAC ``892c``.
* Ordenador 2D tiene la MAC ``51f8``.
* Ordenador 3D tiene la MAC ``7d04``.
* Ordenador 4D tiene la MAC ``81b9``.

.. table:: Tabla MAC de Switch 1

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  --      
                   2  ``5fef``
                   3  ``abff``
                   4  --      
                   5  ``6026``
                   6  --      
                   7  ``892c``
    ================  ========


.. table:: Tabla MAC de Switch 2

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  ``81b9``
                   1  --      
                   2  --      
                   3  ``51f8``
                   4  --      
                   5  --      
                   6  --      
                   7  --      
    ================  ========


Indica si las siguientes afirmaciones son verdaderas o falsas:

1. El Switch 2 envía el mensaje por el puerto 0.
2. El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
3. El Switch 1 envía el mensaje por el puerto 1.
4. El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
5. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
6. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
7. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``5fef``.
8. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``5fef``.


Ejercicio 28 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 1 que va al puerto 1 del switch 2. Se pretende enviar desde ``6ac1`` a ``75c8`` sabiendo lo siguiente:


.. figure:: Switches3-3.png

* Ordenador 1I tiene la MAC ``6aec``.
* Ordenador 2I tiene la MAC ``6ac1``.
* Ordenador 3I tiene la MAC ``8a98``.
* Ordenador 1D tiene la MAC ``da28``.
* Ordenador 2D tiene la MAC ``75c8``.
* Ordenador 3D tiene la MAC ``c241``.

.. table:: Tabla MAC de Switch 1

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  ``da28``
                   2  ``6aec``
                   3  --      
                   4  ``8a98``
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

1. El Switch 2 envía el mensaje por el puerto 3.
2. El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
3. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
4. El Switch 1 envía el mensaje por el puerto 3.
5. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``6ac1``.
6. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``6ac1``.
7. El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
8. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.


Ejercicio 29 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 0 que va al puerto 3 del switch 2. Se pretende enviar desde ``fd2e`` a ``84f1`` sabiendo lo siguiente:


.. figure:: Switches2-4.png

* Ordenador 1I tiene la MAC ``fd2e``.
* Ordenador 2I tiene la MAC ``4ad9``.
* Ordenador 1D tiene la MAC ``8d5d``.
* Ordenador 2D tiene la MAC ``84f1``.
* Ordenador 3D tiene la MAC ``8d8b``.
* Ordenador 4D tiene la MAC ``b6eb``.

.. table:: Tabla MAC de Switch 1

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  ``84f1``
                   1  --      
                   2  --      
                   3  ``fd2e``
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
                   2  --      
                   3  ``fd2e``
                   4  --      
                   5  --      
                   6  ``84f1``
                   7  --      
    ================  ========


Indica si las siguientes afirmaciones son verdaderas o falsas:

1. El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
2. El Switch 1 envía el mensaje por el puerto 0.
3. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
4. El Switch 2 envía el mensaje por el puerto 6.
5. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
6. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``fd2e``.
7. El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
8. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``fd2e``.


Ejercicio 30 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 6 que va al puerto 7 del switch 2. Se pretende enviar desde ``9e19`` a ``bf0d`` sabiendo lo siguiente:


.. figure:: Switches3-4.png

* Ordenador 1I tiene la MAC ``bf0d``.
* Ordenador 2I tiene la MAC ``7c59``.
* Ordenador 3I tiene la MAC ``5588``.
* Ordenador 1D tiene la MAC ``bf94``.
* Ordenador 2D tiene la MAC ``b315``.
* Ordenador 3D tiene la MAC ``9e19``.
* Ordenador 4D tiene la MAC ``5b55``.

.. table:: Tabla MAC de Switch 1

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  ``7c59``
                   1  --      
                   2  --      
                   3  --      
                   4  ``5588``
                   5  --      
                   6  ``5b55``
                   7  --      
    ================  ========


.. table:: Tabla MAC de Switch 2

    ================  ========
    Numero de puerto    MAC   
    ================  ========
                   0  --      
                   1  --      
                   2  ``bf94``
                   3  --      
                   4  --      
                   5  --      
                   6  --      
                   7  ``bf0d``
    ================  ========


Indica si las siguientes afirmaciones son verdaderas o falsas:

1. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
2. El Switch 2 envía el mensaje por el puerto 7.
3. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``9e19``.
4. El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
5. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``9e19``.
6. El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
7. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
8. El Switch 1 envía el mensaje por el puerto 3.

Solucion al ejercicio 1 de switches
-----------------------------------------
Las respuestas son:

1. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen ``65fc``.
2. El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino ``a15e`` en su tabla
3. El Switch 2 envía el mensaje por el puerto 7. **Falsa**, no conoce a la MAC de destino ``a15e``, así que necesita difundir.
4. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``65fc``. **Falsa**, ya tenía esa MAC
5. El Switch 1 envía el mensaje por el puerto 6. **Falsa**, no conoce a la MAC de destino ``a15e``, así que necesita difundir.
6. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``65fc``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen ``65fc``.
7. El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino ``a15e`` en su tabla
8. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen ``65fc``, así que la anota.

Solucion al ejercicio 2 de switches
-----------------------------------------
Las respuestas son:

1. El Switch 2 envía el mensaje por el puerto 2. **Falsa**, no conoce a la MAC de destino ``c50e``, así que necesita difundir.
2. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``b039``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen ``b039``.
3. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen ``b039``, así que la anota.
4. El Switch 1 envía el mensaje por el puerto 0. **Falsa**, no conoce a la MAC de destino ``c50e``, así que necesita difundir.
5. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``b039``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen ``b039``.
6. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen ``b039``, así que la anota.
7. El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino ``c50e`` en su tabla
8. El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino ``c50e`` en su tabla

Solucion al ejercicio 3 de switches
-----------------------------------------
Las respuestas son:

1. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen ``a636``, así que la anota.
2. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``a636``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen ``a636``.
3. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``a636``. **Falsa**, ya tenía esa MAC
4. El Switch 2 envía el mensaje por el puerto 3. **Falsa**, no conoce a la MAC de destino ``8fc8``, así que necesita difundir.
5. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen ``a636``.
6. El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino ``8fc8`` en su tabla
7. El Switch 1 envía el mensaje por el puerto 3. **Falsa**, no conoce a la MAC de destino ``8fc8``, así que necesita difundir.
8. El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino ``8fc8`` en su tabla

Solucion al ejercicio 4 de switches
-----------------------------------------
Las respuestas son:

1. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``b4f3``. **Falsa**, ya tenía esa MAC
2. El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino ``7a3c`` en su tabla, en el puerto 6.
3. El Switch 1 envía el mensaje por el puerto 6. **Verdadera**, ``7a3c`` está en esa posición en la tabla de MACs
4. El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino ``7a3c`` en su tabla, en el puerto 1.
5. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen ``b4f3``.
6. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen ``b4f3``, así que la anota.
7. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``b4f3``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen ``b4f3``.
8. El Switch 2 envía el mensaje por el puerto 1. **Verdadera**, ``7a3c`` está en esa posición en la tabla de MACs

Solucion al ejercicio 5 de switches
-----------------------------------------
Las respuestas son:

1. El Switch 2 envía el mensaje por el puerto 4. **Falsa**, no conoce a la MAC de destino ``bf66``, así que necesita difundir.
2. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``bf67``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen ``bf67``.
3. El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino ``bf66`` en su tabla
4. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen ``bf67``, así que la anota.
5. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``bf67``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen ``bf67``.
6. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen ``bf67``, así que la anota.
7. El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino ``bf66`` en su tabla
8. El Switch 1 envía el mensaje por el puerto 3. **Falsa**, no conoce a la MAC de destino ``bf66``, así que necesita difundir.

Solucion al ejercicio 6 de switches
-----------------------------------------
Las respuestas son:

1. El Switch 1 envía el mensaje por el puerto 4. **Falsa**, no conoce a la MAC de destino ``b5f1``, así que necesita difundir.
2. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``61a4``. **Falsa**, ya tenía esa MAC
3. El Switch 2 envía el mensaje por el puerto 3. **Falsa**, no conoce a la MAC de destino ``b5f1``, así que necesita difundir.
4. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen ``61a4``.
5. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen ``61a4``.
6. El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino ``b5f1`` en su tabla
7. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``61a4``. **Falsa**, ya tenía esa MAC
8. El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino ``b5f1`` en su tabla

Solucion al ejercicio 7 de switches
-----------------------------------------
Las respuestas son:

1. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen ``6d8d``, así que la anota.
2. El Switch 2 envía el mensaje por el puerto 7. **Falsa**, no conoce a la MAC de destino ``5fa6``, así que necesita difundir.
3. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen ``6d8d``.
4. El Switch 1 envía el mensaje por el puerto 1. **Falsa**, no conoce a la MAC de destino ``5fa6``, así que necesita difundir.
5. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``6d8d``. **Falsa**, ya tenía esa MAC
6. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``6d8d``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen ``6d8d``.
7. El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino ``5fa6`` en su tabla
8. El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino ``5fa6`` en su tabla

Solucion al ejercicio 8 de switches
-----------------------------------------
Las respuestas son:

1. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen ``958c``, así que la anota.
2. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen ``958c``, así que la anota.
3. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``958c``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen ``958c``.
4. El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino ``bb84`` en su tabla
5. El Switch 2 envía el mensaje por el puerto 2. **Falsa**, no conoce a la MAC de destino ``bb84``, así que necesita difundir.
6. El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino ``bb84`` en su tabla
7. El Switch 1 envía el mensaje por el puerto 4. **Falsa**, no conoce a la MAC de destino ``bb84``, así que necesita difundir.
8. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``958c``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen ``958c``.

Solucion al ejercicio 9 de switches
-----------------------------------------
Las respuestas son:

1. El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino ``bee9`` en su tabla
2. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen ``cb76``.
3. El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino ``bee9`` en su tabla
4. El Switch 1 envía el mensaje por el puerto 6. **Falsa**, no conoce a la MAC de destino ``bee9``, así que necesita difundir.
5. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen ``cb76``.
6. El Switch 2 envía el mensaje por el puerto 0. **Falsa**, no conoce a la MAC de destino ``bee9``, así que necesita difundir.
7. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``cb76``. **Falsa**, ya tenía esa MAC
8. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``cb76``. **Falsa**, ya tenía esa MAC

Solucion al ejercicio 10 de switches
-----------------------------------------
Las respuestas son:

1. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``5a09``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen ``5a09``.
2. El Switch 1 envía el mensaje por el puerto 0. **Falsa**, no conoce a la MAC de destino ``c525``, así que necesita difundir.
3. El Switch 2 envía el mensaje por el puerto 5. **Verdadera**, ``c525`` está en esa posición en la tabla de MACs
4. El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino ``c525`` en su tabla, en el puerto 5.
5. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen ``5a09``.
6. El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino ``c525`` en su tabla
7. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen ``5a09``, así que la anota.
8. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``5a09``. **Falsa**, ya tenía esa MAC

Solucion al ejercicio 11 de switches
-----------------------------------------
Las respuestas son:

1. El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino ``7019`` en su tabla, en el puerto 2.
2. El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino ``7019`` en su tabla
3. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen ``cc6a``, así que la anota.
4. El Switch 1 envía el mensaje por el puerto 2. **Verdadera**, ``7019`` está en esa posición en la tabla de MACs
5. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``cc6a``. **Falsa**, ya tenía esa MAC
6. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``cc6a``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen ``cc6a``.
7. El Switch 2 envía el mensaje por el puerto 1. **Falsa**, no conoce a la MAC de destino ``7019``, así que necesita difundir.
8. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen ``cc6a``.

Solucion al ejercicio 12 de switches
-----------------------------------------
Las respuestas son:

1. El Switch 2 envía el mensaje por el puerto 1. **Verdadera**, ``500d`` está en esa posición en la tabla de MACs
2. El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino ``500d`` en su tabla, en el puerto 1.
3. El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino ``500d`` en su tabla, en el puerto 1.
4. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen ``a96c``, así que la anota.
5. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``a96c``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen ``a96c``.
6. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen ``a96c``, así que la anota.
7. El Switch 1 envía el mensaje por el puerto 1. **Verdadera**, ``500d`` está en esa posición en la tabla de MACs
8. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``a96c``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen ``a96c``.

Solucion al ejercicio 13 de switches
-----------------------------------------
Las respuestas son:

1. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``8ce0``. **Falsa**, ya tenía esa MAC
2. El Switch 2 envía el mensaje por el puerto 2. **Falsa**, no conoce a la MAC de destino ``9b8c``, así que necesita difundir.
3. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen ``8ce0``.
4. El Switch 1 envía el mensaje por el puerto 6. **Verdadera**, ``9b8c`` está en esa posición en la tabla de MACs
5. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``8ce0``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen ``8ce0``.
6. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen ``8ce0``, así que la anota.
7. El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino ``9b8c`` en su tabla, en el puerto 6.
8. El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino ``9b8c`` en su tabla

Solucion al ejercicio 14 de switches
-----------------------------------------
Las respuestas son:

1. El Switch 1 envía el mensaje por el puerto 7. **Verdadera**, ``bafc`` está en esa posición en la tabla de MACs
2. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``af07``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen ``af07``.
3. El Switch 2 envía el mensaje por el puerto 4. **Falsa**, no conoce a la MAC de destino ``bafc``, así que necesita difundir.
4. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen ``af07``, así que la anota.
5. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``af07``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen ``af07``.
6. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen ``af07``, así que la anota.
7. El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino ``bafc`` en su tabla, en el puerto 7.
8. El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino ``bafc`` en su tabla

Solucion al ejercicio 15 de switches
-----------------------------------------
Las respuestas son:

1. El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino ``ac7b`` en su tabla
2. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen ``c85b``.
3. El Switch 2 envía el mensaje por el puerto 1. **Falsa**, no conoce a la MAC de destino ``ac7b``, así que necesita difundir.
4. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``c85b``. **Falsa**, ya tenía esa MAC
5. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``c85b``. **Falsa**, ya tenía esa MAC
6. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen ``c85b``.
7. El Switch 1 envía el mensaje por el puerto 3. **Falsa**, no conoce a la MAC de destino ``ac7b``, así que necesita difundir.
8. El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino ``ac7b`` en su tabla

Solucion al ejercicio 16 de switches
-----------------------------------------
Las respuestas son:

1. El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino ``e281`` en su tabla, en el puerto 0.
2. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen ``6bdc``.
3. El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino ``e281`` en su tabla, en el puerto 6.
4. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``6bdc``. **Falsa**, ya tenía esa MAC
5. El Switch 1 envía el mensaje por el puerto 6. **Verdadera**, ``e281`` está en esa posición en la tabla de MACs
6. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``6bdc``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen ``6bdc``.
7. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen ``6bdc``, así que la anota.
8. El Switch 2 envía el mensaje por el puerto 0. **Verdadera**, ``e281`` está en esa posición en la tabla de MACs

Solucion al ejercicio 17 de switches
-----------------------------------------
Las respuestas son:

1. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen ``c21f``, así que la anota.
2. El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino ``6c3f`` en su tabla, en el puerto 3.
3. El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino ``6c3f`` en su tabla
4. El Switch 1 envía el mensaje por el puerto 3. **Verdadera**, ``6c3f`` está en esa posición en la tabla de MACs
5. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``c21f``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen ``c21f``.
6. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen ``c21f``, así que la anota.
7. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``c21f``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen ``c21f``.
8. El Switch 2 envía el mensaje por el puerto 1. **Falsa**, no conoce a la MAC de destino ``6c3f``, así que necesita difundir.

Solucion al ejercicio 18 de switches
-----------------------------------------
Las respuestas son:

1. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen ``aeaf``, así que la anota.
2. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen ``aeaf``.
3. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``aeaf``. **Falsa**, ya tenía esa MAC
4. El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino ``8913`` en su tabla
5. El Switch 2 envía el mensaje por el puerto 0. **Falsa**, no conoce a la MAC de destino ``8913``, así que necesita difundir.
6. El Switch 1 envía el mensaje por el puerto 4. **Falsa**, no conoce a la MAC de destino ``8913``, así que necesita difundir.
7. El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino ``8913`` en su tabla
8. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``aeaf``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen ``aeaf``.

Solucion al ejercicio 19 de switches
-----------------------------------------
Las respuestas son:

1. El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino ``eea3`` en su tabla
2. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``523d``. **Falsa**, ya tenía esa MAC
3. El Switch 1 envía el mensaje por el puerto 0. **Falsa**, no conoce a la MAC de destino ``eea3``, así que necesita difundir.
4. El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino ``eea3`` en su tabla
5. El Switch 2 envía el mensaje por el puerto 7. **Falsa**, no conoce a la MAC de destino ``eea3``, así que necesita difundir.
6. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``523d``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen ``523d``.
7. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen ``523d``, así que la anota.
8. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen ``523d``.

Solucion al ejercicio 20 de switches
-----------------------------------------
Las respuestas son:

1. El Switch 1 envía el mensaje por el puerto 6. **Falsa**, no conoce a la MAC de destino ``c600``, así que necesita difundir.
2. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``f4c2``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen ``f4c2``.
3. El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino ``c600`` en su tabla, en el puerto 2.
4. El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino ``c600`` en su tabla
5. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``f4c2``. **Falsa**, ya tenía esa MAC
6. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen ``f4c2``.
7. El Switch 2 envía el mensaje por el puerto 2. **Verdadera**, ``c600`` está en esa posición en la tabla de MACs
8. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen ``f4c2``, así que la anota.

Solucion al ejercicio 21 de switches
-----------------------------------------
Las respuestas son:

1. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``d008``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen ``d008``.
2. El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino ``da71`` en su tabla, en el puerto 4.
3. El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino ``da71`` en su tabla
4. El Switch 2 envía el mensaje por el puerto 1. **Falsa**, no conoce a la MAC de destino ``da71``, así que necesita difundir.
5. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``d008``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen ``d008``.
6. El Switch 1 envía el mensaje por el puerto 4. **Verdadera**, ``da71`` está en esa posición en la tabla de MACs
7. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen ``d008``, así que la anota.
8. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen ``d008``, así que la anota.

Solucion al ejercicio 22 de switches
-----------------------------------------
Las respuestas son:

1. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``a4a0``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen ``a4a0``.
2. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen ``a4a0``, así que la anota.
3. El Switch 2 envía el mensaje por el puerto 1. **Verdadera**, ``bd89`` está en esa posición en la tabla de MACs
4. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``a4a0``. **Falsa**, ya tenía esa MAC
5. El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino ``bd89`` en su tabla, en el puerto 1.
6. El Switch 1 envía el mensaje por el puerto 6. **Falsa**, no conoce a la MAC de destino ``bd89``, así que necesita difundir.
7. El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino ``bd89`` en su tabla
8. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen ``a4a0``.

Solucion al ejercicio 23 de switches
-----------------------------------------
Las respuestas son:

1. El Switch 1 envía el mensaje por el puerto 6. **Falsa**, no conoce a la MAC de destino ``ff22``, así que necesita difundir.
2. El Switch 2 envía el mensaje por el puerto 1. **Verdadera**, ``ff22`` está en esa posición en la tabla de MACs
3. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen ``cf1a``, así que la anota.
4. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``cf1a``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen ``cf1a``.
5. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``cf1a``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen ``cf1a``.
6. El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino ``ff22`` en su tabla, en el puerto 1.
7. El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino ``ff22`` en su tabla
8. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen ``cf1a``, así que la anota.

Solucion al ejercicio 24 de switches
-----------------------------------------
Las respuestas son:

1. El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino ``f384`` en su tabla, en el puerto 6.
2. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``aad0``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen ``aad0``.
3. El Switch 1 envía el mensaje por el puerto 5. **Verdadera**, ``f384`` está en esa posición en la tabla de MACs
4. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen ``aad0``, así que la anota.
5. El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino ``f384`` en su tabla, en el puerto 5.
6. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``aad0``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen ``aad0``.
7. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen ``aad0``, así que la anota.
8. El Switch 2 envía el mensaje por el puerto 6. **Verdadera**, ``f384`` está en esa posición en la tabla de MACs

Solucion al ejercicio 25 de switches
-----------------------------------------
Las respuestas son:

1. El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino ``abe5`` en su tabla
2. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``e75d``. **Falsa**, ya tenía esa MAC
3. El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino ``abe5`` en su tabla
4. El Switch 1 envía el mensaje por el puerto 4. **Falsa**, no conoce a la MAC de destino ``abe5``, así que necesita difundir.
5. El Switch 2 envía el mensaje por el puerto 3. **Falsa**, no conoce a la MAC de destino ``abe5``, así que necesita difundir.
6. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen ``e75d``.
7. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen ``e75d``, así que la anota.
8. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``e75d``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen ``e75d``.

Solucion al ejercicio 26 de switches
-----------------------------------------
Las respuestas son:

1. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen ``6dfe``, así que la anota.
2. El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino ``b530`` en su tabla
3. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen ``6dfe``.
4. El Switch 1 envía el mensaje por el puerto 4. **Falsa**, no conoce a la MAC de destino ``b530``, así que necesita difundir.
5. El Switch 2 envía el mensaje por el puerto 0. **Falsa**, no conoce a la MAC de destino ``b530``, así que necesita difundir.
6. El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino ``b530`` en su tabla
7. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``6dfe``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen ``6dfe``.
8. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``6dfe``. **Falsa**, ya tenía esa MAC

Solucion al ejercicio 27 de switches
-----------------------------------------
Las respuestas son:

1. El Switch 2 envía el mensaje por el puerto 0. **Verdadera**, ``81b9`` está en esa posición en la tabla de MACs
2. El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino ``81b9`` en su tabla
3. El Switch 1 envía el mensaje por el puerto 1. **Falsa**, no conoce a la MAC de destino ``81b9``, así que necesita difundir.
4. El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino ``81b9`` en su tabla, en el puerto 0.
5. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen ``5fef``, así que la anota.
6. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen ``5fef``.
7. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``5fef``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen ``5fef``.
8. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``5fef``. **Falsa**, ya tenía esa MAC

Solucion al ejercicio 28 de switches
-----------------------------------------
Las respuestas son:

1. El Switch 2 envía el mensaje por el puerto 3. **Falsa**, no conoce a la MAC de destino ``75c8``, así que necesita difundir.
2. El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino ``75c8`` en su tabla
3. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen ``6ac1``, así que la anota.
4. El Switch 1 envía el mensaje por el puerto 3. **Falsa**, no conoce a la MAC de destino ``75c8``, así que necesita difundir.
5. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``6ac1``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen ``6ac1``.
6. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``6ac1``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen ``6ac1``.
7. El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino ``75c8`` en su tabla
8. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen ``6ac1``, así que la anota.

Solucion al ejercicio 29 de switches
-----------------------------------------
Las respuestas son:

1. El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino ``84f1`` en su tabla, en el puerto 6.
2. El Switch 1 envía el mensaje por el puerto 0. **Verdadera**, ``84f1`` está en esa posición en la tabla de MACs
3. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen ``fd2e``.
4. El Switch 2 envía el mensaje por el puerto 6. **Verdadera**, ``84f1`` está en esa posición en la tabla de MACs
5. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen ``fd2e``.
6. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``fd2e``. **Falsa**, ya tenía esa MAC
7. El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino ``84f1`` en su tabla, en el puerto 0.
8. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``fd2e``. **Falsa**, ya tenía esa MAC

Solucion al ejercicio 30 de switches
-----------------------------------------
Las respuestas son:

1. El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen ``9e19``, así que la anota.
2. El Switch 2 envía el mensaje por el puerto 7. **Verdadera**, ``bf0d`` está en esa posición en la tabla de MACs
3. El Switch 1 apunta en su tabla de MACS  la MAC de origen ``9e19``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen ``9e19``.
4. El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino ``bf0d`` en su tabla, en el puerto 7.
5. El Switch 2 apunta en su tabla de MACS  la MAC de origen ``9e19``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen ``9e19``.
6. El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino ``bf0d`` en su tabla
7. El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen ``9e19``, así que la anota.
8. El Switch 1 envía el mensaje por el puerto 3. **Falsa**, no conoce a la MAC de destino ``bf0d``, así que necesita difundir.
