"""
Programa: tareasfunc.py
Autor: Jesús Díaz Rivas
Fecha:10/10/2020

Propósito:Diseñar un algoritmo que nos pregunte las tareas que queremos hacer hoy, las almacene en un fichero
y podamos acceder a ellas aún después de la ejecución del programa.

Análisis: Tenemos que pedir qué tareas hará el usuario y guardarlas en un fichero

Variables:
...

Algoritmo:
#1. Uso de múltiples funciones.
#2. Importación del módulo pickle que permite almacenar la lista en un fichero de forma permanente.

"""

import pickle
import os


def crearsavedata(savedata):
    os.makedirs(savedata)


def crearpathlist(savedata):
    pathlist = []
    for i in range(4):
        test = "Tarea" + str(i + 1) + ".txt"  # Para crear los 4 archivos del tirón
        savedatafile = os.path.join(savedata, test)  # ruta, ...\test1.txt ... 2.txt ...
        pathlist.append(savedatafile)  # agrega a la lista de directorios cada directorio de cada archivo

    return pathlist


def creararchivo(pathlist):
    with open(pathlist, 'wb') as f:  # Crea cada archivo
        listavacia = []  # Creo una lista vacía para el archivo vacío
        pickle.dump(listavacia, f)  # Guardo dicha lista en el archivo vacío
        return listavacia

        # Ahora tengo 4 archivos con 4 listas vacías listos para ser utilizados
        # Si se borrase uno de los 4 archivos, el programa crearía uno y le asignaría una lista vacía.


def cargarlista(tipodelista):
    lista = pickle.load(open(tipodelista, 'rb'))
    return lista


def actualizarlista(lista, tipodelista):
    pickle.dump(lista, open(tipodelista, 'wb'))
    return lista


def recorrerlista(lista, tipodelista):
    for i in range(len(lista)):
        if i % 25 == 20:
            pausa()
        print("\t", i + 1, "-", lista[i])
    return tipodelista


def mostrartareas(lista, tipodelista):
    lista = actualizarlista(lista, tipodelista)

    if len(lista) == 0:
        print("\n \t No hay elementos en la lista")
    else:
        recorrerlista(lista, tipodelista)


def mostrarmenostareas(lista, tipodelista):
    for i in range(len(lista) - 20, len(lista)):
        print("\t", i + 1, "-", lista[i])
    return tipodelista


def pausa():
    print("         Pulse INTRO para continuar")
    input()
    os.system('cls')
    print("")  # no hay forma directa de borrar la pantalla con Python estandar


def outindex():
    print("\n\nHas indicado una tarea que no está en la lista\n\n")


def listadetareas(lista, tipodelista):
    # Muestra la lista
    os.system('cls')
    print("\n" * 2, "\t LISTA DE TAREAS \n\n")
    mostrartareas(lista, tipodelista)
    print("")
    pausa()


def añadirtarea(lista, tipodelista):
    while True:

        os.system('cls')
        print("\n \n \t Añade una tarea ")
        print("\t (-1 para cancelar)\n\n")
        print("\t Lista de tareas:\n")
        if len(lista) - 20 > 0:
            mostrarmenostareas(lista, tipodelista)
        else:
            mostrartareas(lista, tipodelista)

        tarea = (input("\n\n \t>>>"))

        if tarea == "-1":
            os.system('cls')
            break
        else:

            lista.append(tarea)
            actualizarlista(lista, tipodelista)
            print("")
            print("\n\nSe ha añadido:", tarea, "\n")


def borrartarea(lista, tipodelista):
    while True:

        try:
            os.system('cls')
            print("\n\n \t Que elemento quieres borrrar?")
            print("\t (-1 para volver al menú principal) ")
            print("\n")
            print("\t Lista de tareas:\n")
            if len(lista) - 20 > 0:
                mostrarmenostareas(lista, tipodelista)
            else:
                mostrartareas(lista, tipodelista)

            indicarelemento = int(input("\n\n \t >>>"))

            if indicarelemento == -1:
                os.system('cls')
                break

            if indicarelemento > len(lista) or indicarelemento <= 0:

                outindex()
                pausa()
            else:
                del lista[indicarelemento - 1]
                actualizarlista(lista, tipodelista)

        except:
            print("\n\nDebes introducir un número válido\n\n")
            pausa()


def modificartarea(lista, tipodelista):
    while True:

        try:
            os.system('cls')
            print("\n\n \t Que elemento quieres borrrar?")
            print("\t (-1 para volver al menú principal) ")
            print("\n")
            print("\t Lista de tareas:\n")
            if len(lista) - 20 > 0:
                mostrarmenostareas(lista, tipodelista)
            else:
                mostrartareas(lista, tipodelista)

            modificar = int(input("\n\n \t Que tarea quieres modificar?(-1 para volver al menú principal)\n \t >>>"))


            if modificar == -1:
                os.system('cls')
                break

            if modificar > len(lista) or modificar <= 0:
                outindex()
                pausa()

            else:
                print("\n\n \t Has decido modificar a:", lista[modificar - 1])
                modificado = input("\t Introduce su nuevo valor(-1 para cancelar)\n \n \t >>>")
                if modificado == "-1":
                    pass
                else:
                    lista[modificar - 1] = modificado
                    actualizarlista(lista, tipodelista)

        except:
            print("\n\nDebes introducir un número válido\n\n")
            pausa()

