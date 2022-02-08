#!/usr/bin/python3 
from random import randint, shuffle


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
        self.evento_actual=Evento()
        self.lista.append(self.evento_actual)
    def anadir_mensaje(self, mensaje):
        self.evento_actual.anadir_evento(mensaje)
    def anadir_evento(self):
        self.evento_actual=Evento()
        self.lista.append(self.evento_actual)
    def anadir_evento_con_mensaje(self, mensaje):
        self.evento_actual=Evento()
        self.evento_actual.anadir_evento(mensaje)
        self.lista.append(self.evento_actual)
    


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
        
    def poner_raiz(self):
        self.estado=Puerto.ESTADO_RAIZ
    def poner_designado(self):
        self.estado=Puerto.ESTADO_DESIGNADO
    def poner_bloqueado(self):
        self.estado=Puerto.ESTADO_BLOQUEADO

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
        self.identificador_yo=identificador
        self.coste=0
        self.identificador_raiz=identificador
        self.puertos=lista_puertos
        self.lista_eventos=lista_eventos
        self.lista_decisiones=[]
        self.evento_actual=None


    def ha_terminado(self):
        for puerto in self.puertos:
            if puerto.estado==Puerto.ESTADO_APRENDIENDO:
                return False
        return True
    
    #Se compara p1 con su puerto asociado y se nos dice 
    #si el coste es mayor, igual o menor
    def evaluar_coste(self, puerto):
        coste_puerto=puerto.get_coste_enviado()
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
        

    def establecer_puertos(self):
        if self.identificador_raiz==self.identificador_yo:
            self.lista_decisiones.append(
                str(self.identificador_raiz) + 
                " es raiz y pone todos sus puertos a designado."
            )
            for p in self.puertos:
                p.poner_designado()
            return
        #Si llegamos aquí, este switch no es raíz y ahora
        #Tiene que ir puerto por puerto y comprobar.
        #1.Si su puerto ofrece un coste MENOR que el coste
        #del otro puerto del segmento, ponemos el puerto a DESIGNADO
        #2.Si el puerto ofrece un coste IGUAL que el del otro
        #puerto entonces se mira la MAC. Si este puerto tiene 
        #UNA MAC MENOR se pone el puerto a designado. Si este
        #puerto tiene una MAC MAYOR, pierde y el puerto se bloquea
        #3. Si el puerto tiene un coste MAYOR, el puerto pierde
        #y se bloquea
        for p in self.puertos:
            coste=self.evaluar_coste(p)
            #Caso 1 ¿el coste de este puerto es el mejor del segmento?
            if coste==Puerto.COSTE_MENOR:
                #Si es asi, este puerto es el designado
                plantilla="El puerto con la MAC {0} se convierte en designado. "
                plantilla+="Es el mejor del segmento con un coste de {1} frente "
                plantilla+="un coste de {1} que ofrece el puerto {2}."
                mensaje=plantilla.format(
                    p, p.get_coste_enviado(), p.get_coste_recibido, 
                    p.get_puerto_asociado()
                )
                self.lista_decisiones.append(mensaje)
                #print("Designado..."+str(p))
                p.poner_designado()
                #Pasamos al siguiente puerto
                continue
            #Caso 3 ¿El coste de este puerto es el peor?
            if coste==Puerto.COSTE_MENOR:
                plantilla="El puerto con la MAC {0} se bloquea. "
                plantilla+="Es el peor del segmento con un coste de {1} frente "
                plantilla+="un coste de {1} que ofrece el puerto {2}."
                mensaje=plantilla.format(
                    p, p.get_coste_enviado(), p.get_coste_recibido(), 
                    p.get_puerto_asociado()
                )
                self.lista_decisiones.append(mensaje)
                #print("Bloqueado..."+str(p))
                p.poner_bloqueado()
            #Caso 2 ¿El coste de este puerto es el mismo que
            #el otro puerto del segmento=
            if coste==Puerto.COSTE_IGUAL:
                #print("Empate en coste")
                #Pues si es así, entonces hay que desempatar
                #y mirar las macs
                mac_nuestra=p.mac
                mac_otro   =p.get_puerto_asociado().mac
                if mac_nuestra<mac_otro:
                    plantilla="El puerto con la MAC {0} se convierte en designado. "
                    plantilla+="Hay un empate en coste (que es {1}) pero su mac ({2}) es"
                    plantilla+=" menor que la del otro puerto ({3}) "
                    
                    mensaje=plantilla.format(
                        p, p.get_coste_enviado(), p.mac,
                        p.get_puerto_asociado()
                    )
                    self.lista_decisiones.append(mensaje)
                    
                    p.poner_designado()
                else:
                    plantilla="El puerto con la MAC {0} se bloquea. "
                    plantilla+="Hay un empate en coste (que es {1}) pero su mac ({2}) es"
                    plantilla+=" mayor que la del otro puerto ({3}) "
                    
                    mensaje=plantilla.format(
                        p, p.get_coste_enviado(), p.mac,
                        p.get_puerto_asociado()
                    )
                    self.lista_decisiones.append(mensaje)
                    
                    p.poner_bloqueado()


    def reevaluar_raiz(self, puerto):
        if puerto.buffer_recepcion==None:
            print("¡¡¡Error!!")
        #Examinamos lo que se envió y lo que se ha recibido
        bpdu_enviada=puerto.buffer_envio
        bpdu_recibida=puerto.buffer_recepcion
        plantilla_mensaje="Switch {0} recibe por el puerto {1} la BPDU {2}"
        mensaje=plantilla_mensaje.format(self.identificador_yo, puerto.mac, bpdu_recibida)
        self.lista_eventos.anadir_mensaje(mensaje)
        

        la_recibida_es_mejor=bpdu_recibida.raiz<self.identificador_raiz
        la_recibida_tiene_la_misma_prioridad=bpdu_recibida==self.identificador_raiz
        la_recibida_tiene_mejor_mac=(bpdu_recibida.mac<puerto.mac)
        hay_nueva_raiz=la_recibida_es_mejor or (la_recibida_tiene_la_misma_prioridad and la_recibida_tiene_mejor_mac)
        if hay_nueva_raiz:
            plantilla_mensaje="El switch {0} envió la BPDU {1} y recibió {2}, que es una raíz mejor, así que apunta que la nueva raíz es {3}"
            mensaje=plantilla_mensaje.format(self.identificador_yo, 
                    str(bpdu_enviada), str(bpdu_recibida), str(bpdu_recibida.raiz))
            
            self.lista_eventos.anadir_mensaje(mensaje)
            
            self.identificador_raiz=bpdu_recibida.raiz
            self.coste=bpdu_recibida.coste+1
        #Fin del if
        

    def get_lista_bids_recibidas(self):
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
        bids_recibidas=self.get_lista_bids_recibidas()
        if not self.todas_bids_iguales(bids_recibidas):
            return (-1, False)
        raiz=str(bids_recibidas[0])
        mensaje="En este punto hay convergencia. Todos los switches coinciden en que la raíz es el "+raiz
        self.lista_eventos.anadir_mensaje(mensaje)
        return (raiz, True)


    def es_raiz(self):
        bids=self.get_lista_bids_recibidas()
        if not self.hay_acuerdo_sobre_la_raiz(bids):
            return False
        if self.todas_bids_iguales(bids):
            if bids[0]==self.identificador_yo:
                return True
            else:
                return False

    def enviar_bpdu(self, puerto):
        #Construimos la BPDU
        bpdu=BPDU(self.identificador_raiz, self.coste, self.identificador_yo, puerto.mac)
        id_switch=str(self.identificador_yo)
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
    def hacer_envios(self):
        for i in self.iteraciones:
            i.ejecutar()
    
    def evaluar_switches(self):
        for s in self.switches:
            for p in s.puertos:
                self.lista_eventos.anadir_evento()
                s.reevaluar_raiz(p)

            # id_switch=s.identificador_yo
            # if s.hay_acuerdo_sobre_la_raiz():
            #     print(str(id_switch) + " tiene un acuerdo.")
            #     print()


    def evaluar_estado_raiz_en_switches(self):
        for s in self.switches:
            (raiz, hay_acuerdo)=s.hay_acuerdo_sobre_la_raiz()
            if hay_acuerdo:
                id_switch=str(s.identificador_yo)
                self.establecer_puertos_en_switches()
                return 
                

    def get_lista_decisiones(self):
        lista=[]
        for s in self. switches:
            lista.append(s.lista_decisiones)
        return lista

    def establecer_puertos_en_switches(self):
        for s in self.switches:
            s.establecer_puertos()
    
