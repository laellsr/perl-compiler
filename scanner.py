import re


class scanner:
    # Recebendo o
    def __init__(self, content):
        self.content = content


palavras_reservadas = {"RESERVED_ELSIF": "if", "RESERVED_ELSIF": "elsif",
                       "RESERVED_ELSE": "else",
                       "RESERVED_WHILE": "while",
                       "RESERVED_DEFAULT": "default",
                       "RESERVED_ASYNC": "async",
                       "RESERVED_PACKAGE": "package",
                       "RESERVED_USE": "use",
                       "RESERVED_PRINT": "print",
                       "RESERVED_PRINTF": "printf",
                       "RESERVED_SAY": "say",
                       "RESERVED_TRY": "try",
                       "RESERVED_CATCH": "catch",
                       "RESERVED_SWITCH": "switch",
                       "RESERVED_CASE": "case",
                       "RESERVED_RETURN": "return",
                       "RESERVED_EXIT": "exit",
                       "RESERVED_METHOD": "method",
                       "RESERVED_FUNC": "func"}

t_OPERATOR_AND = r'&&'
t_OPERATOR_MINUS_MINUS = r'--'
t_ignore = r'\t '
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ASSIGN = r'='
t_NE = r'<>'
t_LT = r'<'
t_LTE = r'<='
t_OPERATOR_EQ_NUMERIC = r'=='
t_OPERATOR_NE_NUMERIC = r'!='
t_GT = r'>'
t_GTE = r'>='
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COMMA = r','
t_SEMMICOLOM = r';'
t_DOT = r'\.'
t_LEFT_BRACE = r'\{'
t_RIGHT_BRACE = r'\}'
t_STRING_SPECIAL_NEWLINE = r'\n'
t_STRING_SPECIAL_RETURN = r'\r'
t_STRING_SPECIAL_BACKSPACE = r'\b'

estado = 0
pos = 0

# Funções necessárias com regex


def isDigit(c):
    return re.match("[0-9]", c)


def isChar(c):
    return re.match("[a-zA-Z]", c)


def isID(c):
    return re.search(r'^[$][a-zA-Z0-9_]*', c)


def isKeyWord(c):
    return re.search(r'^[a-z][a-z]*', c)


def nexChar(content, pos):
    pos += 1
    return content[pos]


def back(content, pos):
    pos -= 1
    return content[pos]
