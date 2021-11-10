Anexo: ejercicios con tablas MAC de switches
================================================


Ejercicio 1 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 1 que va al puerto 0 del switch 2. Se pretende enviar desde ``8d0e`` a ``ac67`` sabiendo lo siguiente:


.. figure:: Switches2-2.png

* Ordenador 1I tiene la MAC ``445e``.
* Ordenador 2I tiene la MAC ``ac67``.
* Ordenador 1D tiene la MAC ``8ffb``.
* Ordenador 2D tiene la MAC ``8d0e``.

.. table:: Tabla MAC de Switch 1

    ================  ====
    Numero de puerto  MAC 
    ================  ====
                   0      
                   1      
                   2      
                   3      
                   4  445e
                   5      
                   6      
                   7  ac67
    ================  ====


.. table:: Tabla MAC de Switch 2

    ================  ====
    Numero de puerto  MAC 
    ================  ====
                   0  ac67
                   1  8ffb
                   2      
                   3      
                   4      
                   5      
                   6      
                   7      
    ================  ====


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``8d0e``.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 2 envía el mensaje por el puerto 0.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``8d0e``.
* El Switch 1 envía el mensaje por el puerto 7.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.


Ejercicio 2 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 6 que va al puerto 1 del switch 2. Se pretende enviar desde ``ecee`` a ``fdfd`` sabiendo lo siguiente:


.. figure:: Switches3-3.png

* Ordenador 1I tiene la MAC ``bb48``.
* Ordenador 2I tiene la MAC ``9e04``.
* Ordenador 3I tiene la MAC ``fdfd``.
* Ordenador 1D tiene la MAC ``ecee``.
* Ordenador 2D tiene la MAC ``633d``.
* Ordenador 3D tiene la MAC ``9eda``.

.. table:: Tabla MAC de Switch 1

    ================  =====
    Numero de puerto   MAC 
    ================  =====
                   0       
                   1       
                   2  90000
                   3       
                   4       
                   5       
                   6  ecee 
                   7       
    ================  =====


.. table:: Tabla MAC de Switch 2

    ================  ==============
    Numero de puerto       MAC      
    ================  ==============
                   0                
                   1  bb48,9e04,fdfd
                   2  633d          
                   3                
                   4                
                   5                
                   6  ecee          
                   7                
    ================  ==============


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``ecee``.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 envía el mensaje por el puerto 1.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``ecee``.
* El Switch 2 envía el mensaje por el puerto 1.


Ejercicio 3 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 1 que va al puerto 4 del switch 2. Se pretende enviar desde ``8edc`` a ``5951`` sabiendo lo siguiente:


.. figure:: Switches2-4.png

* Ordenador 1I tiene la MAC ``5951``.
* Ordenador 2I tiene la MAC ``816d``.
* Ordenador 1D tiene la MAC ``70f8``.
* Ordenador 2D tiene la MAC ``8edc``.
* Ordenador 3D tiene la MAC ``6639``.
* Ordenador 4D tiene la MAC ``ae09``.

.. table:: Tabla MAC de Switch 1

    ================  ====
    Numero de puerto  MAC 
    ================  ====
                   0  5951
                   1  ae09
                   2      
                   3      
                   4      
                   5  816d
                   6      
                   7      
    ================  ====


.. table:: Tabla MAC de Switch 2

    ================  =========
    Numero de puerto     MAC   
    ================  =========
                   0       6639
                   1  8edc     
                   2           
                   3           
                   4       5951
                   5           
                   6  70f8,ae09
                   7           
    ================  =========


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 envía el mensaje por el puerto 0.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``8edc``.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 2 envía el mensaje por el puerto 4.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``8edc``.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.


Ejercicio 4 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 1 que va al puerto 3 del switch 2. Se pretende enviar desde ``607c`` a ``c50b`` sabiendo lo siguiente:


.. figure:: Switches3-4.png

* Ordenador 1I tiene la MAC ``c50b``.
* Ordenador 2I tiene la MAC ``41d2``.
* Ordenador 3I tiene la MAC ``be38``.
* Ordenador 1D tiene la MAC ``607c``.
* Ordenador 2D tiene la MAC ``cd41``.
* Ordenador 3D tiene la MAC ``99ea``.
* Ordenador 4D tiene la MAC ``ae65``.

.. table:: Tabla MAC de Switch 1

    ================  ====
    Numero de puerto  MAC 
    ================  ====
                   0      
                   1  99ea
                   2      
                   3  c50b
                   4  41d2
                   5      
                   6      
                   7  be38
    ================  ====


