
class CambioRepresentacion(object):
  base16={
      0:"0",
      1:"1",
      2:"2",
      3:"3",
      4:"4",
      5:"5",
      6:"6",
      7:"7",
      8:"8",
      9:"9",
      10:"A",
      11:"B",
      12:"C",
      13:"D",
      14:"E",
      15:"15"
    }
    @staticmethod
    def get_representacion(tupla, nuevabase):
      (cocientes, restos)=tupla
      #Es necesario invertir los restos
      restos.reverse()
      simbolos=[]
      simbolos.append(cocientes[-1])
      simbolos=simbolos+restos
      if nuevabase==2 or nuevabase==8:
        resultado=list(map(str, lista))
        representacion="".join(resultado)
        return representacion



class Conversor(object):

  @staticmethod
  def cambiar_a_base(numero_en_decimal, nuevabase):
    numero=numero_en_decimal
    restos=[]
    cocientes=[]
    while numero>=nuevabase:
      resto=numero % nuevabase
      restos.append(resto)
      cociente=numero // nuevabase
      cocientes.append(cociente)
      print(cociente, resto)
      numero=cociente
    #Fin del while
    
    return (cocientes, restos)

(cocientes, restos)=Conversor.cambiar_a_base(127, 2)
