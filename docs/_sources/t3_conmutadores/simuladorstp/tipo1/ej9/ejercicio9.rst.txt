
STP Ejercicio 9, dificultad 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Dada la red de switches que se muestra en la figura:

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej9/ejercicio9.png

Indicar el estado final en que quedarán todos los puertos de todos los switches.

Empezando por los eventos de envío, recepción y determinación de cual es el switch raíz la lista de sucesos sería esta:


1. Switch 1:02 envía por el puerto 02 la BPDU (Raíz:1:02, Coste:0, ID:1:02, MAC:02)
2. Switch 1:02 envía por el puerto 71 la BPDU (Raíz:1:02, Coste:0, ID:1:02, MAC:71)
3. Switch 6:21 envía por el puerto 39 la BPDU (Raíz:6:21, Coste:0, ID:6:21, MAC:39)
4. Switch 6:21 envía por el puerto 21 la BPDU (Raíz:6:21, Coste:0, ID:6:21, MAC:21)
5. Switch 5:23 envía por el puerto 31 la BPDU (Raíz:5:23, Coste:0, ID:5:23, MAC:31)
6. Switch 5:23 envía por el puerto 23 la BPDU (Raíz:5:23, Coste:0, ID:5:23, MAC:23)
7. Switch 4:13 envía por el puerto 13 la BPDU (Raíz:4:13, Coste:0, ID:4:13, MAC:13)
8. Switch 4:13 envía por el puerto 16 la BPDU (Raíz:4:13, Coste:0, ID:4:13, MAC:16)
9. Switch 1:02 recibe por el puerto 02 la BPDU (Raíz:4:13, Coste:0, ID:4:13, MAC:16)
10. Switch 1:02 recibe por el puerto 71 la BPDU (Raíz:6:21, Coste:0, ID:6:21, MAC:39)
11. Switch 6:21 recibe por el puerto 39 la BPDU (Raíz:1:02, Coste:0, ID:1:02, MAC:71). La raíz 1:02 es mejor, así que se anota como nueva raíz.
12. Switch 6:21 recibe por el puerto 21 la BPDU (Raíz:5:23, Coste:0, ID:5:23, MAC:31)
13. Switch 5:23 recibe por el puerto 31 la BPDU (Raíz:6:21, Coste:0, ID:6:21, MAC:21)
14. Switch 5:23 recibe por el puerto 23 la BPDU (Raíz:4:13, Coste:0, ID:4:13, MAC:13). La raíz 4:13 es mejor, así que se anota como nueva raíz.
15. Switch 4:13 recibe por el puerto 13 la BPDU (Raíz:5:23, Coste:0, ID:5:23, MAC:23)
16. Switch 4:13 recibe por el puerto 16 la BPDU (Raíz:1:02, Coste:0, ID:1:02, MAC:02). La raíz 1:02 es mejor, así que se anota como nueva raíz.
17. Switch 1:02 envía por el puerto 02 la BPDU (Raíz:1:02, Coste:0, ID:1:02, MAC:02)
18. Switch 1:02 envía por el puerto 71 la BPDU (Raíz:1:02, Coste:0, ID:1:02, MAC:71)
19. Switch 6:21 envía por el puerto 39 la BPDU (Raíz:1:02, Coste:1, ID:6:21, MAC:39)
20. Switch 6:21 envía por el puerto 21 la BPDU (Raíz:1:02, Coste:1, ID:6:21, MAC:21)
21. Switch 5:23 envía por el puerto 31 la BPDU (Raíz:4:13, Coste:1, ID:5:23, MAC:31)
22. Switch 5:23 envía por el puerto 23 la BPDU (Raíz:4:13, Coste:1, ID:5:23, MAC:23)
23. Switch 4:13 envía por el puerto 13 la BPDU (Raíz:1:02, Coste:1, ID:4:13, MAC:13)
24. Switch 4:13 envía por el puerto 16 la BPDU (Raíz:1:02, Coste:1, ID:4:13, MAC:16)
25. Switch 1:02 recibe por el puerto 02 la BPDU (Raíz:1:02, Coste:1, ID:4:13, MAC:16)
26. Switch 1:02 recibe por el puerto 71 la BPDU (Raíz:1:02, Coste:1, ID:6:21, MAC:39)
27. Switch 6:21 recibe por el puerto 39 la BPDU (Raíz:1:02, Coste:0, ID:1:02, MAC:71)
28. Switch 6:21 recibe por el puerto 21 la BPDU (Raíz:4:13, Coste:1, ID:5:23, MAC:31)
29. Switch 5:23 recibe por el puerto 31 la BPDU (Raíz:1:02, Coste:1, ID:6:21, MAC:21). La raíz 1:02 es mejor, así que se anota como nueva raíz.
30. Switch 5:23 recibe por el puerto 23 la BPDU (Raíz:1:02, Coste:1, ID:4:13, MAC:13). Llegó de nuevo la raíz 1:02 pero por un puerto con menor MAC (23), así que ese puerto se anota como posible puerto raíz
31. Switch 4:13 recibe por el puerto 13 la BPDU (Raíz:4:13, Coste:1, ID:5:23, MAC:23)
32. Switch 4:13 recibe por el puerto 16 la BPDU (Raíz:1:02, Coste:0, ID:1:02, MAC:02)
33. Switch 1:02 envía por el puerto 02 la BPDU (Raíz:1:02, Coste:0, ID:1:02, MAC:02)
34. Switch 1:02 envía por el puerto 71 la BPDU (Raíz:1:02, Coste:0, ID:1:02, MAC:71)
35. Switch 6:21 envía por el puerto 39 la BPDU (Raíz:1:02, Coste:1, ID:6:21, MAC:39)
36. Switch 6:21 envía por el puerto 21 la BPDU (Raíz:1:02, Coste:1, ID:6:21, MAC:21)
37. Switch 5:23 envía por el puerto 31 la BPDU (Raíz:1:02, Coste:2, ID:5:23, MAC:31)
38. Switch 5:23 envía por el puerto 23 la BPDU (Raíz:1:02, Coste:2, ID:5:23, MAC:23)
39. Switch 4:13 envía por el puerto 13 la BPDU (Raíz:1:02, Coste:1, ID:4:13, MAC:13)
40. Switch 4:13 envía por el puerto 16 la BPDU (Raíz:1:02, Coste:1, ID:4:13, MAC:16)
41. Switch 1:02 recibe por el puerto 02 la BPDU (Raíz:1:02, Coste:1, ID:4:13, MAC:16)
42. Switch 1:02 recibe por el puerto 71 la BPDU (Raíz:1:02, Coste:1, ID:6:21, MAC:39)
43. Switch 6:21 recibe por el puerto 39 la BPDU (Raíz:1:02, Coste:0, ID:1:02, MAC:71)
44. Switch 6:21 recibe por el puerto 21 la BPDU (Raíz:1:02, Coste:2, ID:5:23, MAC:31)
45. Switch 5:23 recibe por el puerto 31 la BPDU (Raíz:1:02, Coste:1, ID:6:21, MAC:21)
46. Switch 5:23 recibe por el puerto 23 la BPDU (Raíz:1:02, Coste:1, ID:4:13, MAC:13)
47. Switch 4:13 recibe por el puerto 13 la BPDU (Raíz:1:02, Coste:2, ID:5:23, MAC:23)
48. Switch 4:13 recibe por el puerto 16 la BPDU (Raíz:1:02, Coste:0, ID:1:02, MAC:02)



Una vez decidido el switch raíz, los switches toman las siguientes decisiones (volvemos a indicar la figura por comodidad):

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej9/ejercicio9.png




El switch 1:02 toma estas decisiones:

* 1:02 es raiz y pone todos sus puertos a designado.




El switch 6:21 toma estas decisiones:

* El puerto con la MAC 39 se convierte en raíz. 
* El puerto con la MAC 21 se convierte en designado. Es el mejor del segmento con un coste de 1 frente un coste de 2 que ofrece el puerto 31.




El switch 5:23 toma estas decisiones:

* El puerto con la MAC 23 se convierte en raíz. 




El switch 4:13 toma estas decisiones:

* El puerto con la MAC 16 se convierte en raíz. 
* El puerto con la MAC 13 se convierte en designado. Es el mejor del segmento con un coste de 1 frente un coste de 2 que ofrece el puerto 23.


        