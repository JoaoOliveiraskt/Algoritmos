def calcularDesconto(numero):
    novoPreco = numero - (numero * (5/100))
    
    print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preco, novoPreco))

preco = int(input('Qual o preço do produto: R$'))
calcularDesconto(preco)