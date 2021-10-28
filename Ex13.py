i = 0
lista = []
while i <=1000:
    valor = int(input("Digite os valores ! "))
    if valor == 1000:
        break
    lista.append(valor)
    soma = sum(lista)

print(lista)
print("A soma dos valores são : {} ! ".format(soma))
