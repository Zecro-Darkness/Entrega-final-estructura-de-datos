import hashlib
from hmac import digest
from msilib.schema import Class, Error
import sqlite3
import sys
import LINKED_LIST as Linkedlist
import ESTUDIANTE as estudiante_c
import Lista_Hash as listaHash




# Crea la conexíon a la base de datos en caso de fallar imprimirá 'error'

def conexion_a_la_db():
    try:
        con = sqlite3.connect('BD_TuAmigoUN.db')
        return con
    except Error:
        print(Error)


def cerrar_bd(con):
    con.close()

def busqueda_ind(con, id_u):
    cursor_obj = con.cursor()
    ident = id_u
    cons = 'SELECT Nombres, Apellidos, Edad, E_mail, Ciudad FROM Usuarios WHERE Identificador == "' + ident + '"'
    cursor_obj.execute(cons)
    datos = cursor_obj.fetchall()
    info = ""

    for i in range(0, 5):
        if i == 0:
            info += '['
            info += str(datos[0][i])
            info += ','
        elif i == 4:
            info += str(datos[0][i])
            info += ']'
        else:
            info += str(datos[0][i])
            info += ','
    print(info)


'reajuste de la cantidad de veces que se puede usar la recursividad'
sys.setrecursionlimit(10**6)


def Hash_():
    TablaHash = []

    for i in range (2147483647):
        TablaHash.append(list_Hash())


    # crear un elemento para ejecutar la funcion hash
    h = list_Hash()

    for i in range (2147483647):
        TablaHash[i].recorrer()


