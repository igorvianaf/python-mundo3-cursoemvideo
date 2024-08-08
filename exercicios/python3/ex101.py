def voto(anoNascimento):
    from datetime import date
    data_atual = date.today().year
    idade_atual = data_atual - anoNascimento

    if idade_atual < 16 :
        return f'Com {idade_atual} anos você não pode votar!'
    elif 16 <= idade_atual < 18 or idade_atual > 65:
        return f'Com {idade_atual} anos o voto é opicional!'
    else:
        return f'Com {idade_atual} anos o voto é obrigatório!'


user_ano_nascimento = int(input('Informe seu ano de nascimento: '))
print(voto(user_ano_nascimento))