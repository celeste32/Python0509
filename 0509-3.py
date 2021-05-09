# -*- coding: utf-8 -*-
"""
Created on Sun May  9 13:23:06 2021

@author: user
"""
data = [1,2,3,4]
try:
    result = data[1]/data[0]
except Exception as error1:
    print(error1)
else: print(result)
print('-'*30)
data1 = [0,2,3,4]
try:
    result = data1[1]/data1[0]
except Exception as error2:
    print(error2)
else: print(result)
print('-'*30)
def demo(n1,n2):
    try:
        result = divmod(n1,n2)  #divmod=將n1除以n2，將商&餘數變成元組
    except Exception as ex:     #divmod的結果變成(商,餘數)
        print(ex)
    else: print('計算結果：',result)
    finally: print('計算完成')
demo(10,6)
print('-'*30)
def demo(n1,n2):
    try:
        result = divmod(n1,n2)  #divmod=將n1除以n2，將商&餘數變成元組
    except Exception as ex:     #divmod的結果變成(商,餘數)
        print('錯誤，原因為：',ex)  #Exception 可替代成 ZeroDivisionError
    else: print('計算結果：',result)
    finally: print('計算完成')
one,two = eval(input('兩個數字用，分開：'))
demo(one,two)