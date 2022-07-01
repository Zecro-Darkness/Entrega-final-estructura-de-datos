class Series:

    pass

    def __init__(self):
        self.ID_ser = None
        self.Animes = None
        self.Cartoons = None
        self.Animadas = None
        self.Documentales = None
        self.Doramas = None
        self.Series_Normales = None
        self.Novelas = None

# definición de geters para la clase series

    def get_id_series(self):
        return self.ID_ser

    def get_animes(self):
        return self.Animes

    def get_cartoons(self):
        return self.Cartoons

    def get_animadas(self):
        return self.Animadas

    def get_documentales(self):
        return self.Documentales

    def get_doramas(self):
        return self.Doramas

    def get_series_normales(self):
        return self.Series_Normales

    def get_novelas(self):
        return self.Novelas

# definición de seters para la clase gamer

    def set_id_series(self, id_ser):
        self.ID_ser = id_ser

    def set_animes(self):
        self.Animes = input('Si te gustan los animes, pon uno(1) de lo contrario cero(0): ')

    def set_cartoons(self):
        self.Cartoons = int(input('Si te gustan los cartoons, pon uno(1) de lo contrario cero(0): '))

    def set_animadas(self):
        self.Animadas = input('Si te gustan las series animadas, pon uno(1) de lo contrario cero(0): ')

    def set_documentales(self):
        self.Documentales = int(input('Si te gustan los documentales, pon uno(1) de lo contrario cero(0): '))

    def set_doramas(self):
        self.Doramas = int(input('Si te gustan los doramas, pon uno(1) de lo contrario cero(0): '))

    def set_series_normales(self):
        self.Series_Normales = int(input('Si te gustan las series, pon uno(1) de lo contrario cero(0): '))

    def set_novelas(self):
        self.Novelas = int(input('Si te gustan las novelas, pon uno(1) de lo contrario cero(0): '))

    def datos_series(self):
        datos_s = (self.ID_ser, self.Animadas, self.Cartoons, self.Animes, self.Doramas, self.Documentales, self.Series_Normales, self.Novelas)
        return datos_s
        