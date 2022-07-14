def billboard(name, price=30):
    
    if price=="":
        num=len(name)
        return num*30
    else:
        num=len(name)        
        return num*price



print(billboard('Jeong-Ho Aristotelis'))
print(billboard("Hadufuns John",20))