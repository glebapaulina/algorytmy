import  operator

class BNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def set_left(self, node):
        if node is not None:
            node.parent = self
        self.left = node
        return node

    def set_right(self, node):
        if node is not None:
            node.parent = self
        self.right = node
        return node

    def is_leaf(self):
        return self.left is None and self.rigth is None


class ExpressionTree:
    def __init__(self, root=None):
        self._root = root

    def root(self):
        # zwraca korzen drzewa
        return self._root

    def in_order_print(self, node):
        if node is not None:
            self.in_order_print(node.left)
            print(node.data)
            self.in_order_print(node.right)

    def print_expression_tree(self, node):
        operatory = ('+', '-', '*', '/')
        wynik = ""
        if node is not None:
            if node.data in operatory:
                wynik += '('
            wynik += str(self.print_expression_tree(node.left))
            wynik += str(node.data)
            wynik += str(self.print_expression_tree(node.right))
            if node.data in operatory:
                wynik += ')'
        return wynik

    def evaluate(self, node):
        operatory = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        if node is not None:
            if node.data in operatory:
                a = self.evaluate(node.left)
                b = self.evaluate(node.right)
                dzialanie = operatory[node.data]
                return dzialanie(a, b)
            else:
                return node.data





t = ExpressionTree(BNode('/'))

a = t.root().set_left(BNode('*'))
a.set_left(BNode(2))
b = a.set_right(BNode('+'))
b.set_left(BNode(3))
c = b.set_right(BNode('/'))
c.set_left(BNode(6))
c.set_right(BNode(2))
t.root().set_right(BNode(4))

# print(t.print_expression_tree(t.root()))
print(t.evaluate(t.root()))