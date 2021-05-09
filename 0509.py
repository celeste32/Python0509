# -*- coding: utf-8 -*-
"""
Created on Sun May  9 10:12:36 2021

@author: user
"""
#try 把可能出錯的程式碼包裝起來
#except 抓出出錯的程式碼並註明原因
#assert 斷言  直接判斷

data = [10,20,30]
try:
    print(data[1])
    print(data[10])
except IndexError as Error:
    print(Error)
    
print('程式執行完畢')
