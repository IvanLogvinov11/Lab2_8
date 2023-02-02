#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def test():
    num = int(input("Enter number: "))
    if num > 0:
        positive()
    elif num < 0:
        negative()
    else:
        print("Your number is zero")


def positive():
    print("Your number is positive")


def negative():
    print("Your number is negative")


if __name__ == "__main__":
    test()
