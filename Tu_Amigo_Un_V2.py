import sqlite3
from sqlite3 import Error
import GAMER as gamer_c
import ESTUDIANTE as estudiante_c
import SERIES as estudiante_s
import Avl_Tree as AVL
import time

# Crea la conexíon a la base de datos en caso de fallar imprimirá 'error'


def conexion_a_la_db():
    try:
        con = sqlite3.connect('BD_TuAmigoUN.db')
        return con
    except Error:
        print(Error)


def cerrar_bd(con):
    con.close()


# metodo para ingresar los datos del usuario en la tabla de usuarios principal, usa sentecias sql
# hay que tener en cuenta que depues del insert into se debe colocar el nombre de la tabla de destino,
# y los interrogantes es la cantidad de valores que pide la tabla y la ultima variable es una tupla de string y enteros
# con los datos a ingresar en la tabla esta última es muy importante


def ingresar_usuario(con, d_usuario):
    cursor_obj = con.cursor()
    cursor_obj.execute('''INSERT INTO Usuarios VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', d_usuario)
    con.commit()
    return True


def ingresar_gamer(con, d_gamer):
    cursor_obj = con.cursor()
    cursor_obj.execute('''INSERT INTO Gamers VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', d_gamer)
    con.commit()
    return True


def ingresar_series(con, d_series):
    cursor_obj = con.cursor()
    cursor_obj.execute('''INSERT INTO Series VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', d_series)
    con.commit()
    return True


def consulta_general(con):
    tree = AVL.AVL()

    cursor_obj = con.cursor()

    consulta = "SELECT * FROM Usuarios"

    cursor_obj.execute(consulta)

    filas = cursor_obj.fetchall()

    for row in filas:
        tree.insert(row[0])

    return tree


def consulta_gamers(con):
    tree = AVL.AVL()

    cursor_obj = con.cursor()

    consulta = "SELECT * FROM Usuarios WHERE Juegos == 1"

    cursor_obj.execute(consulta)

    filas = cursor_obj.fetchall()

    for row in filas:
        tree.insert(row[0])


    return tree


def cons_g_acc(con):
    tree = AVL.AVL()

    cursor_obj = con.cursor()

    consulta = "SELECT Identificador FROM Gamers WHERE Accion == 1"

    cursor_obj.execute(consulta)

    filas = cursor_obj.fetchall()

    for row in filas:
        tree.insert(row[0])

    return tree


def cons_g_avt(con):
    tree = AVL.AVL()

    cursor_obj = con.cursor()

    consulta = "SELECT Identificador FROM Gamers WHERE Aventura == 1"

    cursor_obj.execute(consulta)

    filas = cursor_obj.fetchall()

    for row in filas:
        tree.insert(row[0])

    return tree


def cons_g_arc(con):
    tree = AVL.AVL()

    cursor_obj = con.cursor()


    consulta = "SELECT Identificador FROM Gamers WHERE Arcade == 1"

    cursor_obj.execute(consulta)

    filas = cursor_obj.fetchall()

    for row in filas:
        tree.insert(row[0])

    return tree


def cons_g_dep(con):
    tree = AVL.AVL()

    cursor_obj = con.cursor()

    consulta = "SELECT Identificador FROM Gamers WHERE Deportivos == 1"

    cursor_obj.execute(consulta)

    filas = cursor_obj.fetchall()

    for row in filas:
        tree.insert(row[0])

    return tree


def cons_g_est(con):
    tree = AVL.AVL()

    cursor_obj = con.cursor()

    consulta = "SELECT Identificador FROM Gamers WHERE Estrategia == 1"

    cursor_obj.execute(consulta)

    filas = cursor_obj.fetchall()

    for row in filas:
        tree.insert(row[0])

    return tree


def cons_g_sim(con):
    tree = AVL.AVL()

    cursor_obj = con.cursor()

    consulta = "SELECT Identificador FROM Gamers WHERE Simulación == 1"

    cursor_obj.execute(consulta)

    filas = cursor_obj.fetchall()

    for row in filas:
        tree.insert(row[0])

    return tree


def cons_g_rpg(con):
    tree = AVL.AVL()

    cursor_obj = con.cursor()

    consulta = "SELECT Identificador FROM Gamers WHERE RPG == 1"

    cursor_obj.execute(consulta)

    filas = cursor_obj.fetchall()

    for row in filas:
        tree.insert(row[0])

    return tree


def consulta_series(con):
    tree = AVL.AVL()

    cursor_obj = con.cursor()

    consulta = "SELECT * FROM Usuarios WHERE Series == 1"

    cursor_obj.execute(consulta)

    filas = cursor_obj.fetchall()

    for row in filas:
        tree.insert(row[0])

    return tree


def cons_s_a_c(con):
    tree = AVL.AVL()

    cursor_obj = con.cursor()

    consulta = "SELECT Identificador FROM Series WHERE Animadas == 1 and Cartoons == 1"

    cursor_obj.execute(consulta)

    filas = cursor_obj.fetchall()

    for row in filas:
        tree.insert(row[0])

    return tree


def cons_s_a_a(con):
    tree = AVL.AVL()

    cursor_obj = con.cursor()

    consulta = "SELECT Identificador FROM Series WHERE Animadas == 1 and Anime == 1"

    cursor_obj.execute(consulta)

    filas = cursor_obj.fetchall()

    for row in filas:
        tree.insert(row[0])

    return tree


def cons_s_a(con):
    tree = AVL.AVL()

    cursor_obj = con.cursor()

    consulta = "SELECT Identificador FROM Series WHERE Animadas == 1 "

    cursor_obj.execute(consulta)

    filas = cursor_obj.fetchall()

    for row in filas:
        tree.insert(row[0])

    return tree


def cons_s_d(con):
    tree = AVL.AVL()

    cursor_obj = con.cursor()

    consulta = "SELECT Identificador FROM Series WHERE Doramas == 1"

    cursor_obj.execute(consulta)

    filas = cursor_obj.fetchall()

    for row in filas:
        tree.insert(row[0])

    return tree

def cons_s_doc(con):
    tree = AVL.AVL()

    cursor_obj = con.cursor()

    consulta = "SELECT Identificador FROM Series WHERE Documentales == 1"

    cursor_obj.execute(consulta)

    filas = cursor_obj.fetchall()

    for row in filas:
        tree.insert(row[0])

    return tree


def cons_s_n(con):
    tree = AVL.AVL()

    cursor_obj = con.cursor()

    consulta = "SELECT Identificador FROM Series WHERE USA_Norm == 1"

    cursor_obj.execute(consulta)

    filas = cursor_obj.fetchall()

    for row in filas:
        tree.insert(row[0])

    return tree


def cons_s_nov(con):
    tree = AVL.AVL()

    cursor_obj = con.cursor()

    consulta = "SELECT Identificador FROM Series WHERE Novelas == 1"

    cursor_obj.execute(consulta)

    filas = cursor_obj.fetchall()

    for row in filas:
        tree.insert(row[0])

    return tree


def menu(con):
    salir = False
    while not salir:
        estudiante = estudiante_c.Estudiante()
        opc = int(input('''Bienvenido a Tu Amigo UN

                     Seleciona el número de la opción que deseas elegir.

                     1) Dejar mi huella.

                     2) Buscar amigos

                     3) Salir

                     >>> '''))
        if opc == 1:
            estudiante.set_id()
            estudiante.set_f_name()
            estudiante.set_l_name()
            estudiante.set_edad()
            estudiante.set_e_mail()
            estudiante.set_city()
            estudiante.set_gamer()

            # comprobación de suscripción a gamers en caso de si se piden datos de preferencias

            if estudiante.get_gamer() == 1:
                gamer = gamer_c.Gamer()
                id_gm = estudiante.get_id()
                gamer.set_id_gamer(id_gm)
                gamer.set_accion()
                gamer.set_aventura()
                gamer.set_arcade()
                gamer.set_deportes()
                gamer.set_estrategia()
                gamer.set_simulacion()
                gamer.set_rpg()
                datos_g = gamer.datos_gamer()
                ingresar_gamer(con, datos_g)
            estudiante.set_series()

            # comprobación de suscripción a series en caso de si se piden datos de preferencias

            if estudiante.get_series() == 1:
                series = estudiante_s.Series()
                id_ser = estudiante.get_id()
                series.set_id_series(id_ser)
                series.set_animadas()
                series.set_cartoons()
                series.set_animes()
                series.set_doramas()
                series.set_documentales()
                series.set_series_normales()
                series.set_novelas()
                datos_s = series.datos_series()
                ingresar_series(con, datos_s)

            datos_e = estudiante.datos()
            ingresar_usuario(con, datos_e)
            print('Ingreso satisfactorio')

        elif opc == 2:
            while not salir:
                seleccion = int(input("""Encuentra tu parche (seleciona el número de la opción que quieres elegir):
                                        1) Todos

                                        2) Gamers

                                        3) Serie-aficionados

                                        4) Regresar

                                        >>>"""))
                if seleccion == 1:
                    datos = consulta_general(con)
                    orden = int(input('Quieres verlos en orden Ascedente o descendente?(1 para ascendente - 2 para descendente): '))
                    if orden == 1:
                        datos.pre_show(datos.get_root())
                    elif orden == 2:
                        datos.preorder(datos.get_root())
                elif seleccion == 2:
                    while not salir:
                        gamer_opc = int(input("""¿Que clase de team quieres?(seleciona el número de la opción que quieres elegir):

                                                             1) Todos: Encuentra tu team o duo entre toda la comunidad Gamer de la U

                                                             2) Acción: Encuentra tu team o duo entre los amantes de los juegos de acción disparos y combate

                                                             3) Aventureros: Encuentra tu team o duo entre los amantes de ka avebtura y la exploración

                                                             4) Arcadieros: Encuentra tu team o duo entre los amantes de juegos freneticos y puzles

                                                             5) Deportes: Encuentra tu team o duo entre los amantes de los juegos deportivos

                                                             6) Estrategas:Encuentra tu team o duo entre los amantes de los juegos de estrategia y corrdinación

                                                             7) Simuladores: Encuentra tu team o duo entre los amantes de los simuladores y juegos VR

                                                             8) RPG´s: Encuentra tu team o duo entre los amantes de juegos de rol e historisa fantasticas

                                                             9) Regresar

                                                             >>>"""))
                        if gamer_opc == 1:
                            datos = consulta_gamers(con)
                            orden = int(input('Quieres verlos en orden Ascedente o descendente?(1 para ascendente - 2 para descendente): '))
                            if orden == 1:
                                datos.pre_show(datos.get_root())
                            elif orden == 2:
                                datos.preorder(datos.get_root())

                        elif gamer_opc == 2:
                            datos = cons_g_acc(con)
                            orden = int(input('Quieres verlos en orden Ascedente o descendente?(1 para ascendente - 2 para descendente): '))
                            if orden == 1:
                                datos.pre_show(datos.get_root())
                            elif orden == 2:
                                datos.preorder(datos.get_root())

                        elif gamer_opc == 3:
                            datos = cons_g_avt(con)
                            orden = int(input('Quieres verlos en orden Ascedente o descendente?(1 para ascendente - 2 para descendente): '))
                            if orden == 1:
                                datos.pre_show(datos.get_root())
                            elif orden == 2:
                                datos.preorder(datos.get_root())

                        elif gamer_opc == 4:
                            datos = cons_g_arc(con)
                            orden = int(input('Quieres verlos en orden Ascedente o descendente?(1 para ascendente - 2 para descendente): '))
                            if orden == 1:
                                datos.pre_show(datos.get_root())
                            elif orden == 2:
                                datos.preorder(datos.get_root())

                        elif gamer_opc == 5:
                            datos = cons_g_dep(con)
                            orden = int(input('Quieres verlos en orden Ascedente o descendente?(1 para ascendente - 2 para descendente): '))
                            if orden == 1:
                                datos.pre_show(datos.get_root())
                            elif orden == 2:
                                datos.preorder(datos.get_root())

                        elif gamer_opc == 6:
                            datos = cons_g_est(con)
                            orden = int(input('Quieres verlos en orden Ascedente o descendente?(1 para ascendente - 2 para descendente): '))
                            if orden == 1:
                                datos.pre_show(datos.get_root())
                            elif orden == 2:
                                datos.preorder(datos.get_root())

                        elif gamer_opc == 7:
                            datos = cons_g_sim(con)
                            orden = int(input('Quieres verlos en orden Ascedente o descendente?(1 para ascendente - 2 para descendente): '))
                            if orden == 1:
                                datos.pre_show(datos.get_root())
                            elif orden == 2:
                                datos.preorder(datos.get_root())

                        elif gamer_opc == 8:
                            datos = cons_g_rpg(con)
                            orden = int(input('Quieres verlos en orden Ascedente o descendente?(1 para ascendente - 2 para descendente): '))
                            if orden == 1:
                                datos.pre_show(datos.get_root())
                            elif orden == 2:
                                datos.preorder(datos.get_root())

                        elif gamer_opc == 9:
                            break
                elif seleccion == 3:
                    while not salir:
                        series_s = int(input("""¿Con quien quieres ver series?: 

                                                1) Todos: Encuentra amigos con diferentes tipos de gustos

                                                2) Animadas: Encuentra aficionados por todo tipo de series animadas

                                                3) Doramas: Encuentra aficionados a los dramas Koreanos

                                                4) Documentales: Encuentra aficionados a los documentales y las series del mundo real

                                                5) Series: Encuentra aficionados de series clasicas americanas y latinas

                                                6) Novelas: Encuentra aficionados a las novelas e historias romanticas

                                                7) Regresar

                                                >>>"""))
                        if series_s == 1:
                            datos = consulta_series(con)
                            orden = int(input('Quieres verlos en orden Ascedente o descendente?(1 para ascendente - 2 para descendente): '))
                            if orden == 1:
                                datos.pre_show(datos.get_root())
                            elif orden == 2:
                                datos.preorder(datos.get_root())

                        elif series_s == 2:
                            while not salir:
                                series_a = int(input("""¿Que series animadas prefieres?
                                                        1) Cartoon

                                                        2)Anime

                                                        3)Todas

                                                        4)Regresar

                                                        >>>"""))
                                if series_a == 1:
                                    datos = cons_s_a_c(con)
                                    orden = int(input('Quieres verlos en orden Ascedente o descendente?(1 para ascendente - 2 para descendente): '))
                                    if orden == 1:
                                        datos.pre_show(datos.get_root())
                                    elif orden == 2:
                                        datos.preorder(datos.get_root())
                                elif series_a == 2:
                                    datos = cons_s_a_a(con)
                                    orden = int(input('Quieres verlos en orden Ascedente o descendente?(1 para ascendente - 2 para descendente): '))
                                    if orden == 1:
                                        datos.pre_show(datos.get_root())
                                    elif orden == 2:
                                        datos.preorder(datos.get_root())
                                elif series_a == 3:
                                    datos = cons_s_a(con)
                                    orden = int(input('Quieres verlos en orden Ascedente o descendente?(1 para ascendente - 2 para descendente): '))
                                    if orden == 1:
                                        datos.pre_show(datos.get_root())
                                    elif orden == 2:
                                        datos.preorder(datos.get_root())
                                elif series_a == 4:
                                    break
                        elif series_s == 3:
                            datos = cons_s_d(con)
                            orden = int(input('Quieres verlos en orden Ascedente o descendente?(1 para ascendente - 2 para descendente): '))
                            if orden == 1:
                                datos.pre_show(datos.get_root())
                            elif orden == 2:
                                datos.preorder(datos.get_root())
                        elif series_s == 4:
                            datos = cons_s_doc(con)
                            orden = int(input('Quieres verlos en orden Ascedente o descendente?(1 para ascendente - 2 para descendente): '))
                            if orden == 1:
                                datos.pre_show(datos.get_root())
                            elif orden == 2:
                                datos.preorder(datos.get_root())
                        elif series_s == 5:
                            datos = cons_s_n(con)
                            orden = int(input('Quieres verlos en orden Ascedente o descendente?(1 para ascendente - 2 para descendente): '))
                            if orden == 1:
                                datos.pre_show(datos.get_root())
                            elif orden == 2:
                                datos.preorder(datos.get_root())
                        elif series_s == 6:
                            datos = cons_s_nov(con)
                            orden = int(input('Quieres verlos en orden Ascedente o descendente?(1 para ascendente - 2 para descendente): '))
                            if orden == 1:
                                datos.pre_show(datos.get_root())
                            elif orden == 2:
                                datos.preorder(datos.get_root())
                        elif series_s == 7:
                            break

                elif seleccion == 4:
                    break
        elif opc == 3:

            break


def main():
    con = conexion_a_la_db()
    menu(con)
    cerrar_bd(con)


main()
