# roll a "die" some number of times.
# roll - run it once and go into a loop
# roll 1 - produce a number 1-6 random and print it
# roll 2 - produce two numbers 1-6 and print them
# roll 3 - produce three numbers and print them.
#
import random

def roll_dice(attempts= None):
    attempts = int(input("How many times you want to roll your dice?\n"))

    for i in range (attempts):
        rand = random.randint(1, 6)
        print("You rolled", rand)

    again = input("Wanna roll again? type yes or no\n")
    if (again =="yes"):
        roll_dice(attempts)
    else:
        print("Thanks for playing!")

roll_dice()