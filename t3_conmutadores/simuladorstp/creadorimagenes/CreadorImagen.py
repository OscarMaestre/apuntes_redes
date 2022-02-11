#!/usr/bin/python3 
# 
# 
#Si no lo tenemos pip3 install Pillow

from PIL import Image, ImageDraw, ImageFont

class CreadorImagen(object):
    def __init__(self, archivo_imagen, archivo_resultado, archivo_fuente) -> None:
        self.imagen=Image.open(archivo_imagen).convert("RGBA")
        self.font= ImageFont.truetype(archivo_fuente, 40)
        self.contexto=ImageDraw.Draw(self.imagen)
        self.archivo_resultado=archivo_resultado    

    def poner_texto(self, texto, x, y, color=(0, 0, 0)):
        self.contexto.text( (x, y), text=texto, font=self.font, fill=color)
        
    def get_resultado(self):
        self.imagen.save(self.archivo_resultado)

class CreadorRoutersCuadrados(CreadorImagen):
    def __init__(self, archivo_imagen, archivo_resultado, archivo_ttf) -> None:
        self.coordenadas=[
            (210, 114), (876,128), 
            (210, 468), (876,468), 
            #Mac 1d
            (296, 150)
        ]
        super().__init__(archivo_imagen, archivo_resultado, archivo_ttf)
        
    
    def poner_texto_switch_arriba_izq(self, texto, color=(255, 0, 0)):
        self.poner_texto(texto, self.coordenadas[0][0], self.coordenadas[0][1], color)

    def poner_texto_switch_arriba_der(self, texto, color=(255, 0, 0)):
        self.poner_texto(texto, self.coordenadas[1][0], self.coordenadas[1][1], color)
    
    def poner_texto_switch_abajo_izq(self, texto, color=(255, 0, 0)):
        self.poner_texto(texto, self.coordenadas[2][0], self.coordenadas[2][1], color)

    def poner_texto_switch_abajo_der(self, texto, color=(255, 0, 0)):
        self.poner_texto(texto, self.coordenadas[3][0], self.coordenadas[3][1], color)
    
    def poner_prioridades(self, switches):
        self.poner_texto_switch_arriba_izq(switches[0].identificador_yo)
        self.poner_texto_switch_abajo_izq(switches[1].identificador_yo)
        self.poner_texto_switch_abajo_der(switches[2].identificador_yo)
        self.poner_texto_switch_arriba_der(switches[3].identificador_yo)
    def poner_macs(self, macs):
        #El orden en sentido inverso de las agujas del reloj empezando
        #por (Switch 1, derecha)
        x0=296
        y0=120

        x1=x0-55
        y1=y0+50

        ALTURA1=250
        x2=x1
        y2=y1+ALTURA1

        ALTURA2=300
        x3=x0
        y3=y1+ALTURA2

        ANCHURA1=510

        x4=x0+ANCHURA1
        y4=y3
        
        ANCHURA2=605

        x5=x2+ANCHURA2
        y5=y2

        x6=x1+ANCHURA2
        y6=y1

        x7=x0+ANCHURA1
        y7=y0

        self.poner_texto(macs[0], x0, y0)
        self.poner_texto(macs[1], x1, y1)
        self.poner_texto(macs[2], x2, y2)
        self.poner_texto(macs[3], x3, y3)
        self.poner_texto(macs[4], x4, y4)
        self.poner_texto(macs[5], x5, y5)
        self.poner_texto(macs[6], x6, y6)
        self.poner_texto(macs[7], x7, y7)

if __name__=="__main__":
  c=CreadorRoutersCuadrados("base1.png", "r1.png")
  c.poner_texto_switch_arriba_izq("1")
  c.poner_texto_switch_arriba_der("2")
  c.poner_texto_switch_abajo_izq("3")
  c.poner_texto_switch_abajo_der("4")
  
  c.poner_macs(["0a", "0b", "0c", "0d", "1a", "1b", "1c", "1d"])

  c.get_resultado()