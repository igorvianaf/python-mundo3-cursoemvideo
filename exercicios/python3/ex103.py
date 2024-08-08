def ficha(nome='<Desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')


jogador = input('Informe o nome do jogador: ')
quantidade_gols = input('Informe a quantidade de gols: ')
if quantidade_gols.isnumeric():
    quantidade_gols = int(quantidade_gols)
else:
    quantidade_gols = 0
if jogador.strip() == '':
    ficha(gols=quantidade_gols)
else:
    ficha(jogador, quantidade_gols)
