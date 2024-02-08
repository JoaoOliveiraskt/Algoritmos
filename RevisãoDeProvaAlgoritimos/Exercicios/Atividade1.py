n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = (n1 + n2 + n3)// 3
print('A sua média é: ',media)

if media >= 6:
    print("Parabéns, você está aprovado!")

elif media >= 4 <=6:
    print("Você está de recuperação!")
else:
    print("Você esá reprovado!")


