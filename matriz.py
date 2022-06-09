import os 
os.system('cls')

def GeradorMatriz (n_Linhas, n_Colunas):
    return [['']*n_Linhas for _ in range(n_Colunas)]

n_Linhas = int(input('Digite o número de linhas: ')) 
n_Colunas = int(input('Digite o número de colunas: '))
matriz = GeradorMatriz(n_Linhas, n_Colunas)

for l in range(n_Linhas):
    for c in range(n_Colunas):
        matriz[l][c] = int(input(f'Digite valor para [{l}, {c}]: '))
print('-'*50)
for l in range(n_Linhas):
    for c in range(n_Colunas):
        print(f'[{matriz[l][c]:^5}]', end='')
    print() 
print('-'* 50)          

