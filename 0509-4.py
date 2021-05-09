# -*- coding: utf-8 -*-
"""
Created on Sun May  9 13:45:28 2021

@author: user
"""

for i in range(5):
    print(i)
else: print('計算完畢')
print('-'*30)
for i in range(5):
    if i == 3:
        continue
    print(i)
else: print('計算完畢')
print('-'*30)
for i in range(5):
    if i == 3:
        break
    print(i)
else: print('計算完畢')
print('-'*30)
for i in range(2,101): #i=2~100
    for x in range(2,i): 
        if i % x ==0:
            break
    else: print(i,'是質數')