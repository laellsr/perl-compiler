class symb:
    def __init__(self):
        self.hash = dict()

    def add(self, id, type):
        self.hash[id] = type

