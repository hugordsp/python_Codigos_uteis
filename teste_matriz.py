import os
os.system('cls')

#FUNÇÃO DEFINIDORA DO TAMANHO DA MATRIZ:
def GeradorMatriz(n_linhas, n_colunas):
    return [[" "]*n_colunas for _ in range(n_linhas)]

#VARIÁVEIS PARA DEFINIR O NÚMERO DE LINHA E COLUNAS DA MATRIZ:
n_linhas = int(input('\nDigite o número de linhas da matriz: '))
n_colunas = int(input('\nDigite o número de colunas da matriz: '))
Matriz = GeradorMatriz(n_linhas, n_colunas)

#TESTES DO QUE SAI AO IMPRIMIR
print(Matriz)
print([''] * n_colunas)
print()

#MATRIZ ESTRUTURADA em LINHAS X COLUNAS, MAS ADICIONANDO VALOR POR VALOR:
for l in range(n_linhas):
    for c in range(n_colunas):
        Matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print()
for l in range(n_linhas):
    for c in range(n_colunas):
        print(f'[{Matriz[l][c]:^5}]', end='')
    print()
print('-' * 10, 'Fim!', '-' * 10)
