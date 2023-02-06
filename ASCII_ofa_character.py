#!/usr/bin/python3
"""
This module prints the ASCII value of a character
"""


def main():
    """
    The function that prints the ASCII value of a character
    """

    a = (input("Please key in your character to print its value: "))
    print("The ASCII value of '{}' is: {}".format(a, ord(a)))


main()
