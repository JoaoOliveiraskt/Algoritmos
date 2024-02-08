## 3- Calcular a tabuada de um número fornecido pelo usuário
numero = int(input("Digite um número para imprimir a tabuada:"))

if numero:
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} X {i} = {resultado}")
else:
    print("O valor digitado não é um número.")



