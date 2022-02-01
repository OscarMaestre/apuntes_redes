#!/usr/bin/python3
 
from utilidades.ip.ipv4 import GeneradorIPV4Azar
from string import Template


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
        if self.modo<=EjercicioConfiguracion.MODO_USUARIO:
            self.comandos_con_prompt.append( "{0}>{1}".format(self.nombre, comando ) )
        else:
            self.comandos_con_prompt.append( "{0}({2})#{1}".format(self.nombre, comando, self.texto_modo ) )
        self.comandos_sin_prompt.append( "{0}".format( comando ) )

    def enable(self):
        self.anadir_comando("enable")
        self.texto_modo=""
        self.modo=EjercicioConfiguracion.MODO_ADMIN

    def configure_terminal(self):
        self.anadir_comando("configure terminal")
        self.texto_modo="config"
        self.modo=EjercicioConfiguracion.MODO_CONFIG

    def exit(self):
        self.anadir_comando("exit")
        
    def ir_a_modo_admin(self):
        if self.modo==EjercicioConfiguracion.MODO_ADMIN:
            return
        if self.modo==EjercicioConfiguracion.MODO_USUARIO:
            self.enable()
        if self.MODO_CONFIG==EjercicioConfiguracion.MODO_CONFIG:
            self.exit()
        if self.MODO_4==EjercicioConfiguracion.MODO_4:
            self.exit()
            self.exit()

    def ir_a_modo_config(self):
        if self.MODO_CONFIG==EjercicioConfiguracion.MODO_CONFIG:
            return 
        if self.modo==EjercicioConfiguracion.MODO_ADMIN:
            self.configure_terminal()
        if self.modo==EjercicioConfiguracion.MODO_USUARIO:
            self.enable()
            self.configure_terminal()
        if self.MODO_4==EjercicioConfiguracion.MODO_4:
            self.exit()

    def ir_a_modo_4(self, comando, texto):
        self.configure_terminal()
        self.anadir_comando(comando)
        self.texto_modo=texto

    def copy_running_startup(self):
        self.ir_a_modo_admin()
        self.anadir_comando("copy running-config startup-config")

    def hostname(self, nuevo_nombre):
        self.ir_a_modo_config()
        self.anadir_comando("hostname " + nuevo_nombre)
        self.nombre=nuevo_nombre
        
    def get_comandos_con_prompt(self):
        return "\n".join(self.comandos_con_prompt)

    def get_comandos_sin_prompt(self):
        return "\n".join(self.comandos_sin_prompt)

    def poner_clave_consola_sin_login(self, clave):
        self.ir_a_modo_config()
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
        self.ir_a_modo_4("line vty 0 15", "config-line")
        self.anadir_comando("password "+clave)
        self.login()


    def poner_ip_gestion(self, ip, mascara):
        self.ir_a_modo_config()
        self.ir_a_modo_4("interface vlan 1", "config-if")
        
        self.anadir_comando("ip address "+ ip + " " + mascara)
        self.anadir_comando("no shutdown")


generador=GeneradorIPV4Azar(num_ejercicio=1)
direccion=generador.generar()
print(generador.convertir_a_decimal(direccion))
#print(dir(generador.direccion))
e=EjercicioConfiguracion()
e.poner_ip_gestion("192.168.1.10", "255.255.255.0")
e.poner_clave_admin("claveadmin1234")
print(e.get_comandos_con_prompt())
