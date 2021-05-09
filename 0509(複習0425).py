# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Animals():
    def __init__(self,name):
        self.name = name
    def which(self):
        return "My Pet " + self.name.title()
    def action(self):
        return "sleeping......"

class Dog(Animals):
    def __init__(self,name):
        super().__init__(name.title())
    def action(self):
        return '跑跑跑'
#繼承>>super().xxx()：使用父類方法

class Monkeys():
    def __init__(self,name):
        self.name = 'My Monkeys' + name.title()
    def which(self):
        return self.name
    def action(self):
        return '吃香蕉'

def doing(obj):
    print(obj.which(),'is ',obj.action())

cat = Animals('Lucky')
doing(cat)
my_dog = Dog('萊福')
doing(my_dog)
monkey = Monkeys('Lala')
doing(monkey)