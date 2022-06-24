

# find two maximum numbers in a list 
def two_highest(arg1):
    mylist = list(dict.fromkeys(arg1)) #return unique list
    hig = max(mylist)
    mylist.remove(hig)
    hig2 = max(mylist)
    return hig, hig2


print(two_highest([15, 20, 20, 17]))
