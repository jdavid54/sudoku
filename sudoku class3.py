#-------------------------------------------------------------------------------
# Name:        sudoku candidates
# Purpose:
#
# Author:      Jean
#
# Created:     12/01/2019
# Copyright:   (c) Jean 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#import numpy as np

class Case:
    def __init__(self,val, zone):
        self.val=val
        self.zone=zone
        self.candidates=pattern
    def set(self,val):
        self.val=val
        self.update()
    def update(self):
        if self.val in pattern:
            self.candidates=''

class Grid():
    def __init__(self):
        self.g=[]
        self.row=['','','','','','','','','']
        self.column=['','','','','','','','','']
        self.zone=['','','','','','','','','']
        self.combi=[['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','',''],
                ['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','',''],
                ['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','','']]
        self.candidates=[['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','',''],
                ['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','',''],
                ['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','','']]

        #create the grid with val=0
        for k in range(9):
            h=[]
            for l in range(9):
                h.append(Case(0,str(k)+str(l)+str(3*(k//3)+l//3)))
            self.g.append(h)
        #print(self.g)

        ##populate with grid values
        for k in range(9):
            for l in range(9):
                self.g[k][l].set(grid[k][l])

        #print grid to solve
        print('Grid to solve')
        for k in range(9):
            for l in range(9):
                print(str(self.g[k][l].val),end='|')
                self.row[k]+=str(self.g[k][l].val)
            print()
        print()

        #grid by columns
        for k in range(9):
            for l in range(9):
                self.column[k]+=str(self.g[l][k].val)
            #print(s)

        #grid by areas
        for m in range(3):
            for n in range(3):
                for k in range(3):
                    for l in range(3):
                        self.zone[3*m+n]+=str(self.g[3*m+k][3*n+l].val)
                #print(s)

        #populate candidates
        for m in range(9):
            for n in range(9):
                self.combi[m][n]=self.row[m]+self.column[n]+self.zone[3*(m//3)+n//3]
                #print(m,n,combi[m][n])
                if self.row[m][n]=='0':
                    for k in pattern:
                        if k not in self.combi[m][n]:
                            self.candidates[m][n]+=str(k)
                else:
                    self.candidates[m][n]=self.row[m][n]
                #print(candidates[m][n])

        #print candidates
        print('candidates grid')
        for m in range(9):
            for n in range(9):
                print(self.candidates[m][n],end='|')
            print()

grid=[
   '609000000',
   '008000702',
   '200034000',
   '000402179',
   '410000258',
   '920108300',
   '704510023',
   '302040615',
   '000000407']
pattern='123456789'
'''
grid=[
   'EUSIOCHMT',
   'THCSEMOUI',
   'OMIUTHECS',
   '0STOHIUEM',
   'IEHMUSCTO',
   'UOMCETSIH',
   'STOEMCIHU',
   'HIETSUMOC',
   'MCUHIETSE']
pattern='UOHSCTEMI'
'''
#init grid
sudoku=Grid()
