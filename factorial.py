
#recussion factor
def recussion(n):
    if n>0:
        result=n+recussion(n-1)
        print(result)
        
    else:
        result=0
    return result

recussion(8)