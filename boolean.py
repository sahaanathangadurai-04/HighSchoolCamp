"""
title: boolean_practice
author: Sahaana
date: 2019-06-11 13:31
"""

print(True and True)  # True
print(False and True)  # False
print(1 == 1 and 2 == 1)  # False
print("test" == "test")  # True
print(1 == 1 or 2 != 1)  # True
print(True and 1 == 1)  # True
print(False and 0 != 0)  # False
print(True or 1 == 1)  # True
print("test" == "testing")  # False
print(1 != 0 and 2 == 1)  # False
print("test" != "testing")  # True
print("test" == 1)  # False
print(not (True and False))  # True
print(not (1 == 1 and 0 != 1)) # False
print(not (10 == 1 or 1000 == 1000))  # False
print(not (1 != 1 or 3 == 4))  # True
print(not ("testing" == "testing" and "Ronny" == "Gool Guy"))  # True
print(1 == 1 and not ("testing" == 1 or 1 == 0))  # True
print("chunky" == "bacon" and not (3 == 4 or 3 == 3))  # False
print(3 == 3 and not ("testing" == "testing" or "Python" == "Fun"))  # False