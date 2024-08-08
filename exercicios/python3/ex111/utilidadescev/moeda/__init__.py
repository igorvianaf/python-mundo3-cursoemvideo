def metade(preco=0, formato=False):
    res = preco / 2
    return res if formato is False else moeda(res)

def dobro(preco=0, formato=False):
    res = preco * 2
    return res if formato is False else moeda(res)

def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * (taxa/100))
    return res if formato is False else moeda(res)

def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * (taxa/100))
    return res if formato is False else moeda(res)

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(preco=0, taxaaumento=10, taxareducao=5, formato=False):
    print('*' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('*' * 30)
    print(f'Preço Analisado: \t{moeda(preco)}')
    print(f'A metade de {preco} é: \t{metade(preco, formato)}')
    print(f'Dobro de {moeda(preco)} é: \t{dobro(preco, formato)}')
    print(f'Aumentando {taxaaumento}%, temos: \t{aumentar(preco, taxaaumento, formato)}')
    print(f'Reduzindo {taxareducao}%, temos: \t{diminuir(preco, taxareducao, formato)}')
    print('*' * 30)
