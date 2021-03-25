import numpy as np
from grids import *

def possible(y,x,n):
    global grid
    for i in range(0,9):
        #print(y,i,grid[y][i])
        if grid[y][i] == n:
            return False
    for i in range(0,9):
        if grid[i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == n:
                return False
    return True

def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if possible(y, x, n):
                        grid[y][x] = n
                        yield from solve()
                        grid[y][x] = 0
                return
    #print(np.matrix(grid))
    yield np.matrix(grid)
    #input('More ?')

# attention ne pas faire comme ci-dessous pour créer la grille
#row = [0,0,0,0,0,0,0,0,0]
#grid0 = [row]*9 # grid est composé de 9 fois le même élément

grid0=[[0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0]]

grid = grid0
print(np.matrix(grid))
print()
s = solve() # s is a generator
# use next to get the nex element in s
for k in range(3):
    print(next(s),'\n')
