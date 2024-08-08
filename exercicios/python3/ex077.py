palavras  = ('hamburguer', 'pastel', 'coxinha', 'refrigerante', 'batata', 'sorvete', 'carne', 'acai', 'pizza')


for indice in palavras:
    vogal = ''

    for letra in indice:
        if letra.lower() in 'aeiou':
            vogal += letra
    print(f'Na palavra {indice.upper()} encontramos as vogais: {vogal}')
