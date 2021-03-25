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
    #input('More ?')
    yield grid      # with yield we have to call : r = solve(); next(r)
    
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

def print_solve(g1,g2):
    for r in range(9):
        print(g1[r],'\t',g2[r])
    print()

        
def print_samourai(g1,g2,g3,g4,g5):
    for r in range(6):   #6 last rows of g1,g2 with 3 spaces in between
        for c in range(9):
            print(g1[r][c],end='')
        print('   ',end='')
        for c in range(9):
            print(g2[r][c],end='')
        print()
    for r in range(6,9):   #3 imbricated rows : 3 last of g1,g2 and 3 first of g3
        for c in range(6):  # 6 first colums of g1
            print(g1[r][c],end='')
        for c in range(9):
            print(g3[r-6][c],end='')  #all 9 columns of g3          
        for c in range(3,9):  # 6 last colums of g2
            print(g2[r][c],end='')
        print()
    for r in range(3,6):  # 3 middle rows of g3
        print('      ',end='')
        for c in range(9):
            print(g3[r][c],end='')            
        print()
    for r in range(3):   #3 imbricated rows : 3 first of g1,g2 and 3 last of g3
        for c in range(6):  # 6 first colums of g4
            print(g4[r][c],end='')
        for c in range(9):
            print(g3[r+6][c],end='')    #all 9 columns of g3        
        for c in range(3,9):   # 6 last colums of g5
            print(g5[r][c],end='')
        print()
    for r in range(3,9):  #6 last rows of g4,g5 with 3 spaces in between
        for c in range(9):
            print(g4[r][c],end='')
        print('   ',end='')
        for c in range(9):
            print(g5[r][c],end='')
        print()
    
def five_grids():
    #print('All 5 grids :\n')
    samourai = []
    global grid
    for n,g in enumerate((grid1, grid2, grid3, grid4, grid5)):
        print('grid',n+1)
        grid = trans_grid(g)
        orig = trans_grid(g)
        #print(np.matrix(orig))
        r = solve()
        s = next(r)
        samourai.append(s)
        print_solve(orig, s)
    return samourai

#multi grids
grid1 =["000000670",
        "024009805",
        "100000020",
        "070000000",
        "010007003",
        "000800046",
        "006400900",
        "000002008",
        "005016000"]

grid2 =["100000000",
        "009000700",
        "504001206",
        "902400008",
        "800100570",
        "005006002",
        "000600080",
        "000283400",
        "050040000"]

grid3 =["900080000",
        "008500000",
        "000040050",
        "020090004",
        "000007069",
        "000005102",
        "700132000",
        "304059000",
        "690000000"]

grid4 =["001640700",
        "750000304",
        "030100690",
        "840015006",
        "000090000",
        "000002050",
        "005000000",
        "000360009",
        "020000040"]

grid5 =["000005001",
        "000040030",
        "000890400",
        "000500800",
        "002004010",
        "000300954",
        "090007005",
        "000600090",
        "068000320"]

from samourai_101 import *

print('Solving samourai 5-grid')
samourai = five_grids()

print_samourai(samourai[0],samourai[1],samourai[2],samourai[3],samourai[4])

