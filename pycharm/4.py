#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_input():
    return input("Enter num: ")


def test_input(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


def str_to_int(num):
    return int(num)


def print_int(num):
    print(num, type(num))


if __name__ == "__main__":
    ent_num = get_input()
    print(ent_num, type(ent_num))
    if test_input(ent_num):
        str_to_int(ent_num)
        print_int(str_to_int(ent_num))
    else:
        print(f"Cant use 'str_to_int' for {ent_num}")
