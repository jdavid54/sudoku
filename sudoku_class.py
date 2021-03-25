
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

#from samourai_grid import *
from samourai_101 import *
row1 = Row()
print(row1, row1.row)
row2 = Row('000111101')
print(row2, row2.row)

grid = Grid(grid1)
print('Sudoku grid :\n')
print(grid)
#print(grid.grid[1].row)   

# samurai_grid = [grid1, grid2, grid3, grid4, grid5]
samurai = Samurai(samurai_grid)
print('\nSamurai grid :\n')
print(samurai)
