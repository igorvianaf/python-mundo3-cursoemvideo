num = (int(input('Digite um valor: ')), int(input('Digite outro valor: ')), 
       int(input('Digite mais um valor: ')), int(input('Digite o último valor: ')))

print(f'Você digitou os valores {num}')


cont_nove = num.count(9)
if cont_nove == 0:
    print('O número 9 não foi digitado')
else:
    print(f'Quantidade de vezes que o número 9 foi digitado: {num.count(9)}')


cont_tres = num.count(3)
if cont_tres == 0:
    print('O número três não foi digitado')
else:
    print(f'O número três apareceu primeiro na {num.index(3) + 1}ª posição')
   

qtd_par = 0

for indice, valor in enumerate(num):
    if int(valor) % 2 == 0:
        qtd_par += 1

print(f'Quantidade de número par: {qtd_par}')
