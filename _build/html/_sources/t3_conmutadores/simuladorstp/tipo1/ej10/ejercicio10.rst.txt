
STP Ejercicio 10, dificultad 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Dada la red de switches que se muestra en la figura:

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej10/ejercicio10.png

Indicar el estado final en que quedarán todos los puertos de todos los switches.

Empezando por los eventos de envío, recepción y determinación de cual es el switch raíz la lista de sucesos sería esta:


1. Switch 6:49 envía por el puerto 49 la BPDU (Raíz:6:49, Coste:0, ID:6:49, MAC:49)
2. Switch 6:49 envía por el puerto 91 la BPDU (Raíz:6:49, Coste:0, ID:6:49, MAC:91)
3. Switch 4:04 envía por el puerto 27 la BPDU (Raíz:4:04, Coste:0, ID:4:04, MAC:27)
4. Switch 4:04 envía por el puerto 04 la BPDU (Raíz:4:04, Coste:0, ID:4:04, MAC:04)
5. Switch 5:88 envía por el puerto 88 la BPDU (Raíz:5:88, Coste:0, ID:5:88, MAC:88)
6. Switch 5:88 envía por el puerto 98 la BPDU (Raíz:5:88, Coste:0, ID:5:88, MAC:98)
7. Switch 2:29 envía por el puerto 65 la BPDU (Raíz:2:29, Coste:0, ID:2:29, MAC:65)
8. Switch 2:29 envía por el puerto 29 la BPDU (Raíz:2:29, Coste:0, ID:2:29, MAC:29)
9. Switch 6:49 recibe por el puerto 49 la BPDU (Raíz:2:29, Coste:0, ID:2:29, MAC:29). La raíz 2:29 es mejor, así que se anota como nueva raíz.
10. Switch 6:49 recibe por el puerto 91 la BPDU (Raíz:4:04, Coste:0, ID:4:04, MAC:27)
11. Switch 4:04 recibe por el puerto 27 la BPDU (Raíz:6:49, Coste:0, ID:6:49, MAC:91)
12. Switch 4:04 recibe por el puerto 04 la BPDU (Raíz:5:88, Coste:0, ID:5:88, MAC:88)
13. Switch 5:88 recibe por el puerto 88 la BPDU (Raíz:4:04, Coste:0, ID:4:04, MAC:04). La raíz 4:04 es mejor, así que se anota como nueva raíz.
14. Switch 5:88 recibe por el puerto 98 la BPDU (Raíz:2:29, Coste:0, ID:2:29, MAC:65). La raíz 2:29 es mejor, así que se anota como nueva raíz.
15. Switch 2:29 recibe por el puerto 65 la BPDU (Raíz:5:88, Coste:0, ID:5:88, MAC:98)
16. Switch 2:29 recibe por el puerto 29 la BPDU (Raíz:6:49, Coste:0, ID:6:49, MAC:49)
17. Switch 6:49 envía por el puerto 49 la BPDU (Raíz:2:29, Coste:1, ID:6:49, MAC:49)
18. Switch 6:49 envía por el puerto 91 la BPDU (Raíz:2:29, Coste:1, ID:6:49, MAC:91)
19. Switch 4:04 envía por el puerto 27 la BPDU (Raíz:4:04, Coste:0, ID:4:04, MAC:27)
20. Switch 4:04 envía por el puerto 04 la BPDU (Raíz:4:04, Coste:0, ID:4:04, MAC:04)
21. Switch 5:88 envía por el puerto 88 la BPDU (Raíz:2:29, Coste:1, ID:5:88, MAC:88)
22. Switch 5:88 envía por el puerto 98 la BPDU (Raíz:2:29, Coste:1, ID:5:88, MAC:98)
23. Switch 2:29 envía por el puerto 65 la BPDU (Raíz:2:29, Coste:0, ID:2:29, MAC:65)
24. Switch 2:29 envía por el puerto 29 la BPDU (Raíz:2:29, Coste:0, ID:2:29, MAC:29)
25. Switch 6:49 recibe por el puerto 49 la BPDU (Raíz:2:29, Coste:0, ID:2:29, MAC:29)
26. Switch 6:49 recibe por el puerto 91 la BPDU (Raíz:4:04, Coste:0, ID:4:04, MAC:27)
27. Switch 4:04 recibe por el puerto 27 la BPDU (Raíz:2:29, Coste:1, ID:6:49, MAC:91). La raíz 2:29 es mejor, así que se anota como nueva raíz.
28. Switch 4:04 recibe por el puerto 04 la BPDU (Raíz:2:29, Coste:1, ID:5:88, MAC:88). Llegó de nuevo la raíz 2:29 pero por un puerto con menor MAC (04), así que ese puerto se anota como posible puerto raíz
29. Switch 5:88 recibe por el puerto 88 la BPDU (Raíz:4:04, Coste:0, ID:4:04, MAC:04)
30. Switch 5:88 recibe por el puerto 98 la BPDU (Raíz:2:29, Coste:0, ID:2:29, MAC:65)
31. Switch 2:29 recibe por el puerto 65 la BPDU (Raíz:2:29, Coste:1, ID:5:88, MAC:98)
32. Switch 2:29 recibe por el puerto 29 la BPDU (Raíz:2:29, Coste:1, ID:6:49, MAC:49)
33. Switch 6:49 envía por el puerto 49 la BPDU (Raíz:2:29, Coste:1, ID:6:49, MAC:49)
34. Switch 6:49 envía por el puerto 91 la BPDU (Raíz:2:29, Coste:1, ID:6:49, MAC:91)
35. Switch 4:04 envía por el puerto 27 la BPDU (Raíz:2:29, Coste:2, ID:4:04, MAC:27)
36. Switch 4:04 envía por el puerto 04 la BPDU (Raíz:2:29, Coste:2, ID:4:04, MAC:04)
37. Switch 5:88 envía por el puerto 88 la BPDU (Raíz:2:29, Coste:1, ID:5:88, MAC:88)
38. Switch 5:88 envía por el puerto 98 la BPDU (Raíz:2:29, Coste:1, ID:5:88, MAC:98)
39. Switch 2:29 envía por el puerto 65 la BPDU (Raíz:2:29, Coste:0, ID:2:29, MAC:65)
40. Switch 2:29 envía por el puerto 29 la BPDU (Raíz:2:29, Coste:0, ID:2:29, MAC:29)
41. Switch 6:49 recibe por el puerto 49 la BPDU (Raíz:2:29, Coste:0, ID:2:29, MAC:29)
42. Switch 6:49 recibe por el puerto 91 la BPDU (Raíz:2:29, Coste:2, ID:4:04, MAC:27)
43. Switch 4:04 recibe por el puerto 27 la BPDU (Raíz:2:29, Coste:1, ID:6:49, MAC:91)
44. Switch 4:04 recibe por el puerto 04 la BPDU (Raíz:2:29, Coste:1, ID:5:88, MAC:88)
45. Switch 5:88 recibe por el puerto 88 la BPDU (Raíz:2:29, Coste:2, ID:4:04, MAC:04)
46. Switch 5:88 recibe por el puerto 98 la BPDU (Raíz:2:29, Coste:0, ID:2:29, MAC:65)
47. Switch 2:29 recibe por el puerto 65 la BPDU (Raíz:2:29, Coste:1, ID:5:88, MAC:98)
48. Switch 2:29 recibe por el puerto 29 la BPDU (Raíz:2:29, Coste:1, ID:6:49, MAC:49)



Una vez decidido el switch raíz, los switches toman las siguientes decisiones (volvemos a indicar la figura por comodidad):

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej10/ejercicio10.png




El switch 6:49 toma estas decisiones:

* El puerto con la MAC 49 se convierte en raíz. 
* El puerto con la MAC 91 se convierte en designado. Es el mejor del segmento con un coste de 1 frente un coste de 2 que ofrece el puerto 27.




El switch 4:04 toma estas decisiones:

* El puerto con la MAC 04 se convierte en raíz. 




El switch 5:88 toma estas decisiones:

* El puerto con la MAC 98 se convierte en raíz. 
* El puerto con la MAC 88 se convierte en designado. Es el mejor del segmento con un coste de 1 frente un coste de 2 que ofrece el puerto 04.




El switch 2:29 toma estas decisiones:

* 2:29 es raiz y pone todos sus puertos a designado.


        