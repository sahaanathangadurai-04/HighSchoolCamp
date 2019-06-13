"""
title: string_practice
author: Sahaana
date: 2019-06-11 13:45
"""
# strings lab

# answer = input('Enter a letter: ')
# print(answer in "qwertyuiopasdfghjklzxcvbnm")

#def is_letter(character):
   # return character[0].lower() in "qwertyuiopasdfghjklzxcvbnm"

# print(is_letter("isadfasdf"))
# print(is_letter("0"))


# short hand lab

# short_hand = "Thank you for that! You are too sweet and kind!"
# print(short_hand.replace("you", "U"))
# print(short_hand.replace("for",  "4"))
# print(short_hand.replace("that", "tht"))
# print(short_hand.replace("are",  "r"))
# print(short_hand.replace("too",  "2"))

def short_hand(short):
    short = short.lower().replace("and", "&").replace("you", "U").replace("for", "4").replace("too", "2")
    return short.replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "")


print(short_hand("Thank you for that! You are too sweet and kind!"))
print(short_hand("How are you today?"))


# phrase = 'Don\'t count your chickens before they hatch'
# slogan = "For Everything Else, There's Mastercard"
# combined = f"{phrase}. {slogan}"
# print(combined)
# print((phrase + "\n") * 3)

def removing(check):
    check = check.replace(",", "").replace("'", "").replace(" ", "")
    return check.lower()


print(removing("Madam, I'm Adam"))


def palindrome(check):
    check = removing(check)
    return check == check[::-1]


print(palindrome("Madam, I'm Adam"))
print(palindrome("Computers"))

name = input('Enter your First Name: ')
name2 = input('Enter your Last Name: ')
city = input('Enter your Birth City: ')
university = input('Enter the University you Graduated from: ')
relative_name = input('Enter a Relative\'s name: ')
friend_name = input('Enter a Friends\'s name: ')









