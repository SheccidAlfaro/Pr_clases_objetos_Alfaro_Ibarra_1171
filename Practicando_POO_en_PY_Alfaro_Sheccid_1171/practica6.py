class terrestre():
  def hablar(self):
    print("Hola soy un animal terrestre!")

class Perro(terrestre):
  def hablar(self):
    print("Soy un perro...")

class Gato(terrestre):
  def hablar(self,mensaje):
    self.mensaje=mensaje
    print(mensaje)

errestre=terrestre()
errestre.hablar()

perro=Perro()
perro.hablar()

gato=Gato()
gato.hablar("Soy un gato...")