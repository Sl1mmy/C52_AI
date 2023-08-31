#1. setup grid
#2. spawn pixels
#3. update()
#3. animate (update x fois secondes)
import random

#pixel valeur (couleur)
ALIVE = 255
DEAD = 0
state = [255, 0]


def grid_populate():
    return 
    
def update(grid_size, grid):
    grid_update = grid.copy()
    for x in grid_size:
        for y in grid_size:
            
            #calcule la somme des voisins (total)
            total = 0
            
            #conway's rules:
            if grid[x][y] == ALIVE:
                if 3 < total < 2:
                    grid_update[x][y] = DEAD
            else:
                if total == 3:
                    grid_update[x][y] = ALIVE
    
    #update
    grid[:] = grid_update[:]
    #update graphics
        
    
def main():
    grid_size = 50
    
    #
    grid = [[list(range(0, grid_size))], [list(range(0, grid_size))]]
    
    #update()
    
    #populate grid
    grid = grid_populate(grid_size)
    
    
if __name__ == '__main__':
    main()