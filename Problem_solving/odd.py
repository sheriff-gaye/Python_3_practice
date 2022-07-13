def odd_count(n):
    list=0
    for i in range(n):
        if i%2==1:
            list+=1
    return list

print(odd_count(15))