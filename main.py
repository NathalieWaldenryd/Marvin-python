#!/usr/bin/env python3
"""
something
"""
# -*- coding: utf-8 -*-
import marvin
"""
import marvin
"""
"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""

marvin_image = r"""
       ;-.               ,
        \ '.           .'/
         \  \ .---. .-' /
          '. '     `\_.'
            |(),()  |     ,
            (  __   /   .' \
           .''.___.'--,/\_,|
          {  /     \   }   |
           '.\     /_.'    /
            |'-.-',  `; _.'
            |  |  |   |`

"""

"""
Its an eternal loop, until q is pressed.
It should check the choice done by the user and call a appropriate
function.
"""
while True:
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print(marvin_image)
    print("Hi, I'm Eevee. What do you want.?")
    print("1) Do you wanna know your age in seconds.?")
    print("2) Do you wanna know a weight on the moon in kg.?")
    print("3) Do you wanna convert minutes to hours.?")
    print("4) Do you wanna convert celcius to the pesky fahrenheit .?")
    print("5) Word multiplication is also fun.")
    print("6) Random number generation.")
    print("7) The arithmetic average of numbers.")
    print("8) Guess that number (1-100).")
    print("9) Return random Word.")
    print("You can also type citat, inv, inv drop itemname, inv pick itemname")
    print("q) Quit.\n\n")

    choice = input("--> ")

    if choice == "q":
        print("\nSee ya!\n")
        break

    elif choice == "1":
        age = input("Whats your age? ")
        marvin.seconds_age(age)

    elif choice == "2":
        kg = input("What weight in kg? ")
        marvin.moon_kg(kg)

    elif choice == "3":
        minutes = input("How many minutes? ")
        marvin.hours_min(minutes)

    elif choice == "4":
        celcius = input("What celcius? ")
        marvin.fahrenheit_c(celcius)

    elif choice == "5":
        words = input("What word? ")
        numberoftimes = input("How many times? ")
        print(marvin.word_times(words, numberoftimes))

    elif choice == "6":
        min1 = int(input("Enter min: "))
        max1 = int(input("Enter max: "))
        marvin.ranommin_max(min1, max1)

    elif choice == "7":
        marvin.choice_7()

    elif choice == "8":
        marvin.choice_8()

    elif choice == "9":
        word1 = input("What word? ")
        print(marvin.shuffle_string(word1))

    elif marvin.checkforcitat(choice):
        print(marvin.citat())

    elif marvin.checkforinv(choice):
        if marvin.checkforpick(choice):
            marvin.pick(choice)
        elif marvin.checkfordrop(choice):
            marvin.drop(choice)
        else:
            marvin.invcheck()

    else:
        print("That is not a valid choice. You can only choose from the menu.")

    input("\nPress enter to continue...")
