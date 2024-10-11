
STP Ejercicio 19, dificultad 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Dada la red de switches que se muestra en la figura:

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej19/ejercicio19.png

Indicar el estado final en que quedarán todos los puertos de todos los switches.

Empezando por los eventos de envío, recepción y determinación de cual es el switch raíz la lista de sucesos sería esta:


1. Switch 2:23 envía por el puerto 23 la BPDU (Raíz:2:23, Coste:0, ID:2:23, MAC:23)
2. Switch 2:23 envía por el puerto 68 la BPDU (Raíz:2:23, Coste:0, ID:2:23, MAC:68)
3. Switch 1:08 envía por el puerto 08 la BPDU (Raíz:1:08, Coste:0, ID:1:08, MAC:08)
4. Switch 1:08 envía por el puerto 67 la BPDU (Raíz:1:08, Coste:0, ID:1:08, MAC:67)
5. Switch 6:11 envía por el puerto 34 la BPDU (Raíz:6:11, Coste:0, ID:6:11, MAC:34)
6. Switch 6:11 envía por el puerto 11 la BPDU (Raíz:6:11, Coste:0, ID:6:11, MAC:11)
7. Switch 6:55 envía por el puerto 77 la BPDU (Raíz:6:55, Coste:0, ID:6:55, MAC:77)
8. Switch 6:55 envía por el puerto 55 la BPDU (Raíz:6:55, Coste:0, ID:6:55, MAC:55)
9. Switch 2:23 recibe por el puerto 23 la BPDU (Raíz:6:55, Coste:0, ID:6:55, MAC:55)
10. Switch 2:23 recibe por el puerto 68 la BPDU (Raíz:1:08, Coste:0, ID:1:08, MAC:08). La raíz 1:08 es mejor, así que se anota como nueva raíz.
11. Switch 1:08 recibe por el puerto 08 la BPDU (Raíz:2:23, Coste:0, ID:2:23, MAC:68)
12. Switch 1:08 recibe por el puerto 67 la BPDU (Raíz:6:11, Coste:0, ID:6:11, MAC:34)
13. Switch 6:11 recibe por el puerto 34 la BPDU (Raíz:1:08, Coste:0, ID:1:08, MAC:67). La raíz 1:08 es mejor, así que se anota como nueva raíz.
14. Switch 6:11 recibe por el puerto 11 la BPDU (Raíz:6:55, Coste:0, ID:6:55, MAC:77)
15. Switch 6:55 recibe por el puerto 77 la BPDU (Raíz:6:11, Coste:0, ID:6:11, MAC:11). La raíz 6:11 es mejor, así que se anota como nueva raíz.
16. Switch 6:55 recibe por el puerto 55 la BPDU (Raíz:2:23, Coste:0, ID:2:23, MAC:23). La raíz 2:23 es mejor, así que se anota como nueva raíz.
17. Switch 2:23 envía por el puerto 23 la BPDU (Raíz:1:08, Coste:1, ID:2:23, MAC:23)
18. Switch 2:23 envía por el puerto 68 la BPDU (Raíz:1:08, Coste:1, ID:2:23, MAC:68)
19. Switch 1:08 envía por el puerto 08 la BPDU (Raíz:1:08, Coste:0, ID:1:08, MAC:08)
20. Switch 1:08 envía por el puerto 67 la BPDU (Raíz:1:08, Coste:0, ID:1:08, MAC:67)
21. Switch 6:11 envía por el puerto 34 la BPDU (Raíz:1:08, Coste:1, ID:6:11, MAC:34)
22. Switch 6:11 envía por el puerto 11 la BPDU (Raíz:1:08, Coste:1, ID:6:11, MAC:11)
23. Switch 6:55 envía por el puerto 77 la BPDU (Raíz:2:23, Coste:1, ID:6:55, MAC:77)
24. Switch 6:55 envía por el puerto 55 la BPDU (Raíz:2:23, Coste:1, ID:6:55, MAC:55)
25. Switch 2:23 recibe por el puerto 23 la BPDU (Raíz:2:23, Coste:1, ID:6:55, MAC:55)
26. Switch 2:23 recibe por el puerto 68 la BPDU (Raíz:1:08, Coste:0, ID:1:08, MAC:08)
27. Switch 1:08 recibe por el puerto 08 la BPDU (Raíz:1:08, Coste:1, ID:2:23, MAC:68)
28. Switch 1:08 recibe por el puerto 67 la BPDU (Raíz:1:08, Coste:1, ID:6:11, MAC:34)
29. Switch 6:11 recibe por el puerto 34 la BPDU (Raíz:1:08, Coste:0, ID:1:08, MAC:67)
30. Switch 6:11 recibe por el puerto 11 la BPDU (Raíz:2:23, Coste:1, ID:6:55, MAC:77)
31. Switch 6:55 recibe por el puerto 77 la BPDU (Raíz:1:08, Coste:1, ID:6:11, MAC:11). La raíz 1:08 es mejor, así que se anota como nueva raíz.
32. Switch 6:55 recibe por el puerto 55 la BPDU (Raíz:1:08, Coste:1, ID:2:23, MAC:23). Llegó de nuevo la raíz 1:08 pero por un puerto con menor MAC (55), así que ese puerto se anota como posible puerto raíz
33. Switch 2:23 envía por el puerto 23 la BPDU (Raíz:1:08, Coste:1, ID:2:23, MAC:23)
34. Switch 2:23 envía por el puerto 68 la BPDU (Raíz:1:08, Coste:1, ID:2:23, MAC:68)
35. Switch 1:08 envía por el puerto 08 la BPDU (Raíz:1:08, Coste:0, ID:1:08, MAC:08)
36. Switch 1:08 envía por el puerto 67 la BPDU (Raíz:1:08, Coste:0, ID:1:08, MAC:67)
37. Switch 6:11 envía por el puerto 34 la BPDU (Raíz:1:08, Coste:1, ID:6:11, MAC:34)
38. Switch 6:11 envía por el puerto 11 la BPDU (Raíz:1:08, Coste:1, ID:6:11, MAC:11)
39. Switch 6:55 envía por el puerto 77 la BPDU (Raíz:1:08, Coste:2, ID:6:55, MAC:77)
40. Switch 6:55 envía por el puerto 55 la BPDU (Raíz:1:08, Coste:2, ID:6:55, MAC:55)
41. Switch 2:23 recibe por el puerto 23 la BPDU (Raíz:1:08, Coste:2, ID:6:55, MAC:55)
42. Switch 2:23 recibe por el puerto 68 la BPDU (Raíz:1:08, Coste:0, ID:1:08, MAC:08)
43. Switch 1:08 recibe por el puerto 08 la BPDU (Raíz:1:08, Coste:1, ID:2:23, MAC:68)
44. Switch 1:08 recibe por el puerto 67 la BPDU (Raíz:1:08, Coste:1, ID:6:11, MAC:34)
45. Switch 6:11 recibe por el puerto 34 la BPDU (Raíz:1:08, Coste:0, ID:1:08, MAC:67)
46. Switch 6:11 recibe por el puerto 11 la BPDU (Raíz:1:08, Coste:2, ID:6:55, MAC:77)
47. Switch 6:55 recibe por el puerto 77 la BPDU (Raíz:1:08, Coste:1, ID:6:11, MAC:11)
48. Switch 6:55 recibe por el puerto 55 la BPDU (Raíz:1:08, Coste:1, ID:2:23, MAC:23)



Una vez decidido el switch raíz, los switches toman las siguientes decisiones (volvemos a indicar la figura por comodidad):

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej19/ejercicio19.png




El switch 2:23 toma estas decisiones:

* El puerto con la MAC 68 se convierte en raíz. 
* El puerto con la MAC 23 se convierte en designado. Es el mejor del segmento con un coste de 1 frente un coste de 2 que ofrece el puerto 55.




El switch 1:08 toma estas decisiones:

* 1:08 es raiz y pone todos sus puertos a designado.




El switch 6:11 toma estas decisiones:

* El puerto con la MAC 34 se convierte en raíz. 
* El puerto con la MAC 11 se convierte en designado. Es el mejor del segmento con un coste de 1 frente un coste de 2 que ofrece el puerto 77.




El switch 6:55 toma estas decisiones:

* El puerto con la MAC 55 se convierte en raíz. 


        