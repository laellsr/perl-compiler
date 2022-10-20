class Parser:
    def __init__(self, token):
        self.token = token
        self.tk = self.token[0]
        self.cont = 0
        
    def nextToken(self):
        self.cont += 1
        if self.cont < len(self.token):
            self.tk = self.token[self.cont]


    def VAR(self):
        if self.tk.category != 'INTEGER_NUMBER' and self.tk.category != 'FLOAT_NUMBER' and self.tk.category != 'SCALAR_IDENTIFIER' :
            print('ERRO! ' + self.tk.category + ' NÃO É IDENTIFICADOR')
            return 0 
    def OPERATOR(self):
        if self.tk.category != 'OPERATOR_PLUS' and self.tk.category != 'OPERATOR_MINUS' and self.tk.category != 'OPERATOR_MUL' and self.tk.category != 'OPERATOR_DIV' and self.tk.category != 'OPERATOR_AND' and self.tk.category != 'OPERATOR_OR' and self.tk.category != 'OPERATOR_MOD' and self.tk.category != 'OPERATOR_LT_NUMERIC' and self.tk.category != 'OPERATOR_GT_NUMERIC' and self.tk.category != 'OPERATOR_GE_NUMERIC' and self.tk.category != 'OPERATOR_LE_NUMERIC' and self.tk.category != 'OPERATOR_EQ_NUMERIC' and self.tk.category != 'OPERATOR_NE_NUMERIC' :
            print('ERRO! O valor ' + self.tk.value + ' não é um OPERADOR!')

     


    def Expr_Op_1(self):
        print(self.cont)
        self.nextToken()
        print(self.cont)
        if self.tk.category != 'SEMICOLON':
            self.OPERATOR()
            self.nextToken()
            self.VAR()
            self.Expr_Op_1()

    def Expr_Op(self): #reconhece uma expressão com operador
        self.VAR()
        self.Expr_Op_1()
        print('VEIO ALGUM PRINT ANTES? NÃO? COMPILAÇÃO BEM SUCEDIDA')
    
    def Op_Declaration(self): #reconhece uma expressão com operador
        if self.tk.category != 'OPERATOR_PLUS' and self.tk.category != 'OPERATOR_MINUS' and self.tk.category != 'OPERATOR_MUL' and self.tk.category != 'OPERATOR_DIV' and self.tk.category != 'OPERATOR_MOD':
              print('ERRO! O valor ' + self.tk.value + ' não é um OPERADOR!')
        else:
            self.nextToken()             
            if self.VAR() != 0:
                self.nextToken()             
                if self.tk.category == 'SEMICOLON':
                    pass
                else:
                    self.Op_Declaration()
                    


    def Scalar_Declaration(self): 
        self.nextToken()
        if self.tk.category != 'OPERATOR_ASSIGN':
            print("ERRO! FALTA UM SÍMBOLO DE ATRIBUIÇÃO")  
        else:
            self.nextToken()
            if self.VAR() != 0: #se não for falso
                self.nextToken()
                if self.tk.category == 'SEMICOLON':
                    pass
                else:
                    self.Op_Declaration()



    def Start(self):
        if self.tk.category == 'SCALAR_IDENTIFIER':
            self.Scalar_Declaration()






