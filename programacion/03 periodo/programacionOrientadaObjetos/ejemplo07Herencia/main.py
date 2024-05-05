
class Vehiculo:

    def __init__(self, marca, modelo) -> None:
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        return "Marca: {}\nModelo: {}\nEn marcha: {}\nAcelera: {}\nFrena: {}\n".format(self.marca, self.modelo, self.enmarcha, self.acelera, self.frena)
    

class Furgoneta(Vehiculo):
     def carga(self, cargar):
         self.cargada=cargar

         if self.cargada:
             return "Esta cargada la furgo"
         else:
             return "No melocotones en la furgo" 
         
class VElectrico:
    def __init__(self) -> None:
        self.autonomia=100

    def cargarEnergia(self):
        self.cargado=True

# Herencia Multiple, solo funciona en lenguajes de tipado dinamico
class BicicletaElectrica(VElectrico, Vehiculo):
    pass

         

class Moto(Vehiculo):
    hcaballito=""

    def caballito(self):
        self.hcaballito="Voy haciendo caballito"

    def estado(self):
        return "Marca: {}\nModelo: {}\nEn marcha: {}\nAcelera: {}\nFrena: {} \n{}\n".format(self.marca, self.modelo, self.enmarcha, self.acelera, self.frena, self.hcaballito)

class Quad(Moto):
    pass




# v1=Vehiculo("Reanult", "C15")
# print(v1.estado())

# v1.arrancar()
# v1.acelerar()
# v1.frenar()
# print(v1.estado())


# moto=Moto("Yamaha","R1")

# print(moto.estado())
# moto.arrancar()
# moto.acelerar()
# moto.frenar()
# moto.caballito()

# print(moto.estado())

# furgo = Furgoneta("Ranault", "Kangoo")
# furgo.arrancar()
# print(furgo.estado())
# print(furgo.carga(True))

# print(moto.carga(True)) # Esto no funciona, porque moto no tiene el metodo carga

biciElectrica=BicicletaElectrica()
