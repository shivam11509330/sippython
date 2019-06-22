# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 11:43:18 2019

@author: aa
"""

i=260
for i in range(260,280,2):
    print(i,end=' ')
    if i==270:
        print('exit')
        break


number=[i*1  for i in range(20,35)]
number
for i in number: print(i, "\t", i%2 > 0 , end = "\n")


