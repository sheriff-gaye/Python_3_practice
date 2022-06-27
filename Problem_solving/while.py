

import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:

        guess = int(input(f'Enter a number from  0 to {x}......:'))

        if guess < random_number:

            print('OOPs too low ! Try again')

        elif guess > random_number:

            print('OOPs too high !Try again')

    print(f'Congrulation you have win , The random number is {random_number}')


guess(10)
