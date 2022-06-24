def reverse(st):
    index=len(st)
    list=st.split()
    while index:
        index-=1
        list.append(st[index])
    return "".join(list)


print(reverse('Hello World'))