from tkCategory import *
import re

class Lexer:
    def __init__(self, file) -> None:
        self.file = file
        self.fileSize = len(self.file)
        self.currentFilePosition = 0
        self.crrentLinePosition = 0
        self.state = 0
        self.lexeme = ""
        self.currentChar = self.file[self.currentFilePosition]
        self.currentCharIsChecked = 0
        self.tokens = []
        self.brackets = Brackets()
        
    def nextChar(self) -> None:
        self.currentFilePosition += 1
        if self.currentFilePosition < self.fileSize:
            self.currentChar = self.file[self.currentFilePosition]
            self.currentCharIsChecked = 0
    
    def nextToken(self) -> None:
        token = Token(self.lexeme)
        if token.category == 'SUBROUTINE_IDENTIFIER':
            if self.tokens[len(self.tokens)-1].category != 'RESERVED_SUBROUTINE':
                token.category = 'FUNC_IDENTIFIER'
        self.tokens.append(token)
        self.lexeme = ""
        self.state = 0
        self.nextChar()
        
    def isDigit(self) -> None:
        if self.currentCharIsChecked == 1:
            return
        elif re.fullmatch(r'[0-9]', self.currentChar):
            self.state = 2
            self.recognized()

    def isDollar(self) -> None:
        if self.currentCharIsChecked == 1:
            return
        elif self.currentChar == '$':
            self.state = 1
            self.recognized()
    
    def isLetter(self) -> None:
        if self.currentCharIsChecked == 1:
            return
        elif re.fullmatch(r'[a-z]', self.currentChar):
            self.state = 3
            self.recognized()
        elif re.fullmatch(r'[A-Z]', self.currentChar):
            self.state = 1
            self.recognized()
    
    def isReservedWord(self) -> None:
        if self.currentCharIsChecked == 1:
            return
        elif re.fullmatch(r'[a-z]', self.currentChar):
            self.recognized()
        elif re.fullmatch(r'[a-zA-z0-9_]', self.currentChar):
            self.state = 1
            self.recognized()
        else:
            self.nextToken()
        
    def isNumber(self) -> None:
        if self.currentCharIsChecked == 1:
            return
        elif re.fullmatch(r'[0-9]|(\.)', self.currentChar):
            self.recognized()
        else:
            self.nextToken()
    
    def isIdentifier(self) -> None:
        if self.currentCharIsChecked == 1:
            return
        elif re.fullmatch(r'[a-zA-Z]', self.currentChar):
            self.recognized()
        else:
            self.nextToken()

    def isPass(self) -> None:
        if self.currentCharIsChecked == 1:
            return
        elif self.currentChar == ' ' or self.currentChar == '\n' or self.currentChar == '\t':
            self.currentCharIsChecked = 1
            self.nextChar()
    
    def isArray(self):
        if self.currentCharIsChecked == 1:
            return
        elif self.currentChar == '@':
            self.state = 1
            self.recognized()
    
    def recognized(self):
        self.currentCharIsChecked = 1
        self.lexeme += self.currentChar
        self.nextChar()

    def isOperator(self):
        if self.currentCharIsChecked == 1:
            return
        elif re.fullmatch(r'[(<)|(>)|(\&)|(\|)|(\*)|(\%)|(\+)|(\-)|(>=)|(<=)|(!=)|(=)]', self.currentChar):
            self.recognized
        else:
            self.nextToken()
        
        
    # def isSemicolon():
    #     if self.currentCharIsChecked:
    #         return
    #     elif self.currentChar == '$':
    #         self.state = 1
    #         self.nextChar()

class Brackets:
    def __init__(self) -> None:
        self.round = 0
        self.square = 0
        self.curvy = 0
        
class Token:
    def __init__(self, lexeme):
        self.category = self.getTokenCategory(lexeme)
        self.value = lexeme
        self.line = 0
        self.column = 0
        self.error = 0
    
    def getTokenCategory(self, lexeme):
        for tkCategory in tkCategories:
            if re.fullmatch(tkCategories[tkCategory], lexeme) != None:
                return tkCategory
        return 'UNKNOW'