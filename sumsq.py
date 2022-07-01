def square_sum(numbers):
    list=[]
    for i in numbers:
        list.append(i**2)
        
    return sum(list)


print(square_sum([0, 3, 4, 5]))