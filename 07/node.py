class Node:
    def __init__(self, name: str, size: int, parent):
        self.children = []
        self.level = 0
        self.name = name
        self.size = size
        self.parent = parent
        if parent is not None:
            self.level = parent.level + 1

    def get_child(self, name: str):
        print('Searching', self.children, 'for', name)
        node = next(filter(lambda n: n.name == name, self.children), None)
        if node is None:
            raise FileNotFoundError('Child not found: ' + name)
        return node

    def add_child(self, name, size):
        self.children.append(Node(name, size, self))

    def get_directories(self):
        # print('Walking', self)
        l = [self]
        for c in self.children:
            if len(c.children) > 0:
                l.extend(c.get_directories())
        return l

    def __str__(self):
        return self.name + '(' + str(self.level) + ')'

    def __repr__(self):
        return self.__str__()
