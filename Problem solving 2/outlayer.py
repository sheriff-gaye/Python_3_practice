def invert(lst):
    list=[]
    
    for i in lst:
        if i<0:
            list.append(abs(i))
        else:
            list.append(-(i))
    return list


print(invert([-1,-2,3]))