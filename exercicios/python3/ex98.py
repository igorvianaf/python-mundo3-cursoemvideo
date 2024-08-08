from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} ao {f} de {p} em {p}')
    
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont -= p
        print('FIM!')



#programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora você pode personalizar a contagem, informando inicio, fim e o intervalo entre os números')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Intervalo: '))
contador(inicio, fim, passo)

