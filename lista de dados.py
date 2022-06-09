
import os
os.system('cls')

vetor = [0,0,0,0,0]
i = 0
for i in range(5):
    vetor[i] = float (input("Digite o valor: "))
    while vetor[i]<0:
        vetor[i] = float (input("Digite um número maior que zero. "))

vetor.sort()
print(vetor[0],vetor[4])

