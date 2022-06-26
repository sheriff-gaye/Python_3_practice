#!/usr/bin/python3


#function that counts number of letters in a word


def str_count(word, letter):
    
    while letter in word:
        num=word.count(letter)
        return num

print(str_count('ccocdewars', 'c'))
print(str_count('ff ff ff ff', 'f'))


