def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mO usuário escolheu deixar o campo vazio!\033[m')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (TypeError, ValueError):
            print('\033[31mO campo só recebe número real\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mErro. O usuário deixou o campo inválido.\033[m')
            return 0
        else:
            return n
