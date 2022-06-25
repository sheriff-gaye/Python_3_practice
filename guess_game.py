#this is guess game in python
import random


secret_number=random.randint(0,5)
guess_count=0
guess_limit=3

while guess_count<guess_limit:
    guess=int(input('Enter the secret number:'))
    guess_count+=1
    
    if guess==secret_number:
        print("You won😍")
        break
    else:
        print("You failed")
print("Thank you for playing this game")


