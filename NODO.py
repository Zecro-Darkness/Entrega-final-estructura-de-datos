"""Se define la clase nodo para crear linked list con cola, queues y pilas, se definendos tributos, el valor del nodo
y el nodo siguiente que es nulo, también se definenalgunos metodos básicos como get_value y set_value, para obtener el
valor o cambiarlo respectivamente también se define el str y el int que convierte los valores del nodo en carateres o
números dependiendo del tipo de dato que se tenga"""


class Node:
    def __init__(self, value):
        self.Value = value
        self.Next = None

    def get_value(self):
        return self.Value

    def set_value(self, val):
        self.Value = val

    def __str__(self):
        return str(self.Value)

    def __int__(self):
        return int(self.Value)
