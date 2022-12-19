class symb:
    def __init__(self):
        self.hash = dict()

    def add(self, id, type, value, scopo):
        self.hash[id] = (type, value, scopo)
        
    def add2(self, id, type, value, scopo, quantPar):
        self.hash[id] = (type, value, scopo, quantPar)
        
    def add3(self, id, type, value, scopo, quantPar, PosIni, ListPara):
        self.hash[id] = (type, value, scopo, quantPar, PosIni, ListPara)
        
    def add4(self, id, type, value, scopo, quantPar, PosIni, ListPara, PosFin):
        self.hash[id] = (type, value, scopo, quantPar, PosIni, ListPara, PosFin)
        
    def add_PosFuncIni(self, id, posIni):
        pos = self.hash[id]
        pos[5] = posIni
        
    def busca(self, id):
          pos = self.hash[id]
          if self.hash.get(id): 
               return pos[0]
           
    def buscaValor(self, id):
          pos = self.hash[id]
          if self.hash.get(id): 
               return pos[1]
           
    def buscaScope(self, id):
          pos = self.hash[id]
          if self.hash.get(id): 
               return pos[2]
           
    def buscaQuantPar(self, id):
          pos = self.hash[id]
          if self.hash.get(id): 
               return pos[3]
           
    def buscaPosIni(self, id):
          pos = self.hash[id]
          if self.hash.get(id): 
               return pos[4]
           
    def buscaListPara(self, id):
          pos = self.hash[id]
          if self.hash.get(id): 
               return pos[5]
           
    def buscaPosFin(self, id):
          pos = self.hash[id]
          if self.hash.get(id): 
            if len(pos) >= 7:
                return pos[6]
            else:
                return -1
           
    def imprimir(self, id):
          pos = self.hash[id]
          if self.hash.get(id): 
               print(pos)

