

list =[0,2,4,2,5,6,8,2,6,3,4,5,6,3,2,2,7,8,9,1,2,2]

elem =3
try:
    # Get last index of item in list
    index_pos = len(list) - list[::-1].index(elem) - 1
    print(f'Last Index of element "{elem}" in the list : ', index_pos)
except ValueError as e:
    print(f'Element "{elem}" not found in the list: ', e)