

list =[0,2,4,7,9,0]

elem =0
try:
    # Get last index of item in list
    index_pos = len(list) - list[::-1].index(elem) - 1
    print(f'Last Index of element "{elem}" in the list : ', index_pos)
except ValueError as e:
    print(f'Element "{elem}" not found in the list: ', e)