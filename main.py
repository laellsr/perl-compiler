import sys
import re
from token import *
from lexer import *
from parser import *
def run(lexer) -> None:
    while lexer.currentFilePosition < lexer.fileSize:
        match lexer.state:
            case 0:
                # initial
                lexer.isPass()
                lexer.isDigit()
                lexer.isLetter()
                lexer.isDollar()
                lexer.isSign()
                lexer.isOperator()
                lexer.isQuote()
                lexer.isScope()
                lexer.isBrackets()
                lexer.isComma()
                lexer.isCurvyBracket()
                lexer.isSemicolon()
                lexer.isCommentLine()
            case 1:
                # identifier: scalar, array, func
                lexer.isIdentifier()
            case 2:
                # number
                lexer.isNumber()
            case 3:
                # reserved word
                lexer.isReservedWord()
            case 4:
                # operator + number
                lexer.isDigit()
                if lexer.currentCharIsChecked==0 and re.fullmatch(r'[^0-9]', lexer.currentChar):
                    lexer.state = 5
            case 5:
                # double operator
                lexer.isDoubleOperator()
            case 6:
                # string
                lexer.isString()
            case default:
                pass
    if lexer.lexeme != '':
            lexer.nextToken()
    

def printLexerTokenList(lexer) -> None:
    for token in lexer.tokens:
        print("<" + token.category + "," + token.value + ">")

def createTxtFile(lexer) -> None:
    with open('out.txt', 'w') as file:
        for token in lexer.tokens:
            file.write("<" + token.category + "," + token.value + ">" + "\n")
        file.close()

if(len(sys.argv) < 2):
    print("Argumento de arquivo de código em perl vazio :c\nTente: python main.py <arquivo_de_codigo.pl>\n")
    exit()
try:
    file = open(sys.argv[1], 'r', encoding="utf-8")
except:
    print("Arquivo inválido")
else:
    print(f"Compilando {sys.argv[1]}")
    fileString = file.read()
    file.close()
    # fileString = re.sub(r'\s', '', fileString)
    lexer = Lexer(fileString)
    run(lexer)
    parser = Parser(lexer.tokens)
    parser.File_Item()
    printLexerTokenList(lexer)
    createTxtFile(lexer)
finally:
    pass
