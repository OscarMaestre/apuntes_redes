
STP Ejercicio 20, dificultad 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Dada la red de switches que se muestra en la figura:

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej20/ejercicio20.png

Indicar el estado final en que quedarán todos los puertos de todos los switches.

Empezando por los eventos de envío, recepción y determinación de cual es el switch raíz la lista de sucesos sería esta:


1. Switch 4:26 envía por el puerto 26 la BPDU (Raíz:4:26, Coste:0, ID:4:26, MAC:26)
2. Switch 4:26 envía por el puerto 85 la BPDU (Raíz:4:26, Coste:0, ID:4:26, MAC:85)
3. Switch 5:63 envía por el puerto 63 la BPDU (Raíz:5:63, Coste:0, ID:5:63, MAC:63)
4. Switch 5:63 envía por el puerto 80 la BPDU (Raíz:5:63, Coste:0, ID:5:63, MAC:80)
5. Switch 5:17 envía por el puerto 17 la BPDU (Raíz:5:17, Coste:0, ID:5:17, MAC:17)
6. Switch 5:17 envía por el puerto 40 la BPDU (Raíz:5:17, Coste:0, ID:5:17, MAC:40)
7. Switch 2:30 envía por el puerto 30 la BPDU (Raíz:2:30, Coste:0, ID:2:30, MAC:30)
8. Switch 2:30 envía por el puerto 71 la BPDU (Raíz:2:30, Coste:0, ID:2:30, MAC:71)
9. Switch 4:26 recibe por el puerto 26 la BPDU (Raíz:2:30, Coste:0, ID:2:30, MAC:71). La raíz 2:30 es mejor, así que se anota como nueva raíz.
10. Switch 4:26 recibe por el puerto 85 la BPDU (Raíz:5:63, Coste:0, ID:5:63, MAC:63)
11. Switch 5:63 recibe por el puerto 63 la BPDU (Raíz:4:26, Coste:0, ID:4:26, MAC:85). La raíz 4:26 es mejor, así que se anota como nueva raíz.
12. Switch 5:63 recibe por el puerto 80 la BPDU (Raíz:5:17, Coste:0, ID:5:17, MAC:17)
13. Switch 5:17 recibe por el puerto 17 la BPDU (Raíz:5:63, Coste:0, ID:5:63, MAC:80)
14. Switch 5:17 recibe por el puerto 40 la BPDU (Raíz:2:30, Coste:0, ID:2:30, MAC:30). La raíz 2:30 es mejor, así que se anota como nueva raíz.
15. Switch 2:30 recibe por el puerto 30 la BPDU (Raíz:5:17, Coste:0, ID:5:17, MAC:40)
16. Switch 2:30 recibe por el puerto 71 la BPDU (Raíz:4:26, Coste:0, ID:4:26, MAC:26)
17. Switch 4:26 envía por el puerto 26 la BPDU (Raíz:2:30, Coste:1, ID:4:26, MAC:26)
18. Switch 4:26 envía por el puerto 85 la BPDU (Raíz:2:30, Coste:1, ID:4:26, MAC:85)
19. Switch 5:63 envía por el puerto 63 la BPDU (Raíz:4:26, Coste:1, ID:5:63, MAC:63)
20. Switch 5:63 envía por el puerto 80 la BPDU (Raíz:4:26, Coste:1, ID:5:63, MAC:80)
21. Switch 5:17 envía por el puerto 17 la BPDU (Raíz:2:30, Coste:1, ID:5:17, MAC:17)
22. Switch 5:17 envía por el puerto 40 la BPDU (Raíz:2:30, Coste:1, ID:5:17, MAC:40)
23. Switch 2:30 envía por el puerto 30 la BPDU (Raíz:2:30, Coste:0, ID:2:30, MAC:30)
24. Switch 2:30 envía por el puerto 71 la BPDU (Raíz:2:30, Coste:0, ID:2:30, MAC:71)
25. Switch 4:26 recibe por el puerto 26 la BPDU (Raíz:2:30, Coste:0, ID:2:30, MAC:71)
26. Switch 4:26 recibe por el puerto 85 la BPDU (Raíz:4:26, Coste:1, ID:5:63, MAC:63)
27. Switch 5:63 recibe por el puerto 63 la BPDU (Raíz:2:30, Coste:1, ID:4:26, MAC:85). La raíz 2:30 es mejor, así que se anota como nueva raíz.
28. Switch 5:63 recibe por el puerto 80 la BPDU (Raíz:2:30, Coste:1, ID:5:17, MAC:17)
29. Switch 5:17 recibe por el puerto 17 la BPDU (Raíz:4:26, Coste:1, ID:5:63, MAC:80)
30. Switch 5:17 recibe por el puerto 40 la BPDU (Raíz:2:30, Coste:0, ID:2:30, MAC:30)
31. Switch 2:30 recibe por el puerto 30 la BPDU (Raíz:2:30, Coste:1, ID:5:17, MAC:40)
32. Switch 2:30 recibe por el puerto 71 la BPDU (Raíz:2:30, Coste:1, ID:4:26, MAC:26)
33. Switch 4:26 envía por el puerto 26 la BPDU (Raíz:2:30, Coste:1, ID:4:26, MAC:26)
34. Switch 4:26 envía por el puerto 85 la BPDU (Raíz:2:30, Coste:1, ID:4:26, MAC:85)
35. Switch 5:63 envía por el puerto 63 la BPDU (Raíz:2:30, Coste:2, ID:5:63, MAC:63)
36. Switch 5:63 envía por el puerto 80 la BPDU (Raíz:2:30, Coste:2, ID:5:63, MAC:80)
37. Switch 5:17 envía por el puerto 17 la BPDU (Raíz:2:30, Coste:1, ID:5:17, MAC:17)
38. Switch 5:17 envía por el puerto 40 la BPDU (Raíz:2:30, Coste:1, ID:5:17, MAC:40)
39. Switch 2:30 envía por el puerto 30 la BPDU (Raíz:2:30, Coste:0, ID:2:30, MAC:30)
40. Switch 2:30 envía por el puerto 71 la BPDU (Raíz:2:30, Coste:0, ID:2:30, MAC:71)
41. Switch 4:26 recibe por el puerto 26 la BPDU (Raíz:2:30, Coste:0, ID:2:30, MAC:71)
42. Switch 4:26 recibe por el puerto 85 la BPDU (Raíz:2:30, Coste:2, ID:5:63, MAC:63)
43. Switch 5:63 recibe por el puerto 63 la BPDU (Raíz:2:30, Coste:1, ID:4:26, MAC:85)
44. Switch 5:63 recibe por el puerto 80 la BPDU (Raíz:2:30, Coste:1, ID:5:17, MAC:17)
45. Switch 5:17 recibe por el puerto 17 la BPDU (Raíz:2:30, Coste:2, ID:5:63, MAC:80)
46. Switch 5:17 recibe por el puerto 40 la BPDU (Raíz:2:30, Coste:0, ID:2:30, MAC:30)
47. Switch 2:30 recibe por el puerto 30 la BPDU (Raíz:2:30, Coste:1, ID:5:17, MAC:40)
48. Switch 2:30 recibe por el puerto 71 la BPDU (Raíz:2:30, Coste:1, ID:4:26, MAC:26)



Una vez decidido el switch raíz, los switches toman las siguientes decisiones (volvemos a indicar la figura por comodidad):

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej20/ejercicio20.png




El switch 4:26 toma estas decisiones:

* El puerto con la MAC 26 se convierte en raíz. 
* El puerto con la MAC 85 se convierte en designado. Es el mejor del segmento con un coste de 1 frente un coste de 2 que ofrece el puerto 63.




El switch 5:63 toma estas decisiones:

* El puerto con la MAC 63 se convierte en raíz. 




El switch 5:17 toma estas decisiones:

* El puerto con la MAC 40 se convierte en raíz. 
* El puerto con la MAC 17 se convierte en designado. Es el mejor del segmento con un coste de 1 frente un coste de 2 que ofrece el puerto 80.




El switch 2:30 toma estas decisiones:

* 2:30 es raiz y pone todos sus puertos a designado.


        