boletim = []
while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    boletim.append([nome, [nota1, nota2], media])
    adc = input('Deseja adicionar um novo aluno? [S/N]: ')

    if adc in 'sS': 
        continue
    elif adc in 'nN':
        break
    else:
        print('Desculpe, resposta inválida!')

print('-' * 30)
print(f'{"No.":<4}{"NOME":<10}{"Média":>8}')
print('-' * 26)

for i, v in enumerate(boletim):
    print(f'{i:<4}{v[0]:<10}{v[2]:>8.1f}')

while True:
    print('-' * 30)
    nota_detalhada = int(input('Baseado no No., gostaria de analisar a nota de qual aluno? [999 para sair]'))

    if nota_detalhada == 999:
        break
    
    if nota_detalhada <= len(boletim)-1:
        print(f'Notas de {boletim[nota_detalhada][0]} são {boletim[nota_detalhada][1]}')
    elif nota_detalhada >= len(boletim)-1:
        print('No. de Índice inválido!')
        