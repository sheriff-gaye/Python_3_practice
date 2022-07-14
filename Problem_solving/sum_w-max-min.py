def sum_array(arr):
    maxi=max(arr)
    mini=min(arr)
    arr.remove(maxi)
    arr.remove(mini)
    return sum(arr)

print(sum_array([1,2,3,4,5]))