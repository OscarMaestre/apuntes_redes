
STP Ejercicio 14, dificultad 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Dada la red de switches que se muestra en la figura:

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej14/ejercicio14.png

Indicar el estado final en que quedarán todos los puertos de todos los switches.

Empezando por los eventos de envío, recepción y determinación de cual es el switch raíz la lista de sucesos sería esta:


1. Switch 3:47 envía por el puerto 47 la BPDU (Raíz:3:47, Coste:0, ID:3:47, MAC:47)
2. Switch 3:47 envía por el puerto 83 la BPDU (Raíz:3:47, Coste:0, ID:3:47, MAC:83)
3. Switch 2:41 envía por el puerto 96 la BPDU (Raíz:2:41, Coste:0, ID:2:41, MAC:96)
4. Switch 2:41 envía por el puerto 41 la BPDU (Raíz:2:41, Coste:0, ID:2:41, MAC:41)
5. Switch 2:33 envía por el puerto 35 la BPDU (Raíz:2:33, Coste:0, ID:2:33, MAC:35)
6. Switch 2:33 envía por el puerto 33 la BPDU (Raíz:2:33, Coste:0, ID:2:33, MAC:33)
7. Switch 2:75 envía por el puerto 75 la BPDU (Raíz:2:75, Coste:0, ID:2:75, MAC:75)
8. Switch 2:75 envía por el puerto 82 la BPDU (Raíz:2:75, Coste:0, ID:2:75, MAC:82)
9. Switch 3:47 recibe por el puerto 47 la BPDU (Raíz:2:75, Coste:0, ID:2:75, MAC:82). La raíz 2:75 es mejor, así que se anota como nueva raíz.
10. Switch 3:47 recibe por el puerto 83 la BPDU (Raíz:2:41, Coste:0, ID:2:41, MAC:96). La raíz 2:41 es mejor, así que se anota como nueva raíz.
11. Switch 2:41 recibe por el puerto 96 la BPDU (Raíz:3:47, Coste:0, ID:3:47, MAC:83)
12. Switch 2:41 recibe por el puerto 41 la BPDU (Raíz:2:33, Coste:0, ID:2:33, MAC:35). La raíz 2:33 es mejor, así que se anota como nueva raíz.
13. Switch 2:33 recibe por el puerto 35 la BPDU (Raíz:2:41, Coste:0, ID:2:41, MAC:41)
14. Switch 2:33 recibe por el puerto 33 la BPDU (Raíz:2:75, Coste:0, ID:2:75, MAC:75)
15. Switch 2:75 recibe por el puerto 75 la BPDU (Raíz:2:33, Coste:0, ID:2:33, MAC:33). La raíz 2:33 es mejor, así que se anota como nueva raíz.
16. Switch 2:75 recibe por el puerto 82 la BPDU (Raíz:3:47, Coste:0, ID:3:47, MAC:47)
17. Switch 3:47 envía por el puerto 47 la BPDU (Raíz:2:41, Coste:1, ID:3:47, MAC:47)
18. Switch 3:47 envía por el puerto 83 la BPDU (Raíz:2:41, Coste:1, ID:3:47, MAC:83)
19. Switch 2:41 envía por el puerto 96 la BPDU (Raíz:2:33, Coste:1, ID:2:41, MAC:96)
20. Switch 2:41 envía por el puerto 41 la BPDU (Raíz:2:33, Coste:1, ID:2:41, MAC:41)
21. Switch 2:33 envía por el puerto 35 la BPDU (Raíz:2:33, Coste:0, ID:2:33, MAC:35)
22. Switch 2:33 envía por el puerto 33 la BPDU (Raíz:2:33, Coste:0, ID:2:33, MAC:33)
23. Switch 2:75 envía por el puerto 75 la BPDU (Raíz:2:33, Coste:1, ID:2:75, MAC:75)
24. Switch 2:75 envía por el puerto 82 la BPDU (Raíz:2:33, Coste:1, ID:2:75, MAC:82)
25. Switch 3:47 recibe por el puerto 47 la BPDU (Raíz:2:33, Coste:1, ID:2:75, MAC:82). La raíz 2:33 es mejor, así que se anota como nueva raíz.
26. Switch 3:47 recibe por el puerto 83 la BPDU (Raíz:2:33, Coste:1, ID:2:41, MAC:96)
27. Switch 2:41 recibe por el puerto 96 la BPDU (Raíz:2:41, Coste:1, ID:3:47, MAC:83)
28. Switch 2:41 recibe por el puerto 41 la BPDU (Raíz:2:33, Coste:0, ID:2:33, MAC:35)
29. Switch 2:33 recibe por el puerto 35 la BPDU (Raíz:2:33, Coste:1, ID:2:41, MAC:41)
30. Switch 2:33 recibe por el puerto 33 la BPDU (Raíz:2:33, Coste:1, ID:2:75, MAC:75)
31. Switch 2:75 recibe por el puerto 75 la BPDU (Raíz:2:33, Coste:0, ID:2:33, MAC:33)
32. Switch 2:75 recibe por el puerto 82 la BPDU (Raíz:2:41, Coste:1, ID:3:47, MAC:47)
33. Switch 3:47 envía por el puerto 47 la BPDU (Raíz:2:33, Coste:2, ID:3:47, MAC:47)
34. Switch 3:47 envía por el puerto 83 la BPDU (Raíz:2:33, Coste:2, ID:3:47, MAC:83)
35. Switch 2:41 envía por el puerto 96 la BPDU (Raíz:2:33, Coste:1, ID:2:41, MAC:96)
36. Switch 2:41 envía por el puerto 41 la BPDU (Raíz:2:33, Coste:1, ID:2:41, MAC:41)
37. Switch 2:33 envía por el puerto 35 la BPDU (Raíz:2:33, Coste:0, ID:2:33, MAC:35)
38. Switch 2:33 envía por el puerto 33 la BPDU (Raíz:2:33, Coste:0, ID:2:33, MAC:33)
39. Switch 2:75 envía por el puerto 75 la BPDU (Raíz:2:33, Coste:1, ID:2:75, MAC:75)
40. Switch 2:75 envía por el puerto 82 la BPDU (Raíz:2:33, Coste:1, ID:2:75, MAC:82)
41. Switch 3:47 recibe por el puerto 47 la BPDU (Raíz:2:33, Coste:1, ID:2:75, MAC:82)
42. Switch 3:47 recibe por el puerto 83 la BPDU (Raíz:2:33, Coste:1, ID:2:41, MAC:96)
43. Switch 2:41 recibe por el puerto 96 la BPDU (Raíz:2:33, Coste:2, ID:3:47, MAC:83)
44. Switch 2:41 recibe por el puerto 41 la BPDU (Raíz:2:33, Coste:0, ID:2:33, MAC:35)
45. Switch 2:33 recibe por el puerto 35 la BPDU (Raíz:2:33, Coste:1, ID:2:41, MAC:41)
46. Switch 2:33 recibe por el puerto 33 la BPDU (Raíz:2:33, Coste:1, ID:2:75, MAC:75)
47. Switch 2:75 recibe por el puerto 75 la BPDU (Raíz:2:33, Coste:0, ID:2:33, MAC:33)
48. Switch 2:75 recibe por el puerto 82 la BPDU (Raíz:2:33, Coste:2, ID:3:47, MAC:47)



Una vez decidido el switch raíz, los switches toman las siguientes decisiones (volvemos a indicar la figura por comodidad):

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej14/ejercicio14.png




El switch 3:47 toma estas decisiones:

* El puerto con la MAC 47 se convierte en raíz. 




El switch 2:41 toma estas decisiones:

* El puerto con la MAC 41 se convierte en raíz. 
* El puerto con la MAC 96 se convierte en designado. Es el mejor del segmento con un coste de 1 frente un coste de 2 que ofrece el puerto 83.




El switch 2:33 toma estas decisiones:

* 2:33 es raiz y pone todos sus puertos a designado.




El switch 2:75 toma estas decisiones:

* El puerto con la MAC 75 se convierte en raíz. 
* El puerto con la MAC 82 se convierte en designado. Es el mejor del segmento con un coste de 1 frente un coste de 2 que ofrece el puerto 47.


        