def reverse_seq(n):
    list = []
    for i in range(1, n+1):
        list.append(i)
        res = (list[::-1])
    return res


print(reverse_seq(100))
print(reverse_seq(50))
