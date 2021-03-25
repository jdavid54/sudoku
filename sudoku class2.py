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
import numpy as np
'''
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r, x.i)

class Bullet:
    def __init__(self, x,y):
        self.x = x
        self.y = y

b = Bullet(3, -5)
print(b.x, b.y)

v=[[Bullet(1,2),Bullet(3,4)],[Bullet(3,7),Bullet(11,4)]]
print(v)


w = []
for x in range(5):
   w.append(Bullet(1,2))
print(w)

for k in range(2):
  for l in range(2):
    print(v[k][l].x,v[k][l].y)
'''
pattern='123456789'
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
        for k in range(9):
            h=[]
            for l in range(9):
                h.append(Case(0,str(k)+str(l)+str(3*(k//3)+l//3)))
            self.g.append(h)
        #print(self.g)

def remove(t,val):
    r=''
    for k in t:
        if k!=val:
            r=r+k
    return r

l1='012007008'
l2='000800000'
l3='600009700'
l4='000400070'
l5='000000000'
l6='390008400'
l7='005000023'
l8='100090000'
l9='000523009'

l1='EUSIOCHMT'
l2='THCSEMOUI'
l3='OMIUTHECS'
l4='0STOHIUEM'
l5='IEHMUSCTO'
l6='UOMCETSIH'
l7='STOEMCIHU'
l8='HIETSUMOC'
l9='MCUHIETSE'
pattern='UOHSCTEMI'

#init grid
g=Grid()
#line1
g.g[0][0].set(l1[0]),g.g[0][1].set(l1[1]),g.g[0][2].set(l1[2])
g.g[0][3].set(l1[3]),g.g[0][4].set(l1[4]),g.g[0][5].set(l1[5])
g.g[0][6].set(l1[6]),g.g[0][7].set(l1[7]),g.g[0][8].set(l1[8])
#line2
g.g[1][0].set(l2[0]),g.g[1][1].set(l2[1]),g.g[1][2].set(l2[2])
g.g[1][3].set(l2[3]),g.g[1][4].set(l2[4]),g.g[1][5].set(l2[5])
g.g[1][6].set(l2[6]),g.g[1][7].set(l2[7]),g.g[1][8].set(l2[8])
#line3
g.g[2][0].set(l3[0]),g.g[2][1].set(l3[1]),g.g[2][2].set(l3[2])
g.g[2][3].set(l3[3]),g.g[2][4].set(l3[4]),g.g[2][5].set(l3[5])
g.g[2][6].set(l3[6]),g.g[2][7].set(l3[7]),g.g[2][8].set(l3[8])
#line4
g.g[3][0].set(l4[0]),g.g[3][1].set(l4[1]),g.g[3][2].set(l4[2])
g.g[3][3].set(l4[3]),g.g[3][4].set(l4[4]),g.g[3][5].set(l4[5])
g.g[3][6].set(l4[6]),g.g[3][7].set(l4[7]),g.g[3][8].set(l4[8])
#line5
g.g[4][0].set(l5[0]),g.g[4][1].set(l5[1]),g.g[4][2].set(l5[2])
g.g[4][3].set(l5[3]),g.g[4][4].set(l5[4]),g.g[4][5].set(l5[5])
g.g[4][6].set(l5[6]),g.g[4][7].set(l5[7]),g.g[4][8].set(l5[8])
#line6
g.g[5][0].set(l6[0]),g.g[5][1].set(l6[1]),g.g[5][2].set(l6[2])
g.g[5][3].set(l6[3]),g.g[5][4].set(l6[4]),g.g[5][5].set(l6[5])
g.g[5][6].set(l6[6]),g.g[5][7].set(l6[7]),g.g[5][8].set(l6[8])
#line7
g.g[6][0].set(l7[0]),g.g[6][1].set(l7[1]),g.g[6][2].set(l7[2])
g.g[6][3].set(l7[3]),g.g[6][4].set(l7[4]),g.g[6][5].set(l7[5])
g.g[6][6].set(l7[6]),g.g[6][7].set(l7[7]),g.g[6][8].set(l7[8])
#line8
g.g[7][0].set(l8[0]),g.g[7][1].set(l8[1]),g.g[7][2].set(l8[2])
g.g[7][3].set(l8[3]),g.g[7][4].set(l8[4]),g.g[7][5].set(l8[5])
g.g[7][6].set(l8[6]),g.g[7][7].set(l8[7]),g.g[7][8].set(l8[8])
#line9
g.g[8][0].set(l9[0]),g.g[8][1].set(l9[1]),g.g[8][2].set(l9[2])
g.g[8][3].set(l9[3]),g.g[8][4].set(l9[4]),g.g[8][5].set(l9[5])
g.g[8][6].set(l9[6]),g.g[8][7].set(l9[7]),g.g[8][8].set(l9[8])
'''
for k in range(9):
    for l in range(9):
        print("case",k,l,g.g[k][l].val,g.g[k][l].zone,g.g[k][l].candidates)
'''
row=['','','','','','','','','']
column=['','','','','','','','','']
zone=['','','','','','','','','']
combi=[['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','',''],
    ['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','',''],
    ['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','','']]
candidates=[['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','',''],
    ['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','',''],
    ['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','','']]
#grid by lines
print('grid by lines')
for k in range(9):
    s=''
    for l in range(9):
        print(str(g.g[k][l].val),end='|')
        s+=str(g.g[k][l].val)
    row[k]=s
    print()

for k in range(9):
    s=''
    for l in range(9):
        s+=str(g.g[l][k].val)
    column[k]=s
    #print(s)

for m in range(3):
    for n in range(3):
        s=''
        for k in range(3):
            for l in range(3):
                s+=str(g.g[3*m+k][3*n+l].val)
            zone[3*m+n]=s
        #print(s)
print()
'''
print(row)
print(column)
print(zone)
'''
for m in range(9):
    for n in range(9):
        combi[m][n]=row[m]+column[n]+zone[3*(m//3)+n//3]
        #print(m,n,combi[m][n])
        if row[m][n]=='0':
            for k in pattern:
                if k not in combi[m][n]:
                    candidates[m][n]+=str(k)
        else:
            candidates[m][n]=row[m][n]
        #print(candidates[m][n])

for m in range(9):
    for n in range(9):
        print(candidates[m][n],end='|')
    print()
