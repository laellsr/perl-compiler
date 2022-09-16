from tokenCategory import TokenCategory
from tokenClass import Token
from isToken import IsToken
# from nextChar import NextChar


class AnalisadorLexico:
    def __init__(self, string):
        self.string = string

    def nextToken(self):
        listaTokens = []
        posAtual = 0
        t = IsToken(self.string)
        while(True):
            fim = t.EOF(posAtual)
            if(fim == False):
                if(t.isVar(posAtual) != posAtual):
                    x = t.isVar(posAtual)
                    listaTokens.append(x.token)
                    posAtual = x.pos
                    print(f"VAR pos atual {posAtual}")
                if(t.isVector(posAtual) != posAtual):
                    x = t.isVector(posAtual)
                    listaTokens.append(x.token)
                    posAtual = x.pos
                    print(f" VECT pos atual {posAtual}")
                if(t.isOpAri(posAtual) != posAtual):
                    x = t.isOpAri(posAtual)
                    listaTokens.append(x.token)
                    posAtual = x.pos
                    print(f"OPARI pos atual {posAtual}")
                # if(t.isNumInt(posAtual) != posAtual):
                #     x = t.isNumInt(posAtual)
                #     listaTokens.append(x.token)
                #     posAtual = x.pos
                #     print(f"NUM pos atual {posAtual}")

                else:
                    print('não reconheci')
                    token = Token(TokenCategory.ERROR.name,
                                  self.string[posAtual])
                    posAtual += 1
                    print(f"ERROR pos atual {posAtual}")

                    listaTokens.append(token)

            else:
                listaTokens.append(fim)
                break
        print('passou aqui')
        for a in listaTokens:
            print(a)

    # def nextTokenq(self):
    #     caracterLido = self.string
    #     listaTokens = []
    #     pos = 0
    #     tamanho = len(self.string)
    #     while pos != tamanho:
    #         # print(caracter[pos])
    #         # print(self.next_char(pos))
    #         # if(self.back(pos) == -1):
    #         #     pass
    #         # else:
    #         #     print(self.back(pos))
    #         # break
    #         caracter = caracterLido[pos]
    #         print(caracter)
    #         if(caracter == ' ' or caracter == '\n'):
    #             pass
    #         if(caracter == ';'):
    #             t = Token(TokenCategory.SEMICOLON.name, ';')
    #             listaTokens.append(t.__str__())
    #         elif(caracter == '*'):
    #             t = Token(TokenCategory.OPERATOR_MUL.name, '*')
    #             listaTokens.append(t.__str__())
    #         elif(caracter == '%'):
    #             t = Token(TokenCategory.OPERATOR_MOD.name, '%')
    #             listaTokens.append(t.__str__())
    #         elif(caracter == '+'):
    #             t = Token(TokenCategory.OPERATOR_PLUS.name, '+')
    #             listaTokens.append(t.__str__())
    #         elif(caracter == '-'):
    #             t = Token(TokenCategory.OPERATOR_MINUS.name, '-')
    #             listaTokens.append(t.__str__())
    #         elif(caracter == '!'):
    #             t = Token(TokenCategory.OPERATOR_NOT.name, '!')
    #             listaTokens.append(t.__str__())
    #         elif(caracter == '/'):
    #             t = Token(TokenCategory.OPERATOR_DIV.name, '/')
    #             listaTokens.append(t.__str__())
    #         elif(caracter == '='):
    #             t = Token(TokenCategory.OPERATOR_ASSIGN.name, '=')
    #             listaTokens.append(t.__str__())
    #         elif(caracter == '('):
    #             t = Token(TokenCategory.LEFT_PAREN.name, '(')
    #             listaTokens.append(t.__str__())
    #         elif(caracter == ')'):
    #             t = Token(TokenCategory.RIGHT_PAREN.name, ')')
    #             listaTokens.append(t.__str__())
    #         elif(caracter == '{'):
    #             t = Token(TokenCategory.LEFT_BRACE.name, '{')
    #             listaTokens.append(t.__str__())
    #         elif(caracter == '}'):
    #             t = Token(TokenCategory.RIGHT_BRACE.name, '}')
    #             listaTokens.append(t.__str__())
    #         elif(caracter == '>'):
    #             proximo = self.next_char(pos)
    #             if(proximo == '='):
    #                 t = Token(TokenCategory.OPERATOR_GE_NUMERIC.name, '>=')
    #                 listaTokens.append(t.__str__())
    #             else:
    #                 t = Token(TokenCategory.OPERATOR_GT_NUMERIC.name, '>')
    #                 listaTokens.append(t.__str__())
    #         elif(caracter == '<'):
    #             proximo = caracter[pos+1]
    #             if(proximo == '='):
    #                 t = Token(TokenCategory.OPERATOR_LE_NUMERIC.name, '<=')
    #                 listaTokens.append(t.__str__())
    #             else:
    #                 t = Token(TokenCategory.OPERATOR_LT_NUMERIC.name, '<')
    #                 listaTokens.append(t.__str__())
    #         else:
    #             t = -1
    #             # listaTokens.append(t)
    #         pos += 1
        # for a in listaTokens:
        #     print(a)
