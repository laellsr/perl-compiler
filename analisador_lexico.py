from tokenCategory import TokenCategory
from tokenClass import Token
# from lerArquivo import LerArquivo
from nextChar import NextChar


class AnalisadorLexico:
    def __init__(self, string):
        self.string = string

    def next_char(self, pos):
        if(pos == len(self.string)):
            return -1  # fim da string
        else:
            pos += 1
            return self.string[pos]

    def back(self, pos):
        if(pos == 0):
            return -1  # inicio da string
        else:
            pos -= 1
            return self.string[pos]

    def nextToken(self):
        caracterLido = self.string
        listaTokens = []
        pos = 0
        tamanho = len(self.string)
        while pos != tamanho:
            # print(caracter[pos])
            # print(self.next_char(pos))
            # if(self.back(pos) == -1):
            #     pass
            # else:
            #     print(self.back(pos))
            # break
            caracter = caracterLido[pos]
            print(caracter)
            if(caracter == ' ' or caracter == '\n'):
                pass
            if(caracter == ';'):
                t = Token(TokenCategory.SEMICOLON.name, ';')
                listaTokens.append(t.__str__())
            elif(caracter == '*'):
                t = Token(TokenCategory.OPERATOR_MUL.name, '*')
                listaTokens.append(t.__str__())
            elif(caracter == '%'):
                t = Token(TokenCategory.OPERATOR_MOD.name, '%')
                listaTokens.append(t.__str__())
            elif(caracter == '+'):
                t = Token(TokenCategory.OPERATOR_PLUS.name, '+')
                listaTokens.append(t.__str__())
            elif(caracter == '-'):
                t = Token(TokenCategory.OPERATOR_MINUS.name, '-')
                listaTokens.append(t.__str__())
            elif(caracter == '!'):
                t = Token(TokenCategory.OPERATOR_NOT.name, '!')
                listaTokens.append(t.__str__())
            elif(caracter == '/'):
                t = Token(TokenCategory.OPERATOR_DIV.name, '/')
                listaTokens.append(t.__str__())
            elif(caracter == '='):
                t = Token(TokenCategory.OPERATOR_ASSIGN.name, '=')
                listaTokens.append(t.__str__())
            elif(caracter == '('):
                t = Token(TokenCategory.LEFT_PAREN.name, '(')
                listaTokens.append(t.__str__())
            elif(caracter == ')'):
                t = Token(TokenCategory.RIGHT_PAREN.name, ')')
                listaTokens.append(t.__str__())
            elif(caracter == '{'):
                t = Token(TokenCategory.LEFT_BRACE.name, '{')
                listaTokens.append(t.__str__())
            elif(caracter == '}'):
                t = Token(TokenCategory.RIGHT_BRACE.name, '}')
                listaTokens.append(t.__str__())
            elif(caracter == '>'):
                proximo = self.next_char(pos)
                if(proximo == '='):
                    t = Token(TokenCategory.OPERATOR_GE_NUMERIC.name, '>=')
                    listaTokens.append(t.__str__())
                else:
                    t = Token(TokenCategory.OPERATOR_GT_NUMERIC.name, '>')
                    listaTokens.append(t.__str__())
            elif(caracter == '<'):
                proximo = caracter[pos+1]
                if(proximo == '='):
                    t = Token(TokenCategory.OPERATOR_LE_NUMERIC.name, '<=')
                    listaTokens.append(t.__str__())
                else:
                    t = Token(TokenCategory.OPERATOR_LT_NUMERIC.name, '<')
                    listaTokens.append(t.__str__())
            else:
                t = -1
                # listaTokens.append(t)
            pos += 1
        for a in listaTokens:
            print(a)
