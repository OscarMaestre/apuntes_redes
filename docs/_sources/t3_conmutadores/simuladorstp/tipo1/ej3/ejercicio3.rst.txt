
STP Ejercicio 3, dificultad 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Dada la red de switches que se muestra en la figura:

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej3/ejercicio3.png

Indicar el estado final en que quedarán todos los puertos de todos los switches.

Empezando por los eventos de envío, recepción y determinación de cual es el switch raíz la lista de sucesos sería esta:


1. Switch 4:14 envía por el puerto 21 la BPDU (Raíz:4:14, Coste:0, ID:4:14, MAC:21)
2. Switch 4:14 envía por el puerto 14 la BPDU (Raíz:4:14, Coste:0, ID:4:14, MAC:14)
3. Switch 3:01 envía por el puerto 01 la BPDU (Raíz:3:01, Coste:0, ID:3:01, MAC:01)
4. Switch 3:01 envía por el puerto 55 la BPDU (Raíz:3:01, Coste:0, ID:3:01, MAC:55)
5. Switch 4:49 envía por el puerto 68 la BPDU (Raíz:4:49, Coste:0, ID:4:49, MAC:68)
6. Switch 4:49 envía por el puerto 49 la BPDU (Raíz:4:49, Coste:0, ID:4:49, MAC:49)
7. Switch 4:59 envía por el puerto 74 la BPDU (Raíz:4:59, Coste:0, ID:4:59, MAC:74)
8. Switch 4:59 envía por el puerto 59 la BPDU (Raíz:4:59, Coste:0, ID:4:59, MAC:59)
9. Switch 4:14 recibe por el puerto 21 la BPDU (Raíz:4:59, Coste:0, ID:4:59, MAC:59)
10. Switch 4:14 recibe por el puerto 14 la BPDU (Raíz:3:01, Coste:0, ID:3:01, MAC:01). La raíz 3:01 es mejor, así que se anota como nueva raíz.
11. Switch 3:01 recibe por el puerto 01 la BPDU (Raíz:4:14, Coste:0, ID:4:14, MAC:14)
12. Switch 3:01 recibe por el puerto 55 la BPDU (Raíz:4:49, Coste:0, ID:4:49, MAC:68)
13. Switch 4:49 recibe por el puerto 68 la BPDU (Raíz:3:01, Coste:0, ID:3:01, MAC:55). La raíz 3:01 es mejor, así que se anota como nueva raíz.
14. Switch 4:49 recibe por el puerto 49 la BPDU (Raíz:4:59, Coste:0, ID:4:59, MAC:74)
15. Switch 4:59 recibe por el puerto 74 la BPDU (Raíz:4:49, Coste:0, ID:4:49, MAC:49). La raíz 4:49 es mejor, así que se anota como nueva raíz.
16. Switch 4:59 recibe por el puerto 59 la BPDU (Raíz:4:14, Coste:0, ID:4:14, MAC:21). La raíz 4:14 es mejor, así que se anota como nueva raíz.
17. Switch 4:14 envía por el puerto 21 la BPDU (Raíz:3:01, Coste:1, ID:4:14, MAC:21)
18. Switch 4:14 envía por el puerto 14 la BPDU (Raíz:3:01, Coste:1, ID:4:14, MAC:14)
19. Switch 3:01 envía por el puerto 01 la BPDU (Raíz:3:01, Coste:0, ID:3:01, MAC:01)
20. Switch 3:01 envía por el puerto 55 la BPDU (Raíz:3:01, Coste:0, ID:3:01, MAC:55)
21. Switch 4:49 envía por el puerto 68 la BPDU (Raíz:3:01, Coste:1, ID:4:49, MAC:68)
22. Switch 4:49 envía por el puerto 49 la BPDU (Raíz:3:01, Coste:1, ID:4:49, MAC:49)
23. Switch 4:59 envía por el puerto 74 la BPDU (Raíz:4:14, Coste:1, ID:4:59, MAC:74)
24. Switch 4:59 envía por el puerto 59 la BPDU (Raíz:4:14, Coste:1, ID:4:59, MAC:59)
25. Switch 4:14 recibe por el puerto 21 la BPDU (Raíz:4:14, Coste:1, ID:4:59, MAC:59)
26. Switch 4:14 recibe por el puerto 14 la BPDU (Raíz:3:01, Coste:0, ID:3:01, MAC:01)
27. Switch 3:01 recibe por el puerto 01 la BPDU (Raíz:3:01, Coste:1, ID:4:14, MAC:14)
28. Switch 3:01 recibe por el puerto 55 la BPDU (Raíz:3:01, Coste:1, ID:4:49, MAC:68)
29. Switch 4:49 recibe por el puerto 68 la BPDU (Raíz:3:01, Coste:0, ID:3:01, MAC:55)
30. Switch 4:49 recibe por el puerto 49 la BPDU (Raíz:4:14, Coste:1, ID:4:59, MAC:74)
31. Switch 4:59 recibe por el puerto 74 la BPDU (Raíz:3:01, Coste:1, ID:4:49, MAC:49). La raíz 3:01 es mejor, así que se anota como nueva raíz.
32. Switch 4:59 recibe por el puerto 59 la BPDU (Raíz:3:01, Coste:1, ID:4:14, MAC:21). Llegó de nuevo la raíz 3:01 pero por un puerto con menor MAC (59), así que ese puerto se anota como posible puerto raíz
33. Switch 4:14 envía por el puerto 21 la BPDU (Raíz:3:01, Coste:1, ID:4:14, MAC:21)
34. Switch 4:14 envía por el puerto 14 la BPDU (Raíz:3:01, Coste:1, ID:4:14, MAC:14)
35. Switch 3:01 envía por el puerto 01 la BPDU (Raíz:3:01, Coste:0, ID:3:01, MAC:01)
36. Switch 3:01 envía por el puerto 55 la BPDU (Raíz:3:01, Coste:0, ID:3:01, MAC:55)
37. Switch 4:49 envía por el puerto 68 la BPDU (Raíz:3:01, Coste:1, ID:4:49, MAC:68)
38. Switch 4:49 envía por el puerto 49 la BPDU (Raíz:3:01, Coste:1, ID:4:49, MAC:49)
39. Switch 4:59 envía por el puerto 74 la BPDU (Raíz:3:01, Coste:2, ID:4:59, MAC:74)
40. Switch 4:59 envía por el puerto 59 la BPDU (Raíz:3:01, Coste:2, ID:4:59, MAC:59)
41. Switch 4:14 recibe por el puerto 21 la BPDU (Raíz:3:01, Coste:2, ID:4:59, MAC:59)
42. Switch 4:14 recibe por el puerto 14 la BPDU (Raíz:3:01, Coste:0, ID:3:01, MAC:01)
43. Switch 3:01 recibe por el puerto 01 la BPDU (Raíz:3:01, Coste:1, ID:4:14, MAC:14)
44. Switch 3:01 recibe por el puerto 55 la BPDU (Raíz:3:01, Coste:1, ID:4:49, MAC:68)
45. Switch 4:49 recibe por el puerto 68 la BPDU (Raíz:3:01, Coste:0, ID:3:01, MAC:55)
46. Switch 4:49 recibe por el puerto 49 la BPDU (Raíz:3:01, Coste:2, ID:4:59, MAC:74)
47. Switch 4:59 recibe por el puerto 74 la BPDU (Raíz:3:01, Coste:1, ID:4:49, MAC:49)
48. Switch 4:59 recibe por el puerto 59 la BPDU (Raíz:3:01, Coste:1, ID:4:14, MAC:21)



Una vez decidido el switch raíz, los switches toman las siguientes decisiones (volvemos a indicar la figura por comodidad):

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej3/ejercicio3.png




El switch 4:14 toma estas decisiones:

* El puerto con la MAC 14 se convierte en raíz. 
* El puerto con la MAC 21 se convierte en designado. Es el mejor del segmento con un coste de 1 frente un coste de 2 que ofrece el puerto 59.




El switch 3:01 toma estas decisiones:

* 3:01 es raiz y pone todos sus puertos a designado.




El switch 4:49 toma estas decisiones:

* El puerto con la MAC 68 se convierte en raíz. 
* El puerto con la MAC 49 se convierte en designado. Es el mejor del segmento con un coste de 1 frente un coste de 2 que ofrece el puerto 74.




El switch 4:59 toma estas decisiones:

* El puerto con la MAC 59 se convierte en raíz. 


        