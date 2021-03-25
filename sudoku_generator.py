import numpy as np

class Sudoku(object): 
    '''
    int mat[]; 
    int N; // number of columns/rows. 
    int SRN; // square root of N 
    int K; // No. Of missing digits
    '''
    #Constructor 
    #Sudoku(int N, int K) 
    def __init__(self,N,K):
        self.N = N; 
        self.K = K; 

        # Compute square root of N 
        SRNd = np.sqrt(N) 
        self.SRN = int(SRNd)
        self.mat = np.array([[0]*N]*N)
        
    def fillValues(self) :
        SRN = self.SRN
        # Fill the diagonal of SRN x SRN matrices 
        self.fillDiagonal() 
        print(self.mat)
        # Fill remaining blocks 
        self.fillRemaining(0, SRN) 
        print(self.mat)
        # Remove Randomly K digits to make game 
        self.removeKDigits()
        return self.mat
        
    # Fill the diagonal SRN number of SRN x SRN matrices 
    def fillDiagonal(self):
        N = self.N
        SRN = self.SRN
        for i in range(0, N, SRN):       #(int i = 0; i<N; i=i+SRN) 
            # for diagonal box, start coordinates->i==j 
            self.fillBox(i, i) 

    # Returns false if given 3 x 3 block contains num. 
    def unUsedInBox(self, rowStart, colStart, num):
        SRN = self.SRN
        for i in range(SRN):         #(int i = 0; i<SRN; i++) 
            for j in range(SRN):      #(int j = 0; j<SRN; j++) 
                if (self.mat[rowStart+i][colStart+j]==num): 
                    return False
        return True

    # Fill a 3 x 3 matrix. 
    def fillBox(self, row, col):
        num=0
        N = self.N
        SRN = self.SRN
        for i in range(SRN):      #(int i=0; i<SRN; i++)         
            for j in range(SRN):  #(int j=0; j<SRN; j++) 
                while not(self.unUsedInBox(row, col, num)):
                    num = self.randomGenerator(N); 
                self.mat[row+i][col+j] = num; 
                
    # Random generator 
    def randomGenerator(self, num):
        return np.floor((np.random.random()*num)+1); 

    # Check if safe to put in cell 
    def CheckIfSafe(self, i, j, num): 
        return (self.unUsedInRow(i, num) and 
                self.unUsedInCol(j, num) and 
                self.unUsedInBox(i-i%self.SRN, j-j%self.SRN, num)); 

    # check in the row for existence 
    def unUsedInRow(self, i, num): 
        for j in range(self.N):        #(int j = 0; j<N; j++) 
          if (self.mat[i][j] == num): 
                return False;
        return True 

    # check in the row for existence 
    def unUsedInCol(self, j, num): 
        for i in range(self.N):       #(int i = 0; i<N; i++) 
            if (self.mat[i][j] == num): 
                return False 
        return True

    # A recursive function to fill remaining 
    # matrix 
    def fillRemaining(self, i, j) :
        N = self.N
        SRN = self.SRN
        # System.out.println(i+" "+j); 
        if (j>=N and i<N-1): 
            i = i + 1         # change row 
            j = 0             # column =0
        if (i>=N and j>=N): 
            return true;      # end of filling 
        if (i < SRN):         # 3 first rows 0-2
            if (j < SRN): 
                j = SRN       # begin at column 3
        elif (i < N - SRN) :  # rows 3-5
            if (j==(int)(i/SRN)*SRN):   # if j = col 3
                j = j + SRN             # j+3  j = col6 ; jump central box
        elif (j == N - SRN):  # column 6
                i = i + 1 
                j = 0 
                if (i>=N): 
                    return True
        for num in range(1,N+1):     #(int num = 1; num<=N; num++) 
            if (self.CheckIfSafe(i, j, num)):          
                self.mat[i][j] = num
                print(i, j, num)
                if (self.fillRemaining(i, j+1)): 
                    return True
                self.mat[i][j] = 0     
        return False

    # Remove the K no. of digits to 
    # complete game 
    def removeKDigits(self):
        count = self.K
        N = self.N
        while (count != 0): 
            cellId = self.randomGenerator(N*N)-1
            # extract coordinates i and j 
            i = int(cellId/N)-1; 
            j = int(cellId%9);
            #print(cellId, i, j); 
            if (j != 0): 
                j = j - 1;             
            if (self.mat[i][j] != 0):             
                count-=1
                self.mat[i][j] = 0

    # Print sudoku 
    def printSudoku(self):
        N = self.N
        for i in range(N) :     #(int i = 0; i<N; i++)          
            for j in range(N):     #(int j = 0; j<N; j++) 
                print(self.mat[i][j],"\t") 
            print(); 
         
        print(); 
     

# Driver code 
def main():
    N = 9; K = 50; 
    sudoku = Sudoku(N, K) 
    grid = sudoku.fillValues()
    #print(grid)
    #sudoku.printSudoku()

main()