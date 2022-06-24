
import string


def str_count(strng, letter):
    for letter in strng:
        l = strng.replace(" ", '')
        num=l.count(letter)
    return num

print(str_count('codewars', 'c'))
# print(str_count('ggggg', 'g'))
print(str_count('hello world', 'o'))

# hey="sheriff gafe"
# l=hey.replace(" ",'')
# s=l.count('f')

# print(s)



