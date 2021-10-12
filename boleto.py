from datetime import date
import random

banco = '341-7'
chave = str(random.randrange(1000, 10001))

data = date.today().strftime('%d%m%Y')
valor = str(input('Qual o valor do boleto? -> R$'))
codigo_boleto = f'{banco} | {chave}{data}{"0"*8}{valor}'

print(codigo_boleto)