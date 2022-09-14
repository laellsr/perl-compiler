import sys
from enum import Enum
from tokenCategory import *
from token import *
from scanner import *
if(len(sys.argv) < 2):
    print("Argumento de arquivo de código em perl vazio :c\nTente: python main.py <arquivo_de_codigo.pl>\n")
    exit()

try:
    file = open(sys.argv[1], 'r', encoding="utf-8")

except:
    print("Arquivo inválido")

else:
    print(f"Compilando {sys.argv[1]}")
    print(file)
    content = file.readlines()
    scanner(content)
    # for line, lineData in enumerate(file, start=1):
    #     for char, charData in enumerate(lineData, start=1):
    #         print(charData)
    # file.seek(0)
    # print(file.readlines())

    # token = TokenCategory.COMMENT_LINE
    # print(token)

finally:
    file.close()
