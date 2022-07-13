def enough(cap, on, wait):
    
    remain=cap-on
    if remain>wait:
        return 0
    else:
        return abs(wait-remain)
    
print(enough(10,5,5))
print(enough(100,50,60))
print(enough(20,5,5))