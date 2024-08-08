def leiaPreco(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'{entrada} não é considerado um preço válido')
        else:
            valido = True
            return float(entrada)