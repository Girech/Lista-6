from random import randrange
vitorias = 0
derrotas = 0
while (derrotas!=1):
    escolha = input("Escolha par ou impar:")
    computador = ""

    if escolha == "par":
        computador = "impar"
    else:
        computador = "par"
    numerop = int(input("Digite o seu numero:"))
    numeroc = randrange(10)
    soma = numeroc + numerop
    if (soma%2==0) and (escolha == "par"):
        vitorias += 1
        print("Jogador: {} Computador: {} Jogador Venceu! Vitorias: {}  Derrotas: {}".format(numerop,numeroc,vitorias,derrotas))
    elif (soma%2!=0) and (escolha == "impar"):
        vitorias += 1
        print("Jogador: {} Computador: {} Jogador Venceu! Vitorias: {}  Derrotas: {}".format(numerop,numeroc,vitorias,derrotas))
    elif (soma%2!=0) and (escolha == "par"):
        derrotas += 1
        print("Jogador: {} Computador: {} Jogador Perdeu! Vitorias: {}  Derrotas: {}".format(numerop,numeroc,vitorias,derrotas))
    elif (soma%2==0) and (escolha == "impar"):
        derrotas += 1 
        print("Jogador: {} Computador: {} Jogador Perdeu! Vitorias: {}  Derrotas: {}".format(numerop,numeroc,vitorias,derrotas))
    





