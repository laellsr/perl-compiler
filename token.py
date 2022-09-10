class Token:
    def __init__(self, category, line, column, value):
        self.category = category
        self.line = line
        self.column = column
        self.value = value