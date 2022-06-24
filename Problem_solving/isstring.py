def isDigit(string):
    leng= 2
    num = len(string)
    for i in string:
        if isinstance(i, int):
            leng+= 1
        if leng == num:
            return True
        else:
            return "False"


print(isDigit("s2324"))
print(isDigit("-234.4"))
