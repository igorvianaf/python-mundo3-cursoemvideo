from random import randint

lista = []
jogos = []

print('x' * 30)
print('    Jogos da mega sena    ')
print('x' * 30)
quant_jogos = int(input('Quantos jogos devo sortear? '))
tot = 1

while tot <= quant_jogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        
        if cont >= 6:
            break

    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

for i, v in enumerate(jogos):
    print(f'Jogo {i+1}: {v} ')

