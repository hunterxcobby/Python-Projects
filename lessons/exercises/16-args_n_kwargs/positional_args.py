#!/usr/bin/python3


def add(*numbers):
    c = 0
    for i in numbers:
        c += i
    print(f"sum is {c}")


add(4, 9, 0, 19, -3)


