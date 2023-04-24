aluno=[]

num_alunos=int(input("Quantos alunos tem na sala de aula?"))
for i in range(num_alunos):
    aluno.append(input("Digite o nome do aluno:"))
for y in range(num_alunos):
    print(aluno[y],y)
f=input("Digite o nome de um aluno")
for g in range(num_alunos):
    if f==aluno[g]:
        print(g,aluno[g])