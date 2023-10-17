import sys
import timeit
import itertools

def calcular_memoria_lista(lista):
    return sys.getsizeof(lista)

def calcular_memoria_tupla(tupla):
    return sys.getsizeof(tupla)

def calcular_tiempo_acceso_lista_con_metodo(lista):
    return timeit.timeit(lambda: "".join(itertools.chain(*lista)), number=100000)

def calcular_tiempo_acceso_lista_como_vector(lista):
    return timeit.timeit(lambda: "".join(list(lista)), number=100000)

def main():
    # Creamos una lista y una tupla con el mismo contenido
    lista = [1, 3, 4, 5, "hello", True]
    tupla = (1, 3, 4, 5, "hello", True)

    # Calculamos el tamaño en memoria de la lista y la tupla
    tamaño_lista = calcular_memoria_lista(lista)
    tamaño_tupla = calcular_memoria_tupla(tupla)

    # Imprimimos el tamaño en memoria de la lista y la tupla
    print("Tamaño en memoria de la lista:", tamaño_lista)
    print("Tamaño en memoria de la tupla:", tamaño_tupla)

    # Calculamos el tiempo de acceso a la lista con el método `join()` y como un vector
    tiempo_acceso_lista_con_metodo = calcular_tiempo_acceso_lista_con_metodo(lista)
    tiempo_acceso_lista_como_vector = calcular_tiempo_acceso_lista_como_vector(lista)

    # Imprimimos el tiempo de acceso a la lista con el método `join()` y como un vector
    print("Tiempo de acceso a la lista con el método `join()`:", tiempo_acceso_lista_con_metodo)
    print("Tiempo de acceso a la lista como un vector:", tiempo_acceso_lista_como_vector)

if __name__ == "__main__":
    main()
