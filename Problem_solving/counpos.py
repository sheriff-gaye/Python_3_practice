
def count_positives_sum_negatives(arr):
    positive=[]
    negative=[]

    if arr==[]:
        return []
    else:
        for i in arr:
            if i>0:
                positive.append(i)
            else:
                negative.append(i)
    count=len(positive)
    sumneg=sum(negative)
    return [count,sumneg]

print(count_positives_sum_negatives([0,0,0,0,0]))
print(count_positives_sum_negatives([]))
print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))