tabela_brasileirao = ('Palmeiras', 'Gremio', 'Atletico MG', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense', 'Athletico PR', 'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco da gama', 'Bahia', 'Santos', 'Goias', 'Coritiba', 'America MG')

print('=' * 30)
print('Os 5 primeiros colocados foram: ')
for indice, valor in enumerate(tabela_brasileirao[:5]):
    print(f'O {indice + 1}º colocado {valor}')

print('=' * 30)

print('Os quatro times rebaixados foram: ')
for cont in range(16, len(tabela_brasileirao)):
    print(f'O {cont + 1}º colocado {tabela_brasileirao[cont]}')

print('=' * 30)
print(sorted(tabela_brasileirao))

print('=' * 30)
print(f'O {tabela_brasileirao[3]} está em', tabela_brasileirao.index('Flamengo') + 1, 'º colocado')
print('=' * 30)
