
STP Ejercicio 12, dificultad 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Dada la red de switches que se muestra en la figura:

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej12/ejercicio12.png

Indicar el estado final en que quedarán todos los puertos de todos los switches.

Empezando por los eventos de envío, recepción y determinación de cual es el switch raíz la lista de sucesos sería esta:


1. Switch 6:41 envía por el puerto 93 la BPDU (Raíz:6:41, Coste:0, ID:6:41, MAC:93)
2. Switch 6:41 envía por el puerto 41 la BPDU (Raíz:6:41, Coste:0, ID:6:41, MAC:41)
3. Switch 1:00 envía por el puerto 86 la BPDU (Raíz:1:00, Coste:0, ID:1:00, MAC:86)
4. Switch 1:00 envía por el puerto 00 la BPDU (Raíz:1:00, Coste:0, ID:1:00, MAC:00)
5. Switch 5:27 envía por el puerto 27 la BPDU (Raíz:5:27, Coste:0, ID:5:27, MAC:27)
6. Switch 5:27 envía por el puerto 53 la BPDU (Raíz:5:27, Coste:0, ID:5:27, MAC:53)
7. Switch 3:50 envía por el puerto 50 la BPDU (Raíz:3:50, Coste:0, ID:3:50, MAC:50)
8. Switch 3:50 envía por el puerto 73 la BPDU (Raíz:3:50, Coste:0, ID:3:50, MAC:73)
9. Switch 6:41 recibe por el puerto 93 la BPDU (Raíz:3:50, Coste:0, ID:3:50, MAC:73). La raíz 3:50 es mejor, así que se anota como nueva raíz.
10. Switch 6:41 recibe por el puerto 41 la BPDU (Raíz:1:00, Coste:0, ID:1:00, MAC:86). La raíz 1:00 es mejor, así que se anota como nueva raíz.
11. Switch 1:00 recibe por el puerto 86 la BPDU (Raíz:6:41, Coste:0, ID:6:41, MAC:41)
12. Switch 1:00 recibe por el puerto 00 la BPDU (Raíz:5:27, Coste:0, ID:5:27, MAC:27)
13. Switch 5:27 recibe por el puerto 27 la BPDU (Raíz:1:00, Coste:0, ID:1:00, MAC:00). La raíz 1:00 es mejor, así que se anota como nueva raíz.
14. Switch 5:27 recibe por el puerto 53 la BPDU (Raíz:3:50, Coste:0, ID:3:50, MAC:50)
15. Switch 3:50 recibe por el puerto 50 la BPDU (Raíz:5:27, Coste:0, ID:5:27, MAC:53)
16. Switch 3:50 recibe por el puerto 73 la BPDU (Raíz:6:41, Coste:0, ID:6:41, MAC:93)
17. Switch 6:41 envía por el puerto 93 la BPDU (Raíz:1:00, Coste:1, ID:6:41, MAC:93)
18. Switch 6:41 envía por el puerto 41 la BPDU (Raíz:1:00, Coste:1, ID:6:41, MAC:41)
19. Switch 1:00 envía por el puerto 86 la BPDU (Raíz:1:00, Coste:0, ID:1:00, MAC:86)
20. Switch 1:00 envía por el puerto 00 la BPDU (Raíz:1:00, Coste:0, ID:1:00, MAC:00)
21. Switch 5:27 envía por el puerto 27 la BPDU (Raíz:1:00, Coste:1, ID:5:27, MAC:27)
22. Switch 5:27 envía por el puerto 53 la BPDU (Raíz:1:00, Coste:1, ID:5:27, MAC:53)
23. Switch 3:50 envía por el puerto 50 la BPDU (Raíz:3:50, Coste:0, ID:3:50, MAC:50)
24. Switch 3:50 envía por el puerto 73 la BPDU (Raíz:3:50, Coste:0, ID:3:50, MAC:73)
25. Switch 6:41 recibe por el puerto 93 la BPDU (Raíz:3:50, Coste:0, ID:3:50, MAC:73)
26. Switch 6:41 recibe por el puerto 41 la BPDU (Raíz:1:00, Coste:0, ID:1:00, MAC:86)
27. Switch 1:00 recibe por el puerto 86 la BPDU (Raíz:1:00, Coste:1, ID:6:41, MAC:41)
28. Switch 1:00 recibe por el puerto 00 la BPDU (Raíz:1:00, Coste:1, ID:5:27, MAC:27)
29. Switch 5:27 recibe por el puerto 27 la BPDU (Raíz:1:00, Coste:0, ID:1:00, MAC:00)
30. Switch 5:27 recibe por el puerto 53 la BPDU (Raíz:3:50, Coste:0, ID:3:50, MAC:50)
31. Switch 3:50 recibe por el puerto 50 la BPDU (Raíz:1:00, Coste:1, ID:5:27, MAC:53). La raíz 1:00 es mejor, así que se anota como nueva raíz.
32. Switch 3:50 recibe por el puerto 73 la BPDU (Raíz:1:00, Coste:1, ID:6:41, MAC:93)
33. Switch 6:41 envía por el puerto 93 la BPDU (Raíz:1:00, Coste:1, ID:6:41, MAC:93)
34. Switch 6:41 envía por el puerto 41 la BPDU (Raíz:1:00, Coste:1, ID:6:41, MAC:41)
35. Switch 1:00 envía por el puerto 86 la BPDU (Raíz:1:00, Coste:0, ID:1:00, MAC:86)
36. Switch 1:00 envía por el puerto 00 la BPDU (Raíz:1:00, Coste:0, ID:1:00, MAC:00)
37. Switch 5:27 envía por el puerto 27 la BPDU (Raíz:1:00, Coste:1, ID:5:27, MAC:27)
38. Switch 5:27 envía por el puerto 53 la BPDU (Raíz:1:00, Coste:1, ID:5:27, MAC:53)
39. Switch 3:50 envía por el puerto 50 la BPDU (Raíz:1:00, Coste:2, ID:3:50, MAC:50)
40. Switch 3:50 envía por el puerto 73 la BPDU (Raíz:1:00, Coste:2, ID:3:50, MAC:73)
41. Switch 6:41 recibe por el puerto 93 la BPDU (Raíz:1:00, Coste:2, ID:3:50, MAC:73)
42. Switch 6:41 recibe por el puerto 41 la BPDU (Raíz:1:00, Coste:0, ID:1:00, MAC:86)
43. Switch 1:00 recibe por el puerto 86 la BPDU (Raíz:1:00, Coste:1, ID:6:41, MAC:41)
44. Switch 1:00 recibe por el puerto 00 la BPDU (Raíz:1:00, Coste:1, ID:5:27, MAC:27)
45. Switch 5:27 recibe por el puerto 27 la BPDU (Raíz:1:00, Coste:0, ID:1:00, MAC:00)
46. Switch 5:27 recibe por el puerto 53 la BPDU (Raíz:1:00, Coste:2, ID:3:50, MAC:50)
47. Switch 3:50 recibe por el puerto 50 la BPDU (Raíz:1:00, Coste:1, ID:5:27, MAC:53)
48. Switch 3:50 recibe por el puerto 73 la BPDU (Raíz:1:00, Coste:1, ID:6:41, MAC:93)



Una vez decidido el switch raíz, los switches toman las siguientes decisiones (volvemos a indicar la figura por comodidad):

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej12/ejercicio12.png




El switch 6:41 toma estas decisiones:

* El puerto con la MAC 41 se convierte en raíz. 
* El puerto con la MAC 93 se convierte en designado. Es el mejor del segmento con un coste de 1 frente un coste de 2 que ofrece el puerto 73.




El switch 1:00 toma estas decisiones:

* 1:00 es raiz y pone todos sus puertos a designado.




El switch 5:27 toma estas decisiones:

* El puerto con la MAC 27 se convierte en raíz. 
* El puerto con la MAC 53 se convierte en designado. Es el mejor del segmento con un coste de 1 frente un coste de 2 que ofrece el puerto 50.




El switch 3:50 toma estas decisiones:

* El puerto con la MAC 50 se convierte en raíz. 


        