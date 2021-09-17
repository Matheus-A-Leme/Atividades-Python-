import time

vetorA = [1, 70, 3, 4, 5, 90, 7, 8, 9, 10, 11]
vetorB = [1, 74, 3, 4, 5, 6, 7, 8, 9, 10, 67, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
vetorC = [1, 78, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 92, 22, 23, 24, 25, 26, 27, 28, 29,
          30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42]
i = 1
n = 42
contador = 0

# VETOR A

inicio = time.time()
print("\n-----------VETOR_A COM 11 POSICOES:-----------------\n")
print(vetorA)
print("\n-----------VETOR_A POSIÇÃO 2 DO VETOR  - MELHOR CASO---------------\n")
# cont = cont * 2
time.sleep(0.01)
procurado = 70
print("\n Numero na posição {} do vetor: {} ".format(vetorA[1], procurado))
fim = time.time()
tempo_decorrido = fim - inicio
print("\nTempo de execucao: \n", tempo_decorrido * 10000)
print("\nContador = ", contador)

# VETOR A

inicio = time.time()
print("\n-----------VETOR_A POSIÇÃO 2 DO VETOR  - CASO MÉDIO-----------------\n")
# cont = cont * 2
procurado = 90
time.sleep(0.01)
print("\nNumero na posição Mediana do vetor: {} ".format(vetorA[5]))
fim = time.time()
tempo_decorrido = fim - inicio
print("\nTempo de execucao: \n", tempo_decorrido * 10000)
print("\nContador = ", contador)

# VETOR A
inicio = time.time()
print("\n-----------VETOR_A POSIÇÃO DO VETOR 2 - PIOR CASO-----------------\n")
# cont = cont * 2
time.sleep(0.03)
local = 90
if (local != vetorA[i]):
    print("\nPior caso posição {} não existe no vetor".format(local))
    fim = time.time()
    tempo_decorrido = fim - inicio
    print("\nTempo de execucao: \n", tempo_decorrido * 10000)
    print("\nContador = ", contador)

# VETOR B

inicio = time.time()
print("\n-----------VETOR_B COM 21 POSICOES:-----------------\n")
print(vetorB)
print("\n-----------VETOR_B POSIÇÃO 2 DO VETOR  - MELHOR CASO---------------\n")
# cont = cont * 2
time.sleep(0.01)
print("\n Numero na posição 2 do vetor: {} ".format(vetorB[1]))
fim = time.time()
tempo_decorrido = fim - inicio
print("\nTempo de execucao: \n", tempo_decorrido * 10000)
print("\nContador = ", contador)

# VETOR B

inicio = time.time()
print("\n-----------VETOR_B POSIÇÃO 2 DO VETOR  - CASO MÉDIO-----------------\n")
# cont = cont * 2
time.sleep(0.01)
print("\nNumero na posição Mediana do vetor: {} ".format(vetorB[10]))
fim = time.time()
tempo_decorrido = fim - inicio
print("\nTempo de execucao: \n", tempo_decorrido * 10000)
print("\nContador = ", contador)

# VETOR B

inicio = time.time()
print("\n-----------VETOR_B POSIÇÃO DO VETOR 2 - PIOR CASO-----------------\n")
# cont = cont * 2
time.sleep(0.03)
local = 90
if (local != vetorB[i]):
    print("\nPosição {} não existe no vetor".format(local))
    fim = time.time()
    tempo_decorrido = fim - inicio
    print("\nTempo de execucao: \n", tempo_decorrido * 10000)
    print("\nContador = ", contador)

# VETOR C

inicio = time.time()
print("\n----------------------VETOR_C COM 42 POSICOES:-----------------------\n")
print(vetorC)
print("\n-----------VETOR_C POSIÇÃO 2 DO VETOR - MELHOR CASO------------------\n")
# cont = cont * 2
time.sleep(0.01)
print("\n Numero na posição 2 do vetor: {} ".format(vetorC[1]))
fim = time.time()
tempo_decorrido = fim - inicio
print("\nTempo de execucao: \n", tempo_decorrido * 10000)
print("\nContador = ", contador)

# VETOR C
inicio = time.time()
print("\n-----------VETOR_C POSIÇÃO 2 DO VETOR  - CASO MÉDIO-----------------\n")
# cont = cont * 2
time.sleep(0.01)
print("\nNumero na posição Mediana do vetor: {} ".format(vetorC[20]))
fim = time.time()
tempo_decorrido = fim - inicio
print("\nTempo de execucao: \n", tempo_decorrido * 10000)
print("\nContador = ", contador)

# VETOR C
inicio = time.time()
print("\n-----------VETOR_C POSIÇÃO DO VETOR 2 - PIOR CASO-----------------\n")
# cont = cont * 2
time.sleep(0.03)
#print(vetorC)
local = 90
if (local != vetorB[i]):
    print("\nPosição {} não existe no vetor".format(local))
    fim = time.time()
    tempo_decorrido = fim - inicio
    print("\nTempo de execucao: \n", tempo_decorrido * 10000)
    print("\nContador = ", contador)

while (vetorA[i] or vetorB[i] or vetorC[i] != x) and (i < n):
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




# Nome: Matheus Augusto Leme
# Turma: 6ºB
# Rgm: 19398476
