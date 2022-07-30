
try:
    num=input('enter number')
    res=0/num
    print(res)
except NameError:
    print("Reenter a correct value")

finally:
    print("Thank you")
    