#!/usr/bin/python3

# find two maximum numbers in a list

def two_highest(arg1):
    mylist = list(dict.fromkeys(arg1))
    hig = max(mylist)
    mylist.remove(hig)
    hig2 = max(mylist)
    return hig, hig2


print(two_highest([15, 20, 20, 17]))
print(two_highest([1,1,3,3,4,4,5,6,6,7,7,8,8]))
