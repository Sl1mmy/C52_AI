#1. setup grid
#2. spawn pixels
#3. update()
#3. animate (update x fois secondes)
import random

#pixel states
ALIVE = 1
DEAD = 0
state = [1, 0]


def grid_populate():
    return 
    
def update(grid_height, grid_width, grid):
    grid_update = grid.copy()
    for x in grid_width:
        for y in grid_height:
            
            #calcule la somme des voisins (total)
            total = int((grid[x, (y-1)%))
            
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
    grid_height = 50
    grid_width = 50
    
    #
    grid = [[list(range(0, grid_height))], [list(range(0, grid_width))]]
    
    #update()
    
    #populate grid
    grid = grid_populate(grid_size)
    
    
if __name__ == '__main__':
    main()