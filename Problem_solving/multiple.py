#function  to find the multiples of a number

def find_multiples(integer, limit):
    list=[]

    for i in range(integer,limit+1,integer):
        list.append(i)
    return (list)

print(find_multiples(5,25))
print(find_multiples(1,2))