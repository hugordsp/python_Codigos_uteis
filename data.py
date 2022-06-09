from datetime import datetime

import os
os.system('cls')

d = input('Digite o dia atual: ')
m = input('Digite o mês atual: ')
a = input('Digite o ano atual: ')


hifen = ('-')
completo = d+hifen+m+hifen+a

d3 = str(datetime.today().strftime('%d-%m-%Y'))

# Data final
d2 = datetime.strptime(d3, '%d-%m-%Y')

# Data inicial
d1 = datetime.strptime(completo, '%d-%m-%Y')


# Realizamos o calculo da quantidade de dias
quantidade_dias = abs((d2 - d1).days)

print(d+hifen+m+hifen+a)

print(quantidade_dias,' dias de vida!')

print(d3)

#print(datetime.today().strftime('%A, %B %d, %Y %H:%M:%S'))

#print(datetime.today().strftime('%Y-%m-%d %H:%M'))

#print(datetime.today().strftime('%Y-%m-%d'))

#print (datetime.today())