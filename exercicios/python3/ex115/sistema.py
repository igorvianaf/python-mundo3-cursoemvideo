from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not verificarArquivo(arq):
    criarArquivo(arq)


while True:
    #lib - criar menu em lista e receber opcao de usuario
    opcao = menu(['Listar','Cadastrar', 'Sair'])

    if opcao == 1:
        lerArquivo(arq)
    elif opcao == 2:
        cabecalho('NOVO CADASTRO')
        nome = input('Nome: ')
        idade = leiaIdade('Idade: ')
        cadastrar(arq, nome, idade)
    elif opcao == 3:
        cabecalho('\033[32mSaindo do sistema...Obrigado e volte sempre!\033[m')
        break
    else:
        print('\033[31mERRO! Por favor, escolha uma opção que esteja disponível no MENU.\033[m')
    sleep(1)
