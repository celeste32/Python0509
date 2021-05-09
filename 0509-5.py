# -*- coding: utf-8 -*-
"""
Created on Sun May  9 14:05:45 2021

@author: user
"""
data = [30,28,26,42,22,54,-71]
def score(data):
    total = 0
    for item in data:
        #assert item > 0, '分數必大於0' #assert(斷言)用於除錯，會顯示出錯誤原因
        if item >=0:
            total += item
        else: print('分數必大於0')
    return total
print('總和：',score(data))
print('-'*30)

