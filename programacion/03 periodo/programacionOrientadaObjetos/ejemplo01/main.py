class Coche:

    def __init__(self):
        self.__largo = 250
        self.__ancho = 120
        self.__ruedas = 4
        self._enmarcha = False

    def arrancar(self, arrancamos):
        self.enmarcha = arrancamos

        if self._enmarcha:
            chequeo = self.__chequeo_interno()
        elif self._enmarcha and chequeo==False:
            return "Algo ha ido mal. No pordemos arrancar"
        else:
            return "El coche esta parado"


    def __estado(self):
        return "Coche tiene {} ruedas. Un largo de {} y un ancho de {}".format(self.ruedas, self.largo, self.ancho)

    def __chequeo_interno(self):
        print("Realizando el chequeo....")

        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="ok"

        if self.gasolina=="ok"  and self.aceite=="ok": 
            return True
        else:
            return False
        


miCoche = Coche()
miCoche2 = Coche()

# print("El largo del coche es de {}".format(miCoche.largo))


# print("Id coche {}".format(id(miCoche)))
# print("Id coche {}".format(id(miCoche2)))
miCoche2.ruedas = 200
print(miCoche2.arrancar(False))
print(miCoche.arrancar(True))

# print("Coche {} - {}".format(id(miCoche2), miCoche2.estado()))
