#!/usr/bin/python3

#creating initials from names

import math


def abbrev_name(name):
    s=name.split()
    first=(s[0])
    second=(s[1])
    s=second[0]
    f=first[0]
    return("{}.{}".format(f,s))


print(abbrev_name("Sam Harris"))

print(math.floor)