num = []

while True:
    num.append(int(input('Digite um valor: ')))

    sair = input('Você deseja continuar? [S/N]: ').strip()

    if sair in 'Ss':
        continue
    elif sair in 'Nn':
        break
    else:
        print('Opção inválida')

#mostrar os elementos
print(f'foram digitados {len(num)} elementos')

#lista em ordem decrescente
num.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {num}')


if 5 in num:
    print(f'O número 5 está dentro da lista')
else:
    print(f'O valor 5 não foi encontrado na lista')
   