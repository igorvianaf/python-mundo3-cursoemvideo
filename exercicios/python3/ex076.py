produtos = ('Caneta', 2.00, 
            'Lápis', 2.00, 
            'Borracha', 0.50, 
            'Caderno', 20.00, 
            'Estojo', 15.00)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R$ {produtos[pos]:>4.2f}')