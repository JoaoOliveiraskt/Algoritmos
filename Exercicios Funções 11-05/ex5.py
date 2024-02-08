def soma_imposto(taxaImposto, custo):
    custo += custo * (taxaImposto / 100)
    return custo

taxaImposto = float(input("Digite a taxa de imposto: "))
custo = float(input("Digite o custo: "))
custo_com_imposto = soma_imposto(taxaImposto, custo)
print(f"O custo com imposto é: {custo_com_imposto}")