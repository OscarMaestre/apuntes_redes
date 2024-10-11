
STP Ejercicio 18, dificultad 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Dada la red de switches que se muestra en la figura:

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej18/ejercicio18.png

Indicar el estado final en que quedarán todos los puertos de todos los switches.

Empezando por los eventos de envío, recepción y determinación de cual es el switch raíz la lista de sucesos sería esta:


1. Switch 1:57 envía por el puerto 97 la BPDU (Raíz:1:57, Coste:0, ID:1:57, MAC:97)
2. Switch 1:57 envía por el puerto 57 la BPDU (Raíz:1:57, Coste:0, ID:1:57, MAC:57)
3. Switch 4:44 envía por el puerto 45 la BPDU (Raíz:4:44, Coste:0, ID:4:44, MAC:45)
4. Switch 4:44 envía por el puerto 44 la BPDU (Raíz:4:44, Coste:0, ID:4:44, MAC:44)
5. Switch 6:02 envía por el puerto 60 la BPDU (Raíz:6:02, Coste:0, ID:6:02, MAC:60)
6. Switch 6:02 envía por el puerto 02 la BPDU (Raíz:6:02, Coste:0, ID:6:02, MAC:02)
7. Switch 3:07 envía por el puerto 07 la BPDU (Raíz:3:07, Coste:0, ID:3:07, MAC:07)
8. Switch 3:07 envía por el puerto 29 la BPDU (Raíz:3:07, Coste:0, ID:3:07, MAC:29)
9. Switch 1:57 recibe por el puerto 97 la BPDU (Raíz:3:07, Coste:0, ID:3:07, MAC:29)
10. Switch 1:57 recibe por el puerto 57 la BPDU (Raíz:4:44, Coste:0, ID:4:44, MAC:45)
11. Switch 4:44 recibe por el puerto 45 la BPDU (Raíz:1:57, Coste:0, ID:1:57, MAC:57). La raíz 1:57 es mejor, así que se anota como nueva raíz.
12. Switch 4:44 recibe por el puerto 44 la BPDU (Raíz:6:02, Coste:0, ID:6:02, MAC:60)
13. Switch 6:02 recibe por el puerto 60 la BPDU (Raíz:4:44, Coste:0, ID:4:44, MAC:44). La raíz 4:44 es mejor, así que se anota como nueva raíz.
14. Switch 6:02 recibe por el puerto 02 la BPDU (Raíz:3:07, Coste:0, ID:3:07, MAC:07). La raíz 3:07 es mejor, así que se anota como nueva raíz.
15. Switch 3:07 recibe por el puerto 07 la BPDU (Raíz:6:02, Coste:0, ID:6:02, MAC:02)
16. Switch 3:07 recibe por el puerto 29 la BPDU (Raíz:1:57, Coste:0, ID:1:57, MAC:97). La raíz 1:57 es mejor, así que se anota como nueva raíz.
17. Switch 1:57 envía por el puerto 97 la BPDU (Raíz:1:57, Coste:0, ID:1:57, MAC:97)
18. Switch 1:57 envía por el puerto 57 la BPDU (Raíz:1:57, Coste:0, ID:1:57, MAC:57)
19. Switch 4:44 envía por el puerto 45 la BPDU (Raíz:1:57, Coste:1, ID:4:44, MAC:45)
20. Switch 4:44 envía por el puerto 44 la BPDU (Raíz:1:57, Coste:1, ID:4:44, MAC:44)
21. Switch 6:02 envía por el puerto 60 la BPDU (Raíz:3:07, Coste:1, ID:6:02, MAC:60)
22. Switch 6:02 envía por el puerto 02 la BPDU (Raíz:3:07, Coste:1, ID:6:02, MAC:02)
23. Switch 3:07 envía por el puerto 07 la BPDU (Raíz:1:57, Coste:1, ID:3:07, MAC:07)
24. Switch 3:07 envía por el puerto 29 la BPDU (Raíz:1:57, Coste:1, ID:3:07, MAC:29)
25. Switch 1:57 recibe por el puerto 97 la BPDU (Raíz:1:57, Coste:1, ID:3:07, MAC:29)
26. Switch 1:57 recibe por el puerto 57 la BPDU (Raíz:1:57, Coste:1, ID:4:44, MAC:45)
27. Switch 4:44 recibe por el puerto 45 la BPDU (Raíz:1:57, Coste:0, ID:1:57, MAC:57)
28. Switch 4:44 recibe por el puerto 44 la BPDU (Raíz:3:07, Coste:1, ID:6:02, MAC:60)
29. Switch 6:02 recibe por el puerto 60 la BPDU (Raíz:1:57, Coste:1, ID:4:44, MAC:44). La raíz 1:57 es mejor, así que se anota como nueva raíz.
30. Switch 6:02 recibe por el puerto 02 la BPDU (Raíz:1:57, Coste:1, ID:3:07, MAC:07). Llegó de nuevo la raíz 1:57 pero por un puerto con menor MAC (02), así que ese puerto se anota como posible puerto raíz
31. Switch 3:07 recibe por el puerto 07 la BPDU (Raíz:3:07, Coste:1, ID:6:02, MAC:02)
32. Switch 3:07 recibe por el puerto 29 la BPDU (Raíz:1:57, Coste:0, ID:1:57, MAC:97)
33. Switch 1:57 envía por el puerto 97 la BPDU (Raíz:1:57, Coste:0, ID:1:57, MAC:97)
34. Switch 1:57 envía por el puerto 57 la BPDU (Raíz:1:57, Coste:0, ID:1:57, MAC:57)
35. Switch 4:44 envía por el puerto 45 la BPDU (Raíz:1:57, Coste:1, ID:4:44, MAC:45)
36. Switch 4:44 envía por el puerto 44 la BPDU (Raíz:1:57, Coste:1, ID:4:44, MAC:44)
37. Switch 6:02 envía por el puerto 60 la BPDU (Raíz:1:57, Coste:2, ID:6:02, MAC:60)
38. Switch 6:02 envía por el puerto 02 la BPDU (Raíz:1:57, Coste:2, ID:6:02, MAC:02)
39. Switch 3:07 envía por el puerto 07 la BPDU (Raíz:1:57, Coste:1, ID:3:07, MAC:07)
40. Switch 3:07 envía por el puerto 29 la BPDU (Raíz:1:57, Coste:1, ID:3:07, MAC:29)
41. Switch 1:57 recibe por el puerto 97 la BPDU (Raíz:1:57, Coste:1, ID:3:07, MAC:29)
42. Switch 1:57 recibe por el puerto 57 la BPDU (Raíz:1:57, Coste:1, ID:4:44, MAC:45)
43. Switch 4:44 recibe por el puerto 45 la BPDU (Raíz:1:57, Coste:0, ID:1:57, MAC:57)
44. Switch 4:44 recibe por el puerto 44 la BPDU (Raíz:1:57, Coste:2, ID:6:02, MAC:60)
45. Switch 6:02 recibe por el puerto 60 la BPDU (Raíz:1:57, Coste:1, ID:4:44, MAC:44)
46. Switch 6:02 recibe por el puerto 02 la BPDU (Raíz:1:57, Coste:1, ID:3:07, MAC:07)
47. Switch 3:07 recibe por el puerto 07 la BPDU (Raíz:1:57, Coste:2, ID:6:02, MAC:02)
48. Switch 3:07 recibe por el puerto 29 la BPDU (Raíz:1:57, Coste:0, ID:1:57, MAC:97)



Una vez decidido el switch raíz, los switches toman las siguientes decisiones (volvemos a indicar la figura por comodidad):

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej18/ejercicio18.png




El switch 1:57 toma estas decisiones:

* 1:57 es raiz y pone todos sus puertos a designado.




El switch 4:44 toma estas decisiones:

* El puerto con la MAC 45 se convierte en raíz. 
* El puerto con la MAC 44 se convierte en designado. Es el mejor del segmento con un coste de 1 frente un coste de 2 que ofrece el puerto 60.




El switch 6:02 toma estas decisiones:

* El puerto con la MAC 02 se convierte en raíz. 




El switch 3:07 toma estas decisiones:

* El puerto con la MAC 29 se convierte en raíz. 
* El puerto con la MAC 07 se convierte en designado. Es el mejor del segmento con un coste de 1 frente un coste de 2 que ofrece el puerto 02.


        