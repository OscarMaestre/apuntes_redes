#!/usr/bin/python3 
import inspect
from random import randint, shuffle

from creadorimagenes.CreadorImagen import CreadorImagen, CreadorRoutersCuadrados
from os import mkdir
from os.path import join, basename, sep
from pathlib import Path
class Evento(object):
    def __init__(self) -> None:
        self.eventos=[]
    def anadir_evento(self, evento):
        self.eventos.append(evento)
    def __str__(self) -> str:
        return ".".join(self.eventos)

class ListaEventos(object):
    def __init__(self) -> None:
        self.lista=[]
        
    def anadir_mensaje(self, mensaje):
        self.evento_actual.anadir_evento(mensaje)
    def anadir_evento(self):
        self.evento_actual=Evento()
        self.lista.append(self.evento_actual)
    def anadir_evento_con_mensaje(self, mensaje):
        self.evento_actual=Evento()
        self.evento_actual.anadir_evento(mensaje)
        self.lista.append(self.evento_actual)
    def __str__(self) -> str:
        texto="\n"
        for i in range(0, len(self.lista)):
            texto+= str(i+1)+". "+ str(self.lista[i])+"\n"
        return texto


class BPDU(object):
    def __init__(self, raiz, coste, yo, mac) -> None:
        self.raiz=raiz
        self.coste=coste
        self.yo=yo
        self.mac=mac
    def __str__(self) -> str:
        textos=list(map(str, [self.raiz, self.coste, self.yo, self.mac]))
        plantilla_mensaje="(Raíz:{0}, Coste:{1}, ID:{2}, MAC:{3})"
        mensaje=plantilla_mensaje.format(textos[0], textos[1], textos[2], textos[3])
        return mensaje
    def recalcular(self, bpdu):
        if bpdu.raiz<self.raiz:
            nueva_bpdu=BPDU(bpdu.raiz, bpdu.coste+1, self.yo, self.mac)
            return nueva_bpdu
        else:
            return self

    def __eq__(self, bpdu: object) -> bool:
        if bpdu==None:
            return False
        if self.raiz!=bpdu.raiz:
            return False
        if self.coste!=bpdu.coste:
            return False
        if self.yo!=bpdu.yo:
            return False
        if self.mac!=bpdu.mac:
            return False
        return True

class Puerto(object):
    ESTADO_APRENDIENDO=1
    ESTADO_RAIZ=ESTADO_APRENDIENDO+1
    ESTADO_DESIGNADO=ESTADO_RAIZ+1
    ESTADO_BLOQUEADO=ESTADO_DESIGNADO+1
    #Posibles estados de costes en los puertos
    COSTE_MAYOR=ESTADO_BLOQUEADO+1
    COSTE_IGUAL=COSTE_MAYOR+1
    COSTE_MENOR=COSTE_IGUAL+1
    def __init__(self, mac) -> None:
        self.mac=mac
        self.buffer_envio=None
        self.buffer_recepcion=None
        self.switch=None
        self.puerto_asociado=None
        self.estado=Puerto.ESTADO_APRENDIENDO

    def __lt__(self, otro_puerto):
        return self.mac < otro_puerto.mac

    def comprobar_error_puerto_ya_establecido(self):
        return 
        if self.estado!=Puerto.ESTADO_APRENDIENDO:
            raise Exception("El puerto ya estaba establecido!!")
    def poner_raiz(self):
        self.comprobar_error_puerto_ya_establecido()
        self.estado=Puerto.ESTADO_RAIZ
    def poner_designado(self):
        self.comprobar_error_puerto_ya_establecido()
        self.estado=Puerto.ESTADO_DESIGNADO
    def poner_bloqueado(self):
        self.comprobar_error_puerto_ya_establecido()
        self.estado=Puerto.ESTADO_BLOQUEADO

    def esta_establecido(self):
        if self.enviar!=Puerto.ESTADO_APRENDIENDO:
            return True
        return False

    def get_raiz_recibida(self):
        """Indica la raíz que se ha recibido en este puerto"""
        return self.buffer_recepcion.raiz

    def enviar(self, bpdu):
        self.buffer_envio=bpdu
        self.puerto_asociado.buffer_recepcion=bpdu
    def recibir(self, bpdu):
        self.buffer_recepcion=bpdu
    def asociar_switch(self, switch):
        self.switch=switch
    def asociar_puerto(self, puerto):
        self.puerto_asociado=puerto

    def get_puerto_asociado(self):
        return self.puerto_asociado
    def get_coste_enviado(self):
        return self.buffer_envio.coste
    def get_coste_recibido(self):
        return self.buffer_recepcion.coste
    def __str__(self) -> str:
        return self.mac

