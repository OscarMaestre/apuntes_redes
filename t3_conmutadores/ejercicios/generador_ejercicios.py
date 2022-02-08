#!/usr/bin/python3
 
from errno import ENETUNREACH
from matplotlib.pyplot import cla
from utilidades.ip.ipv4 import GeneradorIPV4Azar
from string import Template
from random import choice, shuffle, seed, randint

class EjercicioConfiguracion(object):
    #Estado del switch o router
    MODO_USUARIO=1
    MODO_ADMIN  = MODO_USUARIO + 1
    MODO_CONFIG = MODO_ADMIN   + 1
    MODO_4       =MODO_CONFIG  + 1
    
    def __init__(self, estado_inicial=MODO_USUARIO, nombre_inicial="Switch1") -> None:
        self.comandos_con_prompt=[]
        self.comandos_sin_prompt=[]
        self.modo=estado_inicial
        self.nombre=nombre_inicial
        self.texto_modo=""
    
    def get_modo(self):
        return self.modo

    def anadir_comando(self, comando):
        # print("Modo actual:"+str(self.modo))
        # print("Apilando comando:"+comando)
        if self.modo==EjercicioConfiguracion.MODO_USUARIO:
            self.comandos_con_prompt.append( "{0}>{1}".format(self.nombre, comando ) )
        if self.modo==EjercicioConfiguracion.MODO_ADMIN:
            self.comandos_con_prompt.append( "{0}#{1}".format(self.nombre, comando ) )
        if self.modo>EjercicioConfiguracion.MODO_ADMIN:
            self.comandos_con_prompt.append( "{0}({2})#{1}".format(self.nombre, comando, self.texto_modo ) )
        self.comandos_sin_prompt.append( "{0}".format( comando ) )

    def enable(self):
        self.anadir_comando("enable")
        self.activar_modo_admin()

    def configure_terminal(self):
        self.anadir_comando("configure terminal")
        self.activar_modo_config()

    def exit(self):
        self.anadir_comando("exit")
        
    
    def activar_modo_config(self):
        self.texto_modo="config"
        self.modo=EjercicioConfiguracion.MODO_CONFIG
    
    def activar_modo_admin(self):
        self.texto_modo=""
        self.modo=EjercicioConfiguracion.MODO_ADMIN
    
    def activar_modo_usuario(self):
        self.texto_modo=""
        self.modo=EjercicioConfiguracion.MODO_USUARIO

    def ir_a_modo_usuario(self):
        if self.modo==EjercicioConfiguracion.MODO_ADMIN:
            self.exit()
            self.activar_modo_usuario()
        if self.modo==EjercicioConfiguracion.MODO_USUARIO:
            return 
        if self.modo==EjercicioConfiguracion.MODO_CONFIG:
            self.exit()
            self.activar_modo_admin()
            self.exit()
            self.activar_modo_usuario()

        if self.MODO_4==EjercicioConfiguracion.MODO_4:
            self.exit()
            self.activar_modo_config()
            self.exit()
            self.activar_modo_admin()
            self.exit()
            self.activar_modo_usuario()

    def ir_a_modo_admin(self):
        if self.modo==EjercicioConfiguracion.MODO_ADMIN:
            return
        if self.modo==EjercicioConfiguracion.MODO_USUARIO:
            self.enable()
        if self.modo==EjercicioConfiguracion.MODO_CONFIG:
            self.exit()
            self.activar_modo_admin()
        if self.modo==EjercicioConfiguracion.MODO_4:
            self.exit()
            self.activar_modo_config()
            self.exit()
            self.activar_modo_admin()
            

    def ir_a_modo_config(self):
        
        if self.modo==EjercicioConfiguracion.MODO_CONFIG:
            return 
        if self.modo==EjercicioConfiguracion.MODO_ADMIN:
            self.configure_terminal()
        if self.modo==EjercicioConfiguracion.MODO_USUARIO:
            self.enable()
            self.configure_terminal()
        if self.modo==EjercicioConfiguracion.MODO_4:
            self.exit()
        self.activar_modo_config()

    def ir_a_modo_4(self, comando, texto):
        #print("Yendo a modo 4 desde modo:"+str(self.modo))
        if self.modo==EjercicioConfiguracion.MODO_CONFIG:
            pass
        if self.modo==EjercicioConfiguracion.MODO_ADMIN:
            self.configure_terminal()
        if self.modo==EjercicioConfiguracion.MODO_USUARIO:
            self.enable()
            self.configure_terminal()
        if self.modo==EjercicioConfiguracion.MODO_4:
            pass
        
        
        self.anadir_comando(comando)
        self.texto_modo=texto
        self.modo=EjercicioConfiguracion.MODO_4

    def copy_running_startup(self):
        self.ir_a_modo_admin()
        self.anadir_comando("copy running-config startup-config")

    def hostname(self, nuevo_nombre):
        
        self.ir_a_modo_config()
        #print("Nuevo modo:"+str(self.modo))
        self.anadir_comando("hostname " + nuevo_nombre)
        self.nombre=nuevo_nombre
        
    def get_comandos_con_prompt(self):
        return "\n".join(self.comandos_con_prompt)


    def cambiar_prioridad_stp(self, prioridad):
        self.ir_a_modo_config()
        plantilla="spanning tree vlan 1 priority {0}"
        self.anadir_comando(plantilla.format(str(prioridad)))

    def get_comandos_sin_prompt(self):
        return "\n".join(self.comandos_sin_prompt)

    def poner_clave_consola_sin_login(self, clave):
        self.ir_a_modo_4("line console 0", "config-line")
        self.anadir_comando("password " + clave)
    
    def login(self):
        self.anadir_comando("login")

    def poner_clave_consola_con_login(self, clave):
        self.ir_a_modo_config()
        self.ir_a_modo_4("line console 0", "config-line")
        self.anadir_comando("password " + clave)
        self.login()

    def poner_clave_admin(self, clave):
        self.ir_a_modo_config()
        self.anadir_comando("enable secret "+clave)

    def poner_clave_telnet(self, clave):
        self.ir_a_modo_config()
        self.ir_a_modo_4("line vty 0 15", "config-line")
        self.anadir_comando("password "+clave)
        self.login()


    def poner_ip_gestion(self, ip, mascara):
        self.ir_a_modo_4("interface vlan 1", "config-if")
        
        self.anadir_comando("ip address "+ ip + " " + mascara)
        self.anadir_comando("no shutdown")

    def generar_claves_publicas(self, dominio, longitud_clave):
        self.ir_a_modo_config()
        self.anadir_comando("ip domain-name "+dominio)
        self.anadir_comando("crypto key generate rsa general-keys modulus "+str(longitud_clave))

    def configurar_usuario_ssh(self, usuario, clave):
        self.ir_a_modo_config()
        self.anadir_comando(
            "username {0} secret {1}".format(usuario, clave)
        )
        self.ir_a_modo_4("line vty 0 15", "config-line")
        self.anadir_comando("login local")
        self.anadir_comando("transport input ssh")

    def cambiar_timeout_arp(self, segundos):
        self.ir_a_modo_4("interface vlan 1", "config-if")
        self.anadir_comando("arp timeout "+str(segundos))
        self.anadir_comando("no shutdown")

    def anadir_mac_puerto(self, mac, num_puerto):
        self.ir_a_modo_config()
        comando="mac address-table static {0} vlan 1 interface fastEthernet 0/{1}"
        self.anadir_comando( comando.format(mac, str(num_puerto)) )

    def ver_tabla_macs(self):
        self.ir_a_modo_admin()
        self.anadir_comando("show mac-address-table")
    
    def get_cifras_hexadecimales(self, longitud):
        cifras="0123456789abcdef"
        bloque=""
        for i in range(0, longitud):
            bloque=bloque+choice(cifras)
        return bloque


    def generar_mac_azar(self):
        bloque0="00aa"
        bloque1=self.get_cifras_hexadecimales(4)
        bloque2=self.get_cifras_hexadecimales(4)
        return ".".join([bloque0, bloque1, bloque2])

