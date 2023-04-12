f=0
g=0
for x in range(10):
    num=int(input("digite um numero"))
    if num >=10 and num <=20:
        f=f+1
    else:
        g=g+1
print("dentro do intervalo",f)
print("fora do intervalo",g)
