from moeda import *

p = float(input('Digite o preço: '))
print(f'A metade de {p} é: {metade(p)}')
print(f'O dobro de {p} é: {dobro(p)}')
print(f'Aumentando 10%, temos: {aumentar(p, 10)}')
print(f'Reduzindo 13%, temos: {diminuir(p, 13)}')