idades = []
alturas = []

for i in range(2):
    idade = int(input(f"Informe a idade da {i+1}ª pessoa: "))
    altura = float(input(f"Informe a altura da {i+1}ª pessoa (em metros): "))
    idades.append(idade)
    alturas.append(altura)

print("Idades lidas na ordem inversa:")
for idade in reversed(idades):
    print(idade)

print("Alturas lidas na ordem inversa:")
for altura in reversed(alturas):
    print(f"{altura:.2f}")