.. table:: Tabla MAC de Switch 2

    ================  ====
    Numero de puerto  MAC 
    ================  ====
                   0      
                   1  99ea
                   2  cd41
                   3  41d2
                   4      
                   5      
                   6  607c
                   7  ae65
    ================  ====


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 1 envía el mensaje por el puerto 3.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``607c``.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``607c``.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 2 envía el mensaje por el puerto 4.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.


Ejercicio 5 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 3 que va al puerto 3 del switch 2. Se pretende enviar desde ``7175`` a ``de3e`` sabiendo lo siguiente:


.. figure:: Switches2-3.png

* Ordenador 1I tiene la MAC ``99f7``.
* Ordenador 2I tiene la MAC ``de3e``.
* Ordenador 1D tiene la MAC ``7175``.
* Ordenador 2D tiene la MAC ``e0ec``.
* Ordenador 3D tiene la MAC ``75c1``.

.. table:: Tabla MAC de Switch 1

    ================  ====
    Numero de puerto  MAC 
    ================  ====
                   0      
                   1      
                   2      
                   3      
                   4      
                   5  99f7
                   6      
                   7      
    ================  ====


.. table:: Tabla MAC de Switch 2

    ================  =========
    Numero de puerto     MAC   
    ================  =========
                   0           
                   1  e0ec,75c1
                   2           
                   3           
                   4           
                   5           
                   6       7175
                   7           
    ================  =========


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 2 envía el mensaje por el puerto 0.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``7175``.
* El Switch 1 envía el mensaje por el puerto 7.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``7175``.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.


Ejercicio 6 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 4 que va al puerto 3 del switch 2. Se pretende enviar desde ``aa2f`` a ``fed9`` sabiendo lo siguiente:


.. figure:: Switches2-2.png

* Ordenador 1I tiene la MAC ``fed9``.
* Ordenador 2I tiene la MAC ``4c03``.
* Ordenador 1D tiene la MAC ``aa2f``.
* Ordenador 2D tiene la MAC ``814f``.

.. table:: Tabla MAC de Switch 1

    ================  ====
    Numero de puerto  MAC 
    ================  ====
                   0      
                   1      
                   2      
                   3  fed9
                   4  814f
                   5      
                   6      
                   7  4c03
    ================  ====


.. table:: Tabla MAC de Switch 2

    ================  =========
    Numero de puerto     MAC   
    ================  =========
                   0  814f     
                   1  aa2f     
                   2           
                   3  fed9,4c03
                   4           
                   5           
                   6           
                   7           
    ================  =========


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``aa2f``.
* El Switch 1 envía el mensaje por el puerto 3.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 2 envía el mensaje por el puerto 3.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``aa2f``.


Ejercicio 7 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 6 que va al puerto 1 del switch 2. Se pretende enviar desde ``b07c`` a ``cd94`` sabiendo lo siguiente:


.. figure:: Switches3-2.png

* Ordenador 1I tiene la MAC ``8067``.
* Ordenador 2I tiene la MAC ``cd94``.
* Ordenador 3I tiene la MAC ``b11c``.
* Ordenador 1D tiene la MAC ``b07c``.
* Ordenador 2D tiene la MAC ``cae9``.

.. table:: Tabla MAC de Switch 1

    ================  ====
    Numero de puerto  MAC 
    ================  ====
                   0      
                   1  b11c
                   2  8067
                   3      
                   4      
                   5      
                   6      
                   7      
    ================  ====


.. table:: Tabla MAC de Switch 2

    ================  ====
    Numero de puerto  MAC 
    ================  ====
                   0      
                   1  8067
                   2      
                   3      
                   4      
                   5      
                   6  b07c
                   7      
    ================  ====


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 2 envía el mensaje por el puerto 7.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``b07c``.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``b07c``.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 envía el mensaje por el puerto 3.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.


Ejercicio 8 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 0 que va al puerto 1 del switch 2. Se pretende enviar desde ``e818`` a ``89d5`` sabiendo lo siguiente:


.. figure:: Switches3-2.png

* Ordenador 1I tiene la MAC ``ff42``.
* Ordenador 2I tiene la MAC ``89d5``.
* Ordenador 3I tiene la MAC ``798a``.
* Ordenador 1D tiene la MAC ``89b9``.
* Ordenador 2D tiene la MAC ``e818``.

.. table:: Tabla MAC de Switch 1

    ================  =========
    Numero de puerto     MAC   
    ================  =========
                   0           
                   1           
                   2  89d5     
                   3           
                   4           
                   5           
                   6  ff42,798a
                   7           
    ================  =========


