def filter_list(l):
    list=[]
    for i in l:
        if isinstance(i,int):
            list.append(i)
    return list


print(filter_list([1,2,3,'a','b']))