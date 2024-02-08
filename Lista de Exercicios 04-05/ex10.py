vetor1 = []
vetor2 = []
vetor3 = []


for i in range(10):
    numero = int(input(f"Informe o {i+1}º número do primeiro vetor: "))
    vetor1.append(numero)

for i in range(10):
    numero = int(input(f"Informe o {i+1}º número do segundo vetor: "))
    vetor2.append(numero)


for i in range(10):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])

print(f"Números intercalados: {vetor3}")

