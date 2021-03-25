import numpy as np

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
    m = np.matrix(grid)    
    yield m    
    #print(m)
    #input('More ?')
    
def trans_grid(g):
    r = [[0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0]]    
    for y in range(9):
        for x in range(9):
            r[y][x] = int(g[y][x])
    return r

from grids import *
grids = (grid1, grid2, grid3, grid4, grid5)
for grid in grids:
    print('Grille à résoudre :\n', np.matrix(grid))    
    s = solve()
    l = list(enumerate(s))     # soit list(s) soit next(s)
    for n,k in l:
        try:
            print(len(l),'solution(s):',n+1,'\n', k,'\n')
            #print(np.matrix(next(s)))
        except:
            pass
