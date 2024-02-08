## 6- Calcular o fatorial de um número

numero = int(input("Digite um número: "))
fatorial = 1

for i in range(2, numero + 1):
    fatorial *= i

print(f"O fatorial de {numero} é igual a {fatorial}")

