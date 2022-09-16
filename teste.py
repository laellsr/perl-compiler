import re
from palavraReconhecida import PalavraReconhecida
from tokenClass import Token
from tokenCategory import TokenCategory
c = '12121212'
s = re.search(r'^\d+(.\d+)$', c)
print(s)


# def isNumInt(self, posInicial):
#     string = self.strg
#     lexema = ""
#     lexema += string[posInicial]
#     print(f"Lexema inicial {lexema}")
#     pos = posInicial
#     while(True):
#         if re.fullmatch(r'[0-9]*', lexema) != None:
#             pos += 1
#             if(self.EOF(pos) == False):
#                 print(f"A posição agora é: {pos}")
#                 # ando na minha string
#                 lexema += string[pos]
#                 print(f"O lexema é: {lexema}")
#             else:
#               lexema = lexema[:-1]
#               # Setando o Token
#               token = Token(TokenCategory.NUM_INT.name, lexema)
#               # Retorno um objeto com as informações do Token reconhecido e a posição que o nextToken deve continuar lendo
#               return PalavraReconhecida(token, pos)
#         else:
#            # se lexema não saiu do lugar, é pq não reconheceu nem o primeiro lexema
#             if(lexema == string[posInicial]):
#                 print('não é var')
#                 return posInicial
#             else:
#                 # Vou tirar o último lexema que não foi reconhecido
#                 lexema = lexema[:-1]
#                 # Setando o Token
#                 token = Token(TokenCategory.NUM_INT.name, lexema)
#                 # Retorno um objeto com as informações do Token reconhecido e a posição que o nextToken deve continuar lendo
#                 return PalavraReconhecida(token, pos)


# pos = 0
# resposta = isNumInt('123121.21212sa ', pos)
# if resposta == pos:
#     print(f'Continuo em {resposta}')
# else:
#     print(f'O token é {resposta.token}')
#     print(f'E a posição é {resposta.pos}')


# def isOpAri(string, posInicial):
#     # string = self.strg
#     lexema = ""
#     lexema += string[posInicial]
#     pos = posInicial
#     if(lexema == '*'):
#         t = Token(TokenCategory.OPERATOR_MUL.name, lexema)
#         return PalavraReconhecida(t, pos+1)
#     elif(lexema == '%'):
#         t = Token(TokenCategory.OPERATOR_MOD.name, lexema)
#         return PalavraReconhecida(t, pos+1)
#     elif(lexema == '+'):
#         if(string[pos+1] == '+'):
#             lexema += string[pos+1]
#             t = Token(TokenCategory.OPERATOR_PLUS_PLUS.name, lexema)
#             return PalavraReconhecida(t, pos+2)
#         else:
#             t = Token(TokenCategory.OPERATOR_PLUS.name, lexema)
#             return PalavraReconhecida(t, pos+1)
#     elif(lexema == '-'):
#         if(string[pos+1] == '-'):
#             lexema += string[pos+1]
#             t = Token(TokenCategory.OPERATOR_MINUS_MINUS.name, lexema)
#             return PalavraReconhecida(t, pos+2)
#         else:
#             t = Token(TokenCategory.OPERATOR_MINUS.name, lexema)
#             return PalavraReconhecida(t, pos+1)
#     elif(lexema == '!'):
#         t = Token(TokenCategory.OPERATOR_NOT.name, lexema)
#         return PalavraReconhecida(t, pos+1)
#     elif(lexema == '/'):
#         t = Token(TokenCategory.OPERATOR_DIV.name, lexema)
#         return PalavraReconhecida(t, pos+1)
#     elif(lexema == '='):
#         print(lexema)
#         if(string[pos+1] == '='):
#             print(lexema)
#             lexema += string[pos+1]
#             t = Token(TokenCategory.OPERATOR_EQ_NUMERIC.name, lexema)
#             return PalavraReconhecida(t, pos+2)
#         else:
#             t = Token(TokenCategory.OPERATOR_ASSIGN.name, lexema)
#             return PalavraReconhecida(t, pos+1)
#     else:
#         return posInicial


# pos = 0
# resposta = isOpAri('*', pos)
# if resposta == pos:
#     print(f'Continuo em {resposta}')
# else:
#     print(f'O token é {resposta.token}')
#     print(f'E a posição é {resposta.pos}')
# retorna o Token dela e a posição ate terminar a palavra, caso não ache, retorne posição inicial
# def isVar(posInicial, string):
#     lexema = ""
#     lexema += string[posInicial]
#     print(f"Lexema inicial {lexema}")
#     pos = posInicial
#     while(True):
#         if(re.fullmatch(r'^[$][a-zA-Z0-9_]*', lexema) != None):
#             pos += 1
#             print(f"A posição agora é: {pos}")
#             lexema += string[pos]
#             print(f"O lexema é: {lexema}")
#             # ando na minha string
#         else:
#             # se lexema não saiu do lugar, é pq não reconheceu nem o primeiro caracter
#             if(lexema == string[posInicial]):
#                 return posInicial
#             else:
#                 # Vou tirar o último caracter que não foi reconhecido
#                 lexema = lexema[:-1]
#                 # Setando o Token
#                 token = Token(TokenCategory.VAR.name, lexema)
#                 # Retorno um objeto com as informações do Token reconhecido e a posição que o nextToken deve continuar lendo
#                 return PalavraReconhecida(token, pos)
