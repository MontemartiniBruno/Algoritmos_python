import random

def marge_sort(lista):

    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista [medio:]

        # Llamada recursiva en cada mitad para obtener todas las sublistas de 1 elemento
        marge_sort(izquierda)
        marge_sort(derecha) 

        # Definicion de iteradores 
        i = 0
        j = 0
        k = 0

        while i < len(izquierda) and j < len(derecha):
            
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else: 
                lista[k] = derecha [j]
                j += 1
            
            k += 1

        while i < len(izquierda):
            
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            
            lista[k] = derecha[j]
            j += 1
            k += 1


    return (lista)


if __name__ == '__main__':
    
    tamano_lista = int(input('De que tamano deseas la lista: '))

    lista = [random.randint(0, 100) for i in range (tamano_lista)]

    
    print(lista)
    print('-' * 50)

    lista_ordenada = marge_sort(lista)
    print(lista_ordenada)