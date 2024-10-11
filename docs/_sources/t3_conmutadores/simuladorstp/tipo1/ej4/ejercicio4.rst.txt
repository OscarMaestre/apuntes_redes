
STP Ejercicio 4, dificultad 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Dada la red de switches que se muestra en la figura:

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej4/ejercicio4.png

Indicar el estado final en que quedarán todos los puertos de todos los switches.

Empezando por los eventos de envío, recepción y determinación de cual es el switch raíz la lista de sucesos sería esta:


1. Switch 4:81 envía por el puerto 81 la BPDU (Raíz:4:81, Coste:0, ID:4:81, MAC:81)
2. Switch 4:81 envía por el puerto 87 la BPDU (Raíz:4:81, Coste:0, ID:4:81, MAC:87)
3. Switch 5:23 envía por el puerto 63 la BPDU (Raíz:5:23, Coste:0, ID:5:23, MAC:63)
4. Switch 5:23 envía por el puerto 23 la BPDU (Raíz:5:23, Coste:0, ID:5:23, MAC:23)
5. Switch 6:02 envía por el puerto 68 la BPDU (Raíz:6:02, Coste:0, ID:6:02, MAC:68)
6. Switch 6:02 envía por el puerto 02 la BPDU (Raíz:6:02, Coste:0, ID:6:02, MAC:02)
7. Switch 3:01 envía por el puerto 01 la BPDU (Raíz:3:01, Coste:0, ID:3:01, MAC:01)
8. Switch 3:01 envía por el puerto 58 la BPDU (Raíz:3:01, Coste:0, ID:3:01, MAC:58)
9. Switch 4:81 recibe por el puerto 81 la BPDU (Raíz:3:01, Coste:0, ID:3:01, MAC:58). La raíz 3:01 es mejor, así que se anota como nueva raíz.
10. Switch 4:81 recibe por el puerto 87 la BPDU (Raíz:5:23, Coste:0, ID:5:23, MAC:63)
11. Switch 5:23 recibe por el puerto 63 la BPDU (Raíz:4:81, Coste:0, ID:4:81, MAC:87). La raíz 4:81 es mejor, así que se anota como nueva raíz.
12. Switch 5:23 recibe por el puerto 23 la BPDU (Raíz:6:02, Coste:0, ID:6:02, MAC:68)
13. Switch 6:02 recibe por el puerto 68 la BPDU (Raíz:5:23, Coste:0, ID:5:23, MAC:23). La raíz 5:23 es mejor, así que se anota como nueva raíz.
14. Switch 6:02 recibe por el puerto 02 la BPDU (Raíz:3:01, Coste:0, ID:3:01, MAC:01). La raíz 3:01 es mejor, así que se anota como nueva raíz.
15. Switch 3:01 recibe por el puerto 01 la BPDU (Raíz:6:02, Coste:0, ID:6:02, MAC:02)
16. Switch 3:01 recibe por el puerto 58 la BPDU (Raíz:4:81, Coste:0, ID:4:81, MAC:81)
17. Switch 4:81 envía por el puerto 81 la BPDU (Raíz:3:01, Coste:1, ID:4:81, MAC:81)
18. Switch 4:81 envía por el puerto 87 la BPDU (Raíz:3:01, Coste:1, ID:4:81, MAC:87)
19. Switch 5:23 envía por el puerto 63 la BPDU (Raíz:4:81, Coste:1, ID:5:23, MAC:63)
20. Switch 5:23 envía por el puerto 23 la BPDU (Raíz:4:81, Coste:1, ID:5:23, MAC:23)
21. Switch 6:02 envía por el puerto 68 la BPDU (Raíz:3:01, Coste:1, ID:6:02, MAC:68)
22. Switch 6:02 envía por el puerto 02 la BPDU (Raíz:3:01, Coste:1, ID:6:02, MAC:02)
23. Switch 3:01 envía por el puerto 01 la BPDU (Raíz:3:01, Coste:0, ID:3:01, MAC:01)
24. Switch 3:01 envía por el puerto 58 la BPDU (Raíz:3:01, Coste:0, ID:3:01, MAC:58)
25. Switch 4:81 recibe por el puerto 81 la BPDU (Raíz:3:01, Coste:0, ID:3:01, MAC:58)
26. Switch 4:81 recibe por el puerto 87 la BPDU (Raíz:4:81, Coste:1, ID:5:23, MAC:63)
27. Switch 5:23 recibe por el puerto 63 la BPDU (Raíz:3:01, Coste:1, ID:4:81, MAC:87). La raíz 3:01 es mejor, así que se anota como nueva raíz.
28. Switch 5:23 recibe por el puerto 23 la BPDU (Raíz:3:01, Coste:1, ID:6:02, MAC:68). Llegó de nuevo la raíz 3:01 pero por un puerto con menor MAC (23), así que ese puerto se anota como posible puerto raíz
29. Switch 6:02 recibe por el puerto 68 la BPDU (Raíz:4:81, Coste:1, ID:5:23, MAC:23)
30. Switch 6:02 recibe por el puerto 02 la BPDU (Raíz:3:01, Coste:0, ID:3:01, MAC:01)
31. Switch 3:01 recibe por el puerto 01 la BPDU (Raíz:3:01, Coste:1, ID:6:02, MAC:02)
32. Switch 3:01 recibe por el puerto 58 la BPDU (Raíz:3:01, Coste:1, ID:4:81, MAC:81)
33. Switch 4:81 envía por el puerto 81 la BPDU (Raíz:3:01, Coste:1, ID:4:81, MAC:81)
34. Switch 4:81 envía por el puerto 87 la BPDU (Raíz:3:01, Coste:1, ID:4:81, MAC:87)
35. Switch 5:23 envía por el puerto 63 la BPDU (Raíz:3:01, Coste:2, ID:5:23, MAC:63)
36. Switch 5:23 envía por el puerto 23 la BPDU (Raíz:3:01, Coste:2, ID:5:23, MAC:23)
37. Switch 6:02 envía por el puerto 68 la BPDU (Raíz:3:01, Coste:1, ID:6:02, MAC:68)
38. Switch 6:02 envía por el puerto 02 la BPDU (Raíz:3:01, Coste:1, ID:6:02, MAC:02)
39. Switch 3:01 envía por el puerto 01 la BPDU (Raíz:3:01, Coste:0, ID:3:01, MAC:01)
40. Switch 3:01 envía por el puerto 58 la BPDU (Raíz:3:01, Coste:0, ID:3:01, MAC:58)
41. Switch 4:81 recibe por el puerto 81 la BPDU (Raíz:3:01, Coste:0, ID:3:01, MAC:58)
42. Switch 4:81 recibe por el puerto 87 la BPDU (Raíz:3:01, Coste:2, ID:5:23, MAC:63)
43. Switch 5:23 recibe por el puerto 63 la BPDU (Raíz:3:01, Coste:1, ID:4:81, MAC:87)
44. Switch 5:23 recibe por el puerto 23 la BPDU (Raíz:3:01, Coste:1, ID:6:02, MAC:68)
45. Switch 6:02 recibe por el puerto 68 la BPDU (Raíz:3:01, Coste:2, ID:5:23, MAC:23)
46. Switch 6:02 recibe por el puerto 02 la BPDU (Raíz:3:01, Coste:0, ID:3:01, MAC:01)
47. Switch 3:01 recibe por el puerto 01 la BPDU (Raíz:3:01, Coste:1, ID:6:02, MAC:02)
48. Switch 3:01 recibe por el puerto 58 la BPDU (Raíz:3:01, Coste:1, ID:4:81, MAC:81)



Una vez decidido el switch raíz, los switches toman las siguientes decisiones (volvemos a indicar la figura por comodidad):

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej4/ejercicio4.png




El switch 4:81 toma estas decisiones:

* El puerto con la MAC 81 se convierte en raíz. 
* El puerto con la MAC 87 se convierte en designado. Es el mejor del segmento con un coste de 1 frente un coste de 2 que ofrece el puerto 63.




El switch 5:23 toma estas decisiones:

* El puerto con la MAC 23 se convierte en raíz. 




El switch 6:02 toma estas decisiones:

* El puerto con la MAC 02 se convierte en raíz. 
* El puerto con la MAC 68 se convierte en designado. Es el mejor del segmento con un coste de 1 frente un coste de 2 que ofrece el puerto 23.




El switch 3:01 toma estas decisiones:

* 3:01 es raiz y pone todos sus puertos a designado.


        