#!/usr/bin/python3

#convert USD dollars into Chinese Yuan

def usdcny(usd):
    res=usd*6.75
    return ("{:.2f} Chinese Yuan".format(res))

print(usdcny(15))
print(usdcny(35))
print(usdcny(45))