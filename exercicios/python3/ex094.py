pessoa = {}
galera = []
soma = media = 0

while True:
    #limpar o dict para receber novos dados
    pessoa.clear()
    pessoa['nome'] = input('Nome: ')

    #verificando resposta - sexo
    while True:
        pessoa['sexo'] = input('Sexo: [F/M] ').upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        else:
            print('ERRO! O campo recebe apenas F ou M')

    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']

    #copiar um dict dentro de uma lista
    galera.append(pessoa.copy())
    #verificando resp
    while True:
        resp = input('Quer continuar? [S/N]').upper()[0]
        if resp in 'SN':
            break
        else:
            print('ERRO! O campo recebe apenas S/N')
    if resp == 'N':
        break        

print('=-' * 30)
print(f'> Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'> A média de idade do grupo é de {media:5.2f}')
print('> As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}', end=' ')
print()
print('> Lista de pessoas que estão acima da média: ', end='')
for p in galera:
    if p['idade'] >= media:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='' )
        print()
print('<<ENCERRADO>>')
