def imprimirNumeros(n):
    for i in range(1, n+1):
        novaLinha = ' '.join(
            str(r) for r in range(1, i+1)
        )
        print(novaLinha)

termoN = int(input('Digite um número: '))
imprimirNumeros(termoN)
