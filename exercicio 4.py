numx=0
A=[]
M=[]
for m in range(10):
    A.append(int(input("digite um nummero: ")))
x=int(input("Digite um numero: "))
for y in range(10):
    M.append(x*A[y])
print(M)
print(x)
print(A)