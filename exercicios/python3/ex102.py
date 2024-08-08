def fatorial(num, show=False):
        """
        Calculo de fatorial:
        num = numero a ser calculado
        show = Mostrar ou nao a conta
        return = O valor do fatorial de um num
        """
        f = 1    
        for c in range(num, 0, -1):
            if show:
                print(c, end='')
                if c > 1:
                    print(' x ', end='')
                else:
                    print(f' = ', end='')
            f *= c
        if show == False:
            print(f'O resultado de {num} fatorial é: {f}')
        return f




user_num = int(input('Informe um número para saber ser fatorial: '))
while True:
    exibir_conta = input('Gostaria de exibir a conta fatorial? [S/N] ').upper()[0]
    if exibir_conta in 'S': 
        print(fatorial(user_num, show=True))
        break
    elif exibir_conta in 'N':
        fatorial(user_num)
        break
    else:
        print('Resposta inválida. O campo recebe apenas S/N [S=SIM/ N=NÃO]')

