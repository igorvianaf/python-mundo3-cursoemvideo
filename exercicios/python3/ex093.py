estatistica_jogador = {}
gols_por_partidas = []


estatistica_jogador['nome'] = input('Nome do jogador: ')
qtd_partidas = int(input('Quantas partidas foram jogadas: '))

#gols p/ partida
for c in range(0, qtd_partidas):
    gols_por_partidas.append(int(input(f'Quantos gols na partida {c+1}: ')))


estatistica_jogador['gols'] = gols_por_partidas[:]

estatistica_jogador['total'] = sum(gols_por_partidas)


print('=-' * 30)
print(estatistica_jogador)


print('=-' * 30)
for k, v in estatistica_jogador.items():
    print(f'O campo {k} tem o valor {v}')

print('=-' * 30)

print(f'O jogador {estatistica_jogador["nome"]} jogou {qtd_partidas} partidas.')
print('=-' * 30)
for k, v in enumerate(estatistica_jogador['gols']):
    print(f'=> Na partida {k + 1}, fez {v} gols.')
print(f'Com o total de {estatistica_jogador["total"]}')
