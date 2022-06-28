def expression_matter(a, b, c):
    one=a*(b+c)
    two=a*b*c
    three=a+b*c
    four=(a+b)*c
    five=a+b+c
    
    list=[one,two,three,four,five]
    res=max(list)
    return res

print(expression_matter(1, 1, 1))