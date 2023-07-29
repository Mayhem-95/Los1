# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 13:47:28 2023

@author: omarm
"""
#Question 1 
import numpy
sample_list= [2, 3, 6]
result= numpy.prod(sample_list)
print(result)

# Question 2
sample2 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sample2.sort(key=lambda i: i[1])
print(sample2)

# Question 3
from collections import Counter
d1= Counter({'a': 100, 'b': 200, 'c':300})
d2= Counter({'a': 300, 'b': 200, 'd':400})
for key in d2:
    d3= d1+d2
print(d3)

# Question 4
link1 ={1:1 ,2:2 ,3:3 , 4:4 ,5:5 ,6:6 ,7:7 ,8:8}
new_link = {key: value * value for key, value in link1.items()}
print(new_link)

# Question 5
list= [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
result = sorted(list, reverse=True)
print(result)

# Question 6
lista = {0, 1, 2, 3, 4}
lista.add(5)
print(lista)
lista.discard(1)
print(lista)