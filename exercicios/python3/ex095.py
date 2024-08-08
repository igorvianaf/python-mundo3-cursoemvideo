jogador = {}
partidas = []
time = []

while True:
    jogador.clear()
    jogador['nome'] = input('Nome do jogador: ')
    qtd_partidas = int(input('Quantas partidas foram jogadas: '))

    partidas.clear()
    #gols p/ partida
    for c in range(0, qtd_partidas):
        partidas.append(int(input(f'Quantos gols na partida {c+1}: ')))

    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    
    while True:
        resp = input('Quer continuar? [S/N]: ').upper()[0]
        if resp in 'SN':
            break
        else:
            print('ERRO! Resposta inválida')
    if resp == 'N':
        break    

print('=-' * 30)
print('Cod.  ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()

print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

while True:
    busca = int(input('Mostrar dados de qual jogador? [999 = sair] '))
    if busca == 999:
        break
    if busca > len(time):
        print(f'ERRO! Não existe jogador com o código {busca}')
    else:
        print(f'LEVANTAMENTO DO JOGADOR: {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'No jogo {i + 1} fez {g} gols.')
    print('-' * 40)

print('<<< VOLTE SEMPRE >>>')