.. table:: Tabla MAC de Switch 2

    ================  ====
    Numero de puerto  MAC 
    ================  ====
                   0      
                   1  ff42
                   2  e818
                   3      
                   4      
                   5      
                   6      
                   7  89b9
    ================  ====


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``e818``.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 2 envía el mensaje por el puerto 5.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``e818``.
* El Switch 1 envía el mensaje por el puerto 2.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.


Ejercicio 9 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 2 que va al puerto 2 del switch 2. Se pretende enviar desde ``7961`` a ``e06f`` sabiendo lo siguiente:


.. figure:: Switches3-3.png

* Ordenador 1I tiene la MAC ``7961``.
* Ordenador 2I tiene la MAC ``ad42``.
* Ordenador 3I tiene la MAC ``8c70``.
* Ordenador 1D tiene la MAC ``65a8``.
* Ordenador 2D tiene la MAC ``e06f``.
* Ordenador 3D tiene la MAC ``6cdf``.

.. table:: Tabla MAC de Switch 1

    ================  ====
    Numero de puerto  MAC 
    ================  ====
                   0      
                   1      
                   2      
                   3  8c70
                   4      
                   5      
                   6      
                   7      
    ================  ====


.. table:: Tabla MAC de Switch 2

    ================  ====
    Numero de puerto  MAC 
    ================  ====
                   0  65a8
                   1      
                   2  7961
                   3      
                   4  e06f
                   5      
                   6      
                   7      
    ================  ====


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 2 envía el mensaje por el puerto 4.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``7961``.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``7961``.
* El Switch 1 envía el mensaje por el puerto 5.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.


Ejercicio 10 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 5 que va al puerto 5 del switch 2. Se pretende enviar desde ``a0cd`` a ``d588`` sabiendo lo siguiente:


.. figure:: Switches2-3.png

* Ordenador 1I tiene la MAC ``d588``.
* Ordenador 2I tiene la MAC ``6dd7``.
* Ordenador 1D tiene la MAC ``62a8``.
* Ordenador 2D tiene la MAC ``a0cd``.
* Ordenador 3D tiene la MAC ``cb25``.

.. table:: Tabla MAC de Switch 1

    ================  =========
    Numero de puerto     MAC   
    ================  =========
                   0           
                   1  6dd7     
                   2           
                   3           
                   4  d588     
                   5  a0cd,cb25
                   6           
                   7           
    ================  =========


.. table:: Tabla MAC de Switch 2

    ================  =========
    Numero de puerto     MAC   
    ================  =========
                   0           
                   1           
                   2           
                   3           
                   4           
                   5  d588,6dd7
                   6           
                   7  cb25     
    ================  =========


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 2 envía el mensaje por el puerto 5.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``a0cd``.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``a0cd``.
* El Switch 1 envía el mensaje por el puerto 4.


Ejercicio 11 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 5 que va al puerto 6 del switch 2. Se pretende enviar desde ``b4f8`` a ``6dc8`` sabiendo lo siguiente:


.. figure:: Switches3-4.png

* Ordenador 1I tiene la MAC ``fdad``.
* Ordenador 2I tiene la MAC ``53a4``.
* Ordenador 3I tiene la MAC ``6dc8``.
* Ordenador 1D tiene la MAC ``61bf``.
* Ordenador 2D tiene la MAC ``ecbf``.
* Ordenador 3D tiene la MAC ``46fa``.
* Ordenador 4D tiene la MAC ``b4f8``.

.. table:: Tabla MAC de Switch 1

    ================  =========
    Numero de puerto     MAC   
    ================  =========
                   0           
                   1  fdad,6dc8
                   2           
                   3           
                   4           
                   5  61bf,ecbf
                   6           
                   7           
    ================  =========


.. table:: Tabla MAC de Switch 2

    ================  ====
    Numero de puerto  MAC 
    ================  ====
                   0      
                   1  ecbf
                   2      
                   3  46fa
                   4      
                   5  61bf
                   6  53a4
                   7      
    ================  ====


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``b4f8``.
* El Switch 1 envía el mensaje por el puerto 1.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 2 envía el mensaje por el puerto 4.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``b4f8``.


Ejercicio 12 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 5 que va al puerto 2 del switch 2. Se pretende enviar desde ``6133`` a ``6978`` sabiendo lo siguiente:


.. figure:: Switches3-2.png

* Ordenador 1I tiene la MAC ``5a3b``.
* Ordenador 2I tiene la MAC ``7692``.
* Ordenador 3I tiene la MAC ``6978``.
* Ordenador 1D tiene la MAC ``6133``.
* Ordenador 2D tiene la MAC ``cb3d``.

