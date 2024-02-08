## 5- Calcular as potências de 2 até um determinado número

numero = int(input("Digite um número:"))

i = 0
while 2 ** i <= numero:
    potencia = 2 ** i
    print(f"2 elevado a {i} é igual a {potencia}")
    i += 1
