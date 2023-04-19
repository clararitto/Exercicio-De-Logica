print(""" SELECIONE A OPERAÇÃO:
[1] SOMA
[2] SUBTRAÇÃO
[3] MULTIPLICAÇÃO
[4] DIVISÃO
[5] NOVO NUMERO
[6] SAIR""")
n1 = float(input("Digite o 1º Numero: "))
n2 = float(input("Digite o 2º Numero: "))
while True:
    opcao=int(input("Escolha uma das opções"))
     if opcao in "1":
        soma=n1+n2
        print("o resultado da sua soma é: ",soma)
    if opcao in "2":
        sub=n1-n2
        print("o resultado da subtração é: ",sub)
    if opcao in "3":
        multip=n1*n2
        print("o resultado da mutiplicação é: ",multip)
    if opcao in "4":
        div=n1/n2
        print("o resultado da divisão é: ")
        novocal=input("Deseja fazer um novo calculo? s/n")