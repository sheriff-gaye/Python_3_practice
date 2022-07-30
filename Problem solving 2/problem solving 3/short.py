
def find_short(s):
    list=[]
    l =s.split()
    for i in l:
        list.append(len(i))
    return min(list)

    



print(find_short("Let's travel abroad shall we"))