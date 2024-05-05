class A:

    contador=0

    def __init__(self) -> None:
        self.valor=100
        self.valor2=200
        self.suma()

    # metodo de instancia
    def suma(self):
        A.contador+=1
        self.valor=500
    

    #metodo de clase
    # @classmethod
    # def suma(cls):
    #     cls.contador+=1
        # cls.valor=500 #Aqui se crea una variable de clase

    #metodo estatico
    # @staticmethod
    # def suma():
    #     A.contador+=1





obj1=A()
obj2=A()
obj3=A()


print(A.contador)
print(obj1.valor)

A.suma()
print(A.contador)
obj1.suma()
print(A.contador)
print(A.contador)