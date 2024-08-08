geral = []
par = []
impar = []

while True:
    num = int(input('Digite um número: '))
    geral.append(num)

    if num % 2 == 0:
        par.append(num)
    elif num % 2 == 1:
        impar.append(num)
    
    sair = input('Deseja adicionar mais números? [S/N]').strip()

    if sair in 'Ss':
        continue
    elif sair in 'nN':
        break
    else:
        print('Opção inválida.')

print(f'A lista geral é: {geral}')
print(f'Número par digitados: {par}')
print(f'Número ímpar digitados: {impar}')
