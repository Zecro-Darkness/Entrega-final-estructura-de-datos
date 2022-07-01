import NODO_Q as node


class Queue:

    def __init__(self):
        self.head = None
        self.last = None

    def enqueue(self, data):
        if self.last is None:
            self.head = node.Node(data)
            self.last = self.head
        else:
            self.last.next = node.Node(data)
            self.last.next.prev = self.last
            self.last = self.last.next

    def dequeue(self):

        if self.head is None:
            return None
        else:
            temp = self.head.data
            self.head = self.head.next
            self.head.prev = None
            return temp

    def first(self):

        return self.head.data

    def size(self):

        temp = self.head
        count = 0
        while temp is not None:
            count = count + 1
            temp = temp.next
        return count

    def is_empty(self):

        if self.head is None:
            return True
        else:
            return False

    def printqueue(self):

        print("queue elements are:")
        temp = self.head
        while temp is not None:
            print(temp.data, end="->")
            temp = temp.next