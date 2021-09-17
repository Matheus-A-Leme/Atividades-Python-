import time

from buscaprimeiro import buscaprimeiro

while vetorA[i] or vetorB[i] or vetorC[i] != x and i < n:
    i = i + 1
    contador = contador + 1
    time.sleep(1)
    if vetorA[i] or vetorB[i] or vetorC[i] != x:
        sinal = False
        contador = contador + 1

    else:
        sinal = True
        local = i
        contador = contador + 1



