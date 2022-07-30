import math
def get_average(marks):
    list=sum(marks)

    avg=list/len(marks)
    return math.floor(avg)


print(get_average([1,2,3,4,5]))