.. table:: Tabla MAC de Switch 1

    ================  =========
    Numero de puerto     MAC   
    ================  =========
                   0  5a3b,7692
                   1           
                   2           
                   3           
                   4           
                   5  6133,cb3d
                   6           
                   7           
    ================  =========


.. table:: Tabla MAC de Switch 2

    ================  =========
    Numero de puerto     MAC   
    ================  =========
                   0           
                   1           
                   2  5a3b,7692
                   3           
                   4           
                   5       6133
                   6  cb3d     
                   7           
    ================  =========


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``6133``.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``6133``.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 2 envía el mensaje por el puerto 4.
* El Switch 1 envía el mensaje por el puerto 6.


Ejercicio 13 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 2 que va al puerto 3 del switch 2. Se pretende enviar desde ``fcdd`` a ``ab43`` sabiendo lo siguiente:


.. figure:: Switches3-2.png

* Ordenador 1I tiene la MAC ``fcdd``.
* Ordenador 2I tiene la MAC ``48f4``.
* Ordenador 3I tiene la MAC ``e34a``.
* Ordenador 1D tiene la MAC ``ae57``.
* Ordenador 2D tiene la MAC ``ab43``.

.. table:: Tabla MAC de Switch 1

    ================  ====
    Numero de puerto  MAC 
    ================  ====
                   0      
                   1      
                   2  ae57
                   3      
                   4      
                   5      
                   6  48f4
                   7      
    ================  ====


.. table:: Tabla MAC de Switch 2

    ================  ==============
    Numero de puerto       MAC      
    ================  ==============
                   0                
                   1                
                   2                
                   3  fcdd,48f4,e34a
                   4  ab43          
                   5                
                   6                
                   7  ae57          
    ================  ==============


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 1 envía el mensaje por el puerto 3.
* El Switch 2 envía el mensaje por el puerto 4.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``fcdd``.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``fcdd``.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.


Ejercicio 14 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 7 que va al puerto 3 del switch 2. Se pretende enviar desde ``4636`` a ``f23f`` sabiendo lo siguiente:


.. figure:: Switches2-3.png

* Ordenador 1I tiene la MAC ``4636``.
* Ordenador 2I tiene la MAC ``68f0``.
* Ordenador 1D tiene la MAC ``4f6e``.
* Ordenador 2D tiene la MAC ``f23f``.
* Ordenador 3D tiene la MAC ``a52a``.

.. table:: Tabla MAC de Switch 1

    ================  =========
    Numero de puerto     MAC   
    ================  =========
                   0       4636
                   1           
                   2           
                   3           
                   4           
                   5  68f0     
                   6           
                   7  4f6e,a52a
    ================  =========


.. table:: Tabla MAC de Switch 2

    ================  ====
    Numero de puerto  MAC 
    ================  ====
                   0      
                   1      
                   2      
                   3      
                   4      
                   5      
                   6      
                   7  f23f
    ================  ====


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``4636``.
* El Switch 2 envía el mensaje por el puerto 7.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 1 envía el mensaje por el puerto 2.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``4636``.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.


Ejercicio 15 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 5 que va al puerto 0 del switch 2. Se pretende enviar desde ``948c`` a ``ab97`` sabiendo lo siguiente:


.. figure:: Switches2-2.png

* Ordenador 1I tiene la MAC ``9a75``.
* Ordenador 2I tiene la MAC ``ab97``.
* Ordenador 1D tiene la MAC ``b92c``.
* Ordenador 2D tiene la MAC ``948c``.

.. table:: Tabla MAC de Switch 1

    ================  =========
    Numero de puerto     MAC   
    ================  =========
                   0  9a75,ab97
                   1           
                   2           
                   3           
                   4           
                   5  b92c     
                   6           
                   7           
    ================  =========


.. table:: Tabla MAC de Switch 2

    ================  ====
    Numero de puerto  MAC 
    ================  ====
                   0      
                   1      
                   2  948c
                   3      
                   4      
                   5      
                   6      
                   7      
    ================  ====


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``948c``.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``948c``.
* El Switch 2 envía el mensaje por el puerto 4.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 1 envía el mensaje por el puerto 0.


Ejercicio 16 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 2 que va al puerto 1 del switch 2. Se pretende enviar desde ``d82a`` a ``5ad5`` sabiendo lo siguiente:


.. figure:: Switches2-3.png

