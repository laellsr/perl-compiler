from operator import le
import re
from palavraReconhecida import PalavraReconhecida
from tokenClass import Token
from tokenCategory import TokenCategory


class IsToken:
    def __init__(self, strg):
        self.strg = strg

    def EOF(self, pos_inicial):
        if(pos_inicial == len(self.strg)):
            token = Token(TokenCategory.FIM.name, '')
            return token
        else:
            return False

    # retorna o Token dela e a posição ate terminar a palavra, caso não ache, retorne posição inicial
    def isVar(self, posInicial):
        string = self.strg
        lexema = ""
        lexema += string[posInicial]
        print(f"Lexema inicial {lexema}")
        pos = posInicial
        while(True):
            if(re.fullmatch(r'^[$][a-zA-Z0-9_]*', lexema) != None):
                pos += 1
                if(self.EOF(pos) == False):
                    print(f"A posição agora é: {pos}")
                    # ando na minha string
                    lexema += string[pos]
                    print(f"O lexema é: {lexema}")
                else:
                    lexema = lexema[:-1]
                    # Setando o Token
                    token = Token(TokenCategory.VAR.name, lexema)
                    # Retorno um objeto com as informações do Token reconhecido e a posição que o nextToken deve continuar lendo
                    return PalavraReconhecida(token, pos)
            else:
                # se lexema não saiu do lugar, é pq não reconheceu nem o primeiro lexema
                if(lexema == string[posInicial]):
                    print('não é var')
                    return posInicial
                else:
                    # Vou tirar o último lexema que não foi reconhecido
                    lexema = lexema[:-1]
                    # Setando o Token
                    token = Token(TokenCategory.VAR.name, lexema)
                    # Retorno um objeto com as informações do Token reconhecido e a posição que o nextToken deve continuar lendo
                    return PalavraReconhecida(token, pos)

    def isVector(self, posInicial):
        string = self.strg
        lexema = ""
        lexema += string[posInicial]
        print(f"Lexema inicial no vetor{lexema}")
        pos = posInicial
        while(True):
            if(re.fullmatch(r'^[@][a-zA-Z0-9_]*', lexema) != None):
                pos += 1
                if(self.EOF(pos) == False):
                    print(f"A posição agora é: {pos}")
                    # ando na minha string
                    lexema += string[pos]
                    print(f"O lexema é: {lexema}")
                else:
                    lexema = lexema[:-1]
                    # Setando o Token
                    token = Token(
                        TokenCategory.SIGIL_VECTOR.name, lexema)
                    # Retorno um objeto com as informações do Token reconhecido e a posição que o nextToken deve continuar lendo
                    return PalavraReconhecida(token, pos)
            else:
                # se lexema não saiu do lugar, é pq não reconheceu nem o primeiro lexema
                if(lexema == string[posInicial]):
                    print('não é vetor')
                    return posInicial
                else:
                    # Vou tirar o último lexema que não foi reconhecido
                    lexema = lexema[:-1]
                    # Setando o Token
                    token = Token(
                        TokenCategory.SIGIL_VECTOR.name, lexema)
                    # Retorno um objeto com as informações do Token reconhecido e a posição que o nextToken deve continuar lendo
                    return PalavraReconhecida(token, pos)

    def isOpAri(self, posInicial):
        string = self.strg
        print(f'a posição é {posInicial}')
        print(f'entrou aqui com lexema {string[posInicial]}')
        lexema = ""
        lexema += string[posInicial]
        pos = posInicial
        if(lexema == '*'):
            t = Token(TokenCategory.OPERATOR_MUL.name, lexema)
            return PalavraReconhecida(t, pos+1)
        elif(lexema == '%'):
            t = Token(TokenCategory.OPERATOR_MOD.name, lexema)
            return PalavraReconhecida(t, pos+1)
        elif(lexema == '+'):
            if(string[pos+1] == '+'):
                lexema += string[pos+1]
                t = Token(TokenCategory.OPERATOR_PLUS_PLUS.name, lexema)
                return PalavraReconhecida(t, pos+2)
            else:
                t = Token(TokenCategory.OPERATOR_PLUS.name, lexema)
                return PalavraReconhecida(t, pos+1)
        elif(lexema == '-'):
            if(string[pos+1] == '-'):
                lexema += string[pos+1]
                t = Token(TokenCategory.OPERATOR_MINUS_MINUS.name, lexema)
                return PalavraReconhecida(t, pos+2)
            else:
                t = Token(TokenCategory.OPERATOR_MINUS.name, lexema)
                return PalavraReconhecida(t, pos+1)
        elif(lexema == '!'):
            t = Token(TokenCategory.OPERATOR_NOT.name, lexema)
            return PalavraReconhecida(t, pos+1)
        elif(lexema == '/'):
            t = Token(TokenCategory.OPERATOR_DIV.name, lexema)
            return PalavraReconhecida(t, pos+1)
        elif(lexema == '='):
            print(lexema)
            if(string[pos+1] == '='):
                print(lexema)
                lexema += string[pos+1]
                t = Token(TokenCategory.OPERATOR_EQ_NUMERIC.name, lexema)
                return PalavraReconhecida(t, pos+2)
            else:
                t = Token(TokenCategory.OPERATOR_ASSIGN.name, lexema)
                return PalavraReconhecida(t, pos+1)
        else:
            return posInicial
    # def isNumReal(self, posInicial):

    def isNumReal(self, posInicial):
        string = self.strg
        lexema = ""
        lexema += string[posInicial]
        print(f"Lexema inicial {lexema}")
        pos = posInicial
        while(True):
            if re.fullmatch(r'^\d+(.\d+)$', lexema) != None:
                pos += 1
                if(self.EOF(pos) == False):
                    print(f"A posição agora é: {pos}")
                    # ando na minha string
                    lexema += string[pos]
                    print(f"O lexema é: {lexema}")
                else:
                    lexema = lexema[:-1]
                    # Setando o Token
                    token = Token(TokenCategory.NUM_REAL.name, lexema)
                    # Retorno um objeto com as informações do Token reconhecido e a posição que o nextToken deve continuar lendo
                    return PalavraReconhecida(token, pos)
            else:
                # se lexema não saiu do lugar, é pq não reconheceu nem o primeiro lexema
                if(lexema == string[posInicial]):
                    print('não é var')
                    return posInicial
                else:
                    # Vou tirar o último lexema que não foi reconhecido
                    lexema = lexema[:-1]
                    # Setando o Token
                    token = Token(TokenCategory.NUM_REAL.name, lexema)
                    # Retorno um objeto com as informações do Token reconhecido e a posição que o nextToken deve continuar lendo
                    return PalavraReconhecida(token, pos)

    def isNumInt(self, posInicial):
        string = self.strg
        lexema = ""
        lexema += string[posInicial]
        print(f"Lexema inicial {lexema}")
        pos = posInicial
        while(True):
            print(pos)
            if(lexema[pos] == '.'):
                t = self.isNumReal(posInicial)
                if(t != posInicial):
                    return t
            if re.fullmatch(r'[0-9]*', lexema) != None:
                pos += 1
                if(self.EOF(pos) == False):
                    print(f"A posição agora é: {pos}")
                    # ando na minha string
                    lexema += string[pos]
                    print(f"O lexema é: {lexema}")
                else:
                    lexema = lexema[:-1]
                    # Setando o Token
                    token = Token(TokenCategory.NUM_INT.name, lexema)
                    # Retorno um objeto com as informações do Token reconhecido e a posição que o nextToken deve continuar lendo
                    return PalavraReconhecida(token, pos)
            else:
                # se lexema não saiu do lugar, é pq não reconheceu nem o primeiro lexema
                if(lexema == string[posInicial]):
                    print('não é var')
                    return posInicial
                else:
                    # Vou tirar o último lexema que não foi reconhecido
                    lexema = lexema[:-1]
                    # Setando o Token
                    token = Token(TokenCategory.NUM_INT.name, lexema)
                    # Retorno um objeto com as informações do Token reconhecido e a posição que o nextToken deve continuar lendo
                    return PalavraReconhecida(token, pos)
