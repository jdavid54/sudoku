class Row:
    def __init__(self, r='000000000'):
        self.row = r
        self.list = list(r) 
        
#row1 = Row()
#print(row1.row, row1.list)

class Grid:
    def __init__(self, list):
        self.grid = [Row(list[0]), Row(list[1]), Row(list[2]),
                     Row(list[3]), Row(list[4]), Row(list[5]),
                     Row(list[6]), Row(list[7]), Row(list[8])]
    def __repr__(self):
        all = ''
        for r in self.grid:
            all += r.row + '\n'
        return all
    
class Samurai:
    def __init__(self, list):
        self.samurai = [Grid(list[0]), Grid(list[1]), Grid(list[2]),
                     Grid(list[3]), Grid(list[4])]
    '''
    def __repr__(self):
        all = ''
        for r in range(6):   #6 last rows of g1,g2 with 3 spaces in between
            for c in range(9):
                print(self.samurai)
                all += list(self.samurai[0])[r][c]
            all += '   '
            for c in range(9):
                all += self.samurai[1][r][c]
            all += '\n'
        for r in range(6,9):   #3 imbricated rows : 3 last of g1,g2 and 3 first of g3
            for c in range(6):  # 6 first colums of g1
                all += self.samurai[0][r][c]
            for c in range(9):
                all += self.samurai[2][r-6][c]  #all 9 columns of g3          
            for c in range(3,9):  # 6 last colums of g2
                all += self.samurai[1][r][c]
            all += '\n'
        for r in range(3,6):  # 3 middle rows of g3
            all += '      '
            for c in range(9):
                all += self.samurai[2][r][c]
            all += '\n'
        for r in range(3):   #3 imbricated rows : 3 first of g1,g2 and 3 last of g3
            for c in range(6):  # 6 first colums of g4
                all += self.samurai[3][r][c]
            for c in range(9):
                all += self.samurai[2][r+6][c]    #all 9 columns of g3        
            for c in range(3,9):   # 6 last colums of g5
                all += self.samurai[4][r][c]
            all += '\n'
        for r in range(3,9):  #6 last rows of g4,g5 with 3 spaces in between
            for c in range(9):
                all += self.samurai[3][r][c]
            all += '   '
            for c in range(9):
                all += self.samurai[4][r][c]
            all += '\n'
        return all
    '''

grid1 =["000000670",
        "024009805",
        "100000020",
        "070000000",
        "010007003",
        "000800046",
        "006400900",
        "000002008",
        "005016000"]

grid = Grid(grid1)
print(grid)

print(grid.grid[1].row)

from samourai_grid import *
samurai = Samurai(samurai_grid)
print(samurai)