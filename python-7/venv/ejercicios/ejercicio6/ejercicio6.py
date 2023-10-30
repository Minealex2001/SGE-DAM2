def crear_tablero():
    return [[' ' for i in range(3)] for j in range(3)]

def mostrar_tablero(tablero):
    for fila in tablero:
        print(fila)


def hay_tres_en_raya(tablero, turno):
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] == turno:
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] == turno:
            return True
        if tablero[i][0] == tablero[1][1] == tablero[2][2] == turno:
            return True
        if tablero[2][0] == tablero[1][1] == tablero[0][2] == turno:
            return True
    return False

def poner_ficha(tablero, turno, fila, columna):
    if tablero[fila][columna] != ' ':
        raise ValueError("La casilla ya está ocupada")

    elif tablero[fila][columna] != ' ':
        # El jugador ha hecho trampa
        print("El jugador {} ha hecho trampa. Gana el jugador {}.".format(turno, "O" if turno == "X" else "X"))

    else:
        tablero[fila][columna] = turno

def jugar():
    turno = 'X'
    tablero = crear_tablero()

    while True:
        mostrar_tablero(tablero)

        # Solicitar la posición de la ficha
        fila, columna = input("Jugador {}: introduce la fila y la columna (1-3): ".format(turno)).split()
        fila = int(fila) - 1
        columna = int(columna) - 1

        # Poner la ficha en el tablero
        try:
            poner_ficha(tablero, turno, fila, columna)
        except ValueError:
            print("La posición no es válida")
            continue

        # Comprobar si hay tres en raya
        if hay_tres_en_raya(tablero, turno):
            print("¡Ganador el jugador {}!".format(turno))
            return

        # Cambiar de turno
        turno = 'O' if turno == 'X' else 'X'

        # Comprobar si hay empate
        if all(tablero[i][j] != ' ' for i in range(3) for j in range(3)):
            print("¡Empate!")
            return


jugar()
