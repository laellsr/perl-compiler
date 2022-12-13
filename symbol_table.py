class symb:
    def __init__(self):
        self.hash = dict()

    def add(self, id, type, value, scopo):
        self.hash[id] = (type, value, scopo)
        
    def busca(self, id):
          pos = self.hash[id]
          if self.hash.get(id): 
               return pos[0]
           
    def buscaValor(self, id):
          pos = self.hash[id]
          if self.hash.get(id): 
               return pos[1]

