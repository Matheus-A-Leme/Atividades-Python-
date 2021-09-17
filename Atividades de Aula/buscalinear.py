#Busca Linear

def busca(lista, x):
    for i in range(len(lista)):
        if lista[i] == x:
            return i
    return None
lista_linear = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 28, 29, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30]
numero = 30


indice = busca(lista_linear, numero)
if indice is not None:
    print("O indice do número {} é: {} ".format(numero, indice))
else:
    print("Este número {} não foi encontrado na lista".format(numero))

#Nome: Matheus Augusto Leme
#Turma: 6ºB
#Rgm: 19398476







