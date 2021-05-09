# -*- coding: utf-8 -*-
"""
Created on Sun May  9 14:31:21 2021

@author: user
"""

from CustomError import MyError
import math
class Circle:
    def __init__(self,radius):
        self.setR(radius)
    def setR(self,radius):
        if radius > 0:
            self.__r = radius
        else: raise MyError(radius)
    def getR(self):
        return self.__r
    def periphery(self):
        return 2 * self.__r * math.pi
    def area(self):
        return self.__r * self.__r * math.pi
    def __str__(self):
        return '圓周長:{:4.3f},圓面積:{:4.3f}'.format(self.periphery(),self.area())
try:
    one = Circle(15)
    print(one)
    three = Circle(45)
    print(three)
    two = Circle(-20)
    print(two)
except MyError as Error01:
    print(Error01)
    print('程式執行完畢')