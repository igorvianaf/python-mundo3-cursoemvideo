aluno = {}

aluno['Nome'] = input('Nome: ')
aluno['Média'] = float(input(f'A média de {aluno["Nome"]}: '))


if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'

elif 5 <= aluno['Média'] < 7 :
    aluno['Situação'] = 'Recuperação'   

else:
    aluno['Situação'] = 'Reprovado'

for k, v in aluno.items():
    print(f'{k}: {v}')