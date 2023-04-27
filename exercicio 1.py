nomes=[]
senhas=[]
for i in range(5):
    nomes.append(input("Digite um nome: "))
    senhas.append(input("Digite sua senha: "))
login_nome=input("Digite seu login: ")
login_senha=input("Digite sua senha: ")
for f in range(5):
    if login_nome==nomes[f] and login_senha==senhas[f]:
        print("login efetuado com sucesso! ")
        break
else:
    print("Usuario não encontrado ou senha incorreta! ")
