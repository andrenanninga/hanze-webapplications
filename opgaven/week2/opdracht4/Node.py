__author__ = 'Lasse'


class Node:
    def __init__(self, name, left=None, right=None):
        self._name = name
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)

    def performAction(self, depth):
        print(" " * depth, self._name)


def traverse(node, depth=0):
    if node == None: return
    node.performAction(depth)
    traverse(node.left, depth + 1)
    traverse(node.right, depth + 1)


if __name__ == "__main__":
    tetanurae = Node("tetanurae", Node("coelurosauria", Node("T-Rex"), Node("Eend")))
    ceratosauria = Node("ceratosauria", Node("coelophysoi"), Node("abelisauroi"))
    theropodia = Node("theropodia", ceratosauria, tetanurae)

traverse(theropodia)
