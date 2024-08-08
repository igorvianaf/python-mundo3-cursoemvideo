from utilidadescev import moeda, dado


p = dado.leiaPreco('Digite o preço: ')
aumentar = float(input('Porcentagem de aumento de preço: '))
diminuir = float(input('Porcentagem para diminuir o preço: '))



moeda.resumo(p, aumentar, diminuir, formato=True)