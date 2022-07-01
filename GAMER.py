
class Gamer:

    pass

    def __init__(self):
        self.Gamer_id = None
        self.Accion = None
        self.Aventura = None
        self.Arcade = None
        self.Deportivo = None
        self.Estrategia = None
        self.Simulacion = None
        self.RPG = None

# definición de geters para la clase gamers
    def get_gamer_id(self):
        return self.Gamer_id

    def get_accion(self):
        return self.Accion

    def get_aventura(self):
        return self.Aventura

    def get_arcade(self):
        return self.Arcade

    def get_deportes(self):
        return self.Deportivo

    def get_estrategia(self):
        return self.Estrategia

    def get_simulacion(self):
        return self.Simulacion

    def get_rpg(self):
        return self.RPG

# definición de seters para la clase gamer

    def set_id_gamer(self, id_g):
        self.Gamer_id = id_g

    def set_accion(self):
        self.Accion = int(input('Si te gustanlos juegos de accíon, shooters y peleas freneticas pon uno(1) de lo contrario cero(0): '))

    def set_aventura(self):
        self.Aventura = int(input('Si te gustanlos juegos de aventura, exploración y mundos abiertos pon uno(1) de lo contrario cero(0): '))

    def set_arcade(self):
        self.Arcade = int(input('Si te gustanlos juegos de plataformas con mecanicas complejas y acertijos pon uno(1) de lo contrario cero(0): '))

    def set_deportes(self):
        self.Deportivo = int(input('Si te gustanlos juegos de deportes pon uno(1) de lo contrario cero(0): '))

    def set_estrategia(self):
        self.Estrategia = int(input('Si te gustanlos juegos de estrategía y planeación pon uno(1) de lo contrario cero(0): '))

    def set_simulacion(self):
        self.Simulacion = int(input('Si te gustanlos juegos de simulacíon y VR pon uno(1) de lo contrario cero(0): '))

    def set_rpg(self):
        self.RPG = int(input('Si te gustanlos juegos de rol y mundos fantasticos pon uno(1) de lo contrario cero(0): '))

    def datos_gamer(self):
        datos_g = (self.Gamer_id, self.Accion, self.Aventura, self.Arcade, self.Deportivo, self.Estrategia, self.Simulacion, self.RPG, )
        return datos_g



