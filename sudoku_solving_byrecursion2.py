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
    
def solve2():  # no using yield method
    #global grid
    trans_grid(grid)
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if possible(y, x, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    print(np.matrix(grid))
    input('More ?')

gridA = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,0,0,0,7,9]]

# need trans_grid()
gridB = ["084560000",
        "090007000",
        "503000900",
        "800600040",
        "200050009",
        "010003005",
        "005000201",
        "000200030",
        "000041570"]
'''
def transgrid(g):
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

def trans_grid(g):
    r = []
    for l in g:
        r.append(list(int(i) for i in l))
    return r
'''
def trans_grid(g):
    return list(list(int(i) for i in l) for l in g)

def test():
    global grid
    grid = gridA
    print(np.matrix(grid))
    solve()

    grid=trans_grid(gridB)
    print(np.matrix(grid))
    solve()

def print_solve(g1,g2):
    for r in range(9):
        print(g1[r],'\t',g2[r])
    print()


def five_grids():
    global grid
    for n,g in enumerate((grid8, grid9, grid10, grid11, grid12)):
        print('grid',n+1)
        grid = trans_grid(g)
        orig = trans_grid(g)
        #print(np.matrix(orig))
        r = solve()
        print_solve(orig, next(r))
        try :
            print(np.matrix(next(r)))
        except:
            print('no more solution\n')

board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
grid = board
'''
print('Test1')

print(np.matrix(grid))
r = solve()
print(np.matrix(next(r)))
try :
    print(np.matrix(next(r)))
except:
    print('no more solution\n')

# grille à résoudre
grid = ["900002008",
        "010004070",
        "000007000",
        "000003215",
        "000000000",
        "632400000",
        "000100000",
        "070300040",
        "800900002"]
print('Test2 with transgrid')
grid = trans_grid(grid)
print(np.matrix(grid))
r = solve()
print('Solution:')
print(np.matrix(next(r)))
try :
    print(np.matrix(next(r)))
except:
    print('no more solution')
'''
print('Test 5 grids')
five_grids()