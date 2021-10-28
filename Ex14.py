
import numpy as pd
lista = []
while True:
    numeros = float(input("Digite o seus valores !! "))
    lista.append(numeros)
    
    media = pd.mean(lista)
    maior = max(lista)
    menor = min(lista)

    continuar = input("1 - Continuar ou 2 - Sair").lower()
    if continuar == "sair":
        break
    
print("A média foi de {} ! ".format(media))
print("O maior número foi {} ! ".format(maior))
print("O menor número é {} ! ".format(menor))