class Switch(object):
    def __init__(self, identificador, lista_puertos, lista_eventos) -> None:
        
        self.coste=0
        
        self.puertos=lista_puertos
        self.lista_eventos=lista_eventos
        self.lista_decisiones=[]
        self.set_mi_prioridad(identificador)
        self.evento_actual=None
        self.menor_mac=self.get_menor_mac()
        self.puerto_raiz=None
        self.soy_raiz=False

    
    def set_mi_prioridad(self, numero):
        """Establece la prioridad del switch en formato Prioridad:Menor mac"""
        plantilla="{0}:{1}"
        prioridad=plantilla.format(str(numero), self.get_menor_mac())
        self.identificador_yo=prioridad
        self.identificador_raiz=prioridad
    
    def get_decisiones_formateadas(self):
        """Devuelve en forma de cadena la lista de decisiones sobre puertos
        que tomó este switch"""
        texto=""
        texto+="\n\n\nEl switch "+ self.identificador_yo+ " toma estas decisiones:\n\n"
        for d in self.lista_decisiones:
            texto+="* "+d+"\n"
        return texto

    def get_menor_mac(self):
        """Devuelve la MAC más pequeña del switch"""
        puerto_menor=min(self.puertos)
        macs=list(map(str, self.puertos))
        return puerto_menor.mac
        #print(macs)
        #print("La menor es:"+puerto_menor.mac)
    
    def ha_terminado(self):
        """Nos dice si todos los puertos han sido establecidos"""
        for puerto in self.puertos:
            if puerto.estado==Puerto.ESTADO_APRENDIENDO:
                return False
        return True
    
    #Se compara p1 con su puerto asociado y se nos dice 
    #si el coste es mayor, igual o menor
    def evaluar_coste(self, puerto):
        """Nos dice si este puerto tiene el mayor coste o no del segmento
        
        Parámetros:

        puerto -- puerto que queremos analizar
        """
        coste_puerto=self.coste
        coste_asociado=puerto.get_coste_recibido()
        # informe_envio="El puerto {0} envio un coste de {1}"
        # informe_recep="El puerto {0} recib un coste de {1}"
        # print(informe_envio.format(puerto, coste_puerto))
        # print(informe_recep.format(puerto, coste_asociado))
        if coste_puerto>coste_asociado:
            return Puerto.COSTE_MAYOR
        if coste_puerto==coste_asociado:
            return Puerto.COSTE_IGUAL
        if coste_puerto<coste_asociado:
            return Puerto.COSTE_MENOR
        

    def actuar_si_somos_raiz(self):
        """Este switch comprueba si es el raíz y si es así pone
        todos los puertos a DESIGNADO"""
        if self.identificador_raiz==self.identificador_yo:
            #Si ya anotamos antes que éramos raíz, lo ignoramos
            #si no ignoramos aparecerán eventos dos veces
            if self.soy_raiz:
                return 
            #Si llegamos aquí sabemos por primera vez que
            #somos la raíz
            self.soy_raiz=True
            self.lista_decisiones.append(
                str(self.identificador_raiz) + 
                " es raiz y pone todos sus puertos a designado."
            )

            for p in self.puertos:
                if not p.esta_establecido():
                    p.poner_designado()
            return True #Si somos la raíz
        #Si llegamos aquí es que no somos la raíz. Terminamos
        #y avisamos de que no somos la raíz
        return False

    def establecer_puerto_raiz(self):
        """El switch busca cual de los puertos tiene el mejor camino
        a la raíz y lo marca como puerto raíz"""

    def bloquear_puertos_restantes(self):
        """Se bloque cualquier puerto que estuviese en el estado APRENDIENDO"""
        for p in self.puertos:
            if p.estado==Puerto.ESTADO_APRENDIENDO:
                p.bloquear_puerto()

    def establecer_puerto_raiz(self):
        """Se marca como puerto raíz la MAC que ofrece un menor coste
        a la raíz"""
        plantilla="El puerto con la MAC {0} se convierte en raíz. "
        
        mensaje=plantilla.format( self.puerto_raiz  )
        self.lista_decisiones.append(mensaje)
        self.puerto_raiz.poner_raiz()
        #Fin del for

    def actuar_si_coste_menor_en_segmento(self, puerto):
        """Examina si este puerto es el mejor del segmento y si es así
        se marca el puerto como designado"""
        coste=self.evaluar_coste(puerto)
        #Caso 1 ¿el coste de este puerto es el mejor del segmento?
        if coste==Puerto.COSTE_MENOR:
            #print("{0} es el mejor de su segmento".format(str(puerto)))
            #Si es asi, este puerto es el designado
            plantilla="El puerto con la MAC {0} se convierte en designado. "
            plantilla+="Es el mejor del segmento con un coste de {1} frente "
            plantilla+="un coste de {2} que ofrece el puerto {3}."
            mensaje=plantilla.format(
                puerto, puerto.get_coste_enviado(), puerto.get_coste_recibido(), 
                puerto.get_puerto_asociado()
            )
            self.lista_decisiones.append(mensaje)
            #print("Designado..."+str(p))
            puerto.poner_designado()

    def establecer_puertos(self):
        """Repasa todos los puertos del switch decidiendo si los
        tiene que poner a BLOQUEADO, DESIGNADO o RAÍZ"""
        

        if self.actuar_si_somos_raiz():
            #Si somos la raíz se habrá puesto todo a designado y acabamos
            return 
        
        #Si llegamos aquí, no somos raíz así que hay que marcar
        #un puerto como raíz
        self.establecer_puerto_raiz()

        #Si llegamos aquí, este switch no es raíz y
        #ya hemos marcado un puerto raíz. Así que ahora
        #tiene que ir puerto por puerto y comprobar.
        #1.Si su puerto ofrece un coste MENOR que el coste
        #del otro puerto del segmento, ponemos el puerto a DESIGNADO
        #2.Si el puerto ofrece un coste IGUAL que el del otro
        #puerto entonces se mira la MAC. Si este puerto tiene 
        #UNA MAC MENOR se pone el puerto a designado. Si este
        #puerto tiene una MAC MAYOR, pierde y el puerto se bloquea
        #3. Si el puerto tiene un coste MAYOR, el puerto pierde
        #y se bloquea
        
        for p in self.puertos:
            #Ignoramos los puertos que ya estuvieran establecidos
            if p.estado!=Puerto.ESTADO_APRENDIENDO:
                continue
            coste=self.evaluar_coste(p)
            self.actuar_si_coste_menor_en_segmento(p)

            # #Caso 1 ¿el coste de este puerto es el mejor del segmento?
            # if coste==Puerto.COSTE_MENOR:
            #     #Si es asi, este puerto es el designado
            #     plantilla="El puerto con la MAC {0} se convierte en designado. "
            #     plantilla+="Es el mejor del segmento con un coste de {1} frente "
            #     plantilla+="un coste de {2} que ofrece el puerto {3}."
            #     mensaje=plantilla.format(
            #         p, p.get_coste_enviado(), p.get_coste_recibido(), 
            #         p.get_puerto_asociado()
            #     )
            #     self.lista_decisiones.append(mensaje)
            #     #print("Designado..."+str(p))
            #     p.poner_designado()
            #     #Pasamos al siguiente puerto
            # #Caso 3 ¿El coste de este puerto es el peor?
            # if coste==Puerto.COSTE_MAYOR:
            #     plantilla="El puerto con la MAC {0} se bloquea. "
            #     # plantilla+="Es el peor del segmento con un coste de {1} frente "
            #     # plantilla+="un coste de {2} que ofrece el puerto {3}."
            #     mensaje=plantilla.format(
            #         p, p.get_coste_enviado(), p.get_coste_recibido(), 
            #         p.get_puerto_asociado()
            #     )
            #     self.lista_decisiones.append(mensaje)
            #     #print("Bloqueado..."+str(p))
            #     p.poner_bloqueado()
            # #Caso 2 ¿El coste de este puerto es el mismo que
            # #el otro puerto del segmento=
            # if coste==Puerto.COSTE_IGUAL:
            #     #print("Empate en coste")
            #     #Pues si es así, entonces hay que desempatar
            #     #y mirar las macs
            #     mac_nuestra=p.mac
            #     mac_otro   =p.get_puerto_asociado().mac
            #     if mac_nuestra<mac_otro:
            #         plantilla="El puerto con la MAC {0} se convierte en designado. "
            #         plantilla+="Hay un empate en coste (que es {1}) pero su mac ({2}) es"
            #         plantilla+=" menor que la del otro puerto ({3}) "
                    
            #         mensaje=plantilla.format(
            #             p, p.get_coste_enviado(), p.mac,
            #             p.get_puerto_asociado()
            #         )
            #         self.lista_decisiones.append(mensaje)
                    
            #         p.poner_designado()
            #     else:
            #         plantilla="El puerto con la MAC {0} se bloquea. "
            #         plantilla+="Hay un empate en coste (que es {1}) pero su mac ({2}) es"
            #         plantilla+=" mayor que la del otro puerto ({3}) "
                    
            #         mensaje=plantilla.format(
            #             p, p.get_coste_enviado(), p.mac,
            #             p.get_puerto_asociado()
            #         )
            #         self.lista_decisiones.append(mensaje)
                    
            #         p.poner_bloqueado()
                    


    def comprobar_si_puerto_contiene_raiz_mejor(self, puerto):
        bpdu_recibida=puerto.buffer_recepcion
        raiz_recibida=puerto.get_raiz_recibida()
        #Si encontramos algo mejor, lo anotamos
        if raiz_recibida<self.identificador_raiz:
            self.identificador_raiz=raiz_recibida
            self.puerto_raiz=puerto
            self.coste=bpdu_recibida.coste+1
            plantilla_mensaje=" La raíz {0} es mejor, así que se anota como nueva raíz."
            mensaje=plantilla_mensaje.format(raiz_recibida)
            self.lista_eventos.anadir_mensaje(mensaje)
            return True
        return False

    def comprobar_si_puerto_contiene_raiz_igual(self, puerto):
        """Comprueba si en este puerto hay una raíz igual a la que 
        teníamos pero que ha llegado por una MAC mejor"""
        
        #Si no hay puerto raíz aún, no hay nada que comparar
        if self.puerto_raiz==None:
            return False
        bpdu_recibida=puerto.buffer_recepcion
        raiz_recibida=puerto.get_raiz_recibida()
        raiz_es_igual=(raiz_recibida==self.identificador_raiz)
        coste_es_igual=(bpdu_recibida.coste+1)==self.coste
        mac_es_menor=puerto.mac < self.puerto_raiz.mac
        #Cambiamos al nuevo puerto como raíz si se cumple todo esto
        hay_que_cambiar=raiz_es_igual and coste_es_igual and mac_es_menor
        #Si la raíz es igual, y con coste igual pero viene por una MAC mejor
        if  hay_que_cambiar:
            self.identificador_raiz=raiz_recibida
            self.puerto_raiz=puerto
            self.coste=bpdu_recibida.coste+1
            plantilla_mensaje=" Llegó de nuevo la raíz {0} pero por un puerto con menor MAC ({1}), así que ese puerto se anota como posible puerto raíz"
            mensaje=plantilla_mensaje.format(raiz_recibida, puerto.mac)
            self.lista_eventos.anadir_mensaje(mensaje)
            return True
        return False

    def reevaluar_raiz(self):
        """Se examina lo que ha llegado a este switch y si la BPDU indica que
        tenemos una raíz mejor, tomamos nota del hecho"""

        #Examinamos si hemos recibido alguna raiz mejor
        #que la que tenemos apuntada. Si encontramos algo mejor, lo anotamos
        hemos_encontrado_raiz_mejor=False
        hemos_encontrado_puerto_mejor=False
        for puerto in self.puertos:
            
            bpdu_recibida=puerto.buffer_recepcion
            plantilla_mensaje="Switch {0} recibe por el puerto {1} la BPDU {2}"
            mensaje=plantilla_mensaje.format(self.identificador_yo, puerto.mac, bpdu_recibida)
            self.lista_eventos.anadir_evento_con_mensaje(mensaje)
            self.comprobar_si_puerto_contiene_raiz_mejor(puerto)
            self.comprobar_si_puerto_contiene_raiz_igual(puerto)    
        
        
        #Hay que volver a repasar los puertos por si hay uno que tenga
        #la misma raíz que otro con el mismo coste pero con una mac mejor
        for puerto in self.puertos:
            self.comprobar_si_puerto_contiene_raiz_igual(puerto)    
        #Fin del for
        

    def get_lista_bids_recibidas(self):
        """Devuelve un vector con todas las BPDU recibidas"""
        #Recuperamos todos los BID que hay en los puertos
        bids=[]
        for p in self.puertos:
            bpdu_recibida=p.buffer_recepcion
            bids.append(bpdu_recibida.raiz)
        # print("La lista de bpdus es:")
        # print(bids)
        # print("------------")
        return bids

    def todas_bids_iguales(self, bids):
        """Se examina un vector con las BPDU recibidas por el switch para
        ver si todas indican el mismo switch raíz"""
        #Si todas son el mismo BID, sí, sabemos la raíz
        #Examinamos la primera y la comparamos con las demas
        bid_inicial=bids[0]
        for bid in bids:
            #Si hay alguna distina si encontramos la raiz
            if bid!=bid_inicial:
                return False
        #Si llegamos aquí son todas iguales
        return True

    def hay_acuerdo_sobre_la_raiz(self):
        """Nos dice si este switch tiene completamente claro quien es la raíz"""
        bids_recibidas=self.get_lista_bids_recibidas()
        #print("Examinado la raíz en switch "+self.identificador_yo+"-->"+self.identificador_raiz)
        #print("Las bids son")
        #print(str(bids_recibidas))
        if not self.todas_bids_iguales(bids_recibidas):
            return (-1, False)
        raiz=str(bids_recibidas[0])
        
        return (raiz, True)


    def es_raiz(self):
        """Nos dice si este switch es el que ha sido elegido como raíz """
        bids=self.get_lista_bids_recibidas()
        if not self.hay_acuerdo_sobre_la_raiz(bids):
            return False
        if self.todas_bids_iguales(bids):
            if bids[0]==self.identificador_yo:
                return True
            else:
                return False

    def enviar_bpdu(self, puerto):
        """Envía a través de un cierto puerto la BPDU correspondiente"""
        #Construimos la BPDU
        if self.identificador_raiz!=self.identificador_yo:
            bpdu=BPDU(self.identificador_raiz, self.coste, self.identificador_yo, puerto.mac)
        else:
            bpdu=BPDU(self.identificador_raiz, 0, self.identificador_yo, puerto.mac)
            
        #print(id_switch+" enviando por puerto "+puerto.mac)
        #print(bpdu)
        plantilla_mensaje="Switch {0} envía por el puerto {1} la BPDU {2}"
        mensaje=plantilla_mensaje.format(self.identificador_yo, puerto.mac, bpdu)
        self.lista_eventos.anadir_evento_con_mensaje(mensaje)
        
        puerto.enviar(bpdu)


