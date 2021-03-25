#-------------------------------------------------------------------------------
# Name:        sudoku
# Purpose:
#
# Author:      Jean
#
# Created:     02/09/2018
# Copyright:   (c) Jean 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

Grid=[[1,2,3,4,5,6,7,8,9],
[4,5,6,7,8,9,1,2,3],
[7,8,9,1,2,3,4,5,6],
[9,1,2,3,4,5,6,7,8],
[3,4,5,6,7,8,9,1,2],
[6,7,8,9,1,2,3,4,5],
[8,9,1,2,3,4,5,6,7],
[2,3,4,5,6,7,8,9,1],
[5,6,7,8,9,1,2,3,4]]
for k in Grid:print(k)
print()

L1=Grid[0]
L2=Grid[1]
L3=Grid[2]
L4=Grid[3]
L5=Grid[4]
L6=Grid[5]
L7=Grid[6]
L8=Grid[7]
L9=Grid[8]
L=[L1,L2,L3,L4,L5,L6,L7,L8,L9]
#print(L)

C1=list([]);
for k in L: C1.append(k[0])
C2=list([]);
for k in L: C2.append(k[1])
C3=list([]);
for k in L: C3.append(k[2])
C4=list([]);
for k in L: C4.append(k[3])
C5=list([]);
for k in L: C5.append(k[4])
C6=list([]);
for k in L: C6.append(k[5])
C7=list([]);
for k in L: C7.append(k[6])
C8=list([]);
for k in L: C8.append(k[7])
C9=list([]);
for k in L: C9.append(k[8])
C=[C1,C2,C3,C4,C5,C6,C7,C8,C9]
#print(C)

Z1=[]
for k in L[0:3]:
    for l in range(0,3):Z1.append(k[l])
Z2=list([])
for k in L[0:3]:
    for l in range(3,6):Z2.append(k[l])
Z3=list([])
for k in L[0:3]:
    for l in range(6,9):Z3.append(k[l])
Z4=list([])
for k in L[3:6]:
    for l in range(0,3):Z4.append(k[l])
Z5=list([])
for k in L[3:6]:
    for l in range(3,6):Z5.append(k[l])
Z6=list([])
for k in L[3:6]:
    for l in range(6,9):Z6.append(k[l])
Z7=list([])
for k in L[6:9]:
    for l in range(0,3):Z7.append(k[l])
Z8=list([])
for k in L[6:9]:
    for l in range(3,6):Z8.append(k[l])
Z9=list([])
for k in L[6:9]:
    for l in range(6,9):Z9.append(k[l])

Z=[Z1,Z2,Z3,Z4,Z5,Z6,Z7,Z8,Z9]
#print(Z)

G1=[L1,L2,L3,L6,L5,L4,L7,L8,L9]
for k in G1:print(k)
print()
G1=[L6,L5,L4,L1,L2,L3,L7,L8,L9]
for k in G1:print(k)