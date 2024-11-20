
class Persona:
   def __init__(self, n, e):
        self.nombre=n
        self.edad=e

   def cumpleaños(self):
        self.edad += 1

p=Persona(input("Coloca tu nombre: "),int(input("Coloque su edad:")))
p.cumpleaños()
p.cumpleaños()
print(f"{p.nombre} cumple {p.edad} años")

