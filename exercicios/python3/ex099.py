def maior(*args):
    cont = maior = 0
    print('\nAnalisando os valores passados')
    for valor in args:
        print(f'{valor}', end=' ')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print()
    print(f'Foram informados {cont} valores ao todo')
    print(f'O maior valor informado foi: {maior}')

#programa principal
maior(19, 8, 3, 5, 39, 15)
maior(3, 76, 21, 1, 34)
maior(4, 64, 23)
maior(0)
