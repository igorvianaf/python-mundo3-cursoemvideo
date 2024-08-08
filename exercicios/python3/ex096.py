def area (x, y):
    a = x * y
    print(f'A área do seu terreno de {x} x {y} é de {a}m²')


#programa principal
print('CONTROLE DE TERRENOS')
print('-' * 30)
area(x=float(input('Largura (m): ')), y=float(input('Comprimento (m): ')))