class ConstructorRedes(object):
    def __init__(self) -> None:
        pass

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
    

    def asociar_puertos(self, puerto1, puerto2):
        puerto1.asociar_puerto(puerto2)
        puerto2.asociar_puerto(puerto1)

    def __init__(self) -> None:
        super().__init__()
        self.lista_eventos=ListaEventos()
        macs=self.generar_macs_azar(8)
        puerto_01=Puerto(macs[0])
        puerto_02=Puerto(macs[1])
        Switch1=Switch(randint(1,6), [puerto_01, puerto_02], self.lista_eventos)

        puerto_03=Puerto(macs[2])
        puerto_04=Puerto(macs[3])
        Switch2=Switch(randint(1,6), [puerto_03, puerto_04], self.lista_eventos)

        puerto_05=Puerto(macs[4])
        puerto_06=Puerto(macs[5])
        Switch3=Switch(randint(1,6), [puerto_05, puerto_06], self.lista_eventos)

        puerto_07=Puerto(macs[6])
        puerto_08=Puerto(macs[7])
        Switch4=Switch(randint(1,6), [puerto_07, puerto_08], self.lista_eventos)


        self.asociar_puertos(puerto_01, puerto_08)
        self.asociar_puertos(puerto_02, puerto_03)
        self.asociar_puertos(puerto_04, puerto_05)
        self.asociar_puertos(puerto_06, puerto_07)

        self.iteraciones=[]
        self.iteraciones.append(Iteracion(Switch1, puerto_01))
        self.iteraciones.append(Iteracion(Switch1, puerto_02))

        self.iteraciones.append(Iteracion(Switch2, puerto_03))
        self.iteraciones.append(Iteracion(Switch2, puerto_04))

        self.iteraciones.append(Iteracion(Switch3, puerto_05))
        self.iteraciones.append(Iteracion(Switch3, puerto_06))

        self.iteraciones.append(Iteracion(Switch4, puerto_07))
        self.iteraciones.append(Iteracion(Switch4, puerto_08))

        self.switches=[Switch1, Switch2, Switch3, Switch4]
        self.puertos=[puerto_01, puerto_02, puerto_03, puerto_04,
                puerto_05, puerto_06, puerto_07, puerto_08]

        self.red=Red(self.switches, self.puertos, self.iteraciones, self.lista_eventos)
        

    def simular(self):
        self.red.hacer_envios()
        self.red.evaluar_switches()
        self.red.evaluar_estado_raiz_en_switches()

        self.red.hacer_envios()
        self.red.evaluar_switches()
        self.red.evaluar_estado_raiz_en_switches()

c=ConstructorCuadradoCuatroLados()
c.simular()
lista_eventos=c.lista_eventos
for e in lista_eventos.lista:
    print(e)
    pass

red=c.red
print(red.get_lista_decisiones())

# red.hacer_envios()
# red.evaluar_switches()
# red.evaluar_estado_raiz_en_switches()