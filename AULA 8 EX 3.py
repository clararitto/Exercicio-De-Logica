resp = 's'
while resp == 's':
    n1 = int(input("Digite um numero diferente de zero(0): "))
    if n1>0:
        print("POSITIVO")
    elif n1<0:
        print("NEGATIVO")
    else:
        print("numero invalido")

    resp=input("deseja realizar uma nova verificação? s/n: ")