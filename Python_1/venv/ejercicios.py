def ejercicio_1():
    nombre = input("Cual es tu nombre: ")
    print("Hola, " + nombre)


def ejercicio_2():
    n = int(input("Que numero quieres: "))
    if (n > 0):
        for x in range(n):
            suma = n * (n + 1) / 2

    print(suma)


def ejercicio_3():
    dinero = int(input("Cuanto dinero tienes"))

    dinero1 = dinero * 1.04
    dinero2 = dinero1 * 1.04
    dinero3 = dinero2 * 1.04

    print("El primer año tendras: " + dinero1)
    print("El segundo año tendras: " + dinero2)
    print("El tercer año tendras: " + dinero3)


def ejercicio_4bucle():
    nombre = input("Introduce tu nombre: ")
    numero = int(input("Introduce un número: "))

    for i in range(numero):
        print(nombre)


def ejercicio_4nobucle():
    nombre = input("Introduce tu nombre: ")
    numero = int(input("Introduce un número: "))

    print(nombre * numero)


def ejercicio_5():
    nombre = input("Introduce tu nombre: ")
    nombre = nombre.upper()
    n_letras = len(nombre)
    print(f"{nombre} tiene {n_letras} letras")


def ejercicio_6():
    numero = input("Introduce el numero de telefono con el formato prefijo-numero-extension ")
    numero = numero[3:-3]
    print(numero)


def ejercicio_7():
    frase = input("Introduce una frase: ")
    vocal = input("Introduce una vocal: ")
    frase = frase.replace(vocal, vocal.upper())
    print(frase)


def ejercicio_8():
    precio = float(input("Introduce el precio del producto: "))
    euros = int(precio)
    centimos = precio - euros
    centimos = round(centimos, 2)
    centimos = centimos * 100
    print(f"El precio es {euros} euros y {centimos} centimos")


def ejercicio_9():
    password = "contraseña"
    password_usuario = input("Introduce la contraseña: ")
    password_usuario = password_usuario.lower()
    if password == password_usuario:
        print("El password es correcto")
    else:
        print("El password no coincide")


def ejercicio_10():
    edad = int(input("Introduce tu edad: "))
    ingresos = float(input("Introduce tus ingresos: "))
    if edad > 16 and ingresos >= 1000:
        print("Tienes que tributar")
    else:
        print("No tienes que tributar")


def ejercicio_11():
    renta_anual = float(input("Introduce tu renta anual: "))
    if renta_anual < 10000:
        print("Tipo impositivo del 5%")
    elif 10000 <= renta_anual < 20000:
        print("Tipo impositivo del 15%")
    elif 20000 <= renta_anual < 35000:
        print("Tipo impositivo del 20%")
    elif 35000 <= renta_anual < 60000:
        print("Tipo impositivo del 30%")
    elif renta_anual >= 60000:
        print("Tipo impositivo del 45%")

def ejercicio_12():
