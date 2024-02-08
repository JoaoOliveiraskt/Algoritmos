def calcPreco(preco):
    if preco == 'Vv':
        descontoAvista = preco - (preco * 10/100)
        print(descontoAvista)
    elif preco == 'Pp':
        parcelado = preco + (preco * 8/100)
        print(parcelado)
    else:
        print('Digite [V] para pagamento a vista com desconto de 10% ou [P] para pagamento parcelado com juros de 8%')

    
valor = float(input('Digite o preço R$'))   
v_ou_p = str(input('Deseja pgar a vista[v] ou parcelado[p] ?'))
calcPreco(valor)