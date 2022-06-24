def string_to_array(s):
    list=[]
    if s=="":
        return ['']
    else:
        l=s.split()
        for i in l:
           list.append(i)
        return list
    
print(string_to_array("I love arrays they are my favorite"))