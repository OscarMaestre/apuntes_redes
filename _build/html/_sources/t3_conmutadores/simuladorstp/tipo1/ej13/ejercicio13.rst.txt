
STP Ejercicio 13, dificultad 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Dada la red de switches que se muestra en la figura:

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej13/ejercicio13.png

Indicar el estado final en que quedarán todos los puertos de todos los switches.

Empezando por los eventos de envío, recepción y determinación de cual es el switch raíz la lista de sucesos sería esta:


1. Switch 3:09 envía por el puerto 42 la BPDU (Raíz:3:09, Coste:0, ID:3:09, MAC:42)
2. Switch 3:09 envía por el puerto 09 la BPDU (Raíz:3:09, Coste:0, ID:3:09, MAC:09)
3. Switch 2:54 envía por el puerto 90 la BPDU (Raíz:2:54, Coste:0, ID:2:54, MAC:90)
4. Switch 2:54 envía por el puerto 54 la BPDU (Raíz:2:54, Coste:0, ID:2:54, MAC:54)
5. Switch 6:70 envía por el puerto 70 la BPDU (Raíz:6:70, Coste:0, ID:6:70, MAC:70)
6. Switch 6:70 envía por el puerto 84 la BPDU (Raíz:6:70, Coste:0, ID:6:70, MAC:84)
7. Switch 5:07 envía por el puerto 07 la BPDU (Raíz:5:07, Coste:0, ID:5:07, MAC:07)
8. Switch 5:07 envía por el puerto 67 la BPDU (Raíz:5:07, Coste:0, ID:5:07, MAC:67)
9. Switch 3:09 recibe por el puerto 42 la BPDU (Raíz:5:07, Coste:0, ID:5:07, MAC:67)
10. Switch 3:09 recibe por el puerto 09 la BPDU (Raíz:2:54, Coste:0, ID:2:54, MAC:90). La raíz 2:54 es mejor, así que se anota como nueva raíz.
11. Switch 2:54 recibe por el puerto 90 la BPDU (Raíz:3:09, Coste:0, ID:3:09, MAC:09)
12. Switch 2:54 recibe por el puerto 54 la BPDU (Raíz:6:70, Coste:0, ID:6:70, MAC:70)
13. Switch 6:70 recibe por el puerto 70 la BPDU (Raíz:2:54, Coste:0, ID:2:54, MAC:54). La raíz 2:54 es mejor, así que se anota como nueva raíz.
14. Switch 6:70 recibe por el puerto 84 la BPDU (Raíz:5:07, Coste:0, ID:5:07, MAC:07)
15. Switch 5:07 recibe por el puerto 07 la BPDU (Raíz:6:70, Coste:0, ID:6:70, MAC:84)
16. Switch 5:07 recibe por el puerto 67 la BPDU (Raíz:3:09, Coste:0, ID:3:09, MAC:42). La raíz 3:09 es mejor, así que se anota como nueva raíz.
17. Switch 3:09 envía por el puerto 42 la BPDU (Raíz:2:54, Coste:1, ID:3:09, MAC:42)
18. Switch 3:09 envía por el puerto 09 la BPDU (Raíz:2:54, Coste:1, ID:3:09, MAC:09)
19. Switch 2:54 envía por el puerto 90 la BPDU (Raíz:2:54, Coste:0, ID:2:54, MAC:90)
20. Switch 2:54 envía por el puerto 54 la BPDU (Raíz:2:54, Coste:0, ID:2:54, MAC:54)
21. Switch 6:70 envía por el puerto 70 la BPDU (Raíz:2:54, Coste:1, ID:6:70, MAC:70)
22. Switch 6:70 envía por el puerto 84 la BPDU (Raíz:2:54, Coste:1, ID:6:70, MAC:84)
23. Switch 5:07 envía por el puerto 07 la BPDU (Raíz:3:09, Coste:1, ID:5:07, MAC:07)
24. Switch 5:07 envía por el puerto 67 la BPDU (Raíz:3:09, Coste:1, ID:5:07, MAC:67)
25. Switch 3:09 recibe por el puerto 42 la BPDU (Raíz:3:09, Coste:1, ID:5:07, MAC:67)
26. Switch 3:09 recibe por el puerto 09 la BPDU (Raíz:2:54, Coste:0, ID:2:54, MAC:90)
27. Switch 2:54 recibe por el puerto 90 la BPDU (Raíz:2:54, Coste:1, ID:3:09, MAC:09)
28. Switch 2:54 recibe por el puerto 54 la BPDU (Raíz:2:54, Coste:1, ID:6:70, MAC:70)
29. Switch 6:70 recibe por el puerto 70 la BPDU (Raíz:2:54, Coste:0, ID:2:54, MAC:54)
30. Switch 6:70 recibe por el puerto 84 la BPDU (Raíz:3:09, Coste:1, ID:5:07, MAC:07)
31. Switch 5:07 recibe por el puerto 07 la BPDU (Raíz:2:54, Coste:1, ID:6:70, MAC:84). La raíz 2:54 es mejor, así que se anota como nueva raíz.
32. Switch 5:07 recibe por el puerto 67 la BPDU (Raíz:2:54, Coste:1, ID:3:09, MAC:42)
33. Switch 3:09 envía por el puerto 42 la BPDU (Raíz:2:54, Coste:1, ID:3:09, MAC:42)
34. Switch 3:09 envía por el puerto 09 la BPDU (Raíz:2:54, Coste:1, ID:3:09, MAC:09)
35. Switch 2:54 envía por el puerto 90 la BPDU (Raíz:2:54, Coste:0, ID:2:54, MAC:90)
36. Switch 2:54 envía por el puerto 54 la BPDU (Raíz:2:54, Coste:0, ID:2:54, MAC:54)
37. Switch 6:70 envía por el puerto 70 la BPDU (Raíz:2:54, Coste:1, ID:6:70, MAC:70)
38. Switch 6:70 envía por el puerto 84 la BPDU (Raíz:2:54, Coste:1, ID:6:70, MAC:84)
39. Switch 5:07 envía por el puerto 07 la BPDU (Raíz:2:54, Coste:2, ID:5:07, MAC:07)
40. Switch 5:07 envía por el puerto 67 la BPDU (Raíz:2:54, Coste:2, ID:5:07, MAC:67)
41. Switch 3:09 recibe por el puerto 42 la BPDU (Raíz:2:54, Coste:2, ID:5:07, MAC:67)
42. Switch 3:09 recibe por el puerto 09 la BPDU (Raíz:2:54, Coste:0, ID:2:54, MAC:90)
43. Switch 2:54 recibe por el puerto 90 la BPDU (Raíz:2:54, Coste:1, ID:3:09, MAC:09)
44. Switch 2:54 recibe por el puerto 54 la BPDU (Raíz:2:54, Coste:1, ID:6:70, MAC:70)
45. Switch 6:70 recibe por el puerto 70 la BPDU (Raíz:2:54, Coste:0, ID:2:54, MAC:54)
46. Switch 6:70 recibe por el puerto 84 la BPDU (Raíz:2:54, Coste:2, ID:5:07, MAC:07)
47. Switch 5:07 recibe por el puerto 07 la BPDU (Raíz:2:54, Coste:1, ID:6:70, MAC:84)
48. Switch 5:07 recibe por el puerto 67 la BPDU (Raíz:2:54, Coste:1, ID:3:09, MAC:42)



Una vez decidido el switch raíz, los switches toman las siguientes decisiones (volvemos a indicar la figura por comodidad):

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej13/ejercicio13.png




El switch 3:09 toma estas decisiones:

* El puerto con la MAC 09 se convierte en raíz. 
* El puerto con la MAC 42 se convierte en designado. Es el mejor del segmento con un coste de 1 frente un coste de 2 que ofrece el puerto 67.




El switch 2:54 toma estas decisiones:

* 2:54 es raiz y pone todos sus puertos a designado.




El switch 6:70 toma estas decisiones:

* El puerto con la MAC 70 se convierte en raíz. 
* El puerto con la MAC 84 se convierte en designado. Es el mejor del segmento con un coste de 1 frente un coste de 2 que ofrece el puerto 07.




El switch 5:07 toma estas decisiones:

* El puerto con la MAC 07 se convierte en raíz. 


        