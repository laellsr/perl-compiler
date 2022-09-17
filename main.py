import sys
from tkCategory import *
from lexer import *

def run(lexer) -> None:
    while lexer.currentFilePosition < lexer.fileSize:
        print(lexer.currentChar, lexer.currentFilePosition)
        match lexer.state:
            case 0:
                # initial
                lexer.isPass()
                lexer.isDigit()
                lexer.isLetter()
                lexer.isDollar()
                lexer.isArray()
                # lexer.isSemicolon()
                # lexer.isSymbol()
            case 1:
                # identifier: scalar, array, func
                lexer.isIdentifier()
            case 2:
                # number
                lexer.isNumber()
            case 3:
                # reserved word
                lexer.isReservedWord()
            case default:
                pass
    if lexer.lexeme != '':
            lexer.nextToken()

def printLexerTokenList(lexer) -> None:
    for token in lexer.tokens:
        print("<" + token.category + "," + token.value + ">")

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
    lexer = Lexer(fileString)
    run(lexer)
    printLexerTokenList(lexer)
finally:
    pass
