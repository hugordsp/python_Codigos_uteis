import os
os.system('cls')

def CalculaJuros(v, j):
    r = v + (v*j/100)
    return r

valor = float(input('Digite o valor da compra: R$ ')) 
juros = float(input('Digite o valor do juros: '))

resultado = CalculaJuros(valor, juros)

print('O valor atualizado é: {:2f}.'.format(resultado))