num1 = float(input("Digite o número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if num1 < num2:
    menor = num1
else:
    menor = num2
    
print("O menor número entre", num1, "e", num2, "é", menor)
