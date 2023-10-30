try:
    r = 34/0
    x = 5 + "hola"
except ZeroDivisionError:
    print("No se puede dividir por cero")
except TypeError:
    print("No se puede sumar un entero con un string")