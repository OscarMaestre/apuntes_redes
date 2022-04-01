
STP Ejercicio 16, dificultad 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Dada la red de switches que se muestra en la figura:

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej16/ejercicio16.png

Indicar el estado final en que quedarán todos los puertos de todos los switches.

Empezando por los eventos de envío, recepción y determinación de cual es el switch raíz la lista de sucesos sería esta:


1. Switch 1:26 envía por el puerto 26 la BPDU (Raíz:1:26, Coste:0, ID:1:26, MAC:26)
2. Switch 1:26 envía por el puerto 59 la BPDU (Raíz:1:26, Coste:0, ID:1:26, MAC:59)
3. Switch 5:28 envía por el puerto 28 la BPDU (Raíz:5:28, Coste:0, ID:5:28, MAC:28)
4. Switch 5:28 envía por el puerto 74 la BPDU (Raíz:5:28, Coste:0, ID:5:28, MAC:74)
5. Switch 4:45 envía por el puerto 62 la BPDU (Raíz:4:45, Coste:0, ID:4:45, MAC:62)
6. Switch 4:45 envía por el puerto 45 la BPDU (Raíz:4:45, Coste:0, ID:4:45, MAC:45)
7. Switch 2:44 envía por el puerto 65 la BPDU (Raíz:2:44, Coste:0, ID:2:44, MAC:65)
8. Switch 2:44 envía por el puerto 44 la BPDU (Raíz:2:44, Coste:0, ID:2:44, MAC:44)
9. Switch 1:26 recibe por el puerto 26 la BPDU (Raíz:2:44, Coste:0, ID:2:44, MAC:44)
10. Switch 1:26 recibe por el puerto 59 la BPDU (Raíz:5:28, Coste:0, ID:5:28, MAC:28)
11. Switch 5:28 recibe por el puerto 28 la BPDU (Raíz:1:26, Coste:0, ID:1:26, MAC:59). La raíz 1:26 es mejor, así que se anota como nueva raíz.
12. Switch 5:28 recibe por el puerto 74 la BPDU (Raíz:4:45, Coste:0, ID:4:45, MAC:62)
13. Switch 4:45 recibe por el puerto 62 la BPDU (Raíz:5:28, Coste:0, ID:5:28, MAC:74)
14. Switch 4:45 recibe por el puerto 45 la BPDU (Raíz:2:44, Coste:0, ID:2:44, MAC:65). La raíz 2:44 es mejor, así que se anota como nueva raíz.
15. Switch 2:44 recibe por el puerto 65 la BPDU (Raíz:4:45, Coste:0, ID:4:45, MAC:45)
16. Switch 2:44 recibe por el puerto 44 la BPDU (Raíz:1:26, Coste:0, ID:1:26, MAC:26). La raíz 1:26 es mejor, así que se anota como nueva raíz.
17. Switch 1:26 envía por el puerto 26 la BPDU (Raíz:1:26, Coste:0, ID:1:26, MAC:26)
18. Switch 1:26 envía por el puerto 59 la BPDU (Raíz:1:26, Coste:0, ID:1:26, MAC:59)
19. Switch 5:28 envía por el puerto 28 la BPDU (Raíz:1:26, Coste:1, ID:5:28, MAC:28)
20. Switch 5:28 envía por el puerto 74 la BPDU (Raíz:1:26, Coste:1, ID:5:28, MAC:74)
21. Switch 4:45 envía por el puerto 62 la BPDU (Raíz:2:44, Coste:1, ID:4:45, MAC:62)
22. Switch 4:45 envía por el puerto 45 la BPDU (Raíz:2:44, Coste:1, ID:4:45, MAC:45)
23. Switch 2:44 envía por el puerto 65 la BPDU (Raíz:1:26, Coste:1, ID:2:44, MAC:65)
24. Switch 2:44 envía por el puerto 44 la BPDU (Raíz:1:26, Coste:1, ID:2:44, MAC:44)
25. Switch 1:26 recibe por el puerto 26 la BPDU (Raíz:1:26, Coste:1, ID:2:44, MAC:44)
26. Switch 1:26 recibe por el puerto 59 la BPDU (Raíz:1:26, Coste:1, ID:5:28, MAC:28)
27. Switch 5:28 recibe por el puerto 28 la BPDU (Raíz:1:26, Coste:0, ID:1:26, MAC:59)
28. Switch 5:28 recibe por el puerto 74 la BPDU (Raíz:2:44, Coste:1, ID:4:45, MAC:62)
29. Switch 4:45 recibe por el puerto 62 la BPDU (Raíz:1:26, Coste:1, ID:5:28, MAC:74). La raíz 1:26 es mejor, así que se anota como nueva raíz.
30. Switch 4:45 recibe por el puerto 45 la BPDU (Raíz:1:26, Coste:1, ID:2:44, MAC:65). Llegó de nuevo la raíz 1:26 pero por un puerto con menor MAC (45), así que ese puerto se anota como posible puerto raíz
31. Switch 2:44 recibe por el puerto 65 la BPDU (Raíz:2:44, Coste:1, ID:4:45, MAC:45)
32. Switch 2:44 recibe por el puerto 44 la BPDU (Raíz:1:26, Coste:0, ID:1:26, MAC:26)
33. Switch 1:26 envía por el puerto 26 la BPDU (Raíz:1:26, Coste:0, ID:1:26, MAC:26)
34. Switch 1:26 envía por el puerto 59 la BPDU (Raíz:1:26, Coste:0, ID:1:26, MAC:59)
35. Switch 5:28 envía por el puerto 28 la BPDU (Raíz:1:26, Coste:1, ID:5:28, MAC:28)
36. Switch 5:28 envía por el puerto 74 la BPDU (Raíz:1:26, Coste:1, ID:5:28, MAC:74)
37. Switch 4:45 envía por el puerto 62 la BPDU (Raíz:1:26, Coste:2, ID:4:45, MAC:62)
38. Switch 4:45 envía por el puerto 45 la BPDU (Raíz:1:26, Coste:2, ID:4:45, MAC:45)
39. Switch 2:44 envía por el puerto 65 la BPDU (Raíz:1:26, Coste:1, ID:2:44, MAC:65)
40. Switch 2:44 envía por el puerto 44 la BPDU (Raíz:1:26, Coste:1, ID:2:44, MAC:44)
41. Switch 1:26 recibe por el puerto 26 la BPDU (Raíz:1:26, Coste:1, ID:2:44, MAC:44)
42. Switch 1:26 recibe por el puerto 59 la BPDU (Raíz:1:26, Coste:1, ID:5:28, MAC:28)
43. Switch 5:28 recibe por el puerto 28 la BPDU (Raíz:1:26, Coste:0, ID:1:26, MAC:59)
44. Switch 5:28 recibe por el puerto 74 la BPDU (Raíz:1:26, Coste:2, ID:4:45, MAC:62)
45. Switch 4:45 recibe por el puerto 62 la BPDU (Raíz:1:26, Coste:1, ID:5:28, MAC:74)
46. Switch 4:45 recibe por el puerto 45 la BPDU (Raíz:1:26, Coste:1, ID:2:44, MAC:65)
47. Switch 2:44 recibe por el puerto 65 la BPDU (Raíz:1:26, Coste:2, ID:4:45, MAC:45)
48. Switch 2:44 recibe por el puerto 44 la BPDU (Raíz:1:26, Coste:0, ID:1:26, MAC:26)



Una vez decidido el switch raíz, los switches toman las siguientes decisiones (volvemos a indicar la figura por comodidad):

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej16/ejercicio16.png




El switch 1:26 toma estas decisiones:

* 1:26 es raiz y pone todos sus puertos a designado.




El switch 5:28 toma estas decisiones:

* El puerto con la MAC 28 se convierte en raíz. 
* El puerto con la MAC 74 se convierte en designado. Es el mejor del segmento con un coste de 1 frente un coste de 2 que ofrece el puerto 62.




El switch 4:45 toma estas decisiones:

* El puerto con la MAC 45 se convierte en raíz. 




El switch 2:44 toma estas decisiones:

* El puerto con la MAC 44 se convierte en raíz. 
* El puerto con la MAC 65 se convierte en designado. Es el mejor del segmento con un coste de 1 frente un coste de 2 que ofrece el puerto 45.


        