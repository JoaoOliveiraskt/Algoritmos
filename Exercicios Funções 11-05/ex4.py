def positivo_zero_negativo(n):
    if n > 0:
        return 'P'
    else: 
        return 'N'

numero_P_ou_N = int(input("Digite o número: "))
resultado =  positivo_zero_negativo(numero_P_ou_N)
print(f"O número {numero_P_ou_N} é: {resultado}")  