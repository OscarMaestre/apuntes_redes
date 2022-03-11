
STP Ejercicio 11, dificultad 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Dada la red de switches que se muestra en la figura:

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej11/ejercicio11.png

Indicar el estado final en que quedarán todos los puertos de todos los switches.

Empezando por los eventos de envío, recepción y determinación de cual es el switch raíz la lista de sucesos sería esta:


1. Switch 3:86 envía por el puerto 94 la BPDU (Raíz:3:86, Coste:0, ID:3:86, MAC:94)
2. Switch 3:86 envía por el puerto 86 la BPDU (Raíz:3:86, Coste:0, ID:3:86, MAC:86)
3. Switch 4:02 envía por el puerto 39 la BPDU (Raíz:4:02, Coste:0, ID:4:02, MAC:39)
4. Switch 4:02 envía por el puerto 02 la BPDU (Raíz:4:02, Coste:0, ID:4:02, MAC:02)
5. Switch 2:92 envía por el puerto 92 la BPDU (Raíz:2:92, Coste:0, ID:2:92, MAC:92)
6. Switch 2:92 envía por el puerto 97 la BPDU (Raíz:2:92, Coste:0, ID:2:92, MAC:97)
7. Switch 4:21 envía por el puerto 36 la BPDU (Raíz:4:21, Coste:0, ID:4:21, MAC:36)
8. Switch 4:21 envía por el puerto 21 la BPDU (Raíz:4:21, Coste:0, ID:4:21, MAC:21)
9. Switch 3:86 recibe por el puerto 94 la BPDU (Raíz:4:21, Coste:0, ID:4:21, MAC:21)
10. Switch 3:86 recibe por el puerto 86 la BPDU (Raíz:4:02, Coste:0, ID:4:02, MAC:39)
11. Switch 4:02 recibe por el puerto 39 la BPDU (Raíz:3:86, Coste:0, ID:3:86, MAC:86). La raíz 3:86 es mejor, así que se anota como nueva raíz.
12. Switch 4:02 recibe por el puerto 02 la BPDU (Raíz:2:92, Coste:0, ID:2:92, MAC:92). La raíz 2:92 es mejor, así que se anota como nueva raíz.
13. Switch 2:92 recibe por el puerto 92 la BPDU (Raíz:4:02, Coste:0, ID:4:02, MAC:02)
14. Switch 2:92 recibe por el puerto 97 la BPDU (Raíz:4:21, Coste:0, ID:4:21, MAC:36)
15. Switch 4:21 recibe por el puerto 36 la BPDU (Raíz:2:92, Coste:0, ID:2:92, MAC:97). La raíz 2:92 es mejor, así que se anota como nueva raíz.
16. Switch 4:21 recibe por el puerto 21 la BPDU (Raíz:3:86, Coste:0, ID:3:86, MAC:94)
17. Switch 3:86 envía por el puerto 94 la BPDU (Raíz:3:86, Coste:0, ID:3:86, MAC:94)
18. Switch 3:86 envía por el puerto 86 la BPDU (Raíz:3:86, Coste:0, ID:3:86, MAC:86)
19. Switch 4:02 envía por el puerto 39 la BPDU (Raíz:2:92, Coste:1, ID:4:02, MAC:39)
20. Switch 4:02 envía por el puerto 02 la BPDU (Raíz:2:92, Coste:1, ID:4:02, MAC:02)
21. Switch 2:92 envía por el puerto 92 la BPDU (Raíz:2:92, Coste:0, ID:2:92, MAC:92)
22. Switch 2:92 envía por el puerto 97 la BPDU (Raíz:2:92, Coste:0, ID:2:92, MAC:97)
23. Switch 4:21 envía por el puerto 36 la BPDU (Raíz:2:92, Coste:1, ID:4:21, MAC:36)
24. Switch 4:21 envía por el puerto 21 la BPDU (Raíz:2:92, Coste:1, ID:4:21, MAC:21)
25. Switch 3:86 recibe por el puerto 94 la BPDU (Raíz:2:92, Coste:1, ID:4:21, MAC:21). La raíz 2:92 es mejor, así que se anota como nueva raíz.
26. Switch 3:86 recibe por el puerto 86 la BPDU (Raíz:2:92, Coste:1, ID:4:02, MAC:39). Llegó de nuevo la raíz 2:92 pero por un puerto con menor MAC (86), así que ese puerto se anota como posible puerto raíz
27. Switch 4:02 recibe por el puerto 39 la BPDU (Raíz:3:86, Coste:0, ID:3:86, MAC:86)
28. Switch 4:02 recibe por el puerto 02 la BPDU (Raíz:2:92, Coste:0, ID:2:92, MAC:92)
29. Switch 2:92 recibe por el puerto 92 la BPDU (Raíz:2:92, Coste:1, ID:4:02, MAC:02)
30. Switch 2:92 recibe por el puerto 97 la BPDU (Raíz:2:92, Coste:1, ID:4:21, MAC:36)
31. Switch 4:21 recibe por el puerto 36 la BPDU (Raíz:2:92, Coste:0, ID:2:92, MAC:97)
32. Switch 4:21 recibe por el puerto 21 la BPDU (Raíz:3:86, Coste:0, ID:3:86, MAC:94)
33. Switch 3:86 envía por el puerto 94 la BPDU (Raíz:2:92, Coste:2, ID:3:86, MAC:94)
34. Switch 3:86 envía por el puerto 86 la BPDU (Raíz:2:92, Coste:2, ID:3:86, MAC:86)
35. Switch 4:02 envía por el puerto 39 la BPDU (Raíz:2:92, Coste:1, ID:4:02, MAC:39)
36. Switch 4:02 envía por el puerto 02 la BPDU (Raíz:2:92, Coste:1, ID:4:02, MAC:02)
37. Switch 2:92 envía por el puerto 92 la BPDU (Raíz:2:92, Coste:0, ID:2:92, MAC:92)
38. Switch 2:92 envía por el puerto 97 la BPDU (Raíz:2:92, Coste:0, ID:2:92, MAC:97)
39. Switch 4:21 envía por el puerto 36 la BPDU (Raíz:2:92, Coste:1, ID:4:21, MAC:36)
40. Switch 4:21 envía por el puerto 21 la BPDU (Raíz:2:92, Coste:1, ID:4:21, MAC:21)
41. Switch 3:86 recibe por el puerto 94 la BPDU (Raíz:2:92, Coste:1, ID:4:21, MAC:21)
42. Switch 3:86 recibe por el puerto 86 la BPDU (Raíz:2:92, Coste:1, ID:4:02, MAC:39)
43. Switch 4:02 recibe por el puerto 39 la BPDU (Raíz:2:92, Coste:2, ID:3:86, MAC:86)
44. Switch 4:02 recibe por el puerto 02 la BPDU (Raíz:2:92, Coste:0, ID:2:92, MAC:92)
45. Switch 2:92 recibe por el puerto 92 la BPDU (Raíz:2:92, Coste:1, ID:4:02, MAC:02)
46. Switch 2:92 recibe por el puerto 97 la BPDU (Raíz:2:92, Coste:1, ID:4:21, MAC:36)
47. Switch 4:21 recibe por el puerto 36 la BPDU (Raíz:2:92, Coste:0, ID:2:92, MAC:97)
48. Switch 4:21 recibe por el puerto 21 la BPDU (Raíz:2:92, Coste:2, ID:3:86, MAC:94)



Una vez decidido el switch raíz, los switches toman las siguientes decisiones (volvemos a indicar la figura por comodidad):

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej11/ejercicio11.png




El switch 3:86 toma estas decisiones:

* El puerto con la MAC 86 se convierte en raíz. 




El switch 4:02 toma estas decisiones:

* El puerto con la MAC 02 se convierte en raíz. 
* El puerto con la MAC 39 se convierte en designado. Es el mejor del segmento con un coste de 1 frente un coste de 2 que ofrece el puerto 86.




El switch 2:92 toma estas decisiones:

* 2:92 es raiz y pone todos sus puertos a designado.




El switch 4:21 toma estas decisiones:

* El puerto con la MAC 36 se convierte en raíz. 
* El puerto con la MAC 21 se convierte en designado. Es el mejor del segmento con un coste de 1 frente un coste de 2 que ofrece el puerto 94.


        