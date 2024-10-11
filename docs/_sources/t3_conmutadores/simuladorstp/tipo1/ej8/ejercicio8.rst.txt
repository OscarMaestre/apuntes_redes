
STP Ejercicio 8, dificultad 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Dada la red de switches que se muestra en la figura:

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej8/ejercicio8.png

Indicar el estado final en que quedarán todos los puertos de todos los switches.

Empezando por los eventos de envío, recepción y determinación de cual es el switch raíz la lista de sucesos sería esta:


1. Switch 4:61 envía por el puerto 92 la BPDU (Raíz:4:61, Coste:0, ID:4:61, MAC:92)
2. Switch 4:61 envía por el puerto 61 la BPDU (Raíz:4:61, Coste:0, ID:4:61, MAC:61)
3. Switch 3:33 envía por el puerto 97 la BPDU (Raíz:3:33, Coste:0, ID:3:33, MAC:97)
4. Switch 3:33 envía por el puerto 33 la BPDU (Raíz:3:33, Coste:0, ID:3:33, MAC:33)
5. Switch 5:44 envía por el puerto 44 la BPDU (Raíz:5:44, Coste:0, ID:5:44, MAC:44)
6. Switch 5:44 envía por el puerto 99 la BPDU (Raíz:5:44, Coste:0, ID:5:44, MAC:99)
7. Switch 1:34 envía por el puerto 34 la BPDU (Raíz:1:34, Coste:0, ID:1:34, MAC:34)
8. Switch 1:34 envía por el puerto 76 la BPDU (Raíz:1:34, Coste:0, ID:1:34, MAC:76)
9. Switch 4:61 recibe por el puerto 92 la BPDU (Raíz:1:34, Coste:0, ID:1:34, MAC:76). La raíz 1:34 es mejor, así que se anota como nueva raíz.
10. Switch 4:61 recibe por el puerto 61 la BPDU (Raíz:3:33, Coste:0, ID:3:33, MAC:97)
11. Switch 3:33 recibe por el puerto 97 la BPDU (Raíz:4:61, Coste:0, ID:4:61, MAC:61)
12. Switch 3:33 recibe por el puerto 33 la BPDU (Raíz:5:44, Coste:0, ID:5:44, MAC:44)
13. Switch 5:44 recibe por el puerto 44 la BPDU (Raíz:3:33, Coste:0, ID:3:33, MAC:33). La raíz 3:33 es mejor, así que se anota como nueva raíz.
14. Switch 5:44 recibe por el puerto 99 la BPDU (Raíz:1:34, Coste:0, ID:1:34, MAC:34). La raíz 1:34 es mejor, así que se anota como nueva raíz.
15. Switch 1:34 recibe por el puerto 34 la BPDU (Raíz:5:44, Coste:0, ID:5:44, MAC:99)
16. Switch 1:34 recibe por el puerto 76 la BPDU (Raíz:4:61, Coste:0, ID:4:61, MAC:92)
17. Switch 4:61 envía por el puerto 92 la BPDU (Raíz:1:34, Coste:1, ID:4:61, MAC:92)
18. Switch 4:61 envía por el puerto 61 la BPDU (Raíz:1:34, Coste:1, ID:4:61, MAC:61)
19. Switch 3:33 envía por el puerto 97 la BPDU (Raíz:3:33, Coste:0, ID:3:33, MAC:97)
20. Switch 3:33 envía por el puerto 33 la BPDU (Raíz:3:33, Coste:0, ID:3:33, MAC:33)
21. Switch 5:44 envía por el puerto 44 la BPDU (Raíz:1:34, Coste:1, ID:5:44, MAC:44)
22. Switch 5:44 envía por el puerto 99 la BPDU (Raíz:1:34, Coste:1, ID:5:44, MAC:99)
23. Switch 1:34 envía por el puerto 34 la BPDU (Raíz:1:34, Coste:0, ID:1:34, MAC:34)
24. Switch 1:34 envía por el puerto 76 la BPDU (Raíz:1:34, Coste:0, ID:1:34, MAC:76)
25. Switch 4:61 recibe por el puerto 92 la BPDU (Raíz:1:34, Coste:0, ID:1:34, MAC:76)
26. Switch 4:61 recibe por el puerto 61 la BPDU (Raíz:3:33, Coste:0, ID:3:33, MAC:97)
27. Switch 3:33 recibe por el puerto 97 la BPDU (Raíz:1:34, Coste:1, ID:4:61, MAC:61). La raíz 1:34 es mejor, así que se anota como nueva raíz.
28. Switch 3:33 recibe por el puerto 33 la BPDU (Raíz:1:34, Coste:1, ID:5:44, MAC:44). Llegó de nuevo la raíz 1:34 pero por un puerto con menor MAC (33), así que ese puerto se anota como posible puerto raíz
29. Switch 5:44 recibe por el puerto 44 la BPDU (Raíz:3:33, Coste:0, ID:3:33, MAC:33)
30. Switch 5:44 recibe por el puerto 99 la BPDU (Raíz:1:34, Coste:0, ID:1:34, MAC:34)
31. Switch 1:34 recibe por el puerto 34 la BPDU (Raíz:1:34, Coste:1, ID:5:44, MAC:99)
32. Switch 1:34 recibe por el puerto 76 la BPDU (Raíz:1:34, Coste:1, ID:4:61, MAC:92)
33. Switch 4:61 envía por el puerto 92 la BPDU (Raíz:1:34, Coste:1, ID:4:61, MAC:92)
34. Switch 4:61 envía por el puerto 61 la BPDU (Raíz:1:34, Coste:1, ID:4:61, MAC:61)
35. Switch 3:33 envía por el puerto 97 la BPDU (Raíz:1:34, Coste:2, ID:3:33, MAC:97)
36. Switch 3:33 envía por el puerto 33 la BPDU (Raíz:1:34, Coste:2, ID:3:33, MAC:33)
37. Switch 5:44 envía por el puerto 44 la BPDU (Raíz:1:34, Coste:1, ID:5:44, MAC:44)
38. Switch 5:44 envía por el puerto 99 la BPDU (Raíz:1:34, Coste:1, ID:5:44, MAC:99)
39. Switch 1:34 envía por el puerto 34 la BPDU (Raíz:1:34, Coste:0, ID:1:34, MAC:34)
40. Switch 1:34 envía por el puerto 76 la BPDU (Raíz:1:34, Coste:0, ID:1:34, MAC:76)
41. Switch 4:61 recibe por el puerto 92 la BPDU (Raíz:1:34, Coste:0, ID:1:34, MAC:76)
42. Switch 4:61 recibe por el puerto 61 la BPDU (Raíz:1:34, Coste:2, ID:3:33, MAC:97)
43. Switch 3:33 recibe por el puerto 97 la BPDU (Raíz:1:34, Coste:1, ID:4:61, MAC:61)
44. Switch 3:33 recibe por el puerto 33 la BPDU (Raíz:1:34, Coste:1, ID:5:44, MAC:44)
45. Switch 5:44 recibe por el puerto 44 la BPDU (Raíz:1:34, Coste:2, ID:3:33, MAC:33)
46. Switch 5:44 recibe por el puerto 99 la BPDU (Raíz:1:34, Coste:0, ID:1:34, MAC:34)
47. Switch 1:34 recibe por el puerto 34 la BPDU (Raíz:1:34, Coste:1, ID:5:44, MAC:99)
48. Switch 1:34 recibe por el puerto 76 la BPDU (Raíz:1:34, Coste:1, ID:4:61, MAC:92)



Una vez decidido el switch raíz, los switches toman las siguientes decisiones (volvemos a indicar la figura por comodidad):

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej8/ejercicio8.png




El switch 4:61 toma estas decisiones:

* El puerto con la MAC 92 se convierte en raíz. 
* El puerto con la MAC 61 se convierte en designado. Es el mejor del segmento con un coste de 1 frente un coste de 2 que ofrece el puerto 97.




El switch 3:33 toma estas decisiones:

* El puerto con la MAC 33 se convierte en raíz. 




El switch 5:44 toma estas decisiones:

* El puerto con la MAC 99 se convierte en raíz. 
* El puerto con la MAC 44 se convierte en designado. Es el mejor del segmento con un coste de 1 frente un coste de 2 que ofrece el puerto 33.




El switch 1:34 toma estas decisiones:

* 1:34 es raiz y pone todos sus puertos a designado.


        