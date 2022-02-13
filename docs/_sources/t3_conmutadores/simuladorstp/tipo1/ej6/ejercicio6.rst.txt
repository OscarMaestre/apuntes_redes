
STP Ejercicio 6, dificultad 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Dada la red de switches que se muestra en la figura:

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej6/ejercicio6.png

Indicar el estado final en que quedarán todos los puertos de todos los switches.

Empezando por los eventos de envío, recepción y determinación de cual es el switch raíz la lista de sucesos sería esta:


1. Switch 5:63 envía por el puerto 87 la BPDU (Raíz:5:63, Coste:0, ID:5:63, MAC:87)
2. Switch 5:63 envía por el puerto 63 la BPDU (Raíz:5:63, Coste:0, ID:5:63, MAC:63)
3. Switch 6:02 envía por el puerto 02 la BPDU (Raíz:6:02, Coste:0, ID:6:02, MAC:02)
4. Switch 6:02 envía por el puerto 78 la BPDU (Raíz:6:02, Coste:0, ID:6:02, MAC:78)
5. Switch 3:41 envía por el puerto 41 la BPDU (Raíz:3:41, Coste:0, ID:3:41, MAC:41)
6. Switch 3:41 envía por el puerto 44 la BPDU (Raíz:3:41, Coste:0, ID:3:41, MAC:44)
7. Switch 2:09 envía por el puerto 81 la BPDU (Raíz:2:09, Coste:0, ID:2:09, MAC:81)
8. Switch 2:09 envía por el puerto 09 la BPDU (Raíz:2:09, Coste:0, ID:2:09, MAC:09)
9. Switch 5:63 recibe por el puerto 87 la BPDU (Raíz:2:09, Coste:0, ID:2:09, MAC:09). La raíz 2:09 es mejor, así que se anota como nueva raíz.
10. Switch 5:63 recibe por el puerto 63 la BPDU (Raíz:6:02, Coste:0, ID:6:02, MAC:02)
11. Switch 6:02 recibe por el puerto 02 la BPDU (Raíz:5:63, Coste:0, ID:5:63, MAC:63). La raíz 5:63 es mejor, así que se anota como nueva raíz.
12. Switch 6:02 recibe por el puerto 78 la BPDU (Raíz:3:41, Coste:0, ID:3:41, MAC:41). La raíz 3:41 es mejor, así que se anota como nueva raíz.
13. Switch 3:41 recibe por el puerto 41 la BPDU (Raíz:6:02, Coste:0, ID:6:02, MAC:78)
14. Switch 3:41 recibe por el puerto 44 la BPDU (Raíz:2:09, Coste:0, ID:2:09, MAC:81). La raíz 2:09 es mejor, así que se anota como nueva raíz.
15. Switch 2:09 recibe por el puerto 81 la BPDU (Raíz:3:41, Coste:0, ID:3:41, MAC:44)
16. Switch 2:09 recibe por el puerto 09 la BPDU (Raíz:5:63, Coste:0, ID:5:63, MAC:87)
17. Switch 5:63 envía por el puerto 87 la BPDU (Raíz:2:09, Coste:1, ID:5:63, MAC:87)
18. Switch 5:63 envía por el puerto 63 la BPDU (Raíz:2:09, Coste:1, ID:5:63, MAC:63)
19. Switch 6:02 envía por el puerto 02 la BPDU (Raíz:3:41, Coste:1, ID:6:02, MAC:02)
20. Switch 6:02 envía por el puerto 78 la BPDU (Raíz:3:41, Coste:1, ID:6:02, MAC:78)
21. Switch 3:41 envía por el puerto 41 la BPDU (Raíz:2:09, Coste:1, ID:3:41, MAC:41)
22. Switch 3:41 envía por el puerto 44 la BPDU (Raíz:2:09, Coste:1, ID:3:41, MAC:44)
23. Switch 2:09 envía por el puerto 81 la BPDU (Raíz:2:09, Coste:0, ID:2:09, MAC:81)
24. Switch 2:09 envía por el puerto 09 la BPDU (Raíz:2:09, Coste:0, ID:2:09, MAC:09)
25. Switch 5:63 recibe por el puerto 87 la BPDU (Raíz:2:09, Coste:0, ID:2:09, MAC:09)
26. Switch 5:63 recibe por el puerto 63 la BPDU (Raíz:3:41, Coste:1, ID:6:02, MAC:02)
27. Switch 6:02 recibe por el puerto 02 la BPDU (Raíz:2:09, Coste:1, ID:5:63, MAC:63). La raíz 2:09 es mejor, así que se anota como nueva raíz.
28. Switch 6:02 recibe por el puerto 78 la BPDU (Raíz:2:09, Coste:1, ID:3:41, MAC:41)
29. Switch 3:41 recibe por el puerto 41 la BPDU (Raíz:3:41, Coste:1, ID:6:02, MAC:78)
30. Switch 3:41 recibe por el puerto 44 la BPDU (Raíz:2:09, Coste:0, ID:2:09, MAC:81)
31. Switch 2:09 recibe por el puerto 81 la BPDU (Raíz:2:09, Coste:1, ID:3:41, MAC:44)
32. Switch 2:09 recibe por el puerto 09 la BPDU (Raíz:2:09, Coste:1, ID:5:63, MAC:87)
33. Switch 5:63 envía por el puerto 87 la BPDU (Raíz:2:09, Coste:1, ID:5:63, MAC:87)
34. Switch 5:63 envía por el puerto 63 la BPDU (Raíz:2:09, Coste:1, ID:5:63, MAC:63)
35. Switch 6:02 envía por el puerto 02 la BPDU (Raíz:2:09, Coste:2, ID:6:02, MAC:02)
36. Switch 6:02 envía por el puerto 78 la BPDU (Raíz:2:09, Coste:2, ID:6:02, MAC:78)
37. Switch 3:41 envía por el puerto 41 la BPDU (Raíz:2:09, Coste:1, ID:3:41, MAC:41)
38. Switch 3:41 envía por el puerto 44 la BPDU (Raíz:2:09, Coste:1, ID:3:41, MAC:44)
39. Switch 2:09 envía por el puerto 81 la BPDU (Raíz:2:09, Coste:0, ID:2:09, MAC:81)
40. Switch 2:09 envía por el puerto 09 la BPDU (Raíz:2:09, Coste:0, ID:2:09, MAC:09)
41. Switch 5:63 recibe por el puerto 87 la BPDU (Raíz:2:09, Coste:0, ID:2:09, MAC:09)
42. Switch 5:63 recibe por el puerto 63 la BPDU (Raíz:2:09, Coste:2, ID:6:02, MAC:02)
43. Switch 6:02 recibe por el puerto 02 la BPDU (Raíz:2:09, Coste:1, ID:5:63, MAC:63)
44. Switch 6:02 recibe por el puerto 78 la BPDU (Raíz:2:09, Coste:1, ID:3:41, MAC:41)
45. Switch 3:41 recibe por el puerto 41 la BPDU (Raíz:2:09, Coste:2, ID:6:02, MAC:78)
46. Switch 3:41 recibe por el puerto 44 la BPDU (Raíz:2:09, Coste:0, ID:2:09, MAC:81)
47. Switch 2:09 recibe por el puerto 81 la BPDU (Raíz:2:09, Coste:1, ID:3:41, MAC:44)
48. Switch 2:09 recibe por el puerto 09 la BPDU (Raíz:2:09, Coste:1, ID:5:63, MAC:87)



Una vez decidido el switch raíz, los switches toman las siguientes decisiones (volvemos a indicar la figura por comodidad):

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej6/ejercicio6.png




El switch 5:63 toma estas decisiones:

* El puerto con la MAC 87 se convierte en raíz. 
* El puerto con la MAC 63 se convierte en designado. Es el mejor del segmento con un coste de 1 frente un coste de 2 que ofrece el puerto 02.




El switch 6:02 toma estas decisiones:

* El puerto con la MAC 02 se convierte en raíz. 




El switch 3:41 toma estas decisiones:

* El puerto con la MAC 44 se convierte en raíz. 
* El puerto con la MAC 41 se convierte en designado. Es el mejor del segmento con un coste de 1 frente un coste de 2 que ofrece el puerto 78.




El switch 2:09 toma estas decisiones:

* 2:09 es raiz y pone todos sus puertos a designado.


        