class Iteracion(object):
    def __init__(self, switch, puerto) -> None:
        self.switch=switch
        self.puerto=puerto
    def ejecutar(self):
        self.switch.enviar_bpdu(self.puerto)

class Red(object):
    def __init__(self, switches, puertos, iteraciones, lista_eventos) -> None:
        self.switches=switches
        self.puertos=puertos
        self.iteraciones=iteraciones
        self.lista_eventos=lista_eventos
        #Utilizamos esto para saber si hay acuerdo
        self.acuerdo_alcanzado=False
        self.switch_raiz=None
        
    def hacer_envios(self):
        for i in self.iteraciones:
            i.ejecutar()
    
    def evaluar_switches(self):
        for s in self.switches:
            s.reevaluar_raiz()
            
    def get_cadena_situacion_actual_raices(self):
        """Devuelve una cadena donde los switches indican quien piensa
        que es la raíz"""
        opiniones=[]
        for s in self.switches:
            plantilla="* El switch {0} piensa que la raíz es {1}"
            texto=plantilla.format(s.identificador_yo, s.identificador_raiz)
            opiniones.append(texto)
        #print("Viendo estado global")
        estado_global="La red tiene en su variable hay_acuerdo el valor:"+str(self.acuerdo_alcanzado)+"\n"
        txt_opiniones="\n".join(opiniones)
        return estado_global+txt_opiniones

    def evaluar_estado_raiz_en_switches(self):
        """Determina si todos los switches están de acuerdo 
        en quien es la raíz. Si es así, se establecen los
        puertos y si no salimos"""
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        #print('Llamador name:', calframe[1][3])
        
        raices=[]
        for s in self.switches:
            
            
            (raiz, hay_acuerdo)=s.hay_acuerdo_sobre_la_raiz()
            plantilla_mensaje="Examinada raíz en switch {0}--Aparece la {1}"
            #print(plantilla_mensaje.format(s.identificador_yo, s.identificador_raiz))
            if not hay_acuerdo:
                #Si ni siquiera hay acuerdo dentro de un switch salimos
                return
            if hay_acuerdo:
                #Si hay acuerdo metemos esa raíz en el vector
                raices.append(raiz)
        #print("Examinando raices:"+str(raices))
        #Si llegamos aquí tenemos un vector de raíces, pero 
        #habrá que ver si todos son iguales
        for pos in range (0, len(raices)-1):
            raiz=raices[pos]
            raiz_sig=raices[pos+1]
            if raiz!=raiz_sig:
                return 
        #Si llegamos aquí no había ninguna distinta, 
        #Tomamos nota del acuerdo, de quien es la raiz y establecemos los puertos
        self.acuerdo_alcanzado=True
        self.switch_raiz=raices[0]
        #print("Hay acuerdo, estableciendo puertos...")
        self.establecer_puertos_en_switches()
        return 
                

    def get_lista_decisiones(self):
        lista=[]
        for s in self.switches:
            lista.append(s.lista_decisiones)
        return lista

    def establecer_puertos_en_switches(self):
        # curframe = inspect.currentframe()
        # calframe = inspect.getouterframes(curframe, 2)
        # print('Llamador name:', calframe[1][3])
        for s in self.switches:
            s.establecer_puertos()
    
