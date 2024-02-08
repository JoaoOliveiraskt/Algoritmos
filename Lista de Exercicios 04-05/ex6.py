quantidade_alunos = 10
quantidade_notas = 4

medias = []
alunos_aprovados = 0

for aluno in range(quantidade_alunos):
    notas_aluno = []
    for nota in range(quantidade_notas):
        nota_atual = float(input(f"Digite a {nota+1}ª nota do {aluno+1}º aluno: "))
        notas_aluno.append(nota_atual)

    media_aluno = sum(notas_aluno) / quantidade_notas
    medias.append(media_aluno)

    if media_aluno >= 7.0:
        alunos_aprovados += 1

print( alunos_aprovados, "Alunos com média maior ou igual a 7.0.")
