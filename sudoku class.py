#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jean
#
# Created:     31/12/2018
# Copyright:   (c) Jean 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r, x.i)

class Case:
    def __init__(self,val, zone):
        self.val=val
        self.zone=zone
        if val==0:
            self.candidates=[1,2,3,4,5,6,7,8,9]
        else:
            self.candidates=[]

candidates='123456789'
array=[1,2,3,4,5,6,7,8,9]
x = Case(3,'111')
y = Case(0,'121')
print(x.val, x.zone,x.candidates)
print(y.val, y.zone,y.candidates)

if '4' in '123':print('oui')

print(array)
array.pop(0)    #retire valeur à l'index 0

print(array)
array.remove(8)   #retire valeur 8
print(array)