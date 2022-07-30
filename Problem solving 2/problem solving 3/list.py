def row_sum_odd_numbers(n):
    sum=0
    for i in range(1,n+1):
        if i%2==1:
            sum+=i
        else:
            return sum
    return sum

print(row_sum_odd_numbers(6))