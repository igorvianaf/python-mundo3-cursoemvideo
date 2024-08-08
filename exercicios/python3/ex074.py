#gerar num aleatórios e comparar valores

import random


numero_aleatorio = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), 
         random.randint(1, 10), random.randint(1, 10))


for n in numero_aleatorio:
    print(n, end=' ')

print(f'\nO menor valor é {min(numero_aleatorio)}')
print(f'O maior valor é {max(numero_aleatorio)}')
