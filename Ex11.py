sexo = ""
while (sexo != "F" or sexo != "M"):
    sexo = input("Digite o seu sexo:")
    if (sexo == "F" or sexo == "M"):
        print("Seu sexo é: {}".format(sexo))
        break
    if (sexo != "F" or sexo != "M"):
        print("Digite um valor valido")