* Ordenador 1I tiene la MAC ``d82a``.
* Ordenador 2I tiene la MAC ``5202``.
* Ordenador 1D tiene la MAC ``5ad5``.
* Ordenador 2D tiene la MAC ``c3be``.
* Ordenador 3D tiene la MAC ``e9a0``.

.. table:: Tabla MAC de Switch 1

    ================  ====
    Numero de puerto  MAC 
    ================  ====
                   0      
                   1      
                   2  e9a0
                   3      
                   4  5202
                   5      
                   6  d82a
                   7      
    ================  ====


.. table:: Tabla MAC de Switch 2

    ================  =========
    Numero de puerto     MAC   
    ================  =========
                   0  5ad5     
                   1  d82a,5202
                   2           
                   3           
                   4           
                   5           
                   6  e9a0     
                   7           
    ================  =========


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 1 envía el mensaje por el puerto 1.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``d82a``.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 2 envía el mensaje por el puerto 0.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``d82a``.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.


Ejercicio 17 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 2 que va al puerto 5 del switch 2. Se pretende enviar desde ``9d7e`` a ``4fa6`` sabiendo lo siguiente:


.. figure:: Switches3-3.png

* Ordenador 1I tiene la MAC ``8a76``.
* Ordenador 2I tiene la MAC ``f628``.
* Ordenador 3I tiene la MAC ``9d7e``.
* Ordenador 1D tiene la MAC ``b45d``.
* Ordenador 2D tiene la MAC ``6091``.
* Ordenador 3D tiene la MAC ``4fa6``.

.. table:: Tabla MAC de Switch 1

    ================  ====
    Numero de puerto  MAC 
    ================  ====
                   0      
                   1      
                   2  b45d
                   3      
                   4  9d7e
                   5      
                   6      
                   7      
    ================  ====


.. table:: Tabla MAC de Switch 2

    ================  ==============
    Numero de puerto       MAC      
    ================  ==============
                   0                
                   1                
                   2                
                   3                
                   4                
                   5  8a76,f628,9d7e
                   6                
                   7  4fa6          
    ================  ==============


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 1 envía el mensaje por el puerto 7.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``9d7e``.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 2 envía el mensaje por el puerto 7.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``9d7e``.


Ejercicio 18 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 3 que va al puerto 7 del switch 2. Se pretende enviar desde ``c862`` a ``b434`` sabiendo lo siguiente:


.. figure:: Switches3-3.png

* Ordenador 1I tiene la MAC ``981e``.
* Ordenador 2I tiene la MAC ``7d35``.
* Ordenador 3I tiene la MAC ``b434``.
* Ordenador 1D tiene la MAC ``d620``.
* Ordenador 2D tiene la MAC ``bebc``.
* Ordenador 3D tiene la MAC ``c862``.

.. table:: Tabla MAC de Switch 1

    ================  ====
    Numero de puerto  MAC 
    ================  ====
                   0      
                   1      
                   2      
                   3      
                   4  981e
                   5      
                   6  b434
                   7      
    ================  ====


.. table:: Tabla MAC de Switch 2

    ================  ====
    Numero de puerto  MAC 
    ================  ====
                   0      
                   1      
                   2      
                   3  c862
                   4      
                   5      
                   6      
                   7  7d35
    ================  ====


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``c862``.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 2 envía el mensaje por el puerto 4.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``c862``.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 envía el mensaje por el puerto 6.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.


Ejercicio 19 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 2 que va al puerto 4 del switch 2. Se pretende enviar desde ``75f7`` a ``e18e`` sabiendo lo siguiente:


.. figure:: Switches2-2.png

* Ordenador 1I tiene la MAC ``e18e``.
* Ordenador 2I tiene la MAC ``ca24``.
* Ordenador 1D tiene la MAC ``75f7``.
* Ordenador 2D tiene la MAC ``bfc8``.

.. table:: Tabla MAC de Switch 1

    ================  =========
    Numero de puerto     MAC   
    ================  =========
                   0           
                   1           
                   2  75f7,bfc8
                   3           
                   4  ca24     
                   5           
                   6  e18e     
                   7           
    ================  =========


.. table:: Tabla MAC de Switch 2

    ================  ====
    Numero de puerto  MAC 
    ================  ====
                   0  bfc8
                   1      
                   2      
                   3      
                   4      
                   5      
                   6      
                   7      
    ================  ====


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``75f7``.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``75f7``.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 2 envía el mensaje por el puerto 5.
* El Switch 1 envía el mensaje por el puerto 6.


Ejercicio 20 de switches
----------------------------------

