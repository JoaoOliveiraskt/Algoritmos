letras = []

for i in range(10):
    letra = input(f'Digite o {i+1}º caractere: ').lower()
    letras.append(letra)

consoantes = 0
listaConsoantes = []

for letra in letras:
    if letra.isalpha() and letra not in ['a', 'e', 'i', 'o', 'u']:
        consoantes += 1
        listaConsoantes.append(letra)

print(f'Foram lidas {consoantes} consoantes.')
if consoantes > 0:
    print('As consoantes digitadas foram: ' + ' '.join(listaConsoantes))
