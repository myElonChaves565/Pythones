class Exemplo:
    def __init__(self, nome, rg):
        self.nome = nome
        self.rg = rg

lista_exemplo = [] 

lista_exemplo.append(Exemplo('Regina', 111))
lista_exemplo.append(Exemplo('Rejane', 222))
lista_exemplo.append(Exemplo('Raquel', 333))

for obj in lista_exemplo:
    print(obj.nome, obj.rg, sep='')


class Dica:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

lista_dica = []

lista_dica.append(Dica("Elon", "Chaves", 16))
lista_dica.append(Dica("João", "Lopes", 18))
lista_dica.append(Dica("Mamu", "Costa", 20))

for obj in lista_dica:
    print(obj.nome, obj.sobrenome, obj.idade, sep=" ")