Dada la red de la figura, en la que el switch 1 tiene un cable en el puerto 5 que va al puerto 4 del switch 2. Se pretende enviar desde ``e5bd`` a ``56db`` sabiendo lo siguiente:


.. figure:: Switches2-2.png

* Ordenador 1I tiene la MAC ``edb2``.
* Ordenador 2I tiene la MAC ``56db``.
* Ordenador 1D tiene la MAC ``4260``.
* Ordenador 2D tiene la MAC ``e5bd``.

.. table:: Tabla MAC de Switch 1

    ================  =========
    Numero de puerto     MAC   
    ================  =========
                   0           
                   1           
                   2  edb2,56db
                   3           
                   4           
                   5  4260,e5bd
                   6           
                   7           
    ================  =========


.. table:: Tabla MAC de Switch 2

    ================  ====
    Numero de puerto  MAC 
    ================  ====
                   0      
                   1      
                   2      
                   3      
                   4  56db
                   5      
                   6      
                   7      
    ================  ====


Indica si las siguientes afirmaciones son verdaderas o falsas:

* El Switch 1 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 1 envía el mensaje por el puerto 2.
* El Switch 2 envía el mensaje por el puerto 4.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``e5bd``.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``e5bd``.

Solucion al ejercicio 1 de switches
-----------------------------------------
Las respuestas son:

* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino ac67 en su tabla, en el puerto 7.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``8d0e``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen 8d0e.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino ac67 en su tabla, en el puerto 0.
* El Switch 2 envía el mensaje por el puerto 0. **Verdadera**, ac67 está en esa posición en la tabla de MACs
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen 8d0e, así que la anota.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``8d0e``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen 8d0e.
* El Switch 1 envía el mensaje por el puerto 7. **Verdadera**, ac67 está en esa posición en la tabla de MACs
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen 8d0e, así que la anota.

Solucion al ejercicio 2 de switches
-----------------------------------------
Las respuestas son:

* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``ecee``. **Falsa**, ya tenía esa MAC
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino fdfd en su tabla, en el puerto 1.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino fdfd en su tabla
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen ecee.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen ecee.
* El Switch 1 envía el mensaje por el puerto 1. **Falsa**, no conoce a la MAC de destino fdfd, así que necesita difundir.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``ecee``. **Falsa**, ya tenía esa MAC
* El Switch 2 envía el mensaje por el puerto 1. **Verdadera**, fdfd está en esa posición en la tabla de MACs

Solucion al ejercicio 3 de switches
-----------------------------------------
Las respuestas son:

* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen 8edc.
* El Switch 1 envía el mensaje por el puerto 0. **Verdadera**, 5951 está en esa posición en la tabla de MACs
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``8edc``. **Falsa**, ya tenía esa MAC
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino 5951 en su tabla, en el puerto 4.
* El Switch 2 envía el mensaje por el puerto 4. **Verdadera**, 5951 está en esa posición en la tabla de MACs
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``8edc``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen 8edc.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino 5951 en su tabla, en el puerto 0.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen 8edc, así que la anota.

Solucion al ejercicio 4 de switches
-----------------------------------------
Las respuestas son:

* El Switch 1 envía el mensaje por el puerto 3. **Verdadera**, c50b está en esa posición en la tabla de MACs
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``607c``. **Falsa**, ya tenía esa MAC
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino c50b en su tabla
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``607c``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen 607c.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen 607c, así que la anota.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino c50b en su tabla, en el puerto 3.
* El Switch 2 envía el mensaje por el puerto 4. **Falsa**, no conoce a la MAC de destino c50b, así que necesita difundir.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen 607c.

Solucion al ejercicio 5 de switches
-----------------------------------------
Las respuestas son:

* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen 7175.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino de3e en su tabla
* El Switch 2 envía el mensaje por el puerto 0. **Falsa**, no conoce a la MAC de destino de3e, así que necesita difundir.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``7175``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen 7175.
* El Switch 1 envía el mensaje por el puerto 7. **Falsa**, no conoce a la MAC de destino de3e, así que necesita difundir.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``7175``. **Falsa**, ya tenía esa MAC
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen 7175, así que la anota.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino de3e en su tabla

Solucion al ejercicio 6 de switches
-----------------------------------------
Las respuestas son:

* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``aa2f``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen aa2f.
* El Switch 1 envía el mensaje por el puerto 3. **Verdadera**, fed9 está en esa posición en la tabla de MACs
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino fed9 en su tabla, en el puerto 3.
* El Switch 2 envía el mensaje por el puerto 3. **Verdadera**, fed9 está en esa posición en la tabla de MACs
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino fed9 en su tabla, en el puerto 3.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen aa2f.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen aa2f, así que la anota.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``aa2f``. **Falsa**, ya tenía esa MAC

