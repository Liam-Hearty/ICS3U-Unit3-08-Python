#!/usr/bin/env python3

# Created by: Liam Hearty
# Created on: October 2019
# This program checks if the input year is a leap year or not.


def main():
    print("This program tells which years are leap years.")
    try:
        year = int(input("Please enter a whole number: "))
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    print("{0} is a leap year".format(year))
                else:
                    print("{0} is not a leap year".format(year))
            else:
                print("{0} is a leap year".format(year))
        else:
            print("{0} is not a leap year".format(year))
    except ValueError:
        print("Please type in a whole number.")


if __name__ == "__main__":
    main()
