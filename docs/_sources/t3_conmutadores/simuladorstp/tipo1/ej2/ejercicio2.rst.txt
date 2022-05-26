
STP Ejercicio 2, dificultad 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Dada la red de switches que se muestra en la figura:

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej2/ejercicio2.png

Indicar el estado final en que quedarán todos los puertos de todos los switches.

Empezando por los eventos de envío, recepción y determinación de cual es el switch raíz la lista de sucesos sería esta:


1. Switch 1:54 envía por el puerto 64 la BPDU (Raíz:1:54, Coste:0, ID:1:54, MAC:64)
2. Switch 1:54 envía por el puerto 54 la BPDU (Raíz:1:54, Coste:0, ID:1:54, MAC:54)
3. Switch 5:08 envía por el puerto 08 la BPDU (Raíz:5:08, Coste:0, ID:5:08, MAC:08)
4. Switch 5:08 envía por el puerto 30 la BPDU (Raíz:5:08, Coste:0, ID:5:08, MAC:30)
5. Switch 3:93 envía por el puerto 93 la BPDU (Raíz:3:93, Coste:0, ID:3:93, MAC:93)
6. Switch 3:93 envía por el puerto 97 la BPDU (Raíz:3:93, Coste:0, ID:3:93, MAC:97)
7. Switch 4:23 envía por el puerto 23 la BPDU (Raíz:4:23, Coste:0, ID:4:23, MAC:23)
8. Switch 4:23 envía por el puerto 33 la BPDU (Raíz:4:23, Coste:0, ID:4:23, MAC:33)
9. Switch 1:54 recibe por el puerto 64 la BPDU (Raíz:4:23, Coste:0, ID:4:23, MAC:33)
10. Switch 1:54 recibe por el puerto 54 la BPDU (Raíz:5:08, Coste:0, ID:5:08, MAC:08)
11. Switch 5:08 recibe por el puerto 08 la BPDU (Raíz:1:54, Coste:0, ID:1:54, MAC:54). La raíz 1:54 es mejor, así que se anota como nueva raíz.
12. Switch 5:08 recibe por el puerto 30 la BPDU (Raíz:3:93, Coste:0, ID:3:93, MAC:93)
13. Switch 3:93 recibe por el puerto 93 la BPDU (Raíz:5:08, Coste:0, ID:5:08, MAC:30)
14. Switch 3:93 recibe por el puerto 97 la BPDU (Raíz:4:23, Coste:0, ID:4:23, MAC:23)
15. Switch 4:23 recibe por el puerto 23 la BPDU (Raíz:3:93, Coste:0, ID:3:93, MAC:97). La raíz 3:93 es mejor, así que se anota como nueva raíz.
16. Switch 4:23 recibe por el puerto 33 la BPDU (Raíz:1:54, Coste:0, ID:1:54, MAC:64). La raíz 1:54 es mejor, así que se anota como nueva raíz.
17. Switch 1:54 envía por el puerto 64 la BPDU (Raíz:1:54, Coste:0, ID:1:54, MAC:64)
18. Switch 1:54 envía por el puerto 54 la BPDU (Raíz:1:54, Coste:0, ID:1:54, MAC:54)
19. Switch 5:08 envía por el puerto 08 la BPDU (Raíz:1:54, Coste:1, ID:5:08, MAC:08)
20. Switch 5:08 envía por el puerto 30 la BPDU (Raíz:1:54, Coste:1, ID:5:08, MAC:30)
21. Switch 3:93 envía por el puerto 93 la BPDU (Raíz:3:93, Coste:0, ID:3:93, MAC:93)
22. Switch 3:93 envía por el puerto 97 la BPDU (Raíz:3:93, Coste:0, ID:3:93, MAC:97)
23. Switch 4:23 envía por el puerto 23 la BPDU (Raíz:1:54, Coste:1, ID:4:23, MAC:23)
24. Switch 4:23 envía por el puerto 33 la BPDU (Raíz:1:54, Coste:1, ID:4:23, MAC:33)
25. Switch 1:54 recibe por el puerto 64 la BPDU (Raíz:1:54, Coste:1, ID:4:23, MAC:33)
26. Switch 1:54 recibe por el puerto 54 la BPDU (Raíz:1:54, Coste:1, ID:5:08, MAC:08)
27. Switch 5:08 recibe por el puerto 08 la BPDU (Raíz:1:54, Coste:0, ID:1:54, MAC:54)
28. Switch 5:08 recibe por el puerto 30 la BPDU (Raíz:3:93, Coste:0, ID:3:93, MAC:93)
29. Switch 3:93 recibe por el puerto 93 la BPDU (Raíz:1:54, Coste:1, ID:5:08, MAC:30). La raíz 1:54 es mejor, así que se anota como nueva raíz.
30. Switch 3:93 recibe por el puerto 97 la BPDU (Raíz:1:54, Coste:1, ID:4:23, MAC:23)
31. Switch 4:23 recibe por el puerto 23 la BPDU (Raíz:3:93, Coste:0, ID:3:93, MAC:97)
32. Switch 4:23 recibe por el puerto 33 la BPDU (Raíz:1:54, Coste:0, ID:1:54, MAC:64)
33. Switch 1:54 envía por el puerto 64 la BPDU (Raíz:1:54, Coste:0, ID:1:54, MAC:64)
34. Switch 1:54 envía por el puerto 54 la BPDU (Raíz:1:54, Coste:0, ID:1:54, MAC:54)
35. Switch 5:08 envía por el puerto 08 la BPDU (Raíz:1:54, Coste:1, ID:5:08, MAC:08)
36. Switch 5:08 envía por el puerto 30 la BPDU (Raíz:1:54, Coste:1, ID:5:08, MAC:30)
37. Switch 3:93 envía por el puerto 93 la BPDU (Raíz:1:54, Coste:2, ID:3:93, MAC:93)
38. Switch 3:93 envía por el puerto 97 la BPDU (Raíz:1:54, Coste:2, ID:3:93, MAC:97)
39. Switch 4:23 envía por el puerto 23 la BPDU (Raíz:1:54, Coste:1, ID:4:23, MAC:23)
40. Switch 4:23 envía por el puerto 33 la BPDU (Raíz:1:54, Coste:1, ID:4:23, MAC:33)
41. Switch 1:54 recibe por el puerto 64 la BPDU (Raíz:1:54, Coste:1, ID:4:23, MAC:33)
42. Switch 1:54 recibe por el puerto 54 la BPDU (Raíz:1:54, Coste:1, ID:5:08, MAC:08)
43. Switch 5:08 recibe por el puerto 08 la BPDU (Raíz:1:54, Coste:0, ID:1:54, MAC:54)
44. Switch 5:08 recibe por el puerto 30 la BPDU (Raíz:1:54, Coste:2, ID:3:93, MAC:93)
45. Switch 3:93 recibe por el puerto 93 la BPDU (Raíz:1:54, Coste:1, ID:5:08, MAC:30)
46. Switch 3:93 recibe por el puerto 97 la BPDU (Raíz:1:54, Coste:1, ID:4:23, MAC:23)
47. Switch 4:23 recibe por el puerto 23 la BPDU (Raíz:1:54, Coste:2, ID:3:93, MAC:97)
48. Switch 4:23 recibe por el puerto 33 la BPDU (Raíz:1:54, Coste:0, ID:1:54, MAC:64)



Una vez decidido el switch raíz, los switches toman las siguientes decisiones (volvemos a indicar la figura por comodidad):

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej2/ejercicio2.png




El switch 1:54 toma estas decisiones:

* 1:54 es raiz y pone todos sus puertos a designado.




El switch 5:08 toma estas decisiones:

* El puerto con la MAC 08 se convierte en raíz. 
* El puerto con la MAC 30 se convierte en designado. Es el mejor del segmento con un coste de 1 frente un coste de 2 que ofrece el puerto 93.




El switch 3:93 toma estas decisiones:

* El puerto con la MAC 93 se convierte en raíz. 




El switch 4:23 toma estas decisiones:

* El puerto con la MAC 33 se convierte en raíz. 
* El puerto con la MAC 23 se convierte en designado. Es el mejor del segmento con un coste de 1 frente un coste de 2 que ofrece el puerto 97.


        