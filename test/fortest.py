# -*- coding: utf-8 -*-
"""
Created on Fri May  7 11:52:59 2021

@author: admin
"""
from hamcrest import *
import json
a={"1":"白色","2":"黑色","3":"绿色"}
print(a.items())

b=('1', '白色'), ('2', '黑色')
#print (b.items())
if b in a.items():
    print("1")


