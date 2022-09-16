import sys
from analisador_lexico import AnalisadorLexico
if(len(sys.argv) < 2):
    print("Argumento de arquivo de código em perl vazio :c\nTente: python main.py <arquivo_de_codigo.pl>\n")
    exit()

try:
    file = open(sys.argv[1], 'r', encoding="utf-8")

except:
    print("Arquivo inválido")

else:
    print(f"Compilando {sys.argv[1]}")
    # print(file.read())
    c = AnalisadorLexico(file.read())
    c.nextToken()
finally:
    file.close()

    # c+=1
    # for line, lineData in enumerate(file, start=1):
    #     for char, charData in enumerate(lineData, start=1):
    #         print(charData)
    # file.seek(0)
    # print(file.readlines())
    # token = TokenCategory.COMMENT_LINE
    # print(token)
