
import unittest

from my_list import LinkedList, Node
from my_list import *

import unittest


class TestList(unittest.TestCase):

    # def test_nowa_lista_nie_ma_glowy(self):
    #     l = LinkedList()
    #     self.assertEqual(l.head, None)
    #
    # def test_wstawienie_pierwszego_elementu(self):
    #     l = LinkedList()
    #     l.insert(Node(10))
    #     self.assertEqual(l.head.data, 10)
    #
    # def test_wstawienie_2_elementow(self):
    #     l = LinkedList()
    #     l.insert(Node(10))
    #     l.insert(Node(20))
    #     self.assertEqual(l.head.data, 20)
    #     self.assertEqual(l.head.next.data, 10)
    #
    # def test_wstawienie_3_elementow(self):
    #     l = LinkedList()
    #     l.insert(Node(10))
    #     l.insert(Node(20))
    #     l.insert(Node(30))
    #     self.assertEqual(l.head.data, 30)
    #     self.assertEqual(l.head.next.data, 20)
    #     self.assertEqual(l.head.next.next.data, 10)
    #
    # def test_wyszukiwanie_z_porazka(self):
    #     l = LinkedList()
    #     l.insert(Node(10))
    #     l.insert(Node(20))
    #     l.insert(Node(30))
    #     self.assertEqual(l.search(40), None)
    #
    # def test_wyszukiwanie_sukces_ostatni(self):
    #     l = LinkedList()
    #     n1 = Node(10)
    #     n2 = Node(20)
    #     n3 = Node(30)
    #     l.insert(n1)
    #     l.insert(n2)
    #     l.insert(n3)
    #     self.assertEqual(l.search(10), n1)
    #
    # def test_wyszukiwanie_sukces_pierwszy(self):
    #     l = LinkedList()
    #     n1 = Node(10)
    #     n2 = Node(20)
    #     n3 = Node(30)
    #     l.insert(n1)
    #     l.insert(n2)
    #     l.insert(n3)
    #     self.assertEqual(l.search(30), n3)
    #
    # def test_dlugosc_listy(self):
    #     l = LinkedList()
    #     n1 = Node(10)
    #     n2 = Node(20)
    #     n3 = Node(30)
    #     l.insert(n1)
    #     l.insert(n2)
    #     l.insert(n3)
    #     self.assertEqual(len(l), 3)

    # def test_zliczanie_wystapienia_elementu_data(self):
    #     l = LinkedList()
    #     l.insert(Node(10))
    #     l.insert(Node(20))
    #     l.insert(Node(30))
    #     l.insert(Node(20))
    #     self.assertEqual(l.count(20), 2)

    # def test_wstawienie_na_koncu(self):
    #     l = LinkedList()
    #     l.append(10)
    #     l.append(20)
    #     self.assertEqual(l.tail.data, 20)
    #
    # def test_wstawianie_na_koncu_do_pustej(self):
    #     l = LinkedList()
    #     l.append(10)
    #     self.assertEqual(l.tail.data, 10)
    #
    # def test_wypisywanie_listy(self):
    #     l = LinkedList()
    #     l.insert(Node(10))
    #     l.insert(Node(20))
    #     l.insert(Node(30))
    #     self.assertEqual(l.show(), [30, 20, 10])

    def test_wstawianie_po_elemencie(self):
        l = LinkedList()
        l.insert(Node(4))
        l.insert(Node(3))
        l.insert(Node(2))
        l.insert(Node(1))
        self.assertEqual (l.show(l.insert_after(8,2))) == [1,2,8,3,4])


if __name__ == '__main__':
    unittest.main()

