import NODO as node

# https://www.youtube.com/watch?v=oXuKUkIlv_o&list=PL78a5SLLX6yrMOVc5xdjV-4N4Dgt3ms1k&index=16


class LinkedList:
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
