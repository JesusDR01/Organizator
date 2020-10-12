"""
Programa: on.py
Autor: Jesús Díaz Rivas
Fecha:10/10/2020

Propósito:Diseñar un algoritmo que nos pregunte las tareas que queremos hacer hoy, las almacene en un fichero
y podamos acceder a ellas aún después de la ejecución del programa.

Análisis: Tenemos que pedir qué tareas hará el usuario y guardarlas en un fichero

Variables:
eleccion (int)
tipodelista (str)
lista (list)

Algoritmo:
#1.Menú
#2.Dependiendo de la opción que seleccione utilizaré un fichero u otro.
#3.Utilizaré un módulo llamado tareasfunc que realizará todo el proceso interno.

"""

import tareasfunc
import os
import sys


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


if __name__ == '__main__':
    os.system('cls')

    userpath = os.getcwd()
    savedata = os.path.join(userpath, 'savedata')

    if not os.path.exists(savedata):
        tareasfunc.crearsavedata(savedata)  # Si no hay carpeta donde contener los datos, creala

    pathlist = tareasfunc.crearpathlist(savedata)  # Tengo la ruta donde debe estar cada archivo

    for i in range(4):
        if not os.path.exists(pathlist[i]):  # Si no existe el archivo
            tareasfunc.creararchivo(pathlist[i])  # Crea el archivo y le asigna una lista vacía

    while True:

        try:
            eleccion = tareasfunc.menuprincipal()
            if eleccion == 1:
                tipodelista = pathlist[0]
                lista = tareasfunc.cargarlista(tipodelista)
                tareasfunc.opcionesgenerales(lista, tipodelista, eleccion)
            elif eleccion == 2:
                tipodelista = pathlist[1]
                lista = tareasfunc.cargarlista(tipodelista)
                tareasfunc.opcionesgenerales(lista, tipodelista, eleccion)
            elif eleccion == 3:
                tipodelista = pathlist[2]
                lista = tareasfunc.cargarlista(tipodelista)
                tareasfunc.opcionesgenerales(lista, tipodelista, eleccion)
            elif eleccion == 4:
                tipodelista = pathlist[3]
                lista = tareasfunc.cargarlista(tipodelista)
                tareasfunc.opcionesgenerales(lista, tipodelista, eleccion)
            elif eleccion < 0 or eleccion > 4:
                os.system('cls')
                print("\n \n Debes introducir un número válido \n \n")
            elif eleccion == 0:
                break
        except:
            os.system('cls')
            print("\n \n Debes introducir un número válido \n \n")

    # Descomenta si quieres reiniciar la lista
    # lista=[]
    # pickle.dump(lista, open('mifichero.txt', 'wb'))
