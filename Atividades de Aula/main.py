import random
from buscabinaria import busca

lista_binaria = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

if __name__ == "__main__":
    continuar = 's'
    while (continuar == 's'):
        print("-------------------------------")
        e = int(input("Elemento a ser procurado: "))
        i = busca(lista_binaria, e)
        print("\n Índice encontrado:", i)
    continuar = input("Repetir? (S/N): ").lower()
print("*******************************")

#Nome: Matheus Augusto Leme
#Turma: 6ºB
#Rgm: 19398476