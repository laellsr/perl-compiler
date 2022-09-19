from token import *
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
        # if token.category == 'SUBROUTINE_IDENTIFIER':
        #     if self.tokens[len(self.tokens)-1].category != 'RESERVED_SUBROUTINE':
        #         token.category = 'FUNC_IDENTIFIER'
        self.tokens.append(token)
        self.lexeme = ""
        self.state = 0
        if self.currentCharIsChecked == 1:
            self.nextChar()
    
    def recognized(self, next):
        self.currentCharIsChecked = 1
        self.lexeme += self.currentChar
        if next:
            self.nextChar()
        else:
            self.nextToken()
        
    def isDigit(self) -> None:
        if self.currentCharIsChecked == 1:
            return
        elif re.fullmatch(r'[0-9]', self.currentChar):
            self.state = 2
            self.recognized(next=True)

    def isDollar(self) -> None:
        if self.currentCharIsChecked == 1:
            return
        elif self.currentChar == '$':
            self.state = 1
            self.recognized(next=True)
    
    def isLetter(self) -> None:
        if self.currentCharIsChecked == 1:
            return
        elif re.fullmatch(r'[a-z]', self.currentChar):
            self.state = 3
            self.recognized(next=True)
        elif re.fullmatch(r'[A-Z]', self.currentChar):
            self.state = 1
            self.recognized(next=True)
    
    def isReservedWord(self) -> None:
        if self.currentCharIsChecked == 1:
            return
        elif re.fullmatch(r'[a-z]', self.currentChar):
            self.recognized(next=True)
        elif re.fullmatch(r'[a-zA-z0-9_]', self.currentChar):
            self.state = 1
            self.recognized(next=True)
        else:
            self.nextToken()
        
    def isNumber(self) -> None:
        if self.currentCharIsChecked == 1:
            return
        elif re.fullmatch(r'[0-9]|(\.)', self.currentChar):
            self.recognized(next=True)
        else:
            self.nextToken()
    
    def isIdentifier(self) -> None:
        if self.currentCharIsChecked == 1:
            return
        elif re.fullmatch(r'[a-zA-Z]', self.currentChar):
            self.recognized(next=True)
        else:
            self.nextToken()

    def isPass(self) -> None:
        if self.currentCharIsChecked == 1:
            return
        elif self.currentChar == ' ' or self.currentChar == '\n' or self.currentChar == '\t':
            self.currentCharIsChecked = 1
            self.nextChar()
    
    def isSign(self):
        if self.currentCharIsChecked == 1:
            return
        elif self.currentChar == '@':
            self.state = 1
            self.recognized(next=True)
    
    def isOperator(self):
        if self.currentCharIsChecked == 1:
            return
        elif re.fullmatch(r'[(\|)|(\*)|(\%)]', self.currentChar):
            if self.lexeme != '':
                self.nextToken()
            else:
                self.recognized(next=False)
        elif re.fullmatch(r'[(<)|(>)|(\&)|(\|)|(\%)|(\+)|(\-)|(=)|(!)]', self.currentChar):
            if self.lexeme != '':
                self.nextToken()
            if re.search(r'NUMBER|IDENTIFIER', self.tokens[len(self.tokens)-1].category) and re.fullmatch(r'[^<>\&\|\%\+\-=!]', self.file[self.currentFilePosition+1]):
                self.recognized(next=False)
            else:
                self.state = 4
                self.recognized(next=True)
    
    def isDoubleOperator(self):
        if self.currentCharIsChecked == 1:
            return
        elif re.fullmatch(r'[(<)|(>)|(\&)|(\|)|(\%)|(\+)|(\-)|(=)|(!)]', self.currentChar):
            self.recognized(next=False)
        else:
            self.state = 0
            self.nextToken()
    
    def isQuote(self):
        if self.currentCharIsChecked == 1:
            return
        elif re.fullmatch(r'["\']', self.currentChar):
            self.state = 6
            self.recognized(next=True)

    def isString(self):
        if self.currentCharIsChecked == 1:
            return
        elif re.fullmatch(r'[^"\']', self.currentChar):
            self.recognized(next=True)
        else:
            self.recognized(next=False)
            
    def isScope(self):
        if self.currentCharIsChecked == 1:
            return
        elif re.fullmatch(r'[{}]', self.currentChar):
            self.recognized(next=False)
       
    def isSemicolon(self):
        if self.currentCharIsChecked == 1:
            return
        elif self.currentChar == ';':
            if self.lexeme == '':
                self.recognized(next=False)
            else:
                self.nextToken()
        
    def isCurvyBracket(self):
        if self.currentCharIsChecked == 1:
            return
        # elif re.fullmatch == '(':
        #     j = self.currentFilePosition
        #     newLexeme = ''
        #     while j < self.fileSize-1:
        #         lexeme += self.file[j]
            # for j in range(self.currentFilePosition+1, self.fileSize-1):
        elif re.fullmatch(r'[\(\)]', self.currentChar):
            self.recognized(next=False)
