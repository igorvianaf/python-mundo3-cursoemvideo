extenso = (('zero', 'um', 'dois', 'três','quatro', 'cinco', 'seis', 'sete', 'oito','nove','dez', 'onze', 'doze', 'treze', 'quatorze','quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'))

numero = int(input('Digite um número entre 0 e 20: '))

while numero not in range(0,21):
    numero = int(input('Número inválido. Digite um número entre 0 e 20: '))
    
print(f'O número digitado foi o {extenso[numero]}')
