
class Pai():


    def __init__(self):
        self.valor = "dentro do pai"


    def resul(self):
        print(self.valor)


class mae(Pai):


    def __init__(self):
        self.valor = "Mãe faz tudo quiser"


    def resul(self):
        print(self.valor)



obj1 = Pai()
obj2 = mae()

obj1.resul()
obj2.resul()