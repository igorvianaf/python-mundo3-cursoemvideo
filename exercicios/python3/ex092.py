from datetime import date

funcionario = {}
ano_atual = date.today().year

#coletar dados
funcionario['nome'] = input('Informe seu nome completo: ')
ano_nascimento = int(input('Informe o ano que você nasceu: '))
funcionario['idade'] = ano_atual - ano_nascimento
funcionario['ctps'] = int(input('Informe o número da sua carteira de trabalho: (0 = não tem) '))

#condicao para o funcionario possua ctps
if funcionario['ctps'] != 0:
    funcionario['ano de contratação'] = int(input('Informe o ano em que você foi contratado: '))
    funcionario['salário'] = float(input('Informe o valor do seu salário R$: '))
    funcionario['aposentadoria'] = (35 - (ano_atual - funcionario['ano de contratação'])) + funcionario['idade']
    
    #informacoes e calculos de items do dict
    for k, v in funcionario.items():
        print(f'{k}: {v}')

#condicao caso o funcionario nao possua ctps
else:
    for k, v in funcionario.items():
        print(f'{k}: {v}')

