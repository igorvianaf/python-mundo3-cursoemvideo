temp = []
principal = []
maior = menor = 0

while True:
    temp.append(input('Nome: ').strip())
    temp.append(float(input('Peso: ').strip()))
    if len (principal) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]

    principal.append(temp[:])
    temp.clear()

    sair = input('Quer continuar? [S/N] ').strip()
    if sair in 'Nn':
        break

print(f'A quantidade de pessoas cadastradas foi: {len(principal)}')

print(f'O maior peso foi de {maior} Kg. Peso de ', end='')
for p in principal:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')

print()
print(f'O menor peso foi de {menor} Kg. Peso de: ', end='')
for p in principal:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()

