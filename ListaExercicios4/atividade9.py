altura = float(input("Digite a sua altura em metros: "))
sexo = input("Digite o seu sexo (M para masculino e F para feminino): ")

if sexo == "M":
    peso_ideal = (72.7 * altura) - 58
    print("O seu peso ideal é", peso_ideal, "kg")
elif sexo == "F":
    peso_ideal = (62.1 * altura) - 44.7
    print("O seu peso ideal é", peso_ideal, "kg")
else:
    print("Sexo inválido. Por favor, digite M para masculino ou F para feminino.")