A=[]
B=[]
C=[]
vetores=int(input("Digite o tamanho dos vetores: "))
for i in range(vetores):
    A.append(input("Digite um valor para A: "))
    B.append(input("Digite um valor para B: "))

for y in range(vetores):
    C.append(A[y]+B[y])

print(A)
print(B)
print(C)