
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
        
        
def main():
    gol = GoL_engine(50, 50)
    
    gol.tic()
    
if __name__ == '__main__':
    main()