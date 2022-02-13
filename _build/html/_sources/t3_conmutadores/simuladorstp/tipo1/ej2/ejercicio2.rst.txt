
STP Ejercicio 2, dificultad 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Dada la red de switches que se muestra en la figura:

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej2/ejercicio2.png

Indicar el estado final en que quedarán todos los puertos de todos los switches.

Empezando por los eventos de envío, recepción y determinación de cual es el switch raíz la lista de sucesos sería esta:

1. 
2. Switch 4:18 envía por el puerto 58 la BPDU (Raíz:4:18, Coste:0, ID:4:18, MAC:58)
3. Switch 4:18 envía por el puerto 18 la BPDU (Raíz:4:18, Coste:0, ID:4:18, MAC:18)
4. Switch 3:42 envía por el puerto 42 la BPDU (Raíz:3:42, Coste:0, ID:3:42, MAC:42)
5. Switch 3:42 envía por el puerto 66 la BPDU (Raíz:3:42, Coste:0, ID:3:42, MAC:66)
6. Switch 5:09 envía por el puerto 50 la BPDU (Raíz:5:09, Coste:0, ID:5:09, MAC:50)
7. Switch 5:09 envía por el puerto 09 la BPDU (Raíz:5:09, Coste:0, ID:5:09, MAC:09)
8. Switch 2:08 envía por el puerto 08 la BPDU (Raíz:2:08, Coste:0, ID:2:08, MAC:08)
9. Switch 2:08 envía por el puerto 41 la BPDU (Raíz:2:08, Coste:0, ID:2:08, MAC:41)
10. Switch 4:18 recibe por el puerto 58 la BPDU (Raíz:2:08, Coste:0, ID:2:08, MAC:41).El switch 4:18 envió la BPDU (Raíz:4:18, Coste:0, ID:4:18, MAC:58) y recibió (Raíz:2:08, Coste:0, ID:2:08, MAC:41), que es una raíz mejor, así que apunta que la nueva raíz es 2:08 y que la mejor salida es por la MAC 58
11. Switch 4:18 recibe por el puerto 18 la BPDU (Raíz:3:42, Coste:0, ID:3:42, MAC:42)
12. Switch 3:42 recibe por el puerto 42 la BPDU (Raíz:4:18, Coste:0, ID:4:18, MAC:18)
13. Switch 3:42 recibe por el puerto 66 la BPDU (Raíz:5:09, Coste:0, ID:5:09, MAC:50)
14. Switch 5:09 recibe por el puerto 50 la BPDU (Raíz:3:42, Coste:0, ID:3:42, MAC:66).El switch 5:09 envió la BPDU (Raíz:5:09, Coste:0, ID:5:09, MAC:50) y recibió (Raíz:3:42, Coste:0, ID:3:42, MAC:66), que es una raíz mejor, así que apunta que la nueva raíz es 3:42 y que la mejor salida es por la MAC 50
15. Switch 5:09 recibe por el puerto 09 la BPDU (Raíz:2:08, Coste:0, ID:2:08, MAC:08).El switch 5:09 envió la BPDU (Raíz:5:09, Coste:0, ID:5:09, MAC:09) y recibió (Raíz:2:08, Coste:0, ID:2:08, MAC:08), que es una raíz mejor, así que apunta que la nueva raíz es 2:08 y que la mejor salida es por la MAC 09
16. Switch 2:08 recibe por el puerto 08 la BPDU (Raíz:5:09, Coste:0, ID:5:09, MAC:09)
17. Switch 2:08 recibe por el puerto 41 la BPDU (Raíz:4:18, Coste:0, ID:4:18, MAC:58)
18. Switch 4:18 envía por el puerto 58 la BPDU (Raíz:2:08, Coste:1, ID:4:18, MAC:58)
19. Switch 4:18 envía por el puerto 18 la BPDU (Raíz:2:08, Coste:1, ID:4:18, MAC:18)
20. Switch 3:42 envía por el puerto 42 la BPDU (Raíz:3:42, Coste:0, ID:3:42, MAC:42)
21. Switch 3:42 envía por el puerto 66 la BPDU (Raíz:3:42, Coste:0, ID:3:42, MAC:66)
22. Switch 5:09 envía por el puerto 50 la BPDU (Raíz:2:08, Coste:1, ID:5:09, MAC:50)
23. Switch 5:09 envía por el puerto 09 la BPDU (Raíz:2:08, Coste:1, ID:5:09, MAC:09)
24. Switch 2:08 envía por el puerto 08 la BPDU (Raíz:2:08, Coste:0, ID:2:08, MAC:08)
25. Switch 2:08 envía por el puerto 41 la BPDU (Raíz:2:08, Coste:0, ID:2:08, MAC:41)
26. Switch 4:18 recibe por el puerto 58 la BPDU (Raíz:2:08, Coste:0, ID:2:08, MAC:41).El switch 4:18 envió la BPDU (Raíz:2:08, Coste:1, ID:4:18, MAC:58) y recibió (Raíz:2:08, Coste:0, ID:2:08, MAC:41), que es una raíz mejor, así que apunta que la nueva raíz es 2:08 y que la mejor salida es por la MAC 58
27. Switch 4:18 recibe por el puerto 18 la BPDU (Raíz:3:42, Coste:0, ID:3:42, MAC:42)
28. Switch 3:42 recibe por el puerto 42 la BPDU (Raíz:2:08, Coste:1, ID:4:18, MAC:18).El switch 3:42 envió la BPDU (Raíz:3:42, Coste:0, ID:3:42, MAC:42) y recibió (Raíz:2:08, Coste:1, ID:4:18, MAC:18), que es una raíz mejor, así que apunta que la nueva raíz es 2:08 y que la mejor salida es por la MAC 42
29. Switch 3:42 recibe por el puerto 66 la BPDU (Raíz:2:08, Coste:1, ID:5:09, MAC:50).El switch 3:42 envió la BPDU (Raíz:3:42, Coste:0, ID:3:42, MAC:66) y recibió (Raíz:2:08, Coste:1, ID:5:09, MAC:50), que es una raíz mejor, así que apunta que la nueva raíz es 2:08 y que la mejor salida es por la MAC 66
30. Switch 5:09 recibe por el puerto 50 la BPDU (Raíz:3:42, Coste:0, ID:3:42, MAC:66)
31. Switch 5:09 recibe por el puerto 09 la BPDU (Raíz:2:08, Coste:0, ID:2:08, MAC:08).El switch 5:09 envió la BPDU (Raíz:2:08, Coste:1, ID:5:09, MAC:09) y recibió (Raíz:2:08, Coste:0, ID:2:08, MAC:08), que es una raíz mejor, así que apunta que la nueva raíz es 2:08 y que la mejor salida es por la MAC 09
32. Switch 2:08 recibe por el puerto 08 la BPDU (Raíz:2:08, Coste:1, ID:5:09, MAC:09)
33. Switch 2:08 recibe por el puerto 41 la BPDU (Raíz:2:08, Coste:1, ID:4:18, MAC:58)
34. Switch 4:18 envía por el puerto 58 la BPDU (Raíz:2:08, Coste:1, ID:4:18, MAC:58)
35. Switch 4:18 envía por el puerto 18 la BPDU (Raíz:2:08, Coste:1, ID:4:18, MAC:18)
36. Switch 3:42 envía por el puerto 42 la BPDU (Raíz:2:08, Coste:2, ID:3:42, MAC:42)
37. Switch 3:42 envía por el puerto 66 la BPDU (Raíz:2:08, Coste:2, ID:3:42, MAC:66)
38. Switch 5:09 envía por el puerto 50 la BPDU (Raíz:2:08, Coste:1, ID:5:09, MAC:50)
39. Switch 5:09 envía por el puerto 09 la BPDU (Raíz:2:08, Coste:1, ID:5:09, MAC:09)
40. Switch 2:08 envía por el puerto 08 la BPDU (Raíz:2:08, Coste:0, ID:2:08, MAC:08)
41. Switch 2:08 envía por el puerto 41 la BPDU (Raíz:2:08, Coste:0, ID:2:08, MAC:41)
42. Switch 4:18 recibe por el puerto 58 la BPDU (Raíz:2:08, Coste:0, ID:2:08, MAC:41).El switch 4:18 envió la BPDU (Raíz:2:08, Coste:1, ID:4:18, MAC:58) y recibió (Raíz:2:08, Coste:0, ID:2:08, MAC:41), que es una raíz mejor, así que apunta que la nueva raíz es 2:08 y que la mejor salida es por la MAC 58
43. Switch 4:18 recibe por el puerto 18 la BPDU (Raíz:2:08, Coste:2, ID:3:42, MAC:42)
44. Switch 3:42 recibe por el puerto 42 la BPDU (Raíz:2:08, Coste:1, ID:4:18, MAC:18).El switch 3:42 envió la BPDU (Raíz:2:08, Coste:2, ID:3:42, MAC:42) y recibió (Raíz:2:08, Coste:1, ID:4:18, MAC:18), que es una raíz mejor, así que apunta que la nueva raíz es 2:08 y que la mejor salida es por la MAC 42
45. Switch 3:42 recibe por el puerto 66 la BPDU (Raíz:2:08, Coste:1, ID:5:09, MAC:50).El switch 3:42 envió la BPDU (Raíz:2:08, Coste:2, ID:3:42, MAC:66) y recibió (Raíz:2:08, Coste:1, ID:5:09, MAC:50), que es una raíz mejor, así que apunta que la nueva raíz es 2:08 y que la mejor salida es por la MAC 66
46. Switch 5:09 recibe por el puerto 50 la BPDU (Raíz:2:08, Coste:2, ID:3:42, MAC:66)
47. Switch 5:09 recibe por el puerto 09 la BPDU (Raíz:2:08, Coste:0, ID:2:08, MAC:08).El switch 5:09 envió la BPDU (Raíz:2:08, Coste:1, ID:5:09, MAC:09) y recibió (Raíz:2:08, Coste:0, ID:2:08, MAC:08), que es una raíz mejor, así que apunta que la nueva raíz es 2:08 y que la mejor salida es por la MAC 09
48. Switch 2:08 recibe por el puerto 08 la BPDU (Raíz:2:08, Coste:1, ID:5:09, MAC:09)
49. Switch 2:08 recibe por el puerto 41 la BPDU (Raíz:2:08, Coste:1, ID:4:18, MAC:58)
50. Switch 4:18 envía por el puerto 58 la BPDU (Raíz:2:08, Coste:1, ID:4:18, MAC:58)
51. Switch 4:18 envía por el puerto 18 la BPDU (Raíz:2:08, Coste:1, ID:4:18, MAC:18)
52. Switch 3:42 envía por el puerto 42 la BPDU (Raíz:2:08, Coste:2, ID:3:42, MAC:42)
53. Switch 3:42 envía por el puerto 66 la BPDU (Raíz:2:08, Coste:2, ID:3:42, MAC:66)
54. Switch 5:09 envía por el puerto 50 la BPDU (Raíz:2:08, Coste:1, ID:5:09, MAC:50)
55. Switch 5:09 envía por el puerto 09 la BPDU (Raíz:2:08, Coste:1, ID:5:09, MAC:09)
56. Switch 2:08 envía por el puerto 08 la BPDU (Raíz:2:08, Coste:0, ID:2:08, MAC:08)
57. Switch 2:08 envía por el puerto 41 la BPDU (Raíz:2:08, Coste:0, ID:2:08, MAC:41)
58. Switch 4:18 recibe por el puerto 58 la BPDU (Raíz:2:08, Coste:0, ID:2:08, MAC:41).El switch 4:18 envió la BPDU (Raíz:2:08, Coste:1, ID:4:18, MAC:58) y recibió (Raíz:2:08, Coste:0, ID:2:08, MAC:41), que es una raíz mejor, así que apunta que la nueva raíz es 2:08 y que la mejor salida es por la MAC 58
59. Switch 4:18 recibe por el puerto 18 la BPDU (Raíz:2:08, Coste:2, ID:3:42, MAC:42)
60. Switch 3:42 recibe por el puerto 42 la BPDU (Raíz:2:08, Coste:1, ID:4:18, MAC:18).El switch 3:42 envió la BPDU (Raíz:2:08, Coste:2, ID:3:42, MAC:42) y recibió (Raíz:2:08, Coste:1, ID:4:18, MAC:18), que es una raíz mejor, así que apunta que la nueva raíz es 2:08 y que la mejor salida es por la MAC 42
61. Switch 3:42 recibe por el puerto 66 la BPDU (Raíz:2:08, Coste:1, ID:5:09, MAC:50).El switch 3:42 envió la BPDU (Raíz:2:08, Coste:2, ID:3:42, MAC:66) y recibió (Raíz:2:08, Coste:1, ID:5:09, MAC:50), que es una raíz mejor, así que apunta que la nueva raíz es 2:08 y que la mejor salida es por la MAC 66
62. Switch 5:09 recibe por el puerto 50 la BPDU (Raíz:2:08, Coste:2, ID:3:42, MAC:66)
63. Switch 5:09 recibe por el puerto 09 la BPDU (Raíz:2:08, Coste:0, ID:2:08, MAC:08).El switch 5:09 envió la BPDU (Raíz:2:08, Coste:1, ID:5:09, MAC:09) y recibió (Raíz:2:08, Coste:0, ID:2:08, MAC:08), que es una raíz mejor, así que apunta que la nueva raíz es 2:08 y que la mejor salida es por la MAC 09
64. Switch 2:08 recibe por el puerto 08 la BPDU (Raíz:2:08, Coste:1, ID:5:09, MAC:09)
65. Switch 2:08 recibe por el puerto 41 la BPDU (Raíz:2:08, Coste:1, ID:4:18, MAC:58)



