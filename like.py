
def likes(names):
    
    for i in names:
        if len(names)>2:
            return ("{}, {} and {} others likes this".format(names[0],names[1], (len(names)-2)))
        elif len(names)==2:
            return ("{},{} likes this".format(names[0],names[1]))
        
        elif len(names)==1:
            return ("{} likes this".format(names[0]))
        
        elif len(names)<1:
            return "no one likes this"

            

print(likes(['Jacob', 'Alex']))
print(likes(['Jacob', 'Alex','sheriff','gaye','fatou']))
print(likes(['sheriff']))
print(likes([]))