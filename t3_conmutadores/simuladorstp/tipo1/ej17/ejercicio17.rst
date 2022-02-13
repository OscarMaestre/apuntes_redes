
STP Ejercicio 17, dificultad 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Dada la red de switches que se muestra en la figura:

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej17/ejercicio17.png

Indicar el estado final en que quedarán todos los puertos de todos los switches.

Empezando por los eventos de envío, recepción y determinación de cual es el switch raíz la lista de sucesos sería esta:


1. Switch 5:11 envía por el puerto 11 la BPDU (Raíz:5:11, Coste:0, ID:5:11, MAC:11)
2. Switch 5:11 envía por el puerto 43 la BPDU (Raíz:5:11, Coste:0, ID:5:11, MAC:43)
3. Switch 5:24 envía por el puerto 80 la BPDU (Raíz:5:24, Coste:0, ID:5:24, MAC:80)
4. Switch 5:24 envía por el puerto 24 la BPDU (Raíz:5:24, Coste:0, ID:5:24, MAC:24)
5. Switch 3:13 envía por el puerto 89 la BPDU (Raíz:3:13, Coste:0, ID:3:13, MAC:89)
6. Switch 3:13 envía por el puerto 13 la BPDU (Raíz:3:13, Coste:0, ID:3:13, MAC:13)
7. Switch 4:71 envía por el puerto 71 la BPDU (Raíz:4:71, Coste:0, ID:4:71, MAC:71)
8. Switch 4:71 envía por el puerto 88 la BPDU (Raíz:4:71, Coste:0, ID:4:71, MAC:88)
9. Switch 5:11 recibe por el puerto 11 la BPDU (Raíz:4:71, Coste:0, ID:4:71, MAC:88). La raíz 4:71 es mejor, así que se anota como nueva raíz.
10. Switch 5:11 recibe por el puerto 43 la BPDU (Raíz:5:24, Coste:0, ID:5:24, MAC:80)
11. Switch 5:24 recibe por el puerto 80 la BPDU (Raíz:5:11, Coste:0, ID:5:11, MAC:43). La raíz 5:11 es mejor, así que se anota como nueva raíz.
12. Switch 5:24 recibe por el puerto 24 la BPDU (Raíz:3:13, Coste:0, ID:3:13, MAC:89). La raíz 3:13 es mejor, así que se anota como nueva raíz.
13. Switch 3:13 recibe por el puerto 89 la BPDU (Raíz:5:24, Coste:0, ID:5:24, MAC:24)
14. Switch 3:13 recibe por el puerto 13 la BPDU (Raíz:4:71, Coste:0, ID:4:71, MAC:71)
15. Switch 4:71 recibe por el puerto 71 la BPDU (Raíz:3:13, Coste:0, ID:3:13, MAC:13). La raíz 3:13 es mejor, así que se anota como nueva raíz.
16. Switch 4:71 recibe por el puerto 88 la BPDU (Raíz:5:11, Coste:0, ID:5:11, MAC:11)
17. Switch 5:11 envía por el puerto 11 la BPDU (Raíz:4:71, Coste:1, ID:5:11, MAC:11)
18. Switch 5:11 envía por el puerto 43 la BPDU (Raíz:4:71, Coste:1, ID:5:11, MAC:43)
19. Switch 5:24 envía por el puerto 80 la BPDU (Raíz:3:13, Coste:1, ID:5:24, MAC:80)
20. Switch 5:24 envía por el puerto 24 la BPDU (Raíz:3:13, Coste:1, ID:5:24, MAC:24)
21. Switch 3:13 envía por el puerto 89 la BPDU (Raíz:3:13, Coste:0, ID:3:13, MAC:89)
22. Switch 3:13 envía por el puerto 13 la BPDU (Raíz:3:13, Coste:0, ID:3:13, MAC:13)
23. Switch 4:71 envía por el puerto 71 la BPDU (Raíz:3:13, Coste:1, ID:4:71, MAC:71)
24. Switch 4:71 envía por el puerto 88 la BPDU (Raíz:3:13, Coste:1, ID:4:71, MAC:88)
25. Switch 5:11 recibe por el puerto 11 la BPDU (Raíz:3:13, Coste:1, ID:4:71, MAC:88). La raíz 3:13 es mejor, así que se anota como nueva raíz.
26. Switch 5:11 recibe por el puerto 43 la BPDU (Raíz:3:13, Coste:1, ID:5:24, MAC:80)
27. Switch 5:24 recibe por el puerto 80 la BPDU (Raíz:4:71, Coste:1, ID:5:11, MAC:43)
28. Switch 5:24 recibe por el puerto 24 la BPDU (Raíz:3:13, Coste:0, ID:3:13, MAC:89)
29. Switch 3:13 recibe por el puerto 89 la BPDU (Raíz:3:13, Coste:1, ID:5:24, MAC:24)
30. Switch 3:13 recibe por el puerto 13 la BPDU (Raíz:3:13, Coste:1, ID:4:71, MAC:71)
31. Switch 4:71 recibe por el puerto 71 la BPDU (Raíz:3:13, Coste:0, ID:3:13, MAC:13)
32. Switch 4:71 recibe por el puerto 88 la BPDU (Raíz:4:71, Coste:1, ID:5:11, MAC:11)
33. Switch 5:11 envía por el puerto 11 la BPDU (Raíz:3:13, Coste:2, ID:5:11, MAC:11)
34. Switch 5:11 envía por el puerto 43 la BPDU (Raíz:3:13, Coste:2, ID:5:11, MAC:43)
35. Switch 5:24 envía por el puerto 80 la BPDU (Raíz:3:13, Coste:1, ID:5:24, MAC:80)
36. Switch 5:24 envía por el puerto 24 la BPDU (Raíz:3:13, Coste:1, ID:5:24, MAC:24)
37. Switch 3:13 envía por el puerto 89 la BPDU (Raíz:3:13, Coste:0, ID:3:13, MAC:89)
38. Switch 3:13 envía por el puerto 13 la BPDU (Raíz:3:13, Coste:0, ID:3:13, MAC:13)
39. Switch 4:71 envía por el puerto 71 la BPDU (Raíz:3:13, Coste:1, ID:4:71, MAC:71)
40. Switch 4:71 envía por el puerto 88 la BPDU (Raíz:3:13, Coste:1, ID:4:71, MAC:88)
41. Switch 5:11 recibe por el puerto 11 la BPDU (Raíz:3:13, Coste:1, ID:4:71, MAC:88)
42. Switch 5:11 recibe por el puerto 43 la BPDU (Raíz:3:13, Coste:1, ID:5:24, MAC:80)
43. Switch 5:24 recibe por el puerto 80 la BPDU (Raíz:3:13, Coste:2, ID:5:11, MAC:43)
44. Switch 5:24 recibe por el puerto 24 la BPDU (Raíz:3:13, Coste:0, ID:3:13, MAC:89)
45. Switch 3:13 recibe por el puerto 89 la BPDU (Raíz:3:13, Coste:1, ID:5:24, MAC:24)
46. Switch 3:13 recibe por el puerto 13 la BPDU (Raíz:3:13, Coste:1, ID:4:71, MAC:71)
47. Switch 4:71 recibe por el puerto 71 la BPDU (Raíz:3:13, Coste:0, ID:3:13, MAC:13)
48. Switch 4:71 recibe por el puerto 88 la BPDU (Raíz:3:13, Coste:2, ID:5:11, MAC:11)



Una vez decidido el switch raíz, los switches toman las siguientes decisiones (volvemos a indicar la figura por comodidad):

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej17/ejercicio17.png




El switch 5:11 toma estas decisiones:

* El puerto con la MAC 11 se convierte en raíz. 




El switch 5:24 toma estas decisiones:

* El puerto con la MAC 24 se convierte en raíz. 
* El puerto con la MAC 80 se convierte en designado. Es el mejor del segmento con un coste de 1 frente un coste de 2 que ofrece el puerto 43.




El switch 3:13 toma estas decisiones:

* 3:13 es raiz y pone todos sus puertos a designado.




El switch 4:71 toma estas decisiones:

* El puerto con la MAC 71 se convierte en raíz. 
* El puerto con la MAC 88 se convierte en designado. Es el mejor del segmento con un coste de 1 frente un coste de 2 que ofrece el puerto 11.


        