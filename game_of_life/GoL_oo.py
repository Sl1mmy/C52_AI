import random

class GoL_engine:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0] * width, [0] * width]
        
    def resize(self, width, height):
        self.width = width
        self.height = height
        self.grid[:] = [[0] * width, [0] * width]
        #update graphics
        
    def populate():
        pass


    def tic(self):
        #grid_update = grid.copy()
        for x in range(self.width):
            for y in range(self.height):
                
                #calcule la somme des voisins (total)
                total = int()
                
                #conway's rules:
                if self.get_cell(x, y) == 1:
                    if 3 < total < 2:
                        self.set_cell(x, y, 0)
                else:
                    if total == 3:
                        self.set_cell(x, y, 1)
        
        self.grid[:] = grid_update[:]
        #update graphics
    
    def print(self):
        pass
    
    @property
    def cell(self, x : int, y : int):
        xr = self.grid[0][x]
        yr = self.grid[1][y]
        return [xr, yr]
    
    def set_cell(self, x, y, value):
        self.grid[x][y] = value
        
        
class GOLEngine:
    
    def __init__(self, width, height):
        self.__width = None
        self.__height = None
        self.__data = None
        self.__temp = None
        
        self.resize(width, height)
        
        
    def validate_size(self, size, context):
        if not isinstance(size, int):
            raise TypeError(f'{context} must be an integer value')
        SIZE_LIMIT = [3, 2500]
        if not ( SIZE_LIMIT[0] <= size <= SIZE_LIMIT[1]):
            raise ValueError(f'{context} must be an integer value')
    
    def resize(self, width, height):
        self.__validate_size(width, 'width')
        self.__validate_size(height, 'height')
        
        self.__width = width
        self.__height = height
        self.__world = []
        self.__temp = []
        
        for x in range(width):
            self.__world.append([])
            self.__temp.append([])
            for _ in range(height):
                #self.__world[x].append(random.randint(0, 1))
                self.__world[x].append(0)
                self.__temp[x].append(0)
        
    def randomize(self, percent=0.5):
        # for y in range(self.__height):
        #     for x in range(self.__width):
        #         if x != 0 and x != self.__width -1 and y != 0 and y != self.__height - 1:
        #             self.__world[x][y] = 1 if random.random() > percent else 0
                    
        for y in range(1, self.__height - 1):
            for x in range(1, self.__width - 1):
                self.__world[x][y] = int(random.random() > percent)
                
                
    def tic(self):
        for x in range(1, self.__width-1):
            for y in range(1, self.__hieght-1):
                neighbours = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i != 0 or j != 0:
                            neighbours += self.__world[x+i][y+i]
                if self.__world[x][y] == 0:
                    self.__temp[x][y] = int(neighbours == 3)
                else:
                    self.__temp[x][y] = int(neighbours in (2, 3))
                    
        # for y in range(self.__height):
        #     for x in range(self.__width):
        #         self.__world[x][y] = self.__temp[x][y]
        
        self.__world, self.__temp = self.__temp, self.__world
        
    
                
        
        
                
def main():
    gol = GOLEngine(12, 10)
                   
# def main():
#     gol = GoL_engine(50, 50)
    
#     gol.tic()
    
if __name__ == '__main__':
    main()