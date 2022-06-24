#!/usr/bin/python3

#palindrome checking

def is_palindrome(s):
    l=s.lower()
    
    if (l==l[::-1]):
        return True
    else:
        return False

print(is_palindrome('a'))
print(is_palindrome('Kasue'))