Una vez decidido el switch raíz, los switches toman las siguientes decisiones (volvemos a indicar la figura por comodidad):

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej2/ejercicio2.png

El switch 4:18 toma estas decisiones:

* El puerto con la MAC 58 se convierte en raíz. Es el mejor de los puertos con un coste de 1 para llegar al switch raíz 2:08.
* El puerto con la MAC 58 se convierte en raíz. Es el mejor de los puertos con un coste de 1 para llegar al switch raíz 2:08.
El switch 3:42 toma estas decisiones:

* El puerto con la MAC 66 se convierte en raíz. Es el mejor de los puertos con un coste de 2 para llegar al switch raíz 2:08.
* El puerto con la MAC 66 se convierte en raíz. Es el mejor de los puertos con un coste de 2 para llegar al switch raíz 2:08.
El switch 5:09 toma estas decisiones:

* El puerto con la MAC 09 se convierte en raíz. Es el mejor de los puertos con un coste de 1 para llegar al switch raíz 2:08.
* El puerto con la MAC 09 se convierte en raíz. Es el mejor de los puertos con un coste de 1 para llegar al switch raíz 2:08.
El switch 2:08 toma estas decisiones:

* 2:08 es raiz y pone todos sus puertos a designado.
* 2:08 es raiz y pone todos sus puertos a designado.


