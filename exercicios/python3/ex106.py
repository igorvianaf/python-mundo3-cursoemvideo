def ajuda(com):
    help(com)


comando = ''
while True:
    comando = input('Função ou Biblioteca: ')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)