# -*- coding: utf-8 -*-
"""
Created on Sun May  9 15:18:09 2021

@author: user
"""

file = 'news-utf8.txt'
fo = open(file,encoding=('utf-8'))
data = fo.read()
fo.close()
print(data)
#fo.read() #全部
#fo.readline() #第一行
#fo.readlines() #串列
print('-'*30)
file = 'news-utf8.txt'
with open(file,'r',encoding=('utf-8')) as fo:
    alldata = fo.readlines()
    for row in alldata:
        print(row.rstrip())
print('-'*30)
file = 'lcc.txt' #w,a只有寫，不可讀 w+,a+可寫可讀
with open(file,'w',encoding=('utf-8')) as fo: #寫檔，檔案不存在，就建立，檔案存在就直接覆寫
    fo.write('聯成電腦') #fo.write()=填入文字檔內要寫入的文字，重複執行會將文字持續寫入檔案
#w是寫檔，檔案不存在>>建立，檔案存在>>覆寫
#a是寫檔，檔案不存在>>建立，檔案存在>>接續著寫