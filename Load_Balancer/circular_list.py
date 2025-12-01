class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.current = None

    def append(self, value):
        new = Node(value)
        if not self.head:
            self.head = new
            new.next = new
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new
            new.next = self.head

    def next(self):
        if not self.current:
            self.current = self.head
        else:
            self.current = self.current.next
        return self.current.value
