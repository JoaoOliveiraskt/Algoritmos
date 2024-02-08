idades = []
alturas = []
total_alturas = 0
num_alunos = 30
count = 0
media_alturas = 0

for i in range(num_alunos):
    idade = int(input(f"Digite a idade do {i+1}º aluno: "))
    altura = float(input(f"Digite a altura do {i+1}º aluno (em metros): "))
    idades.append(idade)
    alturas.append(altura)
    if idade > 13:
        total_alturas += altura
        count += 1

if count > 0:
    media_alturas = total_alturas / count
    for i in range(num_alunos):
        if idades[i] > 13 and alturas[i] < media_alturas:
            count -= 1

if count == 0:
    print("Nenhum aluno com mais de 13 anos possui altura inferior à média das alturas.")
else:
    print(f"{count} alunos com mais de 13 anos possuem altura inferior à média das alturas ({media_alturas:.2f}m).")
