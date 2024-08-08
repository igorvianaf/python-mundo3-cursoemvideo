matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
num_par = soma_colunas = maior_valor = 0


# l é o índice da lista maior, e c é o indice da lista interna - linhas e colunas
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        
        #incluir soma de núm par
        if matriz[l][c] % 2 == 0:
            num_par += matriz[l][c]

#maior valor linha 2        
for v in matriz[1]:
    if v > maior_valor:
        maior_valor = v

#soma colunas        
for l in range(0, 3):
    soma_colunas += matriz[l][2]

print('=-' * 30)

#criando a matri, onde l é a linha da matriz e c são as colunas
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()


print(f'A soma dos números par é de: {num_par}')
print(f'A soma dos valores da terceira coluna é de: {soma_colunas}')
print(f'O maior valor da segunda linha é: {maior_valor}')
