"""
title: random_practice
author: Sahaana
date: 2019-06-12 09:53
"""
import random

name = input('Enter your name: ')
salary = int(input('Enter your salary: '))
print(f"{name} your salary is ${salary} ")
raise_per = (random.randint(0, 100))
print(f"Your raise is {raise_per}% of ${salary}.")
raise_amount = (salary*(raise_per/100)+salary)
print(f"{name}, your new salary is ${raise_amount}.")

