# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 22:53:33 2023

@author: omarm
"""

def my_calc(n1, n2):
    x = input("Specify an operation: ")
    if x == "+":
        return n1 + n2
    elif x == "-":
        return n1 - n2
    elif x == "*":
        return n1 * n2
    elif x == "/":
        while n2 == 0:
            print("you cannot divide by 0")
            n1 = int(input("please enter a number: \n"))
            n2 = int(input("please enter a number: \n"))
        return n1 / n2
n1 = int(input("please enter a number: \n"))
n2 = int(input("please enter a number: \n"))
print(my_calc(n1, n2))