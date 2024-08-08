def fatorial (num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Informe um número para saber o fatorial: '))
print(f'O resultado fatorial de {n} é: {fatorial(n)}')