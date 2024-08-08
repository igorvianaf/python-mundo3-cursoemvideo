numeros = []

while True:
    
    valor = int(input('Digite um valor para adicionar a lista: '))

    #condição para adicionar valor a lista
    if valor not in numeros:
        numeros.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('O valor já foi adicionado anteriormente')
    
    #condicao para sair do loop
    sair = input('Deseja adicionar mais valores? [S/N]')
    if sair in 'Ss':
        continue
    elif sair in 'Nn':
        break
    else:
        print('Opção inválida!')
#nao consegui fazer a lista aparecer em ordem, mesmo usando o sort

print(f'Os números adicionados foram colocados em ordem, são eles:', sorted(numeros))
