class Persona:
    fallecido=False
    __count=0
    

    def __init__(self, nombre, apellido,edad=30):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.poderes=[]
        Persona.__count+=1

        # Metodo

    def nombre_completo(self):
        return '{} {} {} {}'.format(self.nombre, self.apellido, self.edad, Persona.fallecido) 
    
    def get_count():
        return Persona.__count
    
    def set_count():
        Persona._count+=1


pers1=Persona('Jhon','Doe')
pers2=Persona('Jane', 'Doe', 32)


# print(pers1)
# print(Persona)


# print(pers1.nombre, pers1.edad)
# print(pers2.nombre, pers2.edad)




# Otra manera
# print(Persona.nombre_completo(pers1))



# print(Persona.fallecido)
# print(pers1.fallecido)
# print(pers2.fallecido)


pers1.fallecido=True
# print(pers1.fallecido)


# print(Persona.fallecido)
# print(type(pers1).fallecido)

pers1.poderes.append('volar')

print(pers1.poderes)
print(pers2.poderes)

print(pers1.nombre_completo())
print(pers2.nombre_completo())

print(Persona.get_count())



