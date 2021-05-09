# -*- coding: utf-8 -*-
"""
Created on Sun May  9 10:25:35 2021

@author: user
"""
#try 把可能出錯的程式碼包裝起來
#except 抓出出錯的程式碼並註明原因
#assert 斷言  直接判斷

data = [10,20,30]
try:
    raise RuntimeError('執行Error')
    print(data[1])
    print(data[10])
    print(10/0)

except IndexError as Error0:
    print(Error0)

except ZeroDivisionError as Error1:
    print(Error1)

except:
    print('捕獲其他錯誤')
print('程式執行完畢')
print('-'*30)

data = 10,20,30,40
try:
    print(data[0])
    print(name)
    print(data[10])
    
except Exception as Error:
    print(Error)
print('程式除錯完畢')
print('-'*30)

def result(x,y):
    r = x/y
    return r
try:
    print(result(10,3))
    print(result(10,0))

except Exception as ex:
    print(ex)
print('-'*30)

def result(x,y):
    r = None
    try:
        r = x/y
    except Exception as ex:
        print(ex)
        raise(ex)
    return r
    
try:
    print(result(10,3))
    print(result(10,0))

except Exception as ex:
    print('Main',ex)
    