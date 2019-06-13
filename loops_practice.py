"""
title: loops_practice
author: Sahaana
date: 2019-06-13 13:38
"""
# number 1
for i in [89, 41, 73, 90]:
    print(i)

# number 2
for j in range(5, 15):
    print(j, end=" ")

print()

# number 3
for k in range(100, 201, 10):
    print(k, end=" ")

print()

# number 4
for h in range(80, 31, -8):
    print(h, end=" ")

print()

# number 5
word = ["Alright"]
for u in word:
    print(u * 3, end=" ")

print()

# While loops
# number 1
number = 10

while number >= 1:
    print(number, end="-")
    number -= 1

print()
print("You've made it to 1")

# number 2

x_input = int(input("Enter an integer greater than 0: "))  # casting to an int

while x_input < 0:
    print("Try Again")
    x_input = int(input("Enter an integer greater than 0: "))
print("Good Job! You typed an integer greater than 0")

# number 3

first = int(input("Enter a number: "))
second = int(input("Enter a second number: "))

while second < first :
    second = int(input("Invalid response. Enter a second number: "))  # Loop till you get the right valued number

while first < second:
    print(first)
    first += 1

# number 4

x = input("Enter response ('Y', 'y', 'yes', 'YES' or 'N', 'n', 'no', 'NO'): ")

while x not in [ 'Y', 'y', 'yes', 'YES' or 'N', 'n', 'no', 'NO']:
    x = input("Enter response( 'Y', 'y', 'yes', 'YES' or 'N', 'n', 'no', 'NO'): ")

