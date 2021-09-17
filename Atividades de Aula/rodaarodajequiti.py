# ALGORITMO DESENVOLVIDO POR CAIQUE SANTOS GOULART
# E EDUARDO HENRIQUE BRANDÃO

import time
from timeit import default_timer as timer

a = list(range(10, 52))  # Para vetor de 11 termos fazer (10, 21), 21 termos (10, 31) e 42 termos (10, 52)
print(a)
print('Vetor tem: ', len(a), ' elementos')

x = 2000  # Elemento a ser encontrado
j = 1  # Termo inicial do array
cont = 0  # contador de passos do algoritmo
sinal = False

print('Elemento a ser buscado: ', x)
print('Wait.....................................')


start = timer()  # Começo do contador de tempo
while (a[j] != x) and (j < 42):  # Função de busca # Para 11 termos, usar 11 após o J, para 21 termos usar 21 e para 42 termos usar 42
    j = j + 1
    cont = cont + 1
    print('Buscando elemento......')
    time.sleep(0.5)
    if j == 41 and a[j] != x:  # j == 10 para 11 termos, j == 20 para 21 termos, j == 41 para 42 termos
        print('elemento nao existe')
        print('contagem de passos realizados', cont)
        break
    elif a[j] != x:
        sinal = False
    elif a[j] == x:
        sinal = True
        print('Elemento encontrado na posição: ', j)
        print('Contagem de passos realizados: ', cont)
end = timer()  # Término de contagem do tempo

print('Tempo levado: ', int(end - start), ' segundos')


input()