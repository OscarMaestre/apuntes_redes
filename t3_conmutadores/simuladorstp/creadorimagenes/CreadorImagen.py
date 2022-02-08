#!/usr/bin/python3 
# 
# 
#Si no lo tenemos pip3 install Pillow

from PIL import Image, ImageDraw, ImageFont

class CreadorImagen(object):
    def __init__(self, archivo_imagen, archivo_resultado) -> None:
        self.imagen=Image.open(archivo_imagen).convert("RGBA")
        self.font= ImageFont.truetype("Roboto.ttf", 40)
        self.contexto=ImageDraw.Draw(self.imagen)
        self.archivo_resultado=archivo_resultado    

    def poner_texto(self, texto, x, y):
        self.contexto.text( (x, y), text=texto, font=self.font, fill=(0,0,0))
        
    def get_resultado(self):
        self.imagen.save(self.archivo_resultado)

class CreadorRoutersCuadrados(CreadorImagen):
    def __init__(self, archivo_imagen, archivo_resultado) -> None:
        self.coordenadas=[
            (240, 134), (876,128), 
            (240, 468), (876,468), 
        ]
        super().__init__(archivo_imagen, archivo_resultado)
        
    
    def poner_texto_switch_arriba_izq(self, texto):
        self.poner_texto(texto, self.coordenadas[0][0], self.coordenadas[0][1])

    def poner_texto_switch_arriba_der(self, texto):
        self.poner_texto(texto, self.coordenadas[1][0], self.coordenadas[1][1])
    
    def poner_texto_switch_abajo_izq(self, texto):
        self.poner_texto(texto, self.coordenadas[2][0], self.coordenadas[2][1])

    def poner_texto_switch_abajo_der(self, texto):
        self.poner_texto(texto, self.coordenadas[3][0], self.coordenadas[3][1])


if __name__=="__main__":
  c=CreadorRoutersCuadrados("base1.png", "r1.png")
  c.poner_texto_switch_arriba_izq("1")
  c.poner_texto_switch_arriba_der("2")
  c.poner_texto_switch_abajo_izq("3")
  c.poner_texto_switch_abajo_der("4")
  c.get_resultado()