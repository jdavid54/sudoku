import numpy as np
import copy

debug = False
#https://www.programiz.com/python-programming/shallow-deep-copy

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
    yield grid      # with yield we have to call : r = solve(); next(r)
    
def trans_grid(g):
    return list(list(int(i) for i in l) for l in g)

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

def solve_central():    
    global grid
    #print(np.matrix(grid))
    r = solve()
    # all solutions for central grid    
    a = []
    while True:
        try:
            grid = next(r)
            b = copy.deepcopy(grid)
            a.append(b)
            #input('stop')
        except:
            #break
            if debug : print('no more solutions')
            #print(a)
            break
    return a    

def fix_ul(central):
    global samourai
    ul = samourai[0]
    #central = samourai[2]
    for r in range(6,9):
        for c in range(6,9):
            ul[r][c] = central[r-6][c-6]
    samourai[0]= ul

def fix_ur(central):
    global samourai
    ur = samourai[1]
    #central = samourai[2]
    for r in range(6,9):
        for c in range(3):
            ur[r][c] = central[r-6][c+6]
    samourai[1]= ur

def fix_dl(central):
    global samourai
    dl = samourai[3]
    #central = samourai[2]
    for r in range(3):
        for c in range(6,9):
            dl[r][c] = central[r+6][c-6]
    samourai[3]= dl

def fix_dr(central):
    global samourai
    dr = samourai[4]
    #central = samourai[2]
    for r in range(3):
        for c in range(3):
            dr[r][c] = central[r+6][c+6]
    samourai[4]= dr

def five_grids():
    #print('All 5 grids :\n')
    global samourai
    #grid1, grid2, grid3, grid4, grid5 = samourai
    global grid
    for n,g in enumerate(samourai):
        print('grid',n+1)
        grid = g
        orig = g
        r = solve()
        s = next(r)
        print_solve(orig, s)
        samourai[n] = s

# beginning of program
#from grids import *
from samourai_101 import *
original =[trans_grid(grid1), trans_grid(grid2), trans_grid(grid3), trans_grid(grid4), trans_grid(grid5)]
samourai = copy.deepcopy(original)
grid = samourai[2]
num_solutions = 0
central_ok = []

a = solve_central()
'''
for k in range(len(a)):
    print(a[k])
'''

if debug : print('Solving 4 corner grids')
grids = ('Upper left', 'Upper right', 'Lower left', 'Lower right')
l = len(a)

for k in range(l):
    print('Testing with central',k)
    central = a[k]
    samourai = copy.deepcopy(original)
    g1, g2, g3, g4, g5 = samourai
    g3 = central
    fix_ul(central)
    fix_ur(central)
    fix_dl(central)
    fix_dr(central)
    print(np.matrix(central))
    if debug: 
        print('Grid reset with new central')
        print_samourai(g1, g2, central, g4, g5)

    for n, grid in enumerate((g1, g2, g4, g5)):
        solved = False
        if debug : print('Solving grid',grids[n])
        r = solve()
        if debug : print(np.matrix(grid))
        
        while not solved:
            try:
                next(r)
                print('Grid', grids[n], 'OK ...\n',np.matrix(grid))                
                solved = True
                if debug: input('next ?')
            except:
                print('Grid', grids[n], 'has no solutions ...')
                #print('no solution',k)
                break
        #if debug : input('stop')
        if not solved :
            print('Central',k,'not OK !')
            if k < l-1:
                print('Reset all grids for next central !\n')
            else:
                print('All central solutions tested !')
                print('Numbers of solutions :',num_solutions,central_ok)
            break
    if solved:
        print('Central',k,'OK !')
        num_solutions +=1
        central_ok.append(k)
        #break   # first solution only

        print('Samurai grid solved !')
        print_samourai(g1, g2, central, g4, g5)
        
        print('*****************************************')
        # all solutions ?
        #input('more?')