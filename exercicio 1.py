n1=float(input("Digite a 1ºnota "))
n2=float(input("Digite a 2º nota "))
media=(n1+n2)/2
if media>6:
    print("Aprovado")
elif media>=4 and media<=6:
    print("Verificação Suplementar")
else:
    print("Reprovado")