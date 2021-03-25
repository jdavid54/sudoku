import numpy as np

class Grid():
    rows = {}
    cols = {}
    zones = {}
    def __init__(self, grid):
        self.grid = grid
        for r in range(9):
            self.rows['row'+str(r+1)] = list(grid[r])
            self.cols['col'+str(r+1)] = list(grid.T[r])
        #zones
        for x in range(0,9,3):
            for y in range(0,9,3):  
                l = []
                for i in range(0,3):
                    for j in range(0,3):
                        l.append(grid[x+i][y+j])
                self.zones['zone'+str((3*x+y)//3+1)] = l
            
    def __repr__(self):
        g=''
        for r in range(9):
            g += ' '.join([str(elem) for elem in self.rows['row'+str(r+1)]])+'\n'
        return g
    
    def count_occurences(self):
        occurences = {}
        for n in range(1,10):
            occur = 0
            for i in range(9):
               occur += list(self.grid[i]).count(n)
            occurences[str(n)] = occur
        return occurences            
    
    def zone(self,x,y): # x,y in (1..9)
        print(x,y)
        x0 = ((x-1)//3)
        y0 = ((y-1)//3)
        return 'zone'+str((3*x0+y0)+1)
    
    def possible(self,x,y,n): # x,y in (1..9)
        x0 = ((x-1)//3)
        y0 = ((y-1)//3)
        #print(self.zone(x,y))
        if n in self.rows['row'+str(x)]: return False
        if n in self.cols['col'+str(y)]: return False        
        if n in self.zones['zone'+str((3*x0+y0)+1)]: return False
        return True
    
    def find_candidates(self,x,y): # x,y in (1..9)
        candidates = []
        for n in range(1,10):
            if self.possible(x,y,n):
                candidates.append(n)
        return ''.join(str(c) for c in candidates)
        #return candidates
    
    def all_candidates(self):
        candidates = []
        for x in range(1,10):
            r=[]
            for y in range(1,10):
                if self.grid[x-1][y-1] == 0:
                    print(self.find_candidates(x,y),end='\t')
                    r.append(self.find_candidates(x,y))
                else:
                    print(self.grid[x-1][y-1], end='\t')
                    r.append(self.grid[x-1][y-1])
            print()
            candidates.append(r)
        return candidates

grid = np.zeros((9,9), dtype='uint8')  
rows=['000004712',
      '008000640',
      '000007850',
      '310000097',
      '076000030',
      '500740000',
      '000401000',
      '050090004',
      '000806000']
for r in range(len(rows)):
    l=[]
    for i in rows[r]:
        l.append(int(i))
    #print(r,l)
    grid[r]=l

'''
grid[0]=[8,0,3,0,9,4,1,2,5]
grid[1]=[4,5,9,8,2,1,6,7,3]
grid[2]=[2,0,0,5,0,3,0,4,8]
grid[3]=[6,2,7,4,5,9,3,8,1]
grid[4]=[0,9,5,0,0,8,4,6,2]
grid[5]=[0,8,4,2,0,6,5,9,7]
grid[6]=[5,1,6,9,8,2,7,3,4]
grid[7]=[9,4,8,1,3,7,2,5,6]
grid[8]=[7,3,2,0,0,5,8,0,0]
'''
s = Grid(grid)

def test():
    zone = np.zeros((9,9), dtype='uint8') 
    print(grid)

    for x in range(0,9,3):
      for y in range(0,9,3):  
        x0 = (x//3)
        y0 = (y//3)
        l = []
        for i in range(0,3):
            for j in range(0,3):
                l.append(grid[x+i][y+j])
        print((3*x+y)//3,l)

print(s.count_occurences())
s.all_candidates()
