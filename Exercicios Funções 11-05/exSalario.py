def aumentoSalario(salario):
    aumento15 = salario + (salario * 15/100)
    print('O novo salario do funcionário com 15% de aumento é R${:.2f}'.format(aumento15))

salario = float(input('Qual é o salário atual? R$'))
aumentoSalario(salario)