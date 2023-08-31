
class Human:
    
    #def  __new__() #constructeur
    
    def __init__(self, name): #initializateur
        self.name = name
        self.age = 0
    
    def tic(self):
        self.age += 1

numain = Human('Roger')