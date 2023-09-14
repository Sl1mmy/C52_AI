

class Human:
    
    def __init__(self, name):
        self.name = name
        self.age = 0
        
    def tic(self):
        self.age += 1
        
    def print(self):
        print(f"Un '{type(self).__name__}' nommé {self.name} a {self.age:02} an{'s' if self.age > 1 else ''}")


humain = Human('Roger')

humain.tic()
humain.print()

humain.tic()
humain.print()

print(humain.__dict__)



# ----------------------------------

# convention
# variable_membre -> publique
# _variable_membre -> protégé
# __variable_membre -> privée  *** name mangling

class Human:
    
    def __init__(self, name):
        self.name = name
        self.__age = 0
        
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Le nom doit être une chaîne de caractères')
        if len(value) < 2:
            raise ValueError("Le nom doit être d'au moins 2 caractères")
        self.__name = value
    
    @property
    def age(self):
        return self.__age
    
    def tic(self):
        self.__age += 1


u = Human(123)
u.name = 'Gustave'
print(u.name)

pass