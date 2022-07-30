def find_it(seq):
    num=0
    # se=list(dict.fromkeys(seq))
    for i in seq:
        if i%2==1:
            num+=1
    return num

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))
print(find_it([1,1,1,1,1,1,10,1,1,1,1]))