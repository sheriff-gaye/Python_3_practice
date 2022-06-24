
def reverse(st):
    list=()
    one=st.split()
    for i in one:
        list.append(i)
        res=list[::-1]
    return res

print(reverse('Hello World'))
print()