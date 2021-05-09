# -*- coding: utf-8 -*-
"""
Created on Sun May  9 11:50:42 2021

@author: user
"""

def fun(x,y):
    try:
        result = x // y
        print('結果：',result)
    finally:  #finally=不論對錯，一定會執行
        print('計算完畢')
        print('不論對錯，一定會執行')

try:
    fun(30,4)
    fun(100,0)
except Exception as ex:
    print(ex)
    
print('-'*30)

def fun(x,y):
    try:
        result = x // y
        print('結果：',result)
    except Exception as ex1:
        print(ex1)
    finally:  #finally=不論對錯，一定會執行
        print('計算完畢')
fun(36,4)
fun(100,0)
