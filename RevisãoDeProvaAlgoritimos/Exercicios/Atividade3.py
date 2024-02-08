'''numero = int(input('Digite o número que você quer a tabuada: '))

print(f"A tabuada de {numero} é:")

for i in range(1, 11, 1):
    print(f'{numero} x {i} = {numero * i}')'''

prova1 = 10 
prova2 = 5

media = (prova1 + prova2)/ 2

print(f'Sua média é:{media}')

if media >= 6:
    print('Parabéns, você está aprovado!')

elif media >=4 <=6:
    print('Você está de recuperação!')
else:
    print('Você está reprovado!')
