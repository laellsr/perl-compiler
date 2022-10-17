import re

class Brackets:
    def __init__(self) -> None:
        self.round = 0
        self.square = 0
        self.curvy = 0
        
class Token:
    def __init__(self, lexeme):
        self.category = self.getTokenCategory(lexeme)
        self.value = lexeme
        self.line = 0
        self.column = 0
        self.error = 0
    
    def getTokenCategory(self, lexeme):
        for tkCategory in tkCategories:
            if re.fullmatch(tkCategories[tkCategory], lexeme) != None:
                return tkCategory
        return 'UNKNOW'

# necessário começar com as palavras reservadas
# ao contrário dará erro de unknow por causa da condicional no nextToken

tkCategories = {
    "RESERVED_IF": r'if',
    "RESERVED_ELSIF" : r'elsif',
    "RESERVED_ELSE" : r'else',
    "RESERVED_WHILE" : r'while',
    "RESERVED_PRINT" : r'print',
    "RESERVED_SAY" : r'say',
    "RESERVED_RETURN" : r'return',
    "RESERVED_SUBROUTINE" : r'sub',
    "LEFT_PAREN": r'\(',
    "RIGHT_PAREN": r'\)',
    "LEFT_BRACE": r'\{',
    "RIGHT_BRACE" : r'\}',
    "LEFT_BRACKETS": r'\[',
    "RIGHT_BRACKETS" : r'\]',
    "SEMICOLON": r';',
    "COMMENT_LINE": r'#.*',
    "FLOAT_NUMBER" : r"^[\+-]{0,1}[\d]+[\.][\d]+$",
    "INTEGER_NUMBER" : r"^[\+-]{0,1}[0-9]+",
    "STRING_PRINT" : r'\"[^\"]*\"',
    "STRING" : r'\'[^\']*\'',
    "ARRAY_OF_NUMBERS": r'\(([\+\-,. ]*\d+)+\)',
    "ARRAY_OF_STRINGS": r'^\s*\((\s*(("|\')([^\3]+|\\\3)\3|[\x7f-\xff][a-zA-Z0-9_\x7f-\xff])\s*,?)*\s*\)',
    "SUBROUTINE_IDENTIFIER" : r'^[a-zA-Z0-9_]{2,}',
    "SCALAR_IDENTIFIER": r'^[$][a-zA-Z0-9_]*',
    "VECTOR_IDENTIFIER": r'^[@][a-zA-Z0-9_]*',
    "COMMA": r'\,',
    "OPERATOR_LT_NUMERIC": r'<',
    "OPERATOR_GT_NUMERIC" : r'>',
    "OPERATOR_AND": r'&&',
    "OPERATOR_OR" : r'\|\|',
    "OPERATOR_DIV" : r'/',
    "OPERATOR_MUL" : r'\*',
    "OPERATOR_MOD" : r'\%',
    "OPERATOR_PLUS" : r'\+',
    "OPERATOR_MINUS": r'\-',
    "OPERATOR_GE_NUMERIC" : r'>=',
    "OPERATOR_LE_NUMERIC": r'<=',
    "OPERATOR_EQ_NUMERIC": r'==',
    "OPERATOR_NE_NUMERIC" : r'!=',
    "OPERATOR_ASSIGN": r'='
}

reservedWords = {
    "RESERVED_IF": r'if',
    "RESERVED_ELSIF" : r'elsif',
    "RESERVED_ELSE" : r'else',
    "RESERVED_WHILE" : r'while',
    "RESERVED_DEFAULT" : r'default',
    "RESERVED_ASYNC" : r'async',
    "RESERVED_PACKAGE" : r'package',
    "RESERVED_USE" : r'use',
    "RESERVED_PRINT" : r'print',
    "RESERVED_SAY" : r'say',
    "RESERVED_TRY" : r'try',
    "RESERVED_CATCH" : r'catch',
    "RESERVED_SWITCH" : r'switch',
    "RESERVED_CASE" : r'case',
    "RESERVED_RETURN" : r'return',
    "RESERVED_EXIT" : r'exit',
    "RESERVED_METHOD" : r'method',
    "RESERVED_SUBROUTINE" : r'sub',
}