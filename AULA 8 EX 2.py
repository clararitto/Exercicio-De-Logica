medias=[]
nov_resp="Ss"
while nov_resp =="Ss":
    n1=float(input("Digite a 1º nota: "))
    n2=float(input("Digite a 2º nota:  "))
    media=(n1+n2)/2
    medias.append(media)
    print(media)
    if media>=7:
        print("aprovado")
    elif media>=4:
        print("recuperação")
    else:
        print("reprovado")
    nov_resp=input("Deseja fazer um novo calculo? S/N")
print(medias)