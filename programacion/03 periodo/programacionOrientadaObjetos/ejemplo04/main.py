from datetime import date


class Persona:
    fallecido = False
    __count = 0

    def __init__(self, nombre, apellido, fecha_nac, tipo):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nac = fecha_nac
        self.tipo = tipo
        Persona.__count += 1

        Persona.set_count()

    # Metodo de instancia
    def nombre_completo(self):
        # print(self)
        return '{} {} {} {}'.format(self.nombre, self.apellido, self.fecha_nac)

    # Metodo de clase

    @classmethod
    def resetcontador(cls):
        cls.__count = 0

    # metodo estatico
    @staticmethod
    def get_count():
        return Persona.__count


pers1 = Persona('Jhon', 'Doe', date(1980, 5, 1))
pers2 = Persona('Jane', 'Doe', date(1980, 5, 1))

print(pers1.get_count())


Persona.resetcontador()

print(Persona.get_count())
