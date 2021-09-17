import random
from TesteQuick import quicksort


any_numbers = random.sample(range(1, 10000),977)


if __name__ == "__main__":
    test_cases = {'Números aleatórios': any_numbers
                }
    print("*******************************")
    for name, lista in test_cases.items():
        print("\nCaso de teste: {}".format(name))
        print(lista)
        quicksort(lista)
        print("\n Ordenado:")
        print(lista)
    print("*******************************")