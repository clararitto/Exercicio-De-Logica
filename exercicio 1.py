soma=0
alunosn=float(input("Digite a quantidade de Alunos"))
while n <= alunosn :
    notas=float(input("Digite a nota de cada aluno"))
    soma+=notas
    n+=1
media=soma/alunosn
print("a media da sala é",media)