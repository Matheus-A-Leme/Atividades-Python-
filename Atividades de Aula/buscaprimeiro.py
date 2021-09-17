import time
from timeit import default_timer as timer

p1 = "VETOR A COM 11 POSIÇÕES"
p2 = "VETOR B COM 21 POSIÇÕES"
p3 = "VETOR C COM 42 POSIÇÕES"

vetorA = [71, 70, 3, 4, 5, 90, 7, 8, 9, 10, 11] #VETOR A
vetorB = [81, 74, 3, 4, 5, 6, 7, 8, 9, 10, 67, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21] #VETOR B
vetorC = [91, 78, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 92, 22, 23, 24, 25, 26, 27, 28, 29,
          30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42] #VETOR C
i = 0
contador = 0
sinal = False
n = 11
a = 70  #Variavel para armazenar o numero que vai guarda a posicao


print('\nNumero a ser procurado no vetor: ', a)
print("\n----------- {} -----------------\n".format(p1)) #Para ver na tela o tamanho do Vetor esse no caso é o de 11 #Para utilizar o de 21 posicões p2 e p3 para o de 42 posições
print(vetorA)#Printando na tela o vetorA


inicio = timer()
while (vetorA[i] != a) and (i < n):   #ALTERE O VETOR AQUI PARA UTILIZAR OUTROS VETORES NO CASO ESTÁ SENDO UTILIZADO O DE 42 POSIÇÕES
    i = i + 1
    contador = contador + 1
    if a == vetorA[i]:
        sinal = True
        print("\nElemento encontrado na posição: ", i)
        print("Contador: ", contador)
        break
    elif a != vetorA[i]:
        sinal = False
        print("Elemento não encontrado.")
    else:
        print("Este número não foi encontrado no vetor ", a)


final = timer()
tempo_decorrido = final - inicio
print("\nTempo de execução: \n", tempo_decorrido * 100000000)

input()

# Nome: Matheus Augusto Leme   Rgm: 19398476
# Nome: Henrique Sousa Pena    Rgm: 19768281
# Nome: Alexandre Souza Gomes da Silva   Rgm: 18882226
# Turma: 6ºB
