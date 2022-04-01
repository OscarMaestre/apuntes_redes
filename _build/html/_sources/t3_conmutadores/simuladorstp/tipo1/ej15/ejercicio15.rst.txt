
STP Ejercicio 15, dificultad 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Dada la red de switches que se muestra en la figura:

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej15/ejercicio15.png

Indicar el estado final en que quedarán todos los puertos de todos los switches.

Empezando por los eventos de envío, recepción y determinación de cual es el switch raíz la lista de sucesos sería esta:


1. Switch 2:11 envía por el puerto 26 la BPDU (Raíz:2:11, Coste:0, ID:2:11, MAC:26)
2. Switch 2:11 envía por el puerto 11 la BPDU (Raíz:2:11, Coste:0, ID:2:11, MAC:11)
3. Switch 3:55 envía por el puerto 55 la BPDU (Raíz:3:55, Coste:0, ID:3:55, MAC:55)
4. Switch 3:55 envía por el puerto 71 la BPDU (Raíz:3:55, Coste:0, ID:3:55, MAC:71)
5. Switch 6:32 envía por el puerto 32 la BPDU (Raíz:6:32, Coste:0, ID:6:32, MAC:32)
6. Switch 6:32 envía por el puerto 98 la BPDU (Raíz:6:32, Coste:0, ID:6:32, MAC:98)
7. Switch 3:09 envía por el puerto 16 la BPDU (Raíz:3:09, Coste:0, ID:3:09, MAC:16)
8. Switch 3:09 envía por el puerto 09 la BPDU (Raíz:3:09, Coste:0, ID:3:09, MAC:09)
9. Switch 2:11 recibe por el puerto 26 la BPDU (Raíz:3:09, Coste:0, ID:3:09, MAC:09)
10. Switch 2:11 recibe por el puerto 11 la BPDU (Raíz:3:55, Coste:0, ID:3:55, MAC:55)
11. Switch 3:55 recibe por el puerto 55 la BPDU (Raíz:2:11, Coste:0, ID:2:11, MAC:11). La raíz 2:11 es mejor, así que se anota como nueva raíz.
12. Switch 3:55 recibe por el puerto 71 la BPDU (Raíz:6:32, Coste:0, ID:6:32, MAC:32)
13. Switch 6:32 recibe por el puerto 32 la BPDU (Raíz:3:55, Coste:0, ID:3:55, MAC:71). La raíz 3:55 es mejor, así que se anota como nueva raíz.
14. Switch 6:32 recibe por el puerto 98 la BPDU (Raíz:3:09, Coste:0, ID:3:09, MAC:16). La raíz 3:09 es mejor, así que se anota como nueva raíz.
15. Switch 3:09 recibe por el puerto 16 la BPDU (Raíz:6:32, Coste:0, ID:6:32, MAC:98)
16. Switch 3:09 recibe por el puerto 09 la BPDU (Raíz:2:11, Coste:0, ID:2:11, MAC:26). La raíz 2:11 es mejor, así que se anota como nueva raíz.
17. Switch 2:11 envía por el puerto 26 la BPDU (Raíz:2:11, Coste:0, ID:2:11, MAC:26)
18. Switch 2:11 envía por el puerto 11 la BPDU (Raíz:2:11, Coste:0, ID:2:11, MAC:11)
19. Switch 3:55 envía por el puerto 55 la BPDU (Raíz:2:11, Coste:1, ID:3:55, MAC:55)
20. Switch 3:55 envía por el puerto 71 la BPDU (Raíz:2:11, Coste:1, ID:3:55, MAC:71)
21. Switch 6:32 envía por el puerto 32 la BPDU (Raíz:3:09, Coste:1, ID:6:32, MAC:32)
22. Switch 6:32 envía por el puerto 98 la BPDU (Raíz:3:09, Coste:1, ID:6:32, MAC:98)
23. Switch 3:09 envía por el puerto 16 la BPDU (Raíz:2:11, Coste:1, ID:3:09, MAC:16)
24. Switch 3:09 envía por el puerto 09 la BPDU (Raíz:2:11, Coste:1, ID:3:09, MAC:09)
25. Switch 2:11 recibe por el puerto 26 la BPDU (Raíz:2:11, Coste:1, ID:3:09, MAC:09)
26. Switch 2:11 recibe por el puerto 11 la BPDU (Raíz:2:11, Coste:1, ID:3:55, MAC:55)
27. Switch 3:55 recibe por el puerto 55 la BPDU (Raíz:2:11, Coste:0, ID:2:11, MAC:11)
28. Switch 3:55 recibe por el puerto 71 la BPDU (Raíz:3:09, Coste:1, ID:6:32, MAC:32)
29. Switch 6:32 recibe por el puerto 32 la BPDU (Raíz:2:11, Coste:1, ID:3:55, MAC:71). La raíz 2:11 es mejor, así que se anota como nueva raíz.
30. Switch 6:32 recibe por el puerto 98 la BPDU (Raíz:2:11, Coste:1, ID:3:09, MAC:16)
31. Switch 3:09 recibe por el puerto 16 la BPDU (Raíz:3:09, Coste:1, ID:6:32, MAC:98)
32. Switch 3:09 recibe por el puerto 09 la BPDU (Raíz:2:11, Coste:0, ID:2:11, MAC:26)
33. Switch 2:11 envía por el puerto 26 la BPDU (Raíz:2:11, Coste:0, ID:2:11, MAC:26)
34. Switch 2:11 envía por el puerto 11 la BPDU (Raíz:2:11, Coste:0, ID:2:11, MAC:11)
35. Switch 3:55 envía por el puerto 55 la BPDU (Raíz:2:11, Coste:1, ID:3:55, MAC:55)
36. Switch 3:55 envía por el puerto 71 la BPDU (Raíz:2:11, Coste:1, ID:3:55, MAC:71)
37. Switch 6:32 envía por el puerto 32 la BPDU (Raíz:2:11, Coste:2, ID:6:32, MAC:32)
38. Switch 6:32 envía por el puerto 98 la BPDU (Raíz:2:11, Coste:2, ID:6:32, MAC:98)
39. Switch 3:09 envía por el puerto 16 la BPDU (Raíz:2:11, Coste:1, ID:3:09, MAC:16)
40. Switch 3:09 envía por el puerto 09 la BPDU (Raíz:2:11, Coste:1, ID:3:09, MAC:09)
41. Switch 2:11 recibe por el puerto 26 la BPDU (Raíz:2:11, Coste:1, ID:3:09, MAC:09)
42. Switch 2:11 recibe por el puerto 11 la BPDU (Raíz:2:11, Coste:1, ID:3:55, MAC:55)
43. Switch 3:55 recibe por el puerto 55 la BPDU (Raíz:2:11, Coste:0, ID:2:11, MAC:11)
44. Switch 3:55 recibe por el puerto 71 la BPDU (Raíz:2:11, Coste:2, ID:6:32, MAC:32)
45. Switch 6:32 recibe por el puerto 32 la BPDU (Raíz:2:11, Coste:1, ID:3:55, MAC:71)
46. Switch 6:32 recibe por el puerto 98 la BPDU (Raíz:2:11, Coste:1, ID:3:09, MAC:16)
47. Switch 3:09 recibe por el puerto 16 la BPDU (Raíz:2:11, Coste:2, ID:6:32, MAC:98)
48. Switch 3:09 recibe por el puerto 09 la BPDU (Raíz:2:11, Coste:0, ID:2:11, MAC:26)



Una vez decidido el switch raíz, los switches toman las siguientes decisiones (volvemos a indicar la figura por comodidad):

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej15/ejercicio15.png




El switch 2:11 toma estas decisiones:

* 2:11 es raiz y pone todos sus puertos a designado.




El switch 3:55 toma estas decisiones:

* El puerto con la MAC 55 se convierte en raíz. 
* El puerto con la MAC 71 se convierte en designado. Es el mejor del segmento con un coste de 1 frente un coste de 2 que ofrece el puerto 32.




El switch 6:32 toma estas decisiones:

* El puerto con la MAC 32 se convierte en raíz. 




El switch 3:09 toma estas decisiones:

* El puerto con la MAC 09 se convierte en raíz. 
* El puerto con la MAC 16 se convierte en designado. Es el mejor del segmento con un coste de 1 frente un coste de 2 que ofrece el puerto 98.


        