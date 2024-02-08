vetor = []

for i in range(10):
    numero = int(input(f"Informe o {i+1}º número: "))
    vetor.append(numero)

soma_quadrados = 0
for numero in vetor:
    soma_quadrados += numero ** 2

print(f"A soma dos quadrados dos elementos do vetor é: {soma_quadrados}")

