import copy
#https://www.programiz.com/python-programming/shallow-deep-copy

class Row:
    def __init__(self, r='000000000'):
        self.row = list(r)
        
    def __repr__(self):   #called by str() and print()
        return ''.join(c for c in self.row)
        
class Grid:
    def __init__(self, list):
        self.grid = [Row(list[0]), Row(list[1]), Row(list[2]),
                     Row(list[3]), Row(list[4]), Row(list[5]),
                     Row(list[6]), Row(list[7]), Row(list[8])]
    def __repr__(self):
        return '\n'.join(str(r) for r in self.grid)
    
class Samurai:
    def __init__(self, list):
        self.samurai = [Grid(list[0]), Grid(list[1]), Grid(list[2]),
                     Grid(list[3]), Grid(list[4])]
    
    def __repr__(self):
        #print('samurai')
        all = ''
        for r in range(6):   #6 last rows of g1,g2 with 3 spaces in between
            for c in range(9):
                #print(self.samurai)
                all += self.samurai[0].grid[r].row[c]
            all += '   '
            for c in range(9):
                all += self.samurai[1].grid[r].row[c]
            all += '\n'
        
        for r in range(6,9):   #3 imbricated rows : 3 last of g1,g2 and 3 first of g3
            for c in range(6):  # 6 first colums of g1
                all += self.samurai[0].grid[r].row[c]
            for c in range(9):
                all += self.samurai[2].grid[r-6].row[c]  #all 9 columns of g3          
            for c in range(3,9):  # 6 last colums of g2
                all += self.samurai[1].grid[r].row[c]
            all += '\n'
        for r in range(3,6):  # 3 middle rows of g3
            all += '      '
            for c in range(9):
                all += self.samurai[2].grid[r].row[c]
            all += '\n'
        for r in range(3):   #3 imbricated rows : 3 first of g1,g2 and 3 last of g3
            for c in range(6):  # 6 first colums of g4
                all += self.samurai[3].grid[r].row[c]
            for c in range(9):
                all += self.samurai[2].grid[r+6].row[c]    #all 9 columns of g3        
            for c in range(3,9):   # 6 last colums of g5
                all += self.samurai[4].grid[r].row[c]
            all += '\n'
        for r in range(3,9):  #6 last rows of g4,g5 with 3 spaces in between
            for c in range(9):
                all += self.samurai[3].grid[r].row[c]
            all += '   '
            for c in range(9):
                all += self.samurai[4].grid[r].row[c]
            all += '\n'        
        return all

debug = False
#from samourai_grid import *
from samourai_101 import *
row1 = Row()
if debug : print(row1, row1.row)

grid = Grid(grid1)
print('i grid :\n')
print(grid)
#print(grid.grid[1].row)   

# samurai_grid = [grid1, grid2, grid3, grid4, grid5]
samurai = Samurai(samurai_grid)
print('\nSamurai grid :\n')
print(samurai)

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

def trans_grid(g):
    return list(list(int(i) for i in l.row) for l in g.grid)



def solve():
    global grid
    #global c
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if possible(y, x, n):
                        grid[y][x] = n
                        yield from solve()
                        #solve()
                        grid[y][x] = 0
                return
    
    #b = copy.deepcopy(grid)
    #c.append(b)
    #print(np.matrix(grid),'\n')
    #print(b)
    #print()
    #print(b, len(c))
    #input('More ?')
    yield grid      # with yield we have to call : r = solve(); next(r)
    
def copy_grid(grid, corner):
    if corner=='ul': corner=(0,0)
    if corner=='ur': corner=(0,1)
    if corner=='ll': corner=(1,0)
    if corner=='lr': corner=(1,1)
    g = [[0,0,0],
         [0,0,0],
         [0,0,0]]
    for r in range(3):
        for k in range(3):
            g[r][k] = grid[corner[0]*6+r][corner[1]*6+k]
    return g        

def paste_grid(dest, src, corner):
    if corner=='ul': corner=(0,0)
    if corner=='ur': corner=(0,1)
    if corner=='ll': corner=(1,0)
    if corner=='lr': corner=(1,1)
    
    for r in range(3):
        for k in range(3):
            dest[corner[0]*6+r][corner[1]*6+k] = src[r][k]
    return dest   


#print(samurai.samurai[0])
#print()

#print(samurai.samurai[2])

samurai0 = trans_grid(samurai.samurai[0])  # upper left grid
samurai1 = trans_grid(samurai.samurai[1])  # upper right grid
samurai2 = trans_grid(samurai.samurai[2])  # central grid
samurai3 = trans_grid(samurai.samurai[3])  # lower left grid
samurai4 = trans_grid(samurai.samurai[4])  # lower left grid
# central grid
grid = samurai2
# solving central grid
all = []
r = solve()
#print(c)

#loop
#solved1, solved2, solved3, solved4 = False, False, False, False
solved = False
name = {'ul': 'lower right grid',
        'ur': 'lower left grid',
        'll': 'upper right grid',
        'lr': 'upper left grid'}
while not solved:
    # get next r
    next(r)
    b = copy.deepcopy(grid)
    all.append(b)
    print(np.matrix(grid))
    #input('more')
    # copy corners of central grid
    ul = copy_grid(grid, 'ul')
    ur = copy_grid(grid, 'ur')
    ll = copy_grid(grid, 'll')
    lr = copy_grid(grid, 'lr')

    # save intermediate central grid
    save = grid
    # solve each corner grid with central result
    for g,c,t in ((samurai0, ul, 'lr'), (samurai1, ur, 'll'), (samurai3, ll, 'ur'), (samurai4, lr, 'ul')):
        # update corner grid 
        grid = paste_grid(g, c, t)
        s = solve()
        try :
            next(s)
            if debug :
                print('solution for', name[t])
                print(np.matrix(g))
            solved = True
        except:
            if debug :
                print('no solution ',t)
            solved = False
            break
    # restore central grid
    grid = save

def str_list(grid):
    return list((''.join(str(i)) for i in l) for l in grid)

grid0 = str_list(samurai0)
grid1 = str_list(samurai1)
grid2 = str_list(samurai2)
grid3 = str_list(samurai3)
grid4 = str_list(samurai4)
samurai_grid = [grid0, grid1, grid2, grid3, grid4]
samurai_solved = Samurai(samurai_grid)
print('\nSamurai grid solved :\n')
print(samurai_solved)

#print(all, len(all))