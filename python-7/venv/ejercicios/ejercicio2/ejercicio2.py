alumnos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
try:
    for alumno in alumnos:
        print("Alumno número: ", alumno)
except IndexError:
    print("Error de índice")

