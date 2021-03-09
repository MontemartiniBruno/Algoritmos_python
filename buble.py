import random

def buble_sort(lista):
    n = len(lista)
    for i in range (0, n):        
        for j in range(0, n - 1  ):             
             if lista[i] < lista[j]:
                 lista[i], lista[j] = lista[j], lista[i]
    
    return (lista)


if __name__ == '__main__':
    
    tamano_lista = int(input('De que tamano deseas la lista: '))

    lista = [random.randint(0, 100) for i in range (tamano_lista)]

    
    print(lista)

    lista_ordenada = buble_sort(lista)
    print(lista_ordenada)