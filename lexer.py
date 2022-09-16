from tokenCategory import *

class Lexer:
    def __init__(self, file) -> None:
        self.file = file
        self.state = 0
        self.tokens = []
        self.currentToken = Token()
        self.brackets = Brackets()
        self.charChecked = 0
        
    def nextChar(self, char) -> None:
        self.charChecked = 0
        match self.state:
            case 0:
                isScalar(char)
                isArray(char)
                isLetter(char)
                isNumber(char)
                isSemicolon(char)
                isSymbol(char)
            case 1:
                # scalar
                isLetter(char)
                isUnderline(char)
                is
            case default:
                pass
    
    def nextToken(self) -> None:
        self.tokens.append(self.currentToken)
        self.currentToken = Token()        
    
    def isScalar(self, char) -> None:
        if self.charChecked:
            return
        if char == '$':
            self.currentToken.value = self.currentToken.value + char
            self.state = 1
            self.charChecked = 1
            
        
class Brackets:
    def __init__(self) -> None:
        self.round = 0
        self.square = 0
        self.curvy = 0
        
class Token:
    def __init__(self):
        self.category = ""
        self.line = 0
        self.column = 0
        self.value = ""
        self.error = 0