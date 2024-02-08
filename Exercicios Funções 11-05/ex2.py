def imprimir_numeros(n):
    for i in range(1, n+1):
        nova_linha = ' '.join(str(r) for r in range(1, i+1))
        print(nova_linha)

n = int(input("Digite o número: ")) 
imprimir_numeros(n)