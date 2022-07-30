
def arithmetic_arranger(num):

    for i in num:
        s=i.split()
        if s[1]=='+':
            result=int(s[0])+int(s[2])
        elif s[1]=='-':
           result=int(s[0])-int(s[2])

        ouput=("{}\n{}{}\n -------\n{}".format(s[0],s[1],s[2],result))
        return ouput



print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))