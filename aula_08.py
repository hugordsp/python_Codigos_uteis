import os
os.system('cls')

#MATRIZ ESTRUTURADA TODA NA MESMA LINHA:
matriz = [[1,2,3],[4,5,6],[7,8,9]]
print(matriz)
print()

#MATRIZ ESTRUTURADA COMO MATRIZ:
for i in range(0,len(matriz),1):
    print(matriz[i])
print()

#MATRIZ ESTRUTURADA COMO MATRIZ, MAS SEM ASPAS:
for l in range (0,len(matriz),1):
    for c in range(0,len(matriz),1):
        print(f'{matriz[l][c]:^5}',end= ' ')
    print()
print()    
#MATRIZ ESTRUTURADA COMO MATRIZ, MAS ADICIONANDO VALOR POR VALOR:
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite valor para [{l}, {c}]: '))
print('-'*21)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-' * 21)
