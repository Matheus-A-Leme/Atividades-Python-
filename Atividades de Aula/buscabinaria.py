#Busca Binária

def busca(array, elemento, x=0, y=None):
    if y is None:
        y = len(array)-1
    if x <= y:
        res = (x + y)// 2
        if array[res] == elemento:
            return res
        if elemento < array[res]:
            return busca(array, elemento, x, res-1)
        else:
            return busca(array, elemento, res+1, y)
        return None

#Nome: Matheus Augusto Leme
#Turma: 6ºB
#Rgm: 19398476