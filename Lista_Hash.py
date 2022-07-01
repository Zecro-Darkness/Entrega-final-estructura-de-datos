import hashlib
from hmac import digest
from msilib.schema import Class, Error
import sqlite3
import sys
import LINKED_LIST as Linkedlist
import ESTUDIANTE as estudiante_c
import NODO as node


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

class listaHash:


    def __init__(self):
            self.First = None
            self.Size = 0

    def append(self, value):
        nodo = node.Node(value)
        if self.Size == 0:
            self.First = nodo
        else:
            current = self.First
            while current.Next is not None:
                current = current.Next

            current.Next = nodo
        self.Size += 1

    def remove(self, value):
        if self.Size == 0:
            return False
        else:
            current = self.First
            try:
                while current.Next.Value != value:
                    current = current.Next
                deleted = current.Next
                current.Next = deleted.Next
            except AttributeError:
                return False
        self.Size -= 1
        return deleted

    def limpiar(self):
        self.First = None
        self.Size = 0
        return True

    def __len__(self):
        return self.Size

    def __str__(self):
        string = '['
        current = self.First
        for i in range(len(self)):
            string += str(current)
            if i != len(self) - 1:
                string += str(', ')
            current = current.Next
        string += ']'
        return string
    def funcionHash(self, ID):
        return ID % 2147483647 # primo de Mersenne para evitar las mayores colisiones posibles es 2^{31}-1

