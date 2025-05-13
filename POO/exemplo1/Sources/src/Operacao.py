class Operacao:
    def __init__(self,intx=None,inty=None):
        self.__intx = intx
        self.__inty = inty
 
 
           
    def get_Intx(self):
        return self.__intx
   
    def set_Intx(self, intx):
        self.__intx = intx
 
    def get_Inty(self):
        return self.__inty
   
    def set_Inty(self, inty):
        self.__inty = inty
 
    def somar(self):
        return self.__intx + self.__inty
   