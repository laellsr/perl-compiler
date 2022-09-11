from enum import Enum

class Carros(Enum):
    fiat = 1
    bmw = 2
    ford = "olá"


print(Carros.fiat.value)

# tokens = {"azul" : 1, "vermelho" : 2}

# for item in tokens:
#     print(item, tokens[item])