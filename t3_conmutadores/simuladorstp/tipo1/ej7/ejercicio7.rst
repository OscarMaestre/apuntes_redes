
STP Ejercicio 7, dificultad 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Dada la red de switches que se muestra en la figura:

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej7/ejercicio7.png

Indicar el estado final en que quedarán todos los puertos de todos los switches.

Empezando por los eventos de envío, recepción y determinación de cual es el switch raíz la lista de sucesos sería esta:


1. Switch 4:08 envía por el puerto 08 la BPDU (Raíz:4:08, Coste:0, ID:4:08, MAC:08)
2. Switch 4:08 envía por el puerto 89 la BPDU (Raíz:4:08, Coste:0, ID:4:08, MAC:89)
3. Switch 3:00 envía por el puerto 57 la BPDU (Raíz:3:00, Coste:0, ID:3:00, MAC:57)
4. Switch 3:00 envía por el puerto 00 la BPDU (Raíz:3:00, Coste:0, ID:3:00, MAC:00)
5. Switch 3:39 envía por el puerto 53 la BPDU (Raíz:3:39, Coste:0, ID:3:39, MAC:53)
6. Switch 3:39 envía por el puerto 39 la BPDU (Raíz:3:39, Coste:0, ID:3:39, MAC:39)
7. Switch 2:50 envía por el puerto 85 la BPDU (Raíz:2:50, Coste:0, ID:2:50, MAC:85)
8. Switch 2:50 envía por el puerto 50 la BPDU (Raíz:2:50, Coste:0, ID:2:50, MAC:50)
9. Switch 4:08 recibe por el puerto 08 la BPDU (Raíz:2:50, Coste:0, ID:2:50, MAC:50). La raíz 2:50 es mejor, así que se anota como nueva raíz.
10. Switch 4:08 recibe por el puerto 89 la BPDU (Raíz:3:00, Coste:0, ID:3:00, MAC:57)
11. Switch 3:00 recibe por el puerto 57 la BPDU (Raíz:4:08, Coste:0, ID:4:08, MAC:89)
12. Switch 3:00 recibe por el puerto 00 la BPDU (Raíz:3:39, Coste:0, ID:3:39, MAC:53)
13. Switch 3:39 recibe por el puerto 53 la BPDU (Raíz:3:00, Coste:0, ID:3:00, MAC:00). La raíz 3:00 es mejor, así que se anota como nueva raíz.
14. Switch 3:39 recibe por el puerto 39 la BPDU (Raíz:2:50, Coste:0, ID:2:50, MAC:85). La raíz 2:50 es mejor, así que se anota como nueva raíz.
15. Switch 2:50 recibe por el puerto 85 la BPDU (Raíz:3:39, Coste:0, ID:3:39, MAC:39)
16. Switch 2:50 recibe por el puerto 50 la BPDU (Raíz:4:08, Coste:0, ID:4:08, MAC:08)
17. Switch 4:08 envía por el puerto 08 la BPDU (Raíz:2:50, Coste:1, ID:4:08, MAC:08)
18. Switch 4:08 envía por el puerto 89 la BPDU (Raíz:2:50, Coste:1, ID:4:08, MAC:89)
19. Switch 3:00 envía por el puerto 57 la BPDU (Raíz:3:00, Coste:0, ID:3:00, MAC:57)
20. Switch 3:00 envía por el puerto 00 la BPDU (Raíz:3:00, Coste:0, ID:3:00, MAC:00)
21. Switch 3:39 envía por el puerto 53 la BPDU (Raíz:2:50, Coste:1, ID:3:39, MAC:53)
22. Switch 3:39 envía por el puerto 39 la BPDU (Raíz:2:50, Coste:1, ID:3:39, MAC:39)
23. Switch 2:50 envía por el puerto 85 la BPDU (Raíz:2:50, Coste:0, ID:2:50, MAC:85)
24. Switch 2:50 envía por el puerto 50 la BPDU (Raíz:2:50, Coste:0, ID:2:50, MAC:50)
25. Switch 4:08 recibe por el puerto 08 la BPDU (Raíz:2:50, Coste:0, ID:2:50, MAC:50)
26. Switch 4:08 recibe por el puerto 89 la BPDU (Raíz:3:00, Coste:0, ID:3:00, MAC:57)
27. Switch 3:00 recibe por el puerto 57 la BPDU (Raíz:2:50, Coste:1, ID:4:08, MAC:89). La raíz 2:50 es mejor, así que se anota como nueva raíz.
28. Switch 3:00 recibe por el puerto 00 la BPDU (Raíz:2:50, Coste:1, ID:3:39, MAC:53). Llegó de nuevo la raíz 2:50 pero por un puerto con menor MAC (00), así que ese puerto se anota como posible puerto raíz
29. Switch 3:39 recibe por el puerto 53 la BPDU (Raíz:3:00, Coste:0, ID:3:00, MAC:00)
30. Switch 3:39 recibe por el puerto 39 la BPDU (Raíz:2:50, Coste:0, ID:2:50, MAC:85)
31. Switch 2:50 recibe por el puerto 85 la BPDU (Raíz:2:50, Coste:1, ID:3:39, MAC:39)
32. Switch 2:50 recibe por el puerto 50 la BPDU (Raíz:2:50, Coste:1, ID:4:08, MAC:08)
33. Switch 4:08 envía por el puerto 08 la BPDU (Raíz:2:50, Coste:1, ID:4:08, MAC:08)
34. Switch 4:08 envía por el puerto 89 la BPDU (Raíz:2:50, Coste:1, ID:4:08, MAC:89)
35. Switch 3:00 envía por el puerto 57 la BPDU (Raíz:2:50, Coste:2, ID:3:00, MAC:57)
36. Switch 3:00 envía por el puerto 00 la BPDU (Raíz:2:50, Coste:2, ID:3:00, MAC:00)
37. Switch 3:39 envía por el puerto 53 la BPDU (Raíz:2:50, Coste:1, ID:3:39, MAC:53)
38. Switch 3:39 envía por el puerto 39 la BPDU (Raíz:2:50, Coste:1, ID:3:39, MAC:39)
39. Switch 2:50 envía por el puerto 85 la BPDU (Raíz:2:50, Coste:0, ID:2:50, MAC:85)
40. Switch 2:50 envía por el puerto 50 la BPDU (Raíz:2:50, Coste:0, ID:2:50, MAC:50)
41. Switch 4:08 recibe por el puerto 08 la BPDU (Raíz:2:50, Coste:0, ID:2:50, MAC:50)
42. Switch 4:08 recibe por el puerto 89 la BPDU (Raíz:2:50, Coste:2, ID:3:00, MAC:57)
43. Switch 3:00 recibe por el puerto 57 la BPDU (Raíz:2:50, Coste:1, ID:4:08, MAC:89)
44. Switch 3:00 recibe por el puerto 00 la BPDU (Raíz:2:50, Coste:1, ID:3:39, MAC:53)
45. Switch 3:39 recibe por el puerto 53 la BPDU (Raíz:2:50, Coste:2, ID:3:00, MAC:00)
46. Switch 3:39 recibe por el puerto 39 la BPDU (Raíz:2:50, Coste:0, ID:2:50, MAC:85)
47. Switch 2:50 recibe por el puerto 85 la BPDU (Raíz:2:50, Coste:1, ID:3:39, MAC:39)
48. Switch 2:50 recibe por el puerto 50 la BPDU (Raíz:2:50, Coste:1, ID:4:08, MAC:08)



Una vez decidido el switch raíz, los switches toman las siguientes decisiones (volvemos a indicar la figura por comodidad):

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej7/ejercicio7.png




El switch 4:08 toma estas decisiones:

* El puerto con la MAC 08 se convierte en raíz. 
* El puerto con la MAC 89 se convierte en designado. Es el mejor del segmento con un coste de 1 frente un coste de 2 que ofrece el puerto 57.




El switch 3:00 toma estas decisiones:

* El puerto con la MAC 00 se convierte en raíz. 




El switch 3:39 toma estas decisiones:

* El puerto con la MAC 39 se convierte en raíz. 
* El puerto con la MAC 53 se convierte en designado. Es el mejor del segmento con un coste de 1 frente un coste de 2 que ofrece el puerto 00.




El switch 2:50 toma estas decisiones:

* 2:50 es raiz y pone todos sus puertos a designado.


        