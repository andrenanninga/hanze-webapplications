__author__ = 'Lasse'

class Node:

    parent = None
    name = None
    children = []

    def __init__(self, name, parent=None):
        self.name = name
        # self.left = left
        # self.right = right
        self.children = []
        self.parent = parent

    def __str__(self):
        return str(self.name)

    def performAction(self, depth=0, tree=""):
        info = " " * depth + "My name is " + self.name + " "
        tree += " " * depth + self.name

        if self.parent is not None and len(self.parent.children) == 2:
            info += "and I have a sibling "
        else:
            info += "and I do not have a sibling "

        if len(self.children) > 0:
            info += "and I have a childNode"
        else:
            info += "and I do not have a childNode"

        print(info)
        for child in self.children:
            child.performAction(depth + 1)

    def add(self, node):
        node.parent = self;
        self.children.append(node)


if __name__ == "__main__":
    theropodia = Node("theropodia")
    ceratosauria = Node("ceratosauria")
    coelophysoi = Node("coelophysoi")
    abelisauroi = Node("abelisauroi")
    tetanurae = Node("tetanurae")
    coelurosauria = Node("coelurosauria")
    trex = Node("T-rex")
    eend = Node("Eend")

    theropodia.add(ceratosauria)
    theropodia.add(tetanurae)
    ceratosauria.add(coelophysoi)
    ceratosauria.add(abelisauroi)
    tetanurae.add(coelurosauria)
    coelurosauria.add(trex)
    coelurosauria.add(eend)

    theropodia.performAction()
