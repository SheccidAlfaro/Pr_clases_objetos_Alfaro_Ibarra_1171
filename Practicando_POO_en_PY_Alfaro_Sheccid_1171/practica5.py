class Fabrica():
  def __init__(self, llantas, color, precio):
    self._llantas=llantas
    self._color=color
    self._precio=precio

class Moto(Fabrica):
  def cantidad(self):
    print("La cantidad de llantas: {}\nEl color es:{}\nEl precio es: {}". format(self._llantas,self._color,self._precio))

class Carro(Fabrica):
  def cantidad(self):
    print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".           format(self._llantas,self._color,self._precio))

    print("OBJETO=carro")

moto=Moto(2, "rojo", "$1600")
moto.cantidad()

print("OBJETO=moto")

carro=Carro(4 ,"Azul", "$2300")
carro.cantidad()