def count_positives_sum_negatives(arr):
    count=0
    sum=0
    for i in arr:
        if i>0:
            count+=1
        elif i<0:
            sum+=i
    return [count,sum]



print(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]))