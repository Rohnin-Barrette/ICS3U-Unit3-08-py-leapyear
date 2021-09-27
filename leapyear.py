#!/usr/bin/env python3

# Created by: Rohnin Barrette
# Created on: Sep 2021
# This function tells the user if the inputted year is a leap year or not.


def main():
    # This function tells the user if the inputted year is a leap year or not.

    # input
    year_string = input("Enter the year: ")
    print("")

    # process and output
    try:
        year_number = int(year_string)
        if year_number % 4 == 0:
            print("{0} is a leap year.".format(year_number))
        else:
            if year_number % 100 == 0:
                print("{0} is a leap year.".format(year_number))
            else:
                if year_number % 400 == 0:
                    print("{0} is a leap year.".format(year_number))
                else:
                    print("{0} is not a leap year.".format(year_number))
    except Exception:
        print("{0} is an invalid input.".format(year_string))

    print("\nDone.")


if __name__ == "__main__":
    main()
