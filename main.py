import sys

print(sys.argv[1])

try:
    file = open(sys.argv[1], 'r', encoding="utf-8")
except:
    print("Arquivo inválido")
else:
    print("Arquivo aberto")
    for line in file:
        print(line)
    # file.seek(0)
    # print(file.readlines())
finally:
    file.close()