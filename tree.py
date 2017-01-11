# -*- encoding: utf8 -*-
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []
        
    def add_child(self, node):
        node.parent = self
        self.children.append(node)
        return node
        
    def is_leaf(self):
        return len(self.children) == 0


class Tree:
    def __init__(self, root = None):
        self._root = root

    def root(self):
        # zwraca korzen drzewa
        return self._root

    def depth(self, node):
        licz = 0
        current = node.parent
        while current is not None:
            if current.data == node:

                current = current.parent
            licz +=1
        return licz

    def print_tree(self):
        # Wypisuje zawartość drzewa
        def print_node(node, level=1):
            if node is not None and node == self.root():
                print(node.data)
            for child in node.children:
                print ('\t')*level + (child.data)
                print_node(child, level+1)

        print_node(self.root())


# Przyklad konstrukcji drzewa
tree = Tree(TreeNode("Game of Thrones"))

s1 = tree.root().add_child(TreeNode("Season 1"))
s1.add_child(TreeNode("Winter Is Coming"))
s1.add_child(TreeNode("The Kingsroad"))
s1.add_child(TreeNode("Lord Snow"))

s2 = tree.root().add_child(TreeNode("Season 2"))
s2.add_child(TreeNode("The North Remembers"))
s2.add_child(TreeNode("The Night Lands"))
s2.add_child(TreeNode("What Is Dead May Never Die"))

tree.print_tree()
print(tree.depth("Lord Snow"))