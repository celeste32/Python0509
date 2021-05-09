# -*- coding: utf-8 -*-
"""
Created on Sun May  9 14:27:25 2021

@author: user
"""

#自訂錯誤

class MyError(Exception):
    def __init__(self,radius):
        self.r = radius
    def __str__(self):
        return '半徑Error：'+str(self.r)