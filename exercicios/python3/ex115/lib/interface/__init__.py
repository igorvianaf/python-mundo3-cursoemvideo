def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, escolha uma opção que esteja disponível no MENU.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mO usuário escolheu deixar o campo vazio!\033[m')
            break
        else:
            return n


def linha(tam = 42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    """
    Função para criar os itens do menu e receber opção do usuario
    Sendo lista o parametro em list para cada opcao do menu
    Item a iteração para mostrar o menu
    return sendo opc, com a entrada do usuario validada pelo parametro leiaInt
    """
    cabecalho('\033[33mMENU PRINCIPAL\033[m')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - {item}')
        c += 1
    print(linha())
    opc = leiaInt('\033[33mEscolha uma opção: \033[m')
    return opc



def leiaIdade(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Valor inválido para o campo idade. Por favor, informe uma idade válida.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mO usuário escolheu deixar o campo vazio!\033[m')
            break
        else:
            return n