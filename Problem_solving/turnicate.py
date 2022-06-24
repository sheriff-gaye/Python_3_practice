def who_is_paying(name): 

    if(name=="") or len(name)<=2:
        return [name]
    else:
        turn=name[0]+name[1]
        return [name,turn]

print(who_is_paying("sheriff"))
print(who_is_paying("me"))
print(who_is_paying("hi"))
print(who_is_paying("Gaye"))