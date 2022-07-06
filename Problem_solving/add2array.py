
def merge_arrays(arr1, arr2):
    res=(arr1+arr2)
    final=list(dict.fromkeys(res))
    return sorted(final)







print(merge_arrays([1,1,1,2,3,4], [5,6,7,8]))