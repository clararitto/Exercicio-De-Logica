
notas=[]
soma=0
cont=0
for i in range(5):
    notas.append(float(input("digite um numero:  ")))
for x in range(5):
    soma+=notas[x]
media=soma/5
print(media)

for j in range(5):
    if media>=notas[j]:
        cont+=1
print(cont)