import sys
from tokenCategory import *

# print(sys.argv[1])

if(len(sys.argv) < 2):
    print("Argumento de arquivo de código em perl vazio :c\nTente: python main.py <arquivo_de_codigo.pl>\n")
    exit()

try:
    file = open(sys.argv[1], 'r', encoding="utf-8")
except:
    print("Arquivo inválido")
else:
    print(f"Compilando {sys.argv[1]}")
    print(file.readlines())
    # for line, lineData in enumerate(file, start=1):
    #     for char, charData in enumerate(lineData, start=1):
    #         print(charData)
    # file.seek(0)
    # print(file.readlines())
    # token = TokenCategory.COMMENT_LINE
    # print(token)
finally:
    file.close()

class Token:
    def __init__(self, TokenCategory, line, column, value):
        self.category = TokenCategory
        self.line = line
        self.column = column
        self.value = value
        