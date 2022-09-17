import sys
from tkCategory import *
from lexer import *

def run(lexer):
    while lexer.currentFilePosition <= lexer.fileSize:
        if lexer.currentFilePosition==lexer.fileSize:
            lexer.nextToken()
            break
        # print(lexer.currentChar, lexer.currentFilePosition, lexer.fileSize)
        match lexer.state:
            case 0:
                # initial
                lexer.isPass()
                lexer.isDollar()
                lexer.isArray()
                # lexer.isLetter()
                lexer.isDigit()
                # lexer.isSemicolon()
                # lexer.isSymbol()
            case 1:
                # scalar or array
                lexer.isScalarOrArray()
            case 2:
                # number
                lexer.isNumber()
                pass
            case 3:
                # letter
                # lexer.isLetter()
                pass
            case default:
                pass

def printLexerTokenList(lexer):
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
