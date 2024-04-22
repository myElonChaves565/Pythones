tempo = str(input("M - Matutino , V - Vespertino, N - Nortuno"
                  "\nEm que turno você estuda: "))
if tempo == "M":
    print("Bom dia!!")
elif tempo == "V":
    print("Boa tarde!!")
elif tempo == "N":
    print("Boa noite!!")
else:
    print("Inválido!")