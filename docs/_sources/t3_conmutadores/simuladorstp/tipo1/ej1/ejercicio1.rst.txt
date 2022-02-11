
STP Ejercicio 1, dificultad 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Dada la red de switches que se muestra en la figura:

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej1/ejercicio1.png

Indicar el estado final en que quedarán todos los puertos de todos los switches.

Empezando por los eventos de envío, recepción y determinación de cual es el switch raíz la lista de sucesos sería esta:

1. 
2. Switch 3:24 envía por el puerto 87 la BPDU (Raíz:3:24, Coste:0, ID:3:24, MAC:87)
3. Switch 3:24 envía por el puerto 24 la BPDU (Raíz:3:24, Coste:0, ID:3:24, MAC:24)
4. Switch 1:02 envía por el puerto 02 la BPDU (Raíz:1:02, Coste:0, ID:1:02, MAC:02)
5. Switch 1:02 envía por el puerto 79 la BPDU (Raíz:1:02, Coste:0, ID:1:02, MAC:79)
6. Switch 3:15 envía por el puerto 15 la BPDU (Raíz:3:15, Coste:0, ID:3:15, MAC:15)
7. Switch 3:15 envía por el puerto 70 la BPDU (Raíz:3:15, Coste:0, ID:3:15, MAC:70)
8. Switch 1:49 envía por el puerto 93 la BPDU (Raíz:1:49, Coste:0, ID:1:49, MAC:93)
9. Switch 1:49 envía por el puerto 49 la BPDU (Raíz:1:49, Coste:0, ID:1:49, MAC:49)
10. Switch 3:24 recibe por el puerto 87 la BPDU (Raíz:1:49, Coste:0, ID:1:49, MAC:49).El switch 3:24 envió la BPDU (Raíz:3:24, Coste:0, ID:3:24, MAC:87) y recibió (Raíz:1:49, Coste:0, ID:1:49, MAC:49), que es una raíz mejor, así que apunta que la nueva raíz es 1:49 y que la mejor salida es por la MAC 87
11. Switch 3:24 recibe por el puerto 24 la BPDU (Raíz:1:02, Coste:0, ID:1:02, MAC:02).El switch 3:24 envió la BPDU (Raíz:3:24, Coste:0, ID:3:24, MAC:24) y recibió (Raíz:1:02, Coste:0, ID:1:02, MAC:02), que es una raíz mejor, así que apunta que la nueva raíz es 1:02 y que la mejor salida es por la MAC 24
12. Switch 1:02 recibe por el puerto 02 la BPDU (Raíz:3:24, Coste:0, ID:3:24, MAC:24)
13. Switch 1:02 recibe por el puerto 79 la BPDU (Raíz:3:15, Coste:0, ID:3:15, MAC:15)
14. Switch 3:15 recibe por el puerto 15 la BPDU (Raíz:1:02, Coste:0, ID:1:02, MAC:79).El switch 3:15 envió la BPDU (Raíz:3:15, Coste:0, ID:3:15, MAC:15) y recibió (Raíz:1:02, Coste:0, ID:1:02, MAC:79), que es una raíz mejor, así que apunta que la nueva raíz es 1:02 y que la mejor salida es por la MAC 15
15. Switch 3:15 recibe por el puerto 70 la BPDU (Raíz:1:49, Coste:0, ID:1:49, MAC:93)
16. Switch 1:49 recibe por el puerto 93 la BPDU (Raíz:3:15, Coste:0, ID:3:15, MAC:70)
17. Switch 1:49 recibe por el puerto 49 la BPDU (Raíz:3:24, Coste:0, ID:3:24, MAC:87)
18. Switch 3:24 envía por el puerto 87 la BPDU (Raíz:1:02, Coste:1, ID:3:24, MAC:87)
19. Switch 3:24 envía por el puerto 24 la BPDU (Raíz:1:02, Coste:1, ID:3:24, MAC:24)
20. Switch 1:02 envía por el puerto 02 la BPDU (Raíz:1:02, Coste:0, ID:1:02, MAC:02)
21. Switch 1:02 envía por el puerto 79 la BPDU (Raíz:1:02, Coste:0, ID:1:02, MAC:79)
22. Switch 3:15 envía por el puerto 15 la BPDU (Raíz:1:02, Coste:1, ID:3:15, MAC:15)
23. Switch 3:15 envía por el puerto 70 la BPDU (Raíz:1:02, Coste:1, ID:3:15, MAC:70)
24. Switch 1:49 envía por el puerto 93 la BPDU (Raíz:1:49, Coste:0, ID:1:49, MAC:93)
25. Switch 1:49 envía por el puerto 49 la BPDU (Raíz:1:49, Coste:0, ID:1:49, MAC:49)
26. Switch 3:24 recibe por el puerto 87 la BPDU (Raíz:1:49, Coste:0, ID:1:49, MAC:49)
27. Switch 3:24 recibe por el puerto 24 la BPDU (Raíz:1:02, Coste:0, ID:1:02, MAC:02).El switch 3:24 envió la BPDU (Raíz:1:02, Coste:1, ID:3:24, MAC:24) y recibió (Raíz:1:02, Coste:0, ID:1:02, MAC:02), que es una raíz mejor, así que apunta que la nueva raíz es 1:02 y que la mejor salida es por la MAC 24
28. Switch 1:02 recibe por el puerto 02 la BPDU (Raíz:1:02, Coste:1, ID:3:24, MAC:24)
29. Switch 1:02 recibe por el puerto 79 la BPDU (Raíz:1:02, Coste:1, ID:3:15, MAC:15).El switch 1:02 envió la BPDU (Raíz:1:02, Coste:0, ID:1:02, MAC:79) y recibió (Raíz:1:02, Coste:1, ID:3:15, MAC:15), que es una raíz mejor, así que apunta que la nueva raíz es 1:02 y que la mejor salida es por la MAC 79
30. Switch 3:15 recibe por el puerto 15 la BPDU (Raíz:1:02, Coste:0, ID:1:02, MAC:79)
31. Switch 3:15 recibe por el puerto 70 la BPDU (Raíz:1:49, Coste:0, ID:1:49, MAC:93)
32. Switch 1:49 recibe por el puerto 93 la BPDU (Raíz:1:02, Coste:1, ID:3:15, MAC:70).El switch 1:49 envió la BPDU (Raíz:1:49, Coste:0, ID:1:49, MAC:93) y recibió (Raíz:1:02, Coste:1, ID:3:15, MAC:70), que es una raíz mejor, así que apunta que la nueva raíz es 1:02 y que la mejor salida es por la MAC 93
33. Switch 1:49 recibe por el puerto 49 la BPDU (Raíz:1:02, Coste:1, ID:3:24, MAC:87)
34. Switch 3:24 envía por el puerto 87 la BPDU (Raíz:1:02, Coste:1, ID:3:24, MAC:87)
35. Switch 3:24 envía por el puerto 24 la BPDU (Raíz:1:02, Coste:1, ID:3:24, MAC:24)
36. Switch 1:02 envía por el puerto 02 la BPDU (Raíz:1:02, Coste:2, ID:1:02, MAC:02)
37. Switch 1:02 envía por el puerto 79 la BPDU (Raíz:1:02, Coste:2, ID:1:02, MAC:79)
38. Switch 3:15 envía por el puerto 15 la BPDU (Raíz:1:02, Coste:1, ID:3:15, MAC:15)
39. Switch 3:15 envía por el puerto 70 la BPDU (Raíz:1:02, Coste:1, ID:3:15, MAC:70)
40. Switch 1:49 envía por el puerto 93 la BPDU (Raíz:1:02, Coste:2, ID:1:49, MAC:93)
41. Switch 1:49 envía por el puerto 49 la BPDU (Raíz:1:02, Coste:2, ID:1:49, MAC:49)
42. Switch 3:24 recibe por el puerto 87 la BPDU (Raíz:1:02, Coste:2, ID:1:49, MAC:49).El switch 3:24 envió la BPDU (Raíz:1:02, Coste:1, ID:3:24, MAC:87) y recibió (Raíz:1:02, Coste:2, ID:1:49, MAC:49), que es una raíz mejor, así que apunta que la nueva raíz es 1:02 y que la mejor salida es por la MAC 87
43. Switch 3:24 recibe por el puerto 24 la BPDU (Raíz:1:02, Coste:2, ID:1:02, MAC:02).El switch 3:24 envió la BPDU (Raíz:1:02, Coste:1, ID:3:24, MAC:24) y recibió (Raíz:1:02, Coste:2, ID:1:02, MAC:02), que es una raíz mejor, así que apunta que la nueva raíz es 1:02 y que la mejor salida es por la MAC 24
44. Switch 1:02 recibe por el puerto 02 la BPDU (Raíz:1:02, Coste:1, ID:3:24, MAC:24)
45. Switch 1:02 recibe por el puerto 79 la BPDU (Raíz:1:02, Coste:1, ID:3:15, MAC:15).El switch 1:02 envió la BPDU (Raíz:1:02, Coste:2, ID:1:02, MAC:79) y recibió (Raíz:1:02, Coste:1, ID:3:15, MAC:15), que es una raíz mejor, así que apunta que la nueva raíz es 1:02 y que la mejor salida es por la MAC 79
46. Switch 3:15 recibe por el puerto 15 la BPDU (Raíz:1:02, Coste:2, ID:1:02, MAC:79)
47. Switch 3:15 recibe por el puerto 70 la BPDU (Raíz:1:02, Coste:2, ID:1:49, MAC:93)
48. Switch 1:49 recibe por el puerto 93 la BPDU (Raíz:1:02, Coste:1, ID:3:15, MAC:70).El switch 1:49 envió la BPDU (Raíz:1:02, Coste:2, ID:1:49, MAC:93) y recibió (Raíz:1:02, Coste:1, ID:3:15, MAC:70), que es una raíz mejor, así que apunta que la nueva raíz es 1:02 y que la mejor salida es por la MAC 93
49. Switch 1:49 recibe por el puerto 49 la BPDU (Raíz:1:02, Coste:1, ID:3:24, MAC:87)
50. Switch 3:24 envía por el puerto 87 la BPDU (Raíz:1:02, Coste:3, ID:3:24, MAC:87)
51. Switch 3:24 envía por el puerto 24 la BPDU (Raíz:1:02, Coste:3, ID:3:24, MAC:24)
52. Switch 1:02 envía por el puerto 02 la BPDU (Raíz:1:02, Coste:2, ID:1:02, MAC:02)
53. Switch 1:02 envía por el puerto 79 la BPDU (Raíz:1:02, Coste:2, ID:1:02, MAC:79)
54. Switch 3:15 envía por el puerto 15 la BPDU (Raíz:1:02, Coste:1, ID:3:15, MAC:15)
55. Switch 3:15 envía por el puerto 70 la BPDU (Raíz:1:02, Coste:1, ID:3:15, MAC:70)
56. Switch 1:49 envía por el puerto 93 la BPDU (Raíz:1:02, Coste:2, ID:1:49, MAC:93)
57. Switch 1:49 envía por el puerto 49 la BPDU (Raíz:1:02, Coste:2, ID:1:49, MAC:49)
58. Switch 3:24 recibe por el puerto 87 la BPDU (Raíz:1:02, Coste:2, ID:1:49, MAC:49).El switch 3:24 envió la BPDU (Raíz:1:02, Coste:3, ID:3:24, MAC:87) y recibió (Raíz:1:02, Coste:2, ID:1:49, MAC:49), que es una raíz mejor, así que apunta que la nueva raíz es 1:02 y que la mejor salida es por la MAC 87
59. Switch 3:24 recibe por el puerto 24 la BPDU (Raíz:1:02, Coste:2, ID:1:02, MAC:02).El switch 3:24 envió la BPDU (Raíz:1:02, Coste:3, ID:3:24, MAC:24) y recibió (Raíz:1:02, Coste:2, ID:1:02, MAC:02), que es una raíz mejor, así que apunta que la nueva raíz es 1:02 y que la mejor salida es por la MAC 24
60. Switch 1:02 recibe por el puerto 02 la BPDU (Raíz:1:02, Coste:3, ID:3:24, MAC:24)
61. Switch 1:02 recibe por el puerto 79 la BPDU (Raíz:1:02, Coste:1, ID:3:15, MAC:15).El switch 1:02 envió la BPDU (Raíz:1:02, Coste:2, ID:1:02, MAC:79) y recibió (Raíz:1:02, Coste:1, ID:3:15, MAC:15), que es una raíz mejor, así que apunta que la nueva raíz es 1:02 y que la mejor salida es por la MAC 79
62. Switch 3:15 recibe por el puerto 15 la BPDU (Raíz:1:02, Coste:2, ID:1:02, MAC:79)
63. Switch 3:15 recibe por el puerto 70 la BPDU (Raíz:1:02, Coste:2, ID:1:49, MAC:93)
64. Switch 1:49 recibe por el puerto 93 la BPDU (Raíz:1:02, Coste:1, ID:3:15, MAC:70).El switch 1:49 envió la BPDU (Raíz:1:02, Coste:2, ID:1:49, MAC:93) y recibió (Raíz:1:02, Coste:1, ID:3:15, MAC:70), que es una raíz mejor, así que apunta que la nueva raíz es 1:02 y que la mejor salida es por la MAC 93
65. Switch 1:49 recibe por el puerto 49 la BPDU (Raíz:1:02, Coste:3, ID:3:24, MAC:87)



