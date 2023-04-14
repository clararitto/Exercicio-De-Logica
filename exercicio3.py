pin='12345'
n=1
senha=input("digite sua senha")
while senha!=pin:
    n=n+1
    print("senha incorreta,digite novamente:")
    senha=input()
    print(n)
    if n>2 and senha!= pin:
        print("senha bloqueada")
        break
else:
    print("acesso liberado")