try:
    raw_input = input("Introduce un número: ")
    x = int(raw_input)
    print(f"El resultado es", x*x)
except ValueError:
    print("No es un número")
