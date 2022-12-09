from operator import ne
from symbol_table import * 
import sys
class Parser:
    def __init__(self, token):
        self.token = token
        self.tk = self.token[0]
        self.cont = -1
        self.left_brace = 0
        self.sub_ativa = 0
        self.table = symb()
        self.id_current = ''
        self.RED = "\033[1;31m"
        self.RESET = "\033[0;0m"
        self.BLUE = "\033[1;34m"
        self.GREEN = "\033[0;32m"
        self.erro = 0
        self.name_sub = ''
    # Identifica o proximo token
    def nextToken(self):
        self.cont += 1
        # print(f'cont: {self.cont}')
        if self.cont < len(self.token):
            self.tk = self.token[self.cont]
        else:
            if self.left_brace != 0:
                self.erro = 1
                print(self.RED + 'ERRO! A quantidade de chaves está errada.'  + self.RESET)
            if self.erro == 0:
                if self.tk.category == 'SEMICOLON' or self.tk.category == 'RIGHT_BRACE':
                    print(self.GREEN + 'Compilation successful!' + self.RESET)
            self.tk.category = ''
            
    # Identificadores ou Numeros
    def Atom_Expr(self):
        if self.tk.category != 'INTEGER_NUMBER' and self.tk.category != 'FLOAT_NUMBER' and self.tk.category != 'SCALAR_IDENTIFIER':
            self.Sub_Names()
        else:
            self.nextToken()
                
    # Operadores para um bloco de condição            
    def OPERATOR(self):
        if self.tk.category == 'OPERATOR_ASSIGN':
            before_error = self.token[self.cont -1]
            self.erro = 1
            print(before_error.value +self.BLUE +  " <\n" + self.RESET + self.RED + 'ERRO! O valor ' + self.tk.value + ' não é um símbolo válido para o local!' + self.RESET)
            self.nextToken()
        elif self.tk.category != 'OPERATOR_PLUS' and self.tk.category != 'OPERATOR_MINUS' and self.tk.category != 'OPERATOR_MUL' and self.tk.category != 'OPERATOR_DIV' and self.tk.category != 'OPERATOR_AND' and self.tk.category != 'OPERATOR_OR' and self.tk.category != 'OPERATOR_MOD' and self.tk.category != 'OPERATOR_LT_NUMERIC' and self.tk.category != 'OPERATOR_GT_NUMERIC' and self.tk.category != 'OPERATOR_GE_NUMERIC' and self.tk.category != 'OPERATOR_LE_NUMERIC' and self.tk.category != 'OPERATOR_EQ_NUMERIC' and self.tk.category != 'OPERATOR_NE_NUMERIC' :
            before_error = self.token[self.cont -1]
            self.erro = 1
            print(before_error.value +self.BLUE +  " <\n" + self.RESET + self.RED + 'ERRO! O valor ' + self.tk.value + ' não é um símbolo válido para o local!' + self.RESET)
        else:
            self.nextToken()
            
    # Count Braces
    def Brace_Verification(self):
        if self.left_brace == 1:
            if self.sub_ativa == 1:
                self.sub_ativa = 0
        if self.left_brace > 0:
            self.left_brace -= 1
            self.File_Item()
        else:
            self.erro = 1
            print(self.RED +'ERRO! A quantidade de chaves está errada.' + self.RESET)
                
    # BNF Vars ----------------------------------------------------------------------------------------------
    
    def Op_Declaration(self): #reconhece uma expressão com operador
        if self.tk.category != 'OPERATOR_PLUS' and self.tk.category != 'OPERATOR_MINUS' and self.tk.category != 'OPERATOR_MUL' and self.tk.category != 'OPERATOR_DIV' and self.tk.category != 'OPERATOR_MOD':
            before_error = self.token[self.cont -1]
            self.erro = 1
            print( before_error.value + self.BLUE +  " <\n" + self.RESET + self.RED + 'ERRO! É esperado um ; ou um operador.' + self.RESET) 
            self.cont -= 1
            self.File_Item() 
        else: 
            self.nextToken()             
            self.Atom_Expr()             
            if self.tk.category == 'SEMICOLON':
                self.File_Item()            
            else:
                self.Op_Declaration()
                    
    def Operator_Assign(self):
        self.nextToken()
        if self.tk.category != 'OPERATOR_ASSIGN':
            before_error = self.token[self.cont -1]
            self.erro = 1
            print( before_error.value + self.BLUE +  " <\n" + self.RESET + self.RED +"ERRO! Era esperado um símbolo de atribuição." + self.RESET)
        else:
            self.nextToken()
                
    def Values(self):
        if self.tk.category == 'STRING':
            self.nextToken()
            if self.tk.category != 'SEMICOLON':
                before_error = self.token[self.cont -1]
                self.erro = 1
                print( before_error.value + self.BLUE +  " <\n" + self.RESET + self.RED + "ERRO! Era esperado um ';'"  ) 
            self.File_Item() 
        else:
            self.Atom_Expr()
            if self.tk.category == 'SEMICOLON':
                self.File_Item()
            else:
                self.Op_Declaration()
            
    def Scalar_Declaration(self): 
        self.Operator_Assign()
        if self.table.hash.get(self.tk.value) != None:
            #if(self.sub_ativa == 1):
            #    self.table.add(self.id_current, self.name_sub)
            #else:
                self.table.add(self.id_current,self.table.hash[self.tk.value])
        else:
            #if(self.sub_ativa == 1):
            #    self.table.add(self.id_current, self.name_sub)
            #else:
                self.table.add(self.id_current, self.tk.category)
        if self.tk.category != '':
            self.Values()
        else:
            before_error = self.token[self.cont -1]
            self.erro = 1
            print(before_error.value + self.BLUE +  self.BLUE +  " <\n" + self.RESET + self.RESET + self.RED +"ERRO! era esperado um identificador ou um nome de função"+ self.RESET)
        
        
    def Array_Verification(self):
        if self.tk.category != 'ARRAY_OF_NUMBERS' and self.tk.category != 'ARRAY_OF_STRINGS':
            before_error = self.token[self.cont -1]
            self.erro = 1
            print(before_error.value + self.BLUE +  self.BLUE +  " <\n" + self.RESET + self.RESET + self.RED +"ERRO na declaração de Array"+ self.RESET)
        else:
            self.nextToken() 
            if self.tk.category != 'SEMICOLON':
                before_error = self.token[self.cont -1]
                self.erro = 1
                print(before_error.value + self.BLUE +  " <\n" + self.RESET + self.RED + "ERRO! Era esperado um ';'" + self.RESET)
                    
    def Vector_Declaration(self):
        self.Operator_Assign()
        if self.table.hash.get(self.tk.value) != None:
            self.table.add(self.id_current,self.table.hash[self.tk.value])
        else:
            self.table.add(self.id_current, self.tk.category)
        if self.tk.category != '':
            self.Array_Verification() 
            self.File_Item()
        
    # BNF print ------------------------------------------------------------------------------------------------
    
    def Content_Print(self):
        self.nextToken()
        if self.tk.category != 'STRING_PRINT':
            before_error = self.token[self.cont -1]
            self.erro = 1
            print(before_error.value + self.BLUE +  " <\n" + self.RESET+ self.RED + "ERRO! Era esperado uma ASPAS DUPLAS" + self.RESET)
        else: 
            self.nextToken()
            
    def Print(self):
        self.Content_Print()
        if self.tk.category != '':
            if self.tk.category == 'SEMICOLON':
                self.File_Item()
        else:
            before_error = self.token[self.cont -1]
            self.erro = 1
            print( before_error.value + self.BLUE +  " <\n" + self.RESET + self.RED +  "ERRO! Era esperado um ;"+ self.RESET)
        
    # BNF Say ------------------------------------------------------------------------------------------------------------------------
    
    def Say(self):
        self.Print()
    
    # BNF If ------------------------------------------------------------------------------------------------------------------------
    
    def Expr_Op_1(self):
        if self.tk.category != 'RIGHT_PAREN':
            if self.tk.category == 'LEFT_BRACE':
                before_error = self.token[self.cont -1]
                self.erro = 1
                print(before_error.value + self.BLUE +  " <\n" + self.RESET + self.RED +"ERRO! Era esperado um )"+ self.RESET)
            else:
                self.OPERATOR()
                self.Atom_Expr()
                self.Expr_Op_1()
        else:
            self.nextToken()
    
    def Expr(self): #reconhece um id
        self.Atom_Expr()
        self.Expr_Op_1()
    
    def Condition_Expr(self):
        self.nextToken()
        if self.tk.category != 'LEFT_PAREN':
            before_error = self.token[self.cont -1]
            self.erro = 1
            print(before_error.value + self.BLUE +  " <\n" + self.RESET + self.RED +"ERRO! Era esperado um ("+ self.RESET)
        else:
            self.nextToken()
        self.Expr()
        
    def Block(self):
        if self.tk.category != 'LEFT_BRACE':
            before_error = self.token[self.cont -1]
            self.erro = 1
            print(before_error.value + self.BLUE +  " <\n" + self.RESET + self.RED + "ERRO! Era esperado um '{'" + self.RESET)
            self.cont -= 1
        self.left_brace += 1
        self.File_Item()
        
    def Block_Sub(self):
        if self.left_brace != 0:
            before_error = self.token[self.cont -1]
            self.erro = 1
            print(before_error.value + self.BLUE +  " <\n" + self.RESET + self.RED + "ERRO! Não pode criar subroutina dentro de uma função" + self.RESET)
        if self.tk.category != 'LEFT_BRACE':
            before_error = self.token[self.cont -1]
            self.erro = 1
            print(before_error.value + self.BLUE +  " <\n" + self.RESET + self.RED + "ERRO! Era esperado um '{'" + self.RESET)
            self.cont -= 1
        self.left_brace += 1
        self.sub_ativa = 1
        self.File_Item()
    
    def Conditional_Block(self):
        self.Condition_Expr()
        self.Block()
    
    def If(self):
        self.Conditional_Block()
        
    # BNF While -----------------------------------------------------------------------------------------------
    
    def While(self):
        self.Conditional_Block()
        
    # BNF Sub -------------------------------------------------------------------------------------------------
    
    # def Subroutine(self):
    
    def Sub_Names(self):
        if self.tk.category != 'SUBROUTINE_IDENTIFIER':
            before_error = self.token[self.cont -1]
            self.erro = 1
            print(before_error.value + self.BLUE + " <\n" + self.RESET + self.RED +"ERRO! Era esperado um identificador ou um nome para a subrotina"+ self.RESET)
            self.cont -= 1
        self.Sub_Parameters()
            
    def Sub_Names2(self):
        if self.tk.category != 'SUBROUTINE_IDENTIFIER':
            before_error = self.token[self.cont -1]
            self.erro = 1
            print(before_error.value + self.BLUE + " <\n" + self.RESET + self.RED +"ERRO! Era esperado um identificador ou um nome para a subrotina"+ self.RESET)
            self.cont -= 1
        else:
            self.name_sub = self.tk.value
        
    def Comma(self):
        if self.tk.category != 'COMMA':
            before_error = self.token[self.cont -1]
            self.erro = 1
            print(before_error.value + self.BLUE +  " <\n" + self.RESET + self.RED +"ERRO! Era esperado uma ,"+ self.RESET)
        else:
            self.nextToken()
            
        
    def Scalar_Identifier_Error(self):
        if self.tk.category != 'SCALAR_IDENTIFIER':
            before_error = self.token[self.cont -1]
            self.erro = 1
            print(before_error.value + self.BLUE +  " <\n" + self.RESET  + self.RED +"ERRO! Era esperado um identificador ou um )"+ self.RESET)
            self.cont -= 1
        else:
            self.End_Parameters()
            
    def Scalar_Identifier_Error2(self):
        if self.tk.category != 'SCALAR_IDENTIFIER':
            before_error = self.token[self.cont -1]
            self.erro = 1
            print(before_error.value + self.BLUE +  " <\n" + self.RESET  + self.RED +"ERRO! Era esperado um identificador ou um )"+ self.RESET)
            self.cont -= 1
        self.End_Parameters()
            
    def End_Parameters(self):
        self.nextToken()
        if self.tk.category != 'RIGHT_PAREN':
            self.Comma()
            self.Scalar_Identifier_Error2()
        
    def Sub_Parameters(self):
        self.nextToken()
        if self.tk.category != 'LEFT_PAREN':
            before_error = self.token[self.cont -1]
            self.erro = 1
            print(before_error.value + self.BLUE +  " <\n" + self.RESET  + self.RED +"ERRO! Era esperado um ("+ self.RESET)
        else:
            self.nextToken()
        if self.tk.category != 'RIGHT_PAREN':
            self.Scalar_Identifier_Error()
        self.nextToken()
        
    def Sub_Parameters2(self):
        self.nextToken()
        if self.tk.category != 'LEFT_PAREN':
            before_error = self.token[self.cont -1]
            self.erro = 1
            print(before_error.value + self.BLUE +  " <\n" + self.RESET  + self.RED +"ERRO! Era esperado um ("+ self.RESET)
        else:
            self.nextToken()
        if self.tk.category != 'RIGHT_PAREN':
            self.Scalar_Identifier_Error2()
        self.nextToken()
            
    def Semicolon(self):
        if self.tk.category != 'SEMICOLON':
            self.Block_Sub()
        else:
            self.File_Item()
        
    def Subroutine(self):
        if self.table.hash.get(self.tk.value) != None:
            self.table.add(self.id_current,self.table.hash[self.tk.value])
        else:
            self.table.add(self.id_current, self.tk.category)
        self.Sub_Names2()
        self.Sub_Parameters2()
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
        self.erro = 1
        print(before_error.value + self.BLUE +  " <\n" + self.RESET  + self.RED +f"ERRO! return não é reconhecido fora da função." + self.RESET)
        
    def Print_Symbol_Table(self):
        if self.erro == 0:
            print(self.BLUE + "Tabela de Símbolos:\n" + self.RESET)
            print(self.RED + "  ID      " + self.RESET + "|"+ self.RED + "      TYPE      " + self.RESET + "|"+ self.RED + "      VALUE      " + self.RESET + "|"+ self.RED + "      SCOPE" + self.RESET)
            for key, category in self.table.hash.items():
                if(category == 'FLOAT_NUMBER' or category == 'INT_NUMBER' or category == 'ARRAY_OF_NUMBERS'):
                    print(f"{key}" + self.RED + " -> " + self.RESET + f"{category}" + self.RED + " -> " + self.RESET + "0" + self.RED + " -> " + self.RESET + "GLOBAL")
                else:
                    print(f"{key}" + self.RED + " -> " + self.RESET + f"{category}" + self.RED + " -> " + self.RESET + "null" + self.RED + " -> " + self.RESET + "GLOBAL")
                print('-----------------------------------------------------------')

    # possiveis grafos que chamaremos --------------------------------------------------------------------------
    def File_Item(self):
        self.nextToken()
        match self.tk.category:
            case 'UNKNOW':
                self.erro = 1
                print(self.RED + "ERRO! não é reconhecido." + self.RESET)
            case 'RIGHT_BRACE':
                self.Brace_Verification()
            case 'SCALAR_IDENTIFIER':
                self.id_current = self.tk.value
                self.Scalar_Declaration()
            case 'VECTOR_IDENTIFIER':
                self.id_current = self.tk.value
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
                self.nextToken()
                self.id_current = self.tk.value
                self.Subroutine()
            case 'RESERVED_RETURN':
                if self.sub_ativa == 1:
                    self.Return()
                else:
                    self.Error_Return()
            case 'COMMENT_LINE':
                self.File_Item()
            case '':
                pass
            case default:
                before_error = self.token[self.cont -1]
                self.erro = 1
                print(before_error.value + self.BLUE +  " <\n" + self.RESET + self.RED + "ERRO! não é um reconhecimento válido." + self.RESET)
