def calculator(x,y,op):
    ops=['+','-','*','/']
    if (isinstance(y,str))or isinstance(x,str):
        return "unknown value"
    else:
        if(op=="+"):
           return x+y
        elif(op=="-"):
            return x-y
        elif(op=="*"):
            return x*y
        elif(op=="/"):
            return x/y

print(calculator(5, 5, '*'))
print(calculator(5, '*', '*')
)