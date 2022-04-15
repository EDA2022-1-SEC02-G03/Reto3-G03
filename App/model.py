"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import map as mp
import datetime
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------


def newAnalyzer():
    """ Inicializa el analizador

    Crea una lista vacia para guardar todos los crimenes
    Se crean indices (Maps) por los siguientes criterios:
    -Fechas

    Retorna el analizador inicializado.
    """
    analyzer = {'players': None,
                'DateIndex': None
                }

    analyzer['players'] = lt.newList('ARRAY_LIST')
    analyzer['DateIndex'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareDates)
    return analyzer



# Funciones para agregar informacion al catalogo

def addPlayer(analyzer, player):
    """
    """
    lt.addLast(analyzer['players'], player)
    updateDateIndex(analyzer['DateIndex'], player)
    return analyzer


def updateDateIndex(map, player):
    """
    Se toma la fecha del crimen y se busca si ya existe en el arbol
    dicha fecha.  Si es asi, se adiciona a su lista de crimenes
    y se actualiza el indice de tipos de crimenes.

    Si no se encuentra creado un nodo para esa fecha en el arbol
    se crea y se actualiza el indice de tipos de crimenes
    """
    playerrdate = player['club_joined']
    playerdate = datetime.datetime.strptime(playerrdate, '%Y-%m-%d')
    entry = om.get(map, playerdate.date())
    if entry is None:
        datentry = newDataEntry(player)
        om.put(map, playerdate.date(), datentry)
    else:
        datentry = me.getValue(entry)
    addDateIndex(datentry, player)
    return map


def addDateIndex(datentry, player):
    """
    Actualiza un indice de tipo de crimenes.  Este indice tiene una lista
    de crimenes y una tabla de hash cuya llave es el tipo de crimen y
    el valor es una lista con los crimenes de dicho tipo en la fecha que
    se está consultando (dada por el nodo del arbol)
    """
    lst = datentry['lstplayers']
    lt.addLast(lst, player)
    return datentry


def newDataEntry(player):
    """
    Crea una entrada en el indice por fechas, es decir en el arbol
    binario.
    """
    entry = {'lstplayers': None}
    entry['lstplayers'] = lt.newList('ARRAY_LIST')
    return entry


# Funciones para creacion de datos

# ==============================
# Funciones de consulta
# ==============================


def crimesSize(analyzer):
    """
    Número de crimenes
    """
    return lt.size(analyzer['players'])


def indexHeight(analyzer):
    """
    Altura del arbol
    """
    return om.height(analyzer['DateIndex'])


def indexSize(analyzer):
    """
    Numero de elementos en el indice
    """
    return om.size(analyzer['DateIndex'])


def minKey(analyzer):
    """
    Llave mas pequena
    """
    return om.minKey(analyzer['DateIndex'])


def maxKey(analyzer):
    """
    Llave mas grande
    """
    return om.maxKey(analyzer['DateIndex'])


# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento

# ==============================
# Funciones de Comparacion
# ==============================


def compareDates(date1, date2):
    """
    Compara dos fechas
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1

def compareplayers(player1, player2):
    """
    Compara dos jugadores
    """
    player = me.getKey(player2)
    if (player1 == player):
        return 0
    elif (player1 > player):
        return 1
    else:
        return -1