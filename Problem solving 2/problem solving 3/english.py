import math
def find_difference(a, b):
    # first cubid
    volume=a[0]*a[1]*a[2]
    volum2=b[0]*b[1]*b[2]
    diff=volume-volum2
    return abs(diff)

print(find_difference([3, 2, 5], [1, 4, 4]))