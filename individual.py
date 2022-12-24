#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def output_circle(func):
    def f(*args):
        result = func(*args)
        print("Площадь круга равна:", '%.2f' %result)

    return f


@output_circle
def circle(r):
    return math.pi * r * r


if __name__ == "__main__":
    circle(3)