def borrartareas(lista, tipodelista):
    while True:

        try:
            os.system('cls')
            print("\n \t ¿Está seguro de que desea eliminar todas las tareas de la lista?(s/n)\n ")
            mostrartareas(lista, tipodelista)

            confirmacion = input("\n \t>>>")
            if confirmacion == "s":
                os.system('cls')
                lista.clear()
                actualizarlista(lista, tipodelista)
                mostrartareas(lista, tipodelista)

                print("\n \t Se han eliminado todas las tareas satisfactoriamente.")
                print("\n")
                pausa()
                break

            if confirmacion == "n":
                os.system('cls')
                break
            else:
                print("")
        except:
            print("\n\nDebes introducir un s/n\n\n")
            pausa()


def movertareas(lista, tipodelista):
    while True:
        try:
            os.system('cls')
            print("\n\n \t Que elemento quieres mover?")
            print("\t (-1 para volver al menú principal) ")
            print("\n")
            print("\t Lista de tareas:\n")
            if len(lista) - 20 > 0:
                mostrarmenostareas(lista, tipodelista)
            else:
                mostrartareas(lista, tipodelista)

            moverdesde = int(input("\n \t >>>"))

            if moverdesde == -1:
                os.system('cls')
                break

            elif moverdesde > len(lista) or moverdesde <= 0:
                outindex()
                pausa()
            else:
                moverhasta = int(input("\n \t Donde lo quieres mover? (Intercambiar)(-1 para cancelar) \n \t >>>"))
                if moverhasta == -1:
                    pass
                elif moverhasta > len(lista) or moverhasta <= 0:
                    outindex()
                    pausa()
                else:
                    lista[moverdesde - 1], lista[moverhasta - 1] = lista[moverhasta - 1], lista[moverdesde - 1]
                    actualizarlista(lista, tipodelista)
                    os.system('cls')


        except:
            print("\n\nDebes introducir un número válido\n\n")
            pausa()


def mostraropciones(eleccionmain):
    if eleccionmain == 1:
        print("\n\n \t 1. COSAS QUE HAY QUE HAY QUE HACER PARA MAÑANA \n\n")
    if eleccionmain == 2:
        print("\n\n \t 2. COSAS PENDIENTES \n\n")
    if eleccionmain == 3:
        print("\n\n \t 3. EXAMENES PENDIENTES \n\n")
    if eleccionmain == 4:
        print("\n\n \t 4. EXAMENES HECHOS \n\n")

    print("\t Opciones disponibles: \n")
    print("")

    print("\t 1. Lista de tareas")
    print("\t 2. Añadir tarea")
    print("\t 3. Borrar tarea")
    print("\t 4. Modificar tarea")
    print("\t 5. Borrar todas las tareas")
    print("\t 6. Mover tareas")
    print("")

    print("\t 0. VOLVER AL INICIO")


def opcionesgenerales(lista, tipodelista, eleccionmain):
    while True:
        mostraropciones(eleccionmain)
        try:
            eleccion = int(input("\n\n \t>>>"))
            print("\n" * 2)
            if eleccion == 1:
                listadetareas(lista, tipodelista)
            elif eleccion == 2:
                añadirtarea(lista, tipodelista)
            elif eleccion == 3:
                borrartarea(lista, tipodelista)
            elif eleccion == 4:
                modificartarea(lista, tipodelista)
            elif eleccion == 5:
                borrartareas(lista, tipodelista)
            elif eleccion == 6:
                movertareas(lista, tipodelista)
            elif eleccion < 0:
                os.system('cls')
                print("\n \n Debes introducir un número válido \n \n")
            elif eleccion > 6:
                os.system('cls')
                print("\n \n Debes introducir un número válido \n \n")
            elif eleccion != 0:
                print("\n\n")
            if eleccion == 0:
                os.system('cls')
                break
                # actualizarlista(lista, tipodelista) ->
                # Esto haría el programa mucho más optimizado, pero menos seguro a la hora de guardar los cambios.

        except:
            os.system('cls')
            print("\n \n Debes introducir un número válido \n \n")


def menuprincipal():
    print("\n\n \t MENÚ PRINCIPAL\n\n")
    print("\t Opciones disponibles: \n")
    print("")

    print("\t 1. COSAS QUE HAY QUE HAY QUE HACER PARA MAÑANA ")
    print("\t 2. COSAS PENDIENTES")
    print("\t 3. EXAMENES PENDIENTES")
    print("\t 4. EXAMENES HECHOS")

    print("")

    print("\t 0. SALIR \n")

    eleccion = int(input("\t >>>"))
    os.system('cls')
    return eleccion
