x=[]
ç=0
for i in range(5):
    x.append(float(input("Digite um numero: ")))
y=float(input("Digite mais um número para pesquisar: "))
for r in range(5):
    if y==x[r]:
        ç+=1
print(ç)