class GeneradorEjercicioSwitches(object):
    def __init__(self) -> None:
        self.enunciados=[]
        self.ejercicio=EjercicioConfiguracion()

    
    def get_clave_admin_azar(self):
        claves=[
            "admin", "admin1234", "admin_1234", "1234admin",
            "administrador", "administrador_1234"
        ]
        return choice(claves)

    def get_clave_telnet_azar(self):
        claves=[
            "admin", "admin1234", "admin_1234", "1234admin",
            "administrador", "administrador_1234"
        ]
        return choice(claves)
    
    def get_dominio_azar (self):
        dominios=[
            "acme.com", "empresa.com", "redes.es",
            "network.es", "academy.com", "redes.com"
        ]
        return choice(dominios)
    
    def get_longitud_clave_azar(self):
        longitudes=["512", "1024", "2048"]
        return choice(longitudes)

    def get_login_ssh_azar(self):
        logins=[
            "adminssh", "sshadmin", "administradorssh",
            "adminseguro", "adminporssh", "sshadministrador"
        ]
        return choice(logins)
    
    def get_nombres_switch_azar(self):
        nombres=[
            "AulaB08","AulaB09","AulaB10",
            "SwitchB08","SwitchB09","SwitchB10",
            "AulaB11","AulaB14","AulaB15",
            "SwitchB11","SwitchB14","SwitchB15"
        ]
        return choice(nombres)
    
    def get_clave_ssh_azar(self):
        return self.get_login_ssh_azar()

    def poner_clave_admin(self):
        plantilla="Poner al switch la clave de administrador ``{0}``."
        clave_admin_azar=self.get_clave_admin_azar()
        self.enunciados.append(plantilla.format(clave_admin_azar))
        self.ejercicio.poner_clave_admin(clave_admin_azar)
    
    def poner_clave_telnet(self):
        plantilla="Habilitar telnet y ponerle a este acceso la clave ``{0}``."
        clave_telnet_azar=self.get_clave_telnet_azar()
        self.enunciados.append(plantilla.format(clave_telnet_azar))
        self.ejercicio.poner_clave_telnet(clave_telnet_azar)

    def configurar_ssh(self):
        plantilla="Genera la pareja de claves para el dominio ``{0}`` con una longitud de clave de ``{1}``. Añade también un usuario ssh con en login ``{2}`` y la clave ``{3}``."
        dominio=self.get_dominio_azar()
        longitud=self.get_longitud_clave_azar()
        usuario_ssh=self.get_login_ssh_azar()
        clave_ssh=self.get_clave_ssh_azar()
        self.enunciados.append(plantilla.format(dominio, longitud, usuario_ssh, clave_ssh))
        self.ejercicio.generar_claves_publicas(dominio, longitud)
        self.ejercicio.configurar_usuario_ssh(usuario_ssh, clave_ssh)

    def poner_hostname(self):
        nombre=self.get_nombres_switch_azar()
        plantilla="Poner al switch el nombre ``{0}``."
        self.enunciados.append(plantilla.format(nombre))
        self.ejercicio.hostname(nombre)

    def poner_ip_azar(self):
        generador=GeneradorIPV4Azar(num_ejercicio=1)
        direccion=generador.generar()
        mascara=generador.get_mascara_en_decimal()
        cad_direccion=generador.convertir_a_decimal(direccion)
        plantilla="Poner la IP ``{0}`` con la máscara ``{1}``. Recordar activar la interfaz VLAN."
        self.enunciados.append(plantilla.format(cad_direccion, mascara))
        self.ejercicio.poner_ip_gestion(cad_direccion, mascara)
        
    def poner_clave_consola_azar_con_login(self):
        claves=[
            "consola1234", "c0n50l4", "claveabcd",
            "consola33", "claveconsola1234","consola",
            "abcdefg"
        ]
        clave_azar=choice(claves)
        plantilla="Proteger el acceso por consola con la clave ``{0}`` asegurando que se exige el uso de dicha clave"
        self.enunciados.append(plantilla.format(clave_azar))
        self.ejercicio.poner_clave_consola_con_login(clave_azar)
    
    def poner_clave_consola_azar_sin_login(self):
        claves=[
            "consola1234", "claveclave", "claveabcd",
            "consola33", "claveconsola1234","consola",
            "abcdefg"
        ]
        clave_azar=choice(claves)
        plantilla="Proteger el acceso por consola con la clave ``{0}`` y no pidas por ahora el uso de dicha clave"
        self.enunciados.append(plantilla.format(clave_azar))
        self.ejercicio.poner_clave_consola_sin_login(clave_azar)
    

    def anadir_clave_mac_azar(self):
        mac_azar=self.ejercicio.generar_mac_azar()
        puerto_azar=choice([0,1,2,3,4,5,6,7,8])
        plantilla="Usando ARP estático asigna la MAC ``{0}`` al puerto ``FastEthernet 0/{1}``"
        self.enunciados.append(plantilla.format(mac_azar, puerto_azar))
        self.ejercicio.anadir_mac_puerto(mac_azar, puerto_azar)

    def cambiar_timeout(self):
        timeouts=[60, 120, 240, 600, 1200, 3600, 7200]
        plantilla="Modificar el timeout de ARP haciendo que tome un valor de {0} segundos."
        timeout_azar=choice(timeouts)
        self.enunciados.append(plantilla.format(timeout_azar))
        self.ejercicio.cambiar_timeout_arp(timeout_azar)
    
    def mostrar_la_tabla_de_macs(self):
        self.enunciados.append("Mostrar la tabla de MACS.")
        self.ejercicio.ver_tabla_macs()

    def guardar_la_configuracion(self):
        self.enunciados.append("Guardar la configuración hasta este momento.")
        self.ejercicio.copy_running_startup()

    def cambiar_prioridad_stp(self):
        prioridad_azar=randint(2, 12)
        nueva_prioridad=prioridad_azar * 4096
        plantilla="Cambiar la prioridad STP a {0}"
        self.enunciados.append(plantilla.format(nueva_prioridad))
        self.ejercicio.cambiar_prioridad_stp(nueva_prioridad)

    def generar_ejercicio(self, longitud):
        metodos=[
            self.poner_clave_admin,         self.poner_clave_telnet,
            self.configurar_ssh,            self.poner_hostname,
            self.poner_ip_azar,             self.poner_clave_consola_azar_con_login,
            #No tiene mucho sentido poner este
            #self.poner_clave_consola_azar_sin_login
            self.anadir_clave_mac_azar,     self.cambiar_timeout,
            self.mostrar_la_tabla_de_macs,  self.cambiar_prioridad_stp
        ]
        shuffle(metodos)
        for i in range(0, longitud):
            metodos[i]()
    
    def get_enunciado(self):
        enunciado="Configurar un switch Cisco mediante la línea de comandos cumpliendo los requisitos siguientes:\n\n"
        conpuntos=["* "+punto for punto in self.enunciados]
        return enunciado + "\n".join(conpuntos)

    def get_solucion(self):
        texto=self.get_enunciado()+"\n\n"
        texto+="La solución detallada sería esta::\n\n"
        con_prompt=["\t"+comando for comando in self.ejercicio.comandos_con_prompt]
        texto+="\n".join(con_prompt)

        texto+="\n\nLos comandos listos para copiar y pegar serían estos::\n\n"
        sin_prompt=["\t"+comando for comando in self.ejercicio.comandos_sin_prompt]
        texto+="\n".join(sin_prompt)
        return texto
        
    

ejercicios=[]

for i in range(1, 7):
    for j in range(1, 5):
        g=GeneradorEjercicioSwitches ()
        g.generar_ejercicio(i)
        ejercicios.append(g)

contador=1

encabezado="""
Anexo al tema 3: Ejercicios sobre comandos Cisco en switches
--------------------------------------------------------------------
"""



print (encabezado)
for e in ejercicios:
    print("\nEjercicio {0} de switches".format(contador))
    print(50*"~")
    print(e.get_enunciado())
    contador+=1

contador=1
for e in ejercicios:
    print("\nSolución al ejercicio {0} de switches".format(contador))
    print(50*"~")
    print(e.get_solucion())
    contador+=1