class ConstructorRedes(object):
    def __init__(self) -> None:
        pass
    
    def asociar_puertos(self, puerto1, puerto2):
        puerto1.asociar_puerto(puerto2)
        puerto2.asociar_puerto(puerto1)

    def get_red(self):
        pass

    def generar_macs_azar(self, num_macs):
        simbolos=["0","1", "2", "3", "4", "5", "6", "7", "8", "9"]
        macs=[]
        for s1 in simbolos:
            for s2 in simbolos:
                macs.append(s1+s2)
        shuffle(macs)
        return macs[0:num_macs]
    

class ConstructorCuadradoCuatroLados(ConstructorRedes):
    

    

    def __init__(self) -> None:
        super().__init__()
        self.lista_eventos=ListaEventos()
        macs=self.generar_macs_azar(8)
        self.puerto_01=Puerto(macs[0])
        self.puerto_02=Puerto(macs[1])
        self.Switch1=Switch(randint(1,6), [self.puerto_01, self.puerto_02], self.lista_eventos)

        self.puerto_03=Puerto(macs[2])
        self.puerto_04=Puerto(macs[3])
        self.Switch2=Switch(randint(1,6), [self.puerto_03, self.puerto_04], self.lista_eventos)

        self.puerto_05=Puerto(macs[4])
        self.puerto_06=Puerto(macs[5])
        self.Switch3=Switch(randint(1,6), [self.puerto_05, self.puerto_06], self.lista_eventos)

        self.puerto_07=Puerto(macs[6])
        self.puerto_08=Puerto(macs[7])
        self.Switch4=Switch(randint(1,6), [self.puerto_07, self.puerto_08], self.lista_eventos)


        self.asociar_puertos(self.puerto_01, self.puerto_08)
        self.asociar_puertos(self.puerto_02, self.puerto_03)
        self.asociar_puertos(self.puerto_04, self.puerto_05)
        self.asociar_puertos(self.puerto_06, self.puerto_07)

        self.iteraciones=[]
        self.iteraciones.append(Iteracion(self.Switch1, self.puerto_01))
        self.iteraciones.append(Iteracion(self.Switch1, self.puerto_02))

        self.iteraciones.append(Iteracion(self.Switch2, self.puerto_03))
        self.iteraciones.append(Iteracion(self.Switch2, self.puerto_04))

        self.iteraciones.append(Iteracion(self.Switch3, self.puerto_05))
        self.iteraciones.append(Iteracion(self.Switch3, self.puerto_06))

        self.iteraciones.append(Iteracion(self.Switch4, self.puerto_07))
        self.iteraciones.append(Iteracion(self.Switch4, self.puerto_08))

        self.switches=[self.Switch1, self.Switch2, self.Switch3, self.Switch4]
        self.puertos=[self.puerto_01, self.puerto_02, self.puerto_03, self.puerto_04,
                self.puerto_05, self.puerto_06, self.puerto_07, self.puerto_08]

        self.red=Red(self.switches, self.puertos, self.iteraciones, self.lista_eventos)
        
    def set_valores_prueba(self):
        """Establece valores de prueba conocidos para los test de unidad"""
        #La red de prueba es asi
        #         1a               0b    
        #   1:1a--------------------- 3:0a
        #     | 1b                     | 0a
        #     |                        |
        #     | 1c                2a   | 2b
        #    2:1c-------------------- 1:2a
        #         1d
        self.puerto_01.mac="1a"
        self.puerto_02.mac="1b"
        self.puerto_03.mac="1c"
        self.puerto_04.mac="1d"
        self.puerto_05.mac="2a"
        self.puerto_06.mac="2b"
        self.puerto_07.mac="0a"
        self.puerto_08.mac="0b"
        self.Switch1.set_mi_prioridad(1)
        self.Switch2.set_mi_prioridad(2)
        self.Switch3.set_mi_prioridad(1)
        self.Switch4.set_mi_prioridad(3)
        

    def set_valores_prueba_2(self):
        """Establece valores de prueba conocidos para los test de unidad"""
        #La red de prueba es asi
        #         7f               7a    
        #   5:1a--------------------- 3:0a
        #     | 1b                     | 0a
        #     |                        |
        #     | 1c                2a   | 2b
        #    2:1c-------------------- 1:2a
        #         1d
        self.puerto_01.mac="7f"
        self.puerto_02.mac="1b"
        self.puerto_03.mac="1c"
        self.puerto_04.mac="1d"
        self.puerto_05.mac="2a"
        self.puerto_06.mac="2b"
        self.puerto_07.mac="0a"
        self.puerto_08.mac="7a"
        self.Switch1.set_mi_prioridad(5)
        self.Switch2.set_mi_prioridad(2)
        self.Switch3.set_mi_prioridad(1)
        self.Switch4.set_mi_prioridad(3)
        
    def __str__(self) -> str:
        PLANTILLA="""
        
                 {1}               {11}    
           {0}--------------------- {9}
             | {2}                     | {10}
             |                        |
             |                        |
             | {4}                     | {8}
            {3}-------------------- {6}
                 {5}            {7}
"""
        return PLANTILLA.format(self.Switch1.identificador_yo, 
            self.puerto_01, self.puerto_02, 
            self.Switch2.identificador_yo, self.puerto_03, self.puerto_04,
            self.Switch3.identificador_yo, self.puerto_05, self.puerto_06,
            self.Switch4.identificador_yo, self.puerto_07, self.puerto_08)
        
    def generar_texto_ejercicio(self, num_ejercicio):
        
        PLANTILLA="""
STP Ejercicio {0}, dificultad 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Dada la red de switches que se muestra en la figura:

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej{0}/ejercicio{0}.png

Indicar el estado final en que quedarán todos los puertos de todos los switches.

Empezando por los eventos de envío, recepción y determinación de cual es el switch raíz la lista de sucesos sería esta:

{1}


Una vez decidido el switch raíz, los switches toman las siguientes decisiones (volvemos a indicar la figura por comodidad):

.. figure:: /t3_conmutadores/simuladorstp/tipo1/ej{0}/ejercicio{0}.png

{2}

        """
        textos_eventos=str(self.lista_eventos)
        decisiones=[]
        #print(c.red.switches)
        for s in self.red.switches:
            decisiones.append(s.get_decisiones_formateadas())
            
        textos_decisiones="\n".join(decisiones)

        texto_ejercicio=PLANTILLA.format(num_ejercicio, textos_eventos, textos_decisiones)
        return texto_ejercicio

    
    def formatear_lista_decisiones(self):
        texto=""
        # print(self.red.switches[0].lista_decisiones)
        # print(self.red.switches[1].lista_decisiones)
        # print(self.red.switches[2].lista_decisiones)
        # print(self.red.switches[3].lista_decisiones)
        
        
        for s in self.red.switches:
            texto+=s.get_decisiones_formateadas()+"\n"
        return texto+"\n"
    

    def generar_imagen(self, num_ejercicio):
        DIRECTORIO_BASE="tipo1"
        
        DIRECTORIO_EJ=join(DIRECTORIO_BASE, "ej"+str(num_ejercicio)+sep)
        FICHERO_TEXTO="ejercicio"+str(num_ejercicio)+".rst"
        RUTA_TEXTO=join(DIRECTORIO_EJ, FICHERO_TEXTO)
        FICHERO_IMAGEN_BASE="base1.png"
        FICHERO_IMAGEN_FINAL="ejercicio"+str(num_ejercicio)+".png"
        print("Fabricando:"+DIRECTORIO_EJ)
        mkdir(DIRECTORIO_EJ)
        RUTA_IMAGEN=join(DIRECTORIO_EJ, FICHERO_IMAGEN_FINAL)
        FICHERO_TTF=basename("Roboto.ttf")
        macs=[
            self.switches[0].puertos[0].mac, self.switches[0].puertos[1].mac, 
            self.switches[1].puertos[0].mac, self.switches[1].puertos[1].mac, 
            self.switches[2].puertos[0].mac, self.switches[2].puertos[1].mac, 
            self.switches[3].puertos[0].mac, self.switches[3].puertos[1].mac, 
        ]
        c=CreadorRoutersCuadrados(FICHERO_IMAGEN_BASE, RUTA_IMAGEN, FICHERO_TTF)
        c.poner_macs(macs)
        c.poner_prioridades(self.switches)
        c.get_resultado()
        with open(RUTA_TEXTO, "w") as fich:
            texto=self.generar_texto_ejercicio(num_ejercicio)
            fich.write(texto)

    def generar_ejercicio(self, num_ejercicio):
        self.simular()
        self.generar_imagen(num_ejercicio)
    def simular(self):
        self.red.hacer_envios()
        self.red.evaluar_switches()

        self.red.hacer_envios()
        self.red.evaluar_switches()

        self.red.hacer_envios()
        self.red.evaluar_switches()
        
        self.red.evaluar_estado_raiz_en_switches()



