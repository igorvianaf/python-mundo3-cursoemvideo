import moeda

p = float(input('Digite o preço: '))
m = input('Qual moeda você deseja utilizar? ').strip()


print(f'A metade de {moeda.moeda(p, m)} é: {moeda.moeda(moeda.metade(p), m)}')
print(f'O dobro de {moeda.moeda(p, m)} é: {moeda.moeda(moeda.dobro(p), m)}')
print(f'Aumentando 10%, temos: {moeda.moeda(moeda.aumentar(p, 10), m)}')
print(f'Reduzindo 13%, temos: {moeda.moeda(moeda.diminuir(p, 13), m)}')