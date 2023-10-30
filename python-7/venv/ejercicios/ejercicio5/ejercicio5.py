def multiplicar_matrices(a, b):
    if len(a[0]) != len(b):
        raise ValueError("Las matrices deben tener el mismo número de columnas")
    c = [[0 for i in range(len(b[0]))] for j in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(a[0])):
                c[i][j] += a[i][k] * b[k][j]
    return c

def ingresar_matriz(filas, columnas, nombre):
    matriz = []
    for i in range(filas):
        fila = [int(x) for x in input(f"Ingrese los elementos de la fila {i + 1} de la matriz {nombre}: ").split()]
        if len(fila) != columnas:
            raise ValueError(f"La fila {i + 1} de la matriz {nombre} no tiene el número correcto de elementos.")
        matriz.append(fila)
    return matriz

def main():
    try:
        num_filas_a = int(input("Introduce el número de filas de la primera matriz: "))
        num_columnas_a = int(input("Introduce el número de columnas de la primera matriz: "))
        num_filas_b = int(input("Introduce el número de filas de la segunda matriz: "))
        num_columnas_b = int(input("Introduce el número de columnas de la segunda matriz: "))

        if num_columnas_a != num_filas_b:
            raise ValueError("El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz.")

        a = ingresar_matriz(num_filas_a, num_columnas_a, "A")
        b = ingresar_matriz(num_filas_b, num_columnas_b, "B")

        c = multiplicar_matrices(a, b)

        print("El resultado de la multiplicación es:")
        for fila in c:
            print(fila)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Se ha producido un error inesperado: {e}")

if __name__ == "__main__":
    main()
