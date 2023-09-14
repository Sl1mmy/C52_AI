import random


class GOLEngine:
    
    def __init__(self, width, height):
        self.__width = None
        self.__height = None
        self.__world = None
        self.__temp = None
        
        self.resize(width, height)
        
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        self.resize(value, self.__height)
    
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.resize(self.__width, value)      
        
    def get_cell_value(self, x, y):
        # no input validation for performance consideration
        return self.__world[x][y]
        
    def set_cell_value(self, x, y, value):
        # no input validation for performance consideration
        self.__world[x][y] = value      
    
    def __validate_size(self, size, context):
        if not isinstance(size, int):
            raise TypeError(f'{context} must be an integer value')
        SIZE_LIMIT = (3, 2500)
        if not( SIZE_LIMIT[0] <= size <= SIZE_LIMIT[1]):
            raise ValueError(f'{context} must be between {SIZE_LIMIT[0]} and {SIZE_LIMIT[1]}')
    
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
                # self.__world[x].append(random.randint(0, 1))
                self.__world[x].append(0)
                self.__temp[x].append(0)
                
    def randomize(self, percent=0.5):
        # for y in range(self.__height):
        #     for x in range(self.__width):
        #         if x != 0 and x != self.__width - 1 and y != 0 and y != self.__height - 1:
        #             self.__world[x][y] = 1 if random.random() > percent else 0    
        for y in range(1, self.__height - 1):
            for x in range(1, self.__width - 1):
                self.__world[x][y] = int(random.random() > percent)

    def tic(self):
        for x in range(1, self.__width-1):
            for y in range(1, self.__height-1):
                neighbours = 0
                for i in range(-1,2):
                    for j in range(-1,2):
                        if i != 0 or j != 0:
                            # neighbours += 1 if world[x+i][y+j] == 1 else 0
                            neighbours += self.__world[x+i][y+j]
                if self.__world[x][y] == 0: # mort
                    # self.__temp[x][y] = 1 if neighbours == 3 else 0
                    self.__temp[x][y] = int(neighbours == 3)
                else: # vivant
                    # temp[x][y] = 1 if neighbours == 2 or neighbours == 3 else 0
                    # self.__temp[x][y] = 1 if neighbours in (2, 3) else 0
                    self.__temp[x][y] = int(neighbours in (2, 3))
                    
        # for y in range(self.__height):
        #     for x in range(self.__width):
        #         self.__world[x][y] = self.__temp[x][y]                    
        self.__world, self.__temp = self.__temp, self.__world
        
    def print(self):
        for y in range(self.__height):
            for x in range(self.__width):
                print(self.__world[x][y], end='')
            print()        

def main():
    gol = GOLEngine(12, 10)
    
if __name__ == '__main__':
    main()    

