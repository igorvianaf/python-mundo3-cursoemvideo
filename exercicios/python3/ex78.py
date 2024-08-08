valores = []
maior_valor = 0
menor_valor = 0

for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))

    if cont == 0:
        maior_valor = menor_valor = valores[cont]
    else:
        if valores[cont] > maior_valor:
            maior_valor = valores[cont]
        if valores[cont] < menor_valor:
            menor_valor = valores[cont]

print('=-' * 30)
print(f'Você digitou os valores: {valores}')


print(f'O maior valor é: {maior_valor}, nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior_valor:
        print(f'{i}...', end='')
print()

print(f'O menor valor é: {menor_valor}, na posições ', end='')
for i, v in enumerate(valores):
    if v == menor_valor:
        print(f'{i}...', end='')
