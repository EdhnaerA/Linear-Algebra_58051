# -*- coding: utf-8 -*-
"""Task2_Lab4_Arcera

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/179bS7ga1KpuaUXakOo-xfawm9HpH1KDx

# **Task 2**
"""

##Vectors
EA = [3,9,30,23,21]
LP = [5,2,20,4,1]
LA = []

NA = [21,4,8,4,6 ]
SD = [4,9,15,13,18]
NR = []

KJ = [14,28,25,19,9 ]
HS = [3,7,4,22,10]
KH = []

MC = [5,3,6,2,4 ]
JB = [1,5,9,7,3]
MB = []

print('Given vectors:  EA= ', EA, 'LP = ', LP)
print('Inner Product of two vectors: (EA * LP)')
for i in range(len(EA)):
    p1 = EA[i] * LP[i]
    print(EA[i], '*', [i], '=', p1, '+')
    LA.append(p1)

print('(EA * LP) = ',LA)
print('The sum of all numbers :', sum(LA))
print('*'*64)


print('Given vectors:  NA= ', NA, 'SD = ', SD)
print('Inner Product of two vectors: (EA * SD)')
for i in range(len(NA)):
    p2 = NA[i] * SD[i]
    print(NA[i], '*', [i], '=', p2, '+')
    NR.append(p2)

print('(NA * SD) = ',NR)
print('The sum of all numbers :', sum(NR))
print('*'*64)


print('Given vectors:  KJ= ', KJ, 'HS = ', HS)
print('Inner Product of two vectors: (KJ * HS)')
for i in range(len(KJ)):
    p3 = KJ[i] * HS[i]
    print(KJ[i], '*', [i], '=', p3, '+')
    KH.append(p3)

print('(KJ * HS) = ',KH)
print('The sum of all numbers :', sum(KH))
print('*'*64)

print('Given vectors:  MC= ', MC, 'JB = ', JB)
print('Inner Product of two vectors: (KJ * JB)')
for i in range(len(MC)):
    p4 = MC[i] * JB[i]
    print(MC[i], '*', [i], '=', p4, '+')
    MB.append(p4)

print('(MC * JB) = ',MB)
print('The sum of all numbers :', sum(MB))
print('*'*64)