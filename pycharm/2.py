#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def cylinder():
    r = float(input("Enter radius: "))
    h = float(input("Enter high: "))
    s_side = 2 * math.pi * r * h

    def circle():
        s_circle = math.pi * r ** 2
        return s_circle

    check = int(input("Enter 1 if you need side area or 2 for full area: "))
    if check == 1:
        print(f"Side area of cylinder is: {s_side}")
    else:
        full_area = s_side + circle() * 2
        print(f"Full area of cylinder is: {full_area}")


if __name__ == "__main__":
    cylinder()
