
# import os to import os
# os.remove(file name) to remove a file created
#file.close() to close a file open
#file.write to add text to the file
# mode 'w' to write
# mode 'a' to append
# mode 'r' to read a file

import os

file=open('wifi.txt','w')
file.write('hello world my name is sheriff gaye an i am a software developer')
file=open('wifi.txt' 'r')
print(file.read())
file.close()

os.remove('main.text')