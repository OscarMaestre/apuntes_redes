#!/usr/bin/python3

class ACLRed(object):
    
    def __init__(self, prefijo, wildcard) -> None: 
        self.prefijo  = prefijo
        self.wildcard = wildcard

    def __str__(self) -> str: 
        plantilla = "{0} {1}"
        texto     = plantilla.format(self.prefijo, self.wildcard)
    
        return texto

class ACLHost(object):
    
    def __init__(self, ip) -> None:
        self.ip=ip
    
    def __str__(self) -> str:
        plantilla = "host {0}"
        texto     = plantilla.format(self.ip)
        
        return texto

class ACLPuerto(object):
    MAYOR="gt"
    MENOR="lt"
    IGUAL="eq"

    def __init__(self, puerto, estado) -> None:
        self.puerto = puerto
        self.estado = estado
    
    def __str__(self) -> str:
        plantilla = "{0} {1}"
        texto     = plantilla.format(self.estado,)
        return texto

class ACL(object):
    
    def __init__(self, numero, accion, ip_origen, puerto_origen, ip_destino, puerto_destino) -> None:
        self.accion         = accion
        self.numero         = numero
        self.ip_origen      = ip_origen
        self.ip_destino     = ip_destino
        self.puerto_origen  = puerto_origen
        self.puerto_destino = puerto_destino
    
    def __str__(self) -> str:
        plantilla=f'access-list'