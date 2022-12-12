class symb:
    def __init__(self):
        self.hash = dict()

    def add(self, id, type, scope):
        self.hash[id] = (type, "value,",scope)
        # self.hash[id] = type


