# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 23:56:08 2023

@author: omarm
"""

user_estimation = input("Please estimate a value between (1, 100): ")
user_estimation = int(user_estimation)
import random
random_value=(random.randint(1, 100))
random_value=int(random_value)
print(random_value)
while user_estimation != random_value:
    print(user_estimation)
    user_estimation = (int(input("Guess again: ")))
    random_value=(random.randint(1, 100))
    random_value=int(random_value)
    print(random_value)
    if user_estimation > random_value:
        print("you're too high.Guess again")
    elif user_estimation < random_value:
        print("you're too low.Guess again")
    elif user_estimation == random_value:
        print("Congratulation! You guessed the number correctly!")

