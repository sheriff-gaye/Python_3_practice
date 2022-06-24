#!/usr/bin/python3

""'Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.'""

def abbrev_name(name):
    s=name.split()
    first=(s[0])
    second=(s[1])
    s=second[0]
    f=first[0]
    return("{}.{}".format(f,s))


print(abbrev_name("Sam Harris"))