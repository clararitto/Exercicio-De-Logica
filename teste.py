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
    match opcao:
        case 1:
            soma=n1+n2
            print("o resultado da sua soma é: ",soma)
        case 2:
            sub=n1-n2
            print("o resultado da subtração é: ",sub)
        case 3:
            multip=n1*n2
            print("o resultado da mutiplicação é: ",multip)
        case:
            div=n1/n2
            print("o resultado da divisão é: ")
        if opcao in "5"
            break