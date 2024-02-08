## 4- Determinar se um número é primo ou não

numero = int(input("Digite um número:"))

def isPrimo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

if isPrimo(numero):
    print(numero, "é um número primo.")
else:
    print(numero, "não é um número primo.")
