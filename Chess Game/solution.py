class Piece:
    def __init__(self, sort, color, position):
        self.sort= sort
        self.color= color
        self.position= position
        
        
        
class Board():
    def __init__(self,sort,position,color):
        self.kingDic={}
        self.kingDic.update({position:(sort,color)})
      

    def add(self, piece):
        if ((piece.sort,piece.color) in self.kingDic.values()) or (piece.position in self.kingDic.keys()):
            print("invalid query")
            
        else:
                self.kingDic.update({piece.position:(piece.sort,piece.color)})

    def remove(self, position): 
        if (position not in self.kingDic.keys()) or (('K','black')not in self.kingDic.values() 
                                                     or ('P','white')not in self.kingDic.values()) :
            print("invalid query")
        else:
              self.kingDic.pop(position)
        

    def move(self, piece, position2):
        if (piece.position in self.kingDic.keys() and (piece.sort,piece.color)in self.kingDic.values()) and (position2 not in 
       self.kingDic.keys()):   
             self.kingDic.update({position2:(piece.sort,piece.color)})
        if (position2 in self.kingDic.keys() and piece.color!= self.kingDic[position2[-1]])and self.kingDic[position2[0]]!='k':
            self.kingDic.pop(position2)
            self.kingDic.update({position2:(piece.sort,piece.color)})
            
        
        else:
            print("invalid query")
            
            

    def is_mate(self, color):
        pass
    