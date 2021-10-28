
n1 = ""
n2 = ""
opcao = ""
operacao = 0
while opcao != 5:
    opcao = int(input("Digite a opção"))
    n1 = float(input("Digite o primeiro numero:"))
    n2 = float(input("Digite o segundo numero:"))
    
    if opcao == 1:
        operacao = n1+n2
    print("{}+{}={}".format(n1,n2,operacao))
    if opcao == 2:
        operacao = n1-n2
        print("{}-{}={}".format(n1,n2,operacao))
    if opcao == 3:
        operacao = n1*n2
        print("{}*{}={}".format(n1,n2,operacao))
    if opcao == 4:
        operacao = n1/n2
        print("{}/{}={}".format(n1,n2,operacao))
    
    
