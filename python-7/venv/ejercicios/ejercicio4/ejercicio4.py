from fileinput import close
from typing import TextIO

cosa = int(input('Enter number:'))
fichero = open(input('Introduce el nombre del fichero: '), 'r')
mi_lista = [1,2,3,4,5,6,7,8,9,10]
try:
    r = 34 / cosa
    patata = mi_lista[9]
    print(fichero.read())
except ZeroDivisionError:
    print('No se puede dividir por 0')
except FileNotFoundError:
    print('El fichero no existe')
except TypeError:
    print('No se puede dividir por una cadena')
except IndexError:
    print('El indice no existe')
except Exception as e:
    print('Ha ocurrido un error no previsto', type(e).__name__)
else:
    print('Todo ha funcionado correctamente')
finally:
    fichero.close()
