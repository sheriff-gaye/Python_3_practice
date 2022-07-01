def expression_matter(a, b, c):
    one=a*(b+c)
    four=(a+b)*c
    two=a*b*c
    five=a+b+c
    three=a+b*c
    six=a*b+c
    sev=a*c+b
    
    list=[one,two,three,four,five,six,sev]
    res=max(list)
    return res

print(expression_matter(1, 1, 1))