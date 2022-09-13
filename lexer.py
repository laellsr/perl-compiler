from tokenCategory import *

class Lexer:
    def __init__(self) -> None:
        self.state = 0
        self.brackets = Brackets()
        
class Brackets:
    def __init__(self) -> None:
        self.round = 0
        self.square = 0
        self.curvy = 0
        
class Token:
    def __init__(self, TokenCategory, line, column, value):
        self.category = TokenCategory
        self.line = line
        self.column = column
        self.value = value