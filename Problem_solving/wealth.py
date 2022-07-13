

def vaporcode(s):
    res=(s.replace(' ','')).upper()
    new=(res.replace('','  ')).upper()

    return new
    
print(vaporcode('hello world id gaye tech'))