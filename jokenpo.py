


import random

def jogar_pedra_papel_tesoura():
    opcoes = ["pedra", "papel", "tesoura"]
    jogador = input("Escolha pedra, papel ou tesoura: ").lower()
    computador = random.choice(opcoes)

    print(f"Computador escolheu: {computador}")

    if jogador == computador:
        print("Empate!")
    elif jogador == "pedra":
        if computador == "papel":
            print("Você perdeu! Papel cobre pedra.")
        else:
            print("Você ganhou! Pedra quebra tesoura.")
    elif jogador == "papel":
        if computador == "tesoura":
            print("Você perdeu! Tesoura corta papel.")
        else:
            print("Você ganhou! Papel cobre pedra.")
    elif jogador == "tesoura":
        if computador == "pedra":
            print("Você perdeu! Pedra quebra tesoura.")
        else:
            print("Você ganhou! Tesoura corta papel.")
    else:
        print("Escolha inválida. Por favor, escolha entre pedra, papel ou tesoura.")

jogar_pedra_papel_tesoura()
