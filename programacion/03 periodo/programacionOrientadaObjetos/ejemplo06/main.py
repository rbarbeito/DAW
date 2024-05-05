#Metodos de clase y estaticos
import math


class Pastel:

    def __init__(self, ingredientes,tam) -> None:
        self.ingredientes=ingredientes
        self.tamagno=tam

    def estado(self):
        return "Pastel->ingredientes: {}".format(self.ingredientes, self)
    
    def area(self):
        return self.tam_area(self.tamagno)
    
    # Metodos predefinidos que crean objetos con valores predefinidos, en este caso un pastel de chocolate
    @classmethod
    def Pastel_Chocolate(cls):
        return cls("Harina, leche, huevo, chocolate")
    
    @classmethod
    def Pastel_Vainilla(cls):
        return cls("Harina, leche, huevo, vainilla")
    
    @staticmethod
    def tam_area(t):
        return t**2*math.pi

    

    
    

# print(Pastel.Pastel_Chocolate().estado())
# print(Pastel.Pastel_Vainilla().estado())
# print(Pastel("Leche, Cacao, cemento").estado())
    
p=Pastel("cacao, leche, harina",4)

print(p.area())


