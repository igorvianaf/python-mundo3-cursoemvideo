import moeda

p = float(input('Digite o preço: '))
aumentar = float(input('Porcentagem de aumento de preço: '))
diminuir = float(input('Porcentagem para diminuir o preço: '))



moeda.resumo(p, aumentar, diminuir, formato=True)