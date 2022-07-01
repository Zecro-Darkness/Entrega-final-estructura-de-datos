import Avl_Node as Node
import sys
import sqlite3
from sqlite3 import Error
import time

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


class AVL:

    def __init__(self):
        self.root = None
        self.size = 0

        """
        Operación de inserción para agregar nuevos nodos
        al árbol.
        """
    def insert(self, value):
        node = Node.Node(value)

        if self.root is None:
            self.root = node
            self.root.height = 0
            self.size = 1
        else:
            dad_node = None
            curr_node = self.root

            while True:
                if curr_node is not None:

                    dad_node = curr_node

                    if node.label < curr_node.label:
                        curr_node = curr_node.left
                    else:
                        curr_node = curr_node.right
                else:
                    node.height = dad_node.height
                    dad_node.height += 1
                    if node.label < dad_node.label:
                        dad_node.left = node
                    else:
                        dad_node.right = node
                    self.rebalance(node)
                    self.size += 1
                    break

        # Operación de rotación
    def rebalance(self, node):
        n = node

        while n is not None:
            height_right = n.height
            height_left = n.height

            if n.right is not None:
                height_right = n.right.height

            if n.left is not None:
                height_left = n.left.height

            if abs(height_left - height_right) > 1:
                if height_left > height_right:
                    left_child = n.left
                    if left_child is not None:
                        h_right = (left_child.right.height
                                    if (left_child.right is not None) else 0)
                        h_left = (left_child.left.height
                                    if (left_child.left is not None) else 0)
                    if (h_left > h_right):
                        self.rotate_left(n)
                        break
                    else:
                        self.double_rotate_right(n)
                        break
                else:
                    right_child = n.right
                    if right_child is not None:
                        h_right = (right_child.right.height
                            if (right_child.right is not None) else 0)
                        h_left = (right_child.left.height
                            if (right_child.left is not None) else 0)
                    if (h_left > h_right):
                        self.double_rotate_left(n)
                        break
                    else:
                        self.rotate_right(n)
                        break
            n = n.parent

    def rotate_left(self, node):
        aux = node.parent.label
        node.parent.label = node.label
        node.parent.right = Node.Node(aux)
        node.parent.right.height = node.parent.height + 1
        node.parent.left = node.right

    def rotate_right(self, node):
        aux = node.parent.label
        node.parent.label = node.label
        node.parent.left = Node.Node(aux)
        node.parent.left.height = node.parent.height + 1
        node.parent.right = node.right

    def double_rotate_left(self, node):
        self.rotate_right(node.getRight().getRight())
        self.rotate_left(node)

    def double_rotate_right(self, node):
        self.rotate_left(node.getLeft().getLeft())
        self.rotate_right(node)

    def empty(self):
        if self.root is None:
            return True
        return False

    def pre_show(self, curr_node):
        con = conexion_a_la_db()
        if curr_node is not None:
            self.pre_show(curr_node.left)
            node_inf = str(curr_node.label)
            busqueda_ind(con, node_inf)

            self.pre_show(curr_node.right)

    def preorder(self, curr_node):
        con = conexion_a_la_db()
        if curr_node is not None:
            self.pre_show(curr_node.left)
            self.pre_show(curr_node.right)
            node_inf = str(curr_node.label)
            busqueda_ind(con, node_inf)


    def get_root(self):
        return self.root


