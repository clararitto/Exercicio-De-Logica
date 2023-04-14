n1=int(input("Digite a primeira nota"))

while n1<0 or n1>10:
    n1=int(input("numero invalido,digite novamente"))
n2=int(input("digite a segunda nota"))
while n2<0 or n2>10:
    n2=int(input("numero invalido,tente novamente"))
media=(n1+n2)/2
print("a media é  :",media)
