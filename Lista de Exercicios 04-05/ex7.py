numeros = []
quantidade_numeros = 5

for i in range(quantidade_numeros):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)

soma = sum(numeros)
produto = 1
for numero in numeros:
    produto *= numero

print(f"Números lidos: {numeros}")
print(f"Soma dos números: {soma}")
print(f"Produto dos números: {produto}")

