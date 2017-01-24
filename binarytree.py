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
        return self.left is None and self.right is None


class BinaryTree:
    def __init__(self, root=None):
        self._root = root

    def root(self):
        # zwraca korzen drzewa
        return self._root

    # def get_right(self):
    #     return self.right
    #
    # def get_left(self):
    #     return self.left

    def pre_order_print(self, node):
        if node is not None:
            # node = self.root()
            print(node.data)
            self.pre_order_print(node.left)
            self.pre_order_print(node.right)

    def in_order_print(self, node):
        if node is not None:
            self.in_order_print(node.left)
            print(node.data)
            self.in_order_print(node.right)

    def post_order_print(self, node):
        if node is not None:
            self.post_order_print(node.left)
            self.post_order_print(node.right)
            print(node.data)




tree = BinaryTree(BNode('a'))
nodeB = tree.root().set_left(BNode('b'))
nodeC = tree.root().set_right(BNode('c'))
nodeD = nodeC.set_left(BNode('d'))
nodeE = nodeC.set_right(BNode('e'))
# print(tree.pre_order_print(nodeC))
print(tree.in_order_print(tree.root()))
# print(tree.post_order_print(nodeC))
