"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
from App import controller
from DISClib.ADT import list as lt
assert cf

default_limit = 1000
sys.setrecursionlimit(default_limit*10)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________


playersfile = 'fifa-players-2022-utf8-small.csv'
cont = None


# ___________________________________________________
#  Menu principal
# ___________________________________________________

def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información de jugadores")
    print("3- Cargar avance Requerimiento 1")
    print("4-")
    print("0- Salir")
    print("*******************************************")


"""
Menu principal
"""

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("\nInicializando....")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.init()

    elif int(inputs[0]) == 3:
        print("\nCargando información de jugadores ....")
        controller.loadData(cont, playersfile)
        print('Jugadores cargados: ' + str(controller.crimesSize(cont)))
        print('Altura del arbol: ' + str(controller.indexHeight(cont)))
        print('Elementos en el arbol: ' + str(controller.indexSize(cont)))
        print('Menor Llave: ' + str(controller.minKey(cont)))
        print('Mayor Llave: ' + str(controller.maxKey(cont)))

    else:
        sys.exit(0)
sys.exit(0)
