vetor = []

for i in range(10):
    numero = float(input('Digite um número real: '))
    vetor.append(numero)

print('A ordem inversa dos números digitados é: ')
for numero in reversed(vetor):
    print(numero)
