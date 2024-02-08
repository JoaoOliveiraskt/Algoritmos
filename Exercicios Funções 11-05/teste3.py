def positivo_negativo(numero):
   if numero <= 0:
      print(f'{numero} = N')
   else:
      print(f'{numero} = P')


argumento = int(input('Digite um número: '))
positivo_negativo(argumento)
