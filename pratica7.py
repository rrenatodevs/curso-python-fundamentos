""" 
Agora vamos juntar os dois objetivos: mostrar os alunos de cada turma, a quantidade de alunos por turma e, no final, o total geral.

Desafio: tente colocar a contagem individual dentro do mesmo for que percorre turmas_formatadas, aproveitando o acumulador que você acabou de criar.

A saída deverá ficar assim:
Turma 1: Ana, Carlos, Pedro
Quantidade: 3 alunos

Turma 2: Mariana, João
Quantidade: 2 alunos

Turma 3: Lucas, Fernanda, Rafael, Julia
Quantidade: 4 alunos

Total de alunos: 9
"""

salas_1 = "Ana, Carlos, Pedro"
salas_2 = "Mariana, João"
salas_3 = "Lucas, Fernanda, Rafael, Julia"



turmas = [salas_1, salas_2, salas_3]

turmas_formatadas = []

for turma in turmas:
    turma_formatada = turma.split(", ")
    turmas_formatadas.append(turma_formatada)

qtd_alunos = 0
    
for i, turma in enumerate(turmas_formatadas):
    nomes_unidos = ", ".join(turma)
    quantidade = len(turma)

    print(f"Turma {i + 1}: {nomes_unidos}")
    print(f"Quantidade: {quantidade} alunos\n")

    qtd_alunos += quantidade

print(f"Total de alunos: {qtd_alunos}")
