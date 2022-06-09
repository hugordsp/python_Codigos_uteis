from datetime import datetime

import os
os.system('cls')

#Dados da data de nascimento;
d = input('Digite o dia do seu nascimento no formato "dd": ')
m = input('Digite o mês nascimento no formato "mm": ')
a = input('Digite o ano nascimento no formato "aaaa": ')

#Transformando dados anteriores em um única string;
hifen = ('-')
completo = d+hifen+m+hifen+a

#Criação de STRING para data atual;
#OBS: para entrar na função 'datetime' a STRING precisa entrar com o formato dd-mm-aaaa;
dia_atual = str(datetime.today().strftime('%d-%m-%Y'))

# DATA INICIAL;
d1 = datetime.strptime(completo, '%d-%m-%Y')

# DATA FINAL;
d2 = datetime.strptime(dia_atual, '%d-%m-%Y')

#Cálculo da quantidade de dias;
quantidade_dias = abs((d2 - d1).days)

#Cálculo da idade da pessoa em anos meses e dias;
resto_anos = quantidade_dias % 365
anos = (quantidade_dias-resto_anos)/365
resto_meses = resto_anos % 30
meses = (resto_anos - resto_meses)/30

#Imprime na tela a quantidade de dias de vida;
print('')
print('Você possui',quantidade_dias,'dias de vida!')
print('Você possui ', anos, 'anos,', meses,'meses e', resto_meses, 'dia(s) de vida!')
print('')
print('Fim do algoritmo.')