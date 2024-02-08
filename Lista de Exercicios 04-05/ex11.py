vetor1 = []
vetor2 = []
vetor3 = []
vetor4 = []


for i in range(10):
    numero = int(input(f"Informe o {i+1}º número do primeiro vetor: "))
    vetor1.append(numero)

for i in range(10):
    numero = int(input(f"Informe o {i+1}º número do segundo vetor: "))
    vetor2.append(numero)

for i in range(10):
    numero = int(input(f"Informe o {i+1}º número do terceiro vetor: "))
    vetor3.append(numero)


for i in range(10):
    vetor4.append(vetor1[i])
    vetor4.append(vetor2[i])
    vetor4.append(vetor3[i])

print(f"Números intercalados: {vetor4}")