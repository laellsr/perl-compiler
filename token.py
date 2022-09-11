from tokenCategory import *

class Token:
    def __init__(self, TokenCategory, line, column, value):
        self.category = TokenCategory
        self.line = line
        self.column = column
        self.value = value