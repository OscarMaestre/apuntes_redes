
STP Ejercicio 5, dificultad 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Dada la red de switches que se muestra en la figura:

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej5/ejercicio5.png

Indicar el estado final en que quedarán todos los puertos de todos los switches.

Empezando por los eventos de envío, recepción y determinación de cual es el switch raíz la lista de sucesos sería esta:


1. Switch 4:44 envía por el puerto 76 la BPDU (Raíz:4:44, Coste:0, ID:4:44, MAC:76)
2. Switch 4:44 envía por el puerto 44 la BPDU (Raíz:4:44, Coste:0, ID:4:44, MAC:44)
3. Switch 4:25 envía por el puerto 25 la BPDU (Raíz:4:25, Coste:0, ID:4:25, MAC:25)
4. Switch 4:25 envía por el puerto 77 la BPDU (Raíz:4:25, Coste:0, ID:4:25, MAC:77)
5. Switch 2:23 envía por el puerto 78 la BPDU (Raíz:2:23, Coste:0, ID:2:23, MAC:78)
6. Switch 2:23 envía por el puerto 23 la BPDU (Raíz:2:23, Coste:0, ID:2:23, MAC:23)
7. Switch 4:47 envía por el puerto 47 la BPDU (Raíz:4:47, Coste:0, ID:4:47, MAC:47)
8. Switch 4:47 envía por el puerto 99 la BPDU (Raíz:4:47, Coste:0, ID:4:47, MAC:99)
9. Switch 4:44 recibe por el puerto 76 la BPDU (Raíz:4:47, Coste:0, ID:4:47, MAC:99)
10. Switch 4:44 recibe por el puerto 44 la BPDU (Raíz:4:25, Coste:0, ID:4:25, MAC:25). La raíz 4:25 es mejor, así que se anota como nueva raíz.
11. Switch 4:25 recibe por el puerto 25 la BPDU (Raíz:4:44, Coste:0, ID:4:44, MAC:44)
12. Switch 4:25 recibe por el puerto 77 la BPDU (Raíz:2:23, Coste:0, ID:2:23, MAC:78). La raíz 2:23 es mejor, así que se anota como nueva raíz.
13. Switch 2:23 recibe por el puerto 78 la BPDU (Raíz:4:25, Coste:0, ID:4:25, MAC:77)
14. Switch 2:23 recibe por el puerto 23 la BPDU (Raíz:4:47, Coste:0, ID:4:47, MAC:47)
15. Switch 4:47 recibe por el puerto 47 la BPDU (Raíz:2:23, Coste:0, ID:2:23, MAC:23). La raíz 2:23 es mejor, así que se anota como nueva raíz.
16. Switch 4:47 recibe por el puerto 99 la BPDU (Raíz:4:44, Coste:0, ID:4:44, MAC:76)
17. Switch 4:44 envía por el puerto 76 la BPDU (Raíz:4:25, Coste:1, ID:4:44, MAC:76)
18. Switch 4:44 envía por el puerto 44 la BPDU (Raíz:4:25, Coste:1, ID:4:44, MAC:44)
19. Switch 4:25 envía por el puerto 25 la BPDU (Raíz:2:23, Coste:1, ID:4:25, MAC:25)
20. Switch 4:25 envía por el puerto 77 la BPDU (Raíz:2:23, Coste:1, ID:4:25, MAC:77)
21. Switch 2:23 envía por el puerto 78 la BPDU (Raíz:2:23, Coste:0, ID:2:23, MAC:78)
22. Switch 2:23 envía por el puerto 23 la BPDU (Raíz:2:23, Coste:0, ID:2:23, MAC:23)
23. Switch 4:47 envía por el puerto 47 la BPDU (Raíz:2:23, Coste:1, ID:4:47, MAC:47)
24. Switch 4:47 envía por el puerto 99 la BPDU (Raíz:2:23, Coste:1, ID:4:47, MAC:99)
25. Switch 4:44 recibe por el puerto 76 la BPDU (Raíz:2:23, Coste:1, ID:4:47, MAC:99). La raíz 2:23 es mejor, así que se anota como nueva raíz.
26. Switch 4:44 recibe por el puerto 44 la BPDU (Raíz:2:23, Coste:1, ID:4:25, MAC:25). Llegó de nuevo la raíz 2:23 pero por un puerto con menor MAC (44), así que ese puerto se anota como posible puerto raíz
27. Switch 4:25 recibe por el puerto 25 la BPDU (Raíz:4:25, Coste:1, ID:4:44, MAC:44)
28. Switch 4:25 recibe por el puerto 77 la BPDU (Raíz:2:23, Coste:0, ID:2:23, MAC:78)
29. Switch 2:23 recibe por el puerto 78 la BPDU (Raíz:2:23, Coste:1, ID:4:25, MAC:77)
30. Switch 2:23 recibe por el puerto 23 la BPDU (Raíz:2:23, Coste:1, ID:4:47, MAC:47)
31. Switch 4:47 recibe por el puerto 47 la BPDU (Raíz:2:23, Coste:0, ID:2:23, MAC:23)
32. Switch 4:47 recibe por el puerto 99 la BPDU (Raíz:4:25, Coste:1, ID:4:44, MAC:76)
33. Switch 4:44 envía por el puerto 76 la BPDU (Raíz:2:23, Coste:2, ID:4:44, MAC:76)
34. Switch 4:44 envía por el puerto 44 la BPDU (Raíz:2:23, Coste:2, ID:4:44, MAC:44)
35. Switch 4:25 envía por el puerto 25 la BPDU (Raíz:2:23, Coste:1, ID:4:25, MAC:25)
36. Switch 4:25 envía por el puerto 77 la BPDU (Raíz:2:23, Coste:1, ID:4:25, MAC:77)
37. Switch 2:23 envía por el puerto 78 la BPDU (Raíz:2:23, Coste:0, ID:2:23, MAC:78)
38. Switch 2:23 envía por el puerto 23 la BPDU (Raíz:2:23, Coste:0, ID:2:23, MAC:23)
39. Switch 4:47 envía por el puerto 47 la BPDU (Raíz:2:23, Coste:1, ID:4:47, MAC:47)
40. Switch 4:47 envía por el puerto 99 la BPDU (Raíz:2:23, Coste:1, ID:4:47, MAC:99)
41. Switch 4:44 recibe por el puerto 76 la BPDU (Raíz:2:23, Coste:1, ID:4:47, MAC:99)
42. Switch 4:44 recibe por el puerto 44 la BPDU (Raíz:2:23, Coste:1, ID:4:25, MAC:25)
43. Switch 4:25 recibe por el puerto 25 la BPDU (Raíz:2:23, Coste:2, ID:4:44, MAC:44)
44. Switch 4:25 recibe por el puerto 77 la BPDU (Raíz:2:23, Coste:0, ID:2:23, MAC:78)
45. Switch 2:23 recibe por el puerto 78 la BPDU (Raíz:2:23, Coste:1, ID:4:25, MAC:77)
46. Switch 2:23 recibe por el puerto 23 la BPDU (Raíz:2:23, Coste:1, ID:4:47, MAC:47)
47. Switch 4:47 recibe por el puerto 47 la BPDU (Raíz:2:23, Coste:0, ID:2:23, MAC:23)
48. Switch 4:47 recibe por el puerto 99 la BPDU (Raíz:2:23, Coste:2, ID:4:44, MAC:76)



Una vez decidido el switch raíz, los switches toman las siguientes decisiones (volvemos a indicar la figura por comodidad):

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej5/ejercicio5.png




El switch 4:44 toma estas decisiones:

* El puerto con la MAC 44 se convierte en raíz. 




El switch 4:25 toma estas decisiones:

* El puerto con la MAC 77 se convierte en raíz. 
* El puerto con la MAC 25 se convierte en designado. Es el mejor del segmento con un coste de 1 frente un coste de 2 que ofrece el puerto 44.




El switch 2:23 toma estas decisiones:

* 2:23 es raiz y pone todos sus puertos a designado.




El switch 4:47 toma estas decisiones:

* El puerto con la MAC 47 se convierte en raíz. 
* El puerto con la MAC 99 se convierte en designado. Es el mejor del segmento con un coste de 1 frente un coste de 2 que ofrece el puerto 76.


        