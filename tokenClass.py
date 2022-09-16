class Token:
    def __init__(self, tokenCategory, value):
        self.category = tokenCategory
        self.value = value
        # self.line = line
        # self.column = column

    def __str__(self):
        return '<' + self.category + ',' + self.value + '>'


# c = Token(TokenCategory.CADEIA.name, '1', '1', 'vcvc')
# print(c)