def prueba_depuracion():
        
    c=ConstructorCuadradoCuatroLados()
    c.set_valores_prueba_2()
    c.simular()
    print(c.red.get_cadena_situacion_actual_raices())
    lista_eventos=c.lista_eventos
    for e in lista_eventos.lista:
        print(e)

    
    red=c.red
    print("-----------------------RED------------------------")
    print(str(c))
    print("-----------------------FIN RED------------------------")

    print("----------------------------DECISIONES--------------")
    print(red.get_lista_decisiones())
    print("----------------------------FIN DECISIONES--------------")

    #print (c.switches[0].get_menor_mac())
    

    for s in c.switches:
        print(s.get_decisiones_formateadas())

    print (c.red.get_lista_decisiones())



def main():
    
    PLANTILLA="""
Anexo al tema 3:Ejercicios STP 
--------------------------------

{0}

"""
    texto=""
    NUM_EJERCICIOS=20
    for i in range(1, NUM_EJERCICIOS+1):
        c=ConstructorCuadradoCuatroLados()
        print("Generando:"+str(i))
        plantilla=".. include:: tipo1/ej{0}/ejercicio{0}.rst\n\n"
        texto=texto+plantilla.format(str(i))
        c.generar_ejercicio(i)

    with open("stp1.rst", "w") as fich:
        fich.write(PLANTILLA.format(texto))

if __name__=="__main__":
    #prueba_depuracion()
    main()