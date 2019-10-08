#!/usr/bin/env python3

# Created by: Patrick Gemmell
# Created on: September 12 2019
# This program does a guessing game


import random


def main():
    # this function guess and compares number
    while True:
        # input
        integer_as_string = input("Try an guess my integer from 0-9: ")
        try:
            integer_as_number = int(integer_as_string)
            # process and output
            print("")
            if integer_as_number == random.randint(0, 9+1):
                print("Correct!")
                break
            else:
                print("Sorry that's wrong, guess again?")
        except Exception:
            print("This is not an integer")
        finally:
            print("Thanks for playing")


if __name__ == "__main__":
    main()
