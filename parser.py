from operator import ne
import sys
class Parser:
    def __init__(self, token):
        self.token = token
        self.tk = self.token[0]
        self.cont = -1
        self.left_brace = 0
        self.RED = "\033[1;31m"
        self.RESET = "\033[0;0m"
        self.BLUE = "\033[1;34m"
        self.GREEN = "\033[0;32m"
    # Identifica o proximo token
    def nextToken(self):
        self.cont += 1
        # print(f'cont: {self.cont}')
        if self.cont < len(self.token):
            self.tk = self.token[self.cont]
        else:
            if self.left_brace != 0:
                print(self.RED + 'ERRO! A quantidade de chaves está errada.'  + self.RESET)
            print(self.GREEN + 'Compilation successful!' + self.RESET)
            self.tk.category = ''
            
    # Identificadores ou Numeros
    def Atom_Expr(self):
        if self.tk.category != 'INTEGER_NUMBER' and self.tk.category != 'FLOAT_NUMBER' and self.tk.category != 'SCALAR_IDENTIFIER':
            before_error = self.token[self.cont -1]
            raise NameError(before_error.value + self.BLUE +  " <\n" + self.RESET + self.RED + 'ERRO! ' + self.tk.category + ' NÃO É IDENTIFICADOR' + self.RESET)
            # try:
            #     sys.exit()
            # except SystemExit:
            #     print('ERRO! ' + self.tk.category + ' NÃO É IDENTIFICADOR')
                
    # Operadores para um bloco de condição            
    def OPERATOR(self):
        if self.tk.category != 'OPERATOR_PLUS' and self.tk.category != 'OPERATOR_MINUS' and self.tk.category != 'OPERATOR_MUL' and self.tk.category != 'OPERATOR_DIV' and self.tk.category != 'OPERATOR_AND' and self.tk.category != 'OPERATOR_OR' and self.tk.category != 'OPERATOR_MOD' and self.tk.category != 'OPERATOR_LT_NUMERIC' and self.tk.category != 'OPERATOR_GT_NUMERIC' and self.tk.category != 'OPERATOR_GE_NUMERIC' and self.tk.category != 'OPERATOR_LE_NUMERIC' and self.tk.category != 'OPERATOR_EQ_NUMERIC' and self.tk.category != 'OPERATOR_NE_NUMERIC' :
            before_error = self.token[self.cont -1]
            raise NameError(before_error.value +self.BLUE +  " <\n" + self.RESET + self.RED + 'ERRO! O valor ' + self.tk.value + ' não é um símbolo válido!' + self.RESET)
            # try:
            #     sys.exit()
            # except SystemExit:
            #     print('ERRO! O valor ' + self.tk.value + ' não é um OPERADOR!')
        
    # Count Braces
    def Brace_Verification(self):
        if self.left_brace > 0:
            self.left_brace -= 1
            self.File_Item()
        else:
            raise NameError(self.RED +'ERRO! A quantidade de chaves está errada.' + self.RESET)
            # try:
            #     sys.exit()
            # except SystemExit:
            #     print('ERRO! A quantidade de chaves está errada.')
                
    # BNF Vars ----------------------------------------------------------------------------------------------
    
    def Op_Declaration(self): #reconhece uma expressão com operador
        if self.tk.category != 'OPERATOR_PLUS' and self.tk.category != 'OPERATOR_MINUS' and self.tk.category != 'OPERATOR_MUL' and self.tk.category != 'OPERATOR_DIV' and self.tk.category != 'OPERATOR_MOD':
            before_error = self.token[self.cont -1]
            raise NameError( before_error.value + self.BLUE +  " <\n" + self.RESET + self.RED + 'ERRO! É esperado um ; ou um operador' + self.RESET)   
            # try:
            #     sys.exit()
            # except SystemExit:
            #     print('ERRO! O valor ' + self.tk.value + ' não é um OPERADOR!')
        self.nextToken()             
        self.Atom_Expr()
        self.nextToken()             
        if self.tk.category == 'SEMICOLON':
            self.File_Item()            
        else:
            self.Op_Declaration()
                    
    def Operator_Assign(self):
        self.nextToken()
        if self.tk.category != 'OPERATOR_ASSIGN':
            before_error = self.token[self.cont -1]
            raise NameError( before_error.value + self.BLUE +  " <\n" + self.RESET + self.RED +"ERRO! Era esperado um símbolo de atribuição." + self.RESET)
            # try:
            #     sys.exit()
            # except SystemExit:
            #     print("ERRO! Era esperado um símbolo de atribuição.")
                
    def Values(self):
        if self.tk.category == 'STRING':
            self.nextToken()
            if self.tk.category != 'SEMICOLON':
                before_error = self.token[self.cont -1]
                raise NameError( before_error.value + self.BLUE +  " <\n" + self.RESET + self.RED + "ERRO! Era esperado um ';'"  ) 
                # try:
                #     sys.exit()
                # except SystemExit:
                #     print("ERRO! Era esperado um ';'")
            self.File_Item() 
        else:
            self.Atom_Expr()
            self.nextToken()
            if self.tk.category == 'SEMICOLON':
                self.File_Item()
            else:
                self.Op_Declaration()
            
    def Scalar_Declaration(self): 
        self.Operator_Assign()
        self.nextToken()
        self.Values()
        
    def Array_Verification(self):
        if self.tk.category != 'ARRAY_OF_NUMBERS' and self.tk.category != 'ARRAY_OF_STRINGS':
            before_error = self.token[self.cont -1]
            raise NameError(before_error.value + self.BLUE +  self.BLUE +  " <\n" + self.RESET + self.RESET + self.RED +"ERRO! Era esperado uma declaração de Array"+ self.RESET)
            # try:
            #     sys.exit()
            # except SystemExit:
            #     print("ERRO! Era esperado uma declaração de Array")
        self.nextToken() 
        if self.tk.category != 'SEMICOLON':
            before_error = self.token[self.cont -1]
            raise NameError(before_error.value + self.BLUE +  " <\n" + self.RESET + self.RED + "ERRO! Era esperado um ';'" + self.RESET)
            # try:
            #     sys.exit()
            # except SystemExit:
            #     print("ERRO! Era esperado um ';'")
                    
    def Vector_Declaration(self):
        self.Operator_Assign()
        self.nextToken() 
        self.Array_Verification() 
        self.File_Item()
        
    # BNF print ------------------------------------------------------------------------------------------------
    
    def Content_Print(self):
        self.nextToken()
        if self.tk.category != 'STRING_PRINT':
            before_error = self.token[self.cont -1]
            raise NameError(before_error.value + self.BLUE +  " <\n" + self.RESET+ self.RED + "ERRO! Era esperado umA ASPAS DUPLAS" + self.RESET)
            # try:
            #     sys.exit()
            # except SystemExit:
            #     print("ERRO! Era esperado umA ASPAS DUPLAS")
            
    def Print(self):
        self.Content_Print()
        self.nextToken()
        if self.tk.category == 'SEMICOLON':
            self.File_Item()            
        else:
            before_error = self.token[self.cont -1]
            raise NameError( before_error.value + self.BLUE +  " <\n" + self.RESET + self.RED +  "ERRO! Era esperado um ;"+ self.RESET)
            # try:
            #     sys.exit()
            # except SystemExit:
            #     print("ERRO! Era esperado uma semicolon")
        
    # BNF Say ------------------------------------------------------------------------------------------------------------------------
    
    def Say(self):
        self.Print()
    
    # BNF If ------------------------------------------------------------------------------------------------------------------------
    
    def Expr_Op_1(self):
        self.nextToken()
        if self.tk.category != 'RIGHT_PAREN':
            self.OPERATOR()
            self.nextToken()
            self.Atom_Expr()
            self.Expr_Op_1()
    
    def Expr(self): #reconhece uma expressão com operador
        self.Atom_Expr()
        self.nextToken()
        self.OPERATOR()
        self.nextToken()
        self.Atom_Expr()
        self.Expr_Op_1()
    
    def Condition_Expr(self):
        self.nextToken()
        if self.tk.category != 'LEFT_PAREN':
            before_error = self.token[self.cont -1]
            raise NameError(before_error.value + self.BLUE +  " <\n" + self.RESET + self.RED +"ERRO! Era esperado uma abre parênteses"+ self.RESET)
            # try:
            #     sys.exit()
            # except SystemExit:
            #     print("ERRO! Era esperado uma abre parênteses")
        self.nextToken()
        self.Expr()
        
    def Block(self):
        if self.tk.category != 'LEFT_BRACE':
            before_error = self.token[self.cont -1]
            raise NameError(before_error.value + self.BLUE +  " <\n" + self.RESET + self.RED + "ERRO! Era esperado um '{'" + self.RESET)
        self.left_brace += 1
        self.File_Item()
        
    def Block_Sub(self):
        if self.tk.category != 'LEFT_BRACE':
            before_error = self.token[self.cont -1]
            raise NameError(before_error.value + self.BLUE +  " <\n" + self.RESET + self.RED + "ERRO! Era esperado um '{'" + self.RESET)
        self.left_brace += 1
        self.File_Item_Sub()
    
    def Conditional_Block(self):
        self.Condition_Expr()
        self.nextToken()
        self.Block()
    
    def If(self):
        self.Conditional_Block()
        
    # BNF While -----------------------------------------------------------------------------------------------
    
    def While(self):
        self.Conditional_Block()
        
    # BNF Sub -------------------------------------------------------------------------------------------------
    
    # def Subroutine(self):
    
    def Sub_Names(self):
        self.nextToken()
        if self.tk.category != 'SUBROUTINE_IDENTIFIER':
            before_error = self.token[self.cont -1]
            raise NameError(before_error.value + " <\n" + self.RED +"ERRO! Era esperado um nome para a subrotina"+ self.RESET)
        
    def Comma(self):
        if self.tk.category != 'COMMA':
            before_error = self.token[self.cont -1]
            raise NameError(before_error.value + self.BLUE +  " <\n" + self.RESET + self.RED +"ERRO! Era esperado uma ,"+ self.RESET)
        
    def Scalar_Identifier_Error(self):
        if self.tk.category != 'SCALAR_IDENTIFIER':
            before_error = self.token[self.cont -1]
            raise NameError(before_error.value + self.BLUE +  " <\n" + self.RESET  + self.RED +"ERRO! Era esperado um identificador"+ self.RESET)
            
    def End_Parameters(self):
        self.nextToken()
        if self.tk.category != 'RIGHT_PAREN':
            self.Comma()
            self.nextToken()
            self.Scalar_Identifier_Error()
            self.End_Parameters()
        
    def Sub_Parameters(self):
        self.nextToken()
        if self.tk.category != 'LEFT_PAREN':
            before_error = self.token[self.cont -1]
            raise NameError(before_error.value + self.BLUE +  " <\n" + self.RESET  + self.RED +"ERRO! Era esperado um ("+ self.RESET)
        self.nextToken()
        if self.tk.category != 'RIGHT_PAREN':
            self.Scalar_Identifier_Error()
            self.End_Parameters()
            
    def Semicolon(self):
        self.nextToken()
        if self.tk.category != 'SEMICOLON':
            self.Block_Sub()
        else:
            self.File_Item()
        
    def Subroutine(self):
        self.Sub_Names()
        self.Sub_Parameters()
        self.Semicolon()
        
    # return
    
    def Return(self):
        self.nextToken()
        if self.tk.category != 'SEMICOLON':
            self.Values()
        else:
            self.File_Item()
        
    def Error_Return(self):
        before_error = self.token[self.cont -1]
        raise NameError(before_error.value + self.BLUE +  " <\n" + self.RESET  + self.RED +f"ERRO! return não é reconhecido fora da função." + self.RESET)
        

    # possiveis grafos que chamaremos --------------------------------------------------------------------------
    def File_Item(self):
        self.nextToken()
        print(self.tk.category)
        match self.tk.category:
            case 'UNKNOW':
                raise NameError(self.RED+ f"ERRO! {self.tk.value} não é reconhecido." + self.RESET)
            case 'RIGHT_BRACE':
                self.Brace_Verification()
            case 'SCALAR_IDENTIFIER':
                self.Scalar_Declaration()
            case 'VECTOR_IDENTIFIER':
                self.Vector_Declaration()
            case 'RESERVED_PRINT':  
                self.Print()
            case 'RESERVED_SAY':
                self.Say()
            case 'RESERVED_IF':
                self.If()
            case 'RESERVED_WHILE':
                self.While()
            case 'RESERVED_SUBROUTINE':
                self.Subroutine()
            case 'RESERVED_RETURN':
                self.Error_Return()
            case 'COMMENT_LINE':
                self.File_Item()
            case default:
                return
            
    def File_Item_Sub(self):
        self.nextToken()
        match self.tk.category:
            case 'UNKNOW':
                raise NameError(self.RED+ f"ERRO! {self.tk.value} não é reconhecido." + self.RESET)
            case 'RIGHT_BRACE':
                self.Brace_Verification()
            case 'SCALAR_IDENTIFIER':
                self.Scalar_Declaration()
            case 'VECTOR_IDENTIFIER':
                self.Vector_Declaration()
            case 'RESERVED_PRINT':  
                self.Print()
            case 'RESERVED_SAY':
                self.Say()
            case 'RESERVED_IF':
                self.If()
            case 'RESERVED_WHILE':
                self.While()
            case 'RESERVED_SUBROUTINE':
                self.Subroutine()
            case 'RESERVED_RETURN':
                self.Return()
            case 'COMMENT_LINE':
                self.File_Item_Sub()
            case default:
                return
                






