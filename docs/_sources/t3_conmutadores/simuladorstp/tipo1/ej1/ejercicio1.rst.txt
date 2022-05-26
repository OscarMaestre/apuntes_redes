
STP Ejercicio 1, dificultad 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Dada la red de switches que se muestra en la figura:

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej1/ejercicio1.png

Indicar el estado final en que quedarán todos los puertos de todos los switches.

Empezando por los eventos de envío, recepción y determinación de cual es el switch raíz la lista de sucesos sería esta:


1. Switch 4:48 envía por el puerto 48 la BPDU (Raíz:4:48, Coste:0, ID:4:48, MAC:48)
2. Switch 4:48 envía por el puerto 58 la BPDU (Raíz:4:48, Coste:0, ID:4:48, MAC:58)
3. Switch 6:03 envía por el puerto 03 la BPDU (Raíz:6:03, Coste:0, ID:6:03, MAC:03)
4. Switch 6:03 envía por el puerto 76 la BPDU (Raíz:6:03, Coste:0, ID:6:03, MAC:76)
5. Switch 4:00 envía por el puerto 00 la BPDU (Raíz:4:00, Coste:0, ID:4:00, MAC:00)
6. Switch 4:00 envía por el puerto 23 la BPDU (Raíz:4:00, Coste:0, ID:4:00, MAC:23)
7. Switch 6:01 envía por el puerto 01 la BPDU (Raíz:6:01, Coste:0, ID:6:01, MAC:01)
8. Switch 6:01 envía por el puerto 15 la BPDU (Raíz:6:01, Coste:0, ID:6:01, MAC:15)
9. Switch 4:48 recibe por el puerto 48 la BPDU (Raíz:6:01, Coste:0, ID:6:01, MAC:15)
10. Switch 4:48 recibe por el puerto 58 la BPDU (Raíz:6:03, Coste:0, ID:6:03, MAC:03)
11. Switch 6:03 recibe por el puerto 03 la BPDU (Raíz:4:48, Coste:0, ID:4:48, MAC:58). La raíz 4:48 es mejor, así que se anota como nueva raíz.
12. Switch 6:03 recibe por el puerto 76 la BPDU (Raíz:4:00, Coste:0, ID:4:00, MAC:00). La raíz 4:00 es mejor, así que se anota como nueva raíz.
13. Switch 4:00 recibe por el puerto 00 la BPDU (Raíz:6:03, Coste:0, ID:6:03, MAC:76)
14. Switch 4:00 recibe por el puerto 23 la BPDU (Raíz:6:01, Coste:0, ID:6:01, MAC:01)
15. Switch 6:01 recibe por el puerto 01 la BPDU (Raíz:4:00, Coste:0, ID:4:00, MAC:23). La raíz 4:00 es mejor, así que se anota como nueva raíz.
16. Switch 6:01 recibe por el puerto 15 la BPDU (Raíz:4:48, Coste:0, ID:4:48, MAC:48)
17. Switch 4:48 envía por el puerto 48 la BPDU (Raíz:4:48, Coste:0, ID:4:48, MAC:48)
18. Switch 4:48 envía por el puerto 58 la BPDU (Raíz:4:48, Coste:0, ID:4:48, MAC:58)
19. Switch 6:03 envía por el puerto 03 la BPDU (Raíz:4:00, Coste:1, ID:6:03, MAC:03)
20. Switch 6:03 envía por el puerto 76 la BPDU (Raíz:4:00, Coste:1, ID:6:03, MAC:76)
21. Switch 4:00 envía por el puerto 00 la BPDU (Raíz:4:00, Coste:0, ID:4:00, MAC:00)
22. Switch 4:00 envía por el puerto 23 la BPDU (Raíz:4:00, Coste:0, ID:4:00, MAC:23)
23. Switch 6:01 envía por el puerto 01 la BPDU (Raíz:4:00, Coste:1, ID:6:01, MAC:01)
24. Switch 6:01 envía por el puerto 15 la BPDU (Raíz:4:00, Coste:1, ID:6:01, MAC:15)
25. Switch 4:48 recibe por el puerto 48 la BPDU (Raíz:4:00, Coste:1, ID:6:01, MAC:15). La raíz 4:00 es mejor, así que se anota como nueva raíz.
26. Switch 4:48 recibe por el puerto 58 la BPDU (Raíz:4:00, Coste:1, ID:6:03, MAC:03)
27. Switch 6:03 recibe por el puerto 03 la BPDU (Raíz:4:48, Coste:0, ID:4:48, MAC:58)
28. Switch 6:03 recibe por el puerto 76 la BPDU (Raíz:4:00, Coste:0, ID:4:00, MAC:00)
29. Switch 4:00 recibe por el puerto 00 la BPDU (Raíz:4:00, Coste:1, ID:6:03, MAC:76)
30. Switch 4:00 recibe por el puerto 23 la BPDU (Raíz:4:00, Coste:1, ID:6:01, MAC:01)
31. Switch 6:01 recibe por el puerto 01 la BPDU (Raíz:4:00, Coste:0, ID:4:00, MAC:23)
32. Switch 6:01 recibe por el puerto 15 la BPDU (Raíz:4:48, Coste:0, ID:4:48, MAC:48)
33. Switch 4:48 envía por el puerto 48 la BPDU (Raíz:4:00, Coste:2, ID:4:48, MAC:48)
34. Switch 4:48 envía por el puerto 58 la BPDU (Raíz:4:00, Coste:2, ID:4:48, MAC:58)
35. Switch 6:03 envía por el puerto 03 la BPDU (Raíz:4:00, Coste:1, ID:6:03, MAC:03)
36. Switch 6:03 envía por el puerto 76 la BPDU (Raíz:4:00, Coste:1, ID:6:03, MAC:76)
37. Switch 4:00 envía por el puerto 00 la BPDU (Raíz:4:00, Coste:0, ID:4:00, MAC:00)
38. Switch 4:00 envía por el puerto 23 la BPDU (Raíz:4:00, Coste:0, ID:4:00, MAC:23)
39. Switch 6:01 envía por el puerto 01 la BPDU (Raíz:4:00, Coste:1, ID:6:01, MAC:01)
40. Switch 6:01 envía por el puerto 15 la BPDU (Raíz:4:00, Coste:1, ID:6:01, MAC:15)
41. Switch 4:48 recibe por el puerto 48 la BPDU (Raíz:4:00, Coste:1, ID:6:01, MAC:15)
42. Switch 4:48 recibe por el puerto 58 la BPDU (Raíz:4:00, Coste:1, ID:6:03, MAC:03)
43. Switch 6:03 recibe por el puerto 03 la BPDU (Raíz:4:00, Coste:2, ID:4:48, MAC:58)
44. Switch 6:03 recibe por el puerto 76 la BPDU (Raíz:4:00, Coste:0, ID:4:00, MAC:00)
45. Switch 4:00 recibe por el puerto 00 la BPDU (Raíz:4:00, Coste:1, ID:6:03, MAC:76)
46. Switch 4:00 recibe por el puerto 23 la BPDU (Raíz:4:00, Coste:1, ID:6:01, MAC:01)
47. Switch 6:01 recibe por el puerto 01 la BPDU (Raíz:4:00, Coste:0, ID:4:00, MAC:23)
48. Switch 6:01 recibe por el puerto 15 la BPDU (Raíz:4:00, Coste:2, ID:4:48, MAC:48)



Una vez decidido el switch raíz, los switches toman las siguientes decisiones (volvemos a indicar la figura por comodidad):

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej1/ejercicio1.png




El switch 4:48 toma estas decisiones:

* El puerto con la MAC 48 se convierte en raíz. 




El switch 6:03 toma estas decisiones:

* El puerto con la MAC 76 se convierte en raíz. 
* El puerto con la MAC 03 se convierte en designado. Es el mejor del segmento con un coste de 1 frente un coste de 2 que ofrece el puerto 58.




El switch 4:00 toma estas decisiones:

* 4:00 es raiz y pone todos sus puertos a designado.




El switch 6:01 toma estas decisiones:

* El puerto con la MAC 01 se convierte en raíz. 
* El puerto con la MAC 15 se convierte en designado. Es el mejor del segmento con un coste de 1 frente un coste de 2 que ofrece el puerto 48.


        