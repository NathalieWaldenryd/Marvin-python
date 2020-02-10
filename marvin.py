#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main.py funtioner
"""

import random

def seconds_age(age):
    """
    age to seconds
    """
    print("\nEevee says:\n")
    seconds = int(age) * 31536000
    print("You have lived atleast " + str(seconds) + " seconds.\n")

def moon_kg(kg):
    """
    kg on the moon.
    """
    print("\nEevee says:\n")
    moonkg = int(kg) * (16.5/100)
    print("That weight would be " + str(round(moonkg, 3)) + "kgs on the moon.\n")

def hours_min(minutes):
    """
    minutes to hrs and minutes
    """
    print("\nEevee says:\n")
    minutes1 = int(minutes)
    print("That would be", minutes1//60, "hrs and", minutes1%60, "min.\n")

def fahrenheit_c(celcius):
    """
    celcius to fahrenheit
    """
    print("\nEevee says:\n")
    fahrenheit = round(((int(celcius) * 1.8) + 32), 2)
    print("That would be " + str(fahrenheit) + " fahrenheit.\n")

def word_times(words, numberoftimes):
    """
    word * number
    """
    print("\nEevee says:\n")
    return(words * int(numberoftimes))

def ranommin_max(min1, max1):
    """
    random min max
    """
    print("\nEevee says:\n")
    print("Your random numbers are: ", end="")
    for i in range(0, 10):
        if i != 9:
            print(str(random.randint(min1, max1)), end=",")
        else:
            print(str(random.randint(min1, max1)))

def choice_7():
    """
    take all numbers and average them
    """
    numbers = []
    while(True):
        num = input("Type a number and when done type done: ")
        if num != "done":
            numbers.append(int(num))
        else:
            break
    print("\nEevee says:\n")
    print("The average is " + str(sum(numbers)/len(numbers))  + " of "+  str(sum(numbers)))

def choice_8():
    """
    guess that number!
    """
    x = random.randint(1, 100)
    win_flag = False
    for _ in range(0, 6):
        y = int(input("Gimme number between 1-100: "))
        if x == y:
            win_flag = True
            break
        elif x < y:
            print("You guessed a higher value then my number")
        else:
            print("You guessed a lower value then my number")

    if win_flag:
        print("Winner winner chicken dinner!")
    else:
        print("Try again!")

def shuffle_string(word1):
    """
    everyday im shuffling
    """
    list_word = list(word1)
    random.shuffle(list_word)
    print("\nEevee says:\n")
    return "".join(list_word)

def citat():
    """
    Random quotes
    """
    quotes = open("quotes.txt", "r")
    content = quotes.readlines()
    random.shuffle(content)
    return content.pop()

def checkforcitat(sentence):
    """
    Checkar citat
    """
    sentence = sentence.lower()
    return "citat" in sentence

def checkforinv(sentence):
    """
    Checkar inv
    """
    sentence = sentence.lower()
    return "inv" in sentence

def checkfordrop(sentence):
    """
    Checkar drop
    """
    sentence = sentence.lower()
    return "drop" in sentence

def checkforpick(sentence):
    """
    Checkar pick
    """
    sentence = sentence.lower()
    return "pick" in sentence

def pick(command):
    """
    picking up item
    """
    itemToSave = command.split()[2] + "\n"
    files = open("inv.data", "r+")
    files.write(itemToSave)
    items = files.readlines()
    files.seek(0)
    for item in items:
        if item != itemToSave:
            files.write(item)
    files.close()
    print("You have picked up: " + itemToSave, end="")


def drop(command):
    """
    dropping an item
    """
    itemToDrop = command.split()[2] + '\n'
    files = open("inv.data", "r+")
    items = files.readlines()
    files.seek(0)

    flag = False

    if itemToDrop in items:
        flag = True

    for item in items:
        if item != itemToDrop:
            files.write(item)

    if flag:
        print("You have dropped: " + itemToDrop, end="")
    else:
        print("You dont have: " + itemToDrop, end="")

    files.truncate()
    files.close()

def invcheck():
    """
    checkin inv
    """
    array = open("inv.data", "r")
    reading = [item.replace('\n', '') for item in array.readlines()]
    print("You have (" + str(len(reading)) + ") things in inv :" + str(reading), end="")
    array.close()

#import re
#
#def checkforcitat2(sentence):
#    p = re.compile('citat')
#    return bool(p.match(sentence.lower()))
#
#print(checkforcitat("asdasd citatXD"))
#print(checkforcitat2("asdasd citatXD"))
#

#array = open("inv.txt", "r")
#reading = array.readlines()
#
#cleanReading = []
#for item in reading:
#    cleanReading.append(item.replace('\n', ''))

#print("You have (" + str(len(cleanReading)) + ") things in inv :" + str(cleanReading), end="")
#array.close()
