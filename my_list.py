class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    # wstawia element na poczatek listy
    def insert(self, node):
        current = self.head
        self.head = node
        node.next = current

    def delete(self, node):
        raise NotImplementedError()

    # wyszukuje wezel listy, zawierajacy dane o wartosci data
    def search(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return current
            current = current.next
        return None

    #dlugosc listy
    def __len__(self):
        current = self.head
        count = 0
        while current is not None:
            current = current.next
            count += 1
        return count

    #zliczanie wystapienia elemnetu
    def count(self, data):
        current = self.head
        count = 0
        while current is not None:
            if current.data == data:
                count += 1
            current = current.next
        return count

    #dodawanie na koncu listy
    def append(self, new_node):
        new_node = Node(new_node)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    #wyszukiwanie elementu
    def search(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return current
            current = current.next
        return None
    
    #wyswietlanie listy
    def show(self):
        current = self.head
        lista = []
        while current is not None:
            lista.append(current.data)
            current = current.next
        return lista

    #wstawianie po elemencie
    def insert_after(self, new_node, node):
        current = self.head
        if node is None:
            return False
        new_node = Node(new_node)
        node = Node(node)
        tab = []
        while current.data != node.data:
            current = current.next
        new_node.next = current.next
        current.next = new_node
# l = LinkedList()
# l.insert(Node(4))
# l.insert(Node(3))
# l.insert(Node(2))
# l.insert(Node(1))
# l.insert_after(8,3)
# assert l.show() == [1, 2, 3, 8, 4]

    #wstawianie z sortowaniem
    def insert_sorted(self, node):
        current = self.head
        node = Node(node)
        while current is not None and current.next.data < node.data:
            current = current.next
        node.next = current.next
        current.next = node
# l = LinkedList()
# l.insert(Node(5))
# l.insert(Node(3))
# l.insert(Node(2))
# l.insert(Node(1))
# l.insert_sorted(4)
# print(l.show())

    #odwracanie listy
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            self.next = None
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
# l = LinkedList()
# l.insert(Node(5))
# l.insert(Node(3))
# l.insert(Node(2))
# l.insert(Node(1))
# l.insert_sorted(4)
# l.reverse()
# print(l.show())