Solucion al ejercicio 7 de switches
-----------------------------------------
Las respuestas son:

* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen b07c.
* El Switch 2 envía el mensaje por el puerto 7. **Falsa**, no conoce a la MAC de destino cd94, así que necesita difundir.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``b07c``. **Falsa**, ya tenía esa MAC
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino cd94 en su tabla
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``b07c``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen b07c.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen b07c, así que la anota.
* El Switch 1 envía el mensaje por el puerto 3. **Falsa**, no conoce a la MAC de destino cd94, así que necesita difundir.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino cd94 en su tabla

Solucion al ejercicio 8 de switches
-----------------------------------------
Las respuestas son:

* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen e818, así que la anota.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino 89d5 en su tabla, en el puerto 2.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``e818``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen e818.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen e818.
* El Switch 2 envía el mensaje por el puerto 5. **Falsa**, no conoce a la MAC de destino 89d5, así que necesita difundir.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``e818``. **Falsa**, ya tenía esa MAC
* El Switch 1 envía el mensaje por el puerto 2. **Verdadera**, 89d5 está en esa posición en la tabla de MACs
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino 89d5 en su tabla

Solucion al ejercicio 9 de switches
-----------------------------------------
Las respuestas son:

* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino e06f en su tabla, en el puerto 4.
* El Switch 2 envía el mensaje por el puerto 4. **Verdadera**, e06f está en esa posición en la tabla de MACs
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen 7961.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``7961``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen 7961.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``7961``. **Falsa**, ya tenía esa MAC
* El Switch 1 envía el mensaje por el puerto 5. **Falsa**, no conoce a la MAC de destino e06f, así que necesita difundir.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino e06f en su tabla
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen 7961, así que la anota.

Solucion al ejercicio 10 de switches
-----------------------------------------
Las respuestas son:

* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino d588 en su tabla, en el puerto 5.
* El Switch 2 envía el mensaje por el puerto 5. **Verdadera**, d588 está en esa posición en la tabla de MACs
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino d588 en su tabla, en el puerto 4.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``a0cd``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen a0cd.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen a0cd, así que la anota.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen a0cd.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``a0cd``. **Falsa**, ya tenía esa MAC
* El Switch 1 envía el mensaje por el puerto 4. **Verdadera**, d588 está en esa posición en la tabla de MACs

Solucion al ejercicio 11 de switches
-----------------------------------------
Las respuestas son:

* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen b4f8, así que la anota.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``b4f8``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen b4f8.
* El Switch 1 envía el mensaje por el puerto 1. **Verdadera**, 6dc8 está en esa posición en la tabla de MACs
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen b4f8, así que la anota.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino 6dc8 en su tabla, en el puerto 1.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino 6dc8 en su tabla
* El Switch 2 envía el mensaje por el puerto 4. **Falsa**, no conoce a la MAC de destino 6dc8, así que necesita difundir.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``b4f8``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen b4f8.

Solucion al ejercicio 12 de switches
-----------------------------------------
Las respuestas son:

* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino 6978 en su tabla
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino 6978 en su tabla
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen 6133.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``6133``. **Falsa**, ya tenía esa MAC
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``6133``. **Falsa**, ya tenía esa MAC
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen 6133.
* El Switch 2 envía el mensaje por el puerto 4. **Falsa**, no conoce a la MAC de destino 6978, así que necesita difundir.
* El Switch 1 envía el mensaje por el puerto 6. **Falsa**, no conoce a la MAC de destino 6978, así que necesita difundir.

Solucion al ejercicio 13 de switches
-----------------------------------------
Las respuestas son:

* El Switch 1 envía el mensaje por el puerto 3. **Falsa**, no conoce a la MAC de destino ab43, así que necesita difundir.
* El Switch 2 envía el mensaje por el puerto 4. **Verdadera**, ab43 está en esa posición en la tabla de MACs
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``fcdd``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen fcdd.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``fcdd``. **Falsa**, ya tenía esa MAC
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino ab43 en su tabla, en el puerto 4.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen fcdd, así que la anota.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino ab43 en su tabla
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen fcdd.

Solucion al ejercicio 14 de switches
-----------------------------------------
Las respuestas son:

* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``4636``. **Falsa**, ya tenía esa MAC
* El Switch 2 envía el mensaje por el puerto 7. **Verdadera**, f23f está en esa posición en la tabla de MACs
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen 4636, así que la anota.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino f23f en su tabla, en el puerto 7.
* El Switch 1 envía el mensaje por el puerto 2. **Falsa**, no conoce a la MAC de destino f23f, así que necesita difundir.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen 4636.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``4636``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen 4636.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino f23f en su tabla

Solucion al ejercicio 15 de switches
-----------------------------------------
Las respuestas son:

* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``948c``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen 948c.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen 948c.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino ab97 en su tabla, en el puerto 0.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen 948c, así que la anota.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``948c``. **Falsa**, ya tenía esa MAC
* El Switch 2 envía el mensaje por el puerto 4. **Falsa**, no conoce a la MAC de destino ab97, así que necesita difundir.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino ab97 en su tabla
* El Switch 1 envía el mensaje por el puerto 0. **Verdadera**, ab97 está en esa posición en la tabla de MACs

Solucion al ejercicio 16 de switches
-----------------------------------------
Las respuestas son:

* El Switch 1 envía el mensaje por el puerto 1. **Falsa**, no conoce a la MAC de destino 5ad5, así que necesita difundir.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``d82a``. **Falsa**, ya tenía esa MAC
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen d82a.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino 5ad5 en su tabla, en el puerto 0.
* El Switch 2 envía el mensaje por el puerto 0. **Verdadera**, 5ad5 está en esa posición en la tabla de MACs
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino 5ad5 en su tabla
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``d82a``. **Falsa**, ya tenía esa MAC
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen d82a.

Solucion al ejercicio 17 de switches
-----------------------------------------
Las respuestas son:

* El Switch 1 envía el mensaje por el puerto 7. **Falsa**, no conoce a la MAC de destino 4fa6, así que necesita difundir.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino 4fa6 en su tabla, en el puerto 7.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino 4fa6 en su tabla
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``9d7e``. **Falsa**, ya tenía esa MAC
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen 9d7e.
* El Switch 2 envía el mensaje por el puerto 7. **Verdadera**, 4fa6 está en esa posición en la tabla de MACs
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen 9d7e.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``9d7e``. **Falsa**, ya tenía esa MAC

Solucion al ejercicio 18 de switches
-----------------------------------------
Las respuestas son:

* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``c862``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen c862.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino b434 en su tabla
* El Switch 2 envía el mensaje por el puerto 4. **Falsa**, no conoce a la MAC de destino b434, así que necesita difundir.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``c862``. **Falsa**, ya tenía esa MAC
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino b434 en su tabla, en el puerto 6.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen c862, así que la anota.
* El Switch 1 envía el mensaje por el puerto 6. **Verdadera**, b434 está en esa posición en la tabla de MACs
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen c862.

Solucion al ejercicio 19 de switches
-----------------------------------------
Las respuestas son:

* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Verdadera**, necesita hacerlo porque no tiene la MAC de destino e18e en su tabla
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen 75f7, así que la anota.
* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino e18e en su tabla, en el puerto 6.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``75f7``. **Falsa**, ya tenía esa MAC
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``75f7``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen 75f7.
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen 75f7.
* El Switch 2 envía el mensaje por el puerto 5. **Falsa**, no conoce a la MAC de destino e18e, así que necesita difundir.
* El Switch 1 envía el mensaje por el puerto 6. **Verdadera**, e18e está en esa posición en la tabla de MACs

Solucion al ejercicio 20 de switches
-----------------------------------------
Las respuestas son:

* El Switch 1 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino 56db en su tabla, en el puerto 2.
* El Switch 1 envía el mensaje por el puerto 2. **Verdadera**, 56db está en esa posición en la tabla de MACs
* El Switch 2 envía el mensaje por el puerto 4. **Verdadera**, 56db está en esa posición en la tabla de MACs
* El Switch 1 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, sí la modifica, no tenía la MAC de origen e5bd.
* El Switch 2 apunta en su tabla de MACS  la MAC de origen ``e5bd``. **Verdadera**, antes no lo conocía, así que sí anota la MAC de origen e5bd.
* El Switch 2 envía el mensaje por todos los puertos menos por donde vino. **Falsa** no necesita hacer difusión, tiene la MAC de destino 56db en su tabla, en el puerto 4.
* El Switch 2 no modifica su tabla de MACS, no aprende nada nuevo. **Falsa**, no conocía la MAC de origen e5bd, así que la anota.
* El Switch 1 apunta en su tabla de MACS  la MAC de origen ``e5bd``. **Falsa**, ya tenía esa MAC