Una vez decidido el switch raíz, los switches toman las siguientes decisiones (volvemos a indicar la figura por comodidad):

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej1/ejercicio1.png

El switch 3:24 toma estas decisiones:

* El puerto con la MAC 24 se convierte en raíz. Es el mejor de los puertos con un coste de 3 para llegar al switch raíz 1:02.
* El puerto con la MAC 24 se convierte en raíz. Es el mejor de los puertos con un coste de 3 para llegar al switch raíz 1:02.
El switch 1:02 toma estas decisiones:

* 1:02 es raiz y pone todos sus puertos a designado.
* 1:02 es raiz y pone todos sus puertos a designado.
El switch 3:15 toma estas decisiones:

* El puerto con la MAC 15 se convierte en raíz. Es el mejor de los puertos con un coste de 1 para llegar al switch raíz 1:02.
* El puerto con la MAC 15 se convierte en raíz. Es el mejor de los puertos con un coste de 1 para llegar al switch raíz 1:02.
El switch 1:49 toma estas decisiones:

* El puerto con la MAC 93 se convierte en raíz. Es el mejor de los puertos con un coste de 2 para llegar al switch raíz 1:02.
* El puerto con la MAC 93 se convierte en raíz. Es el mejor de los puertos con un coste de 2 para llegar al switch raíz 1:02.


