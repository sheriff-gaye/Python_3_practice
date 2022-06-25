
from word import words
import random
import string


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or '' in word:
        word = random.choice(words)

    return word


def hangman():
    word = get_valid_word(words)
    word_letter = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    # getting user input
    while len(word_letter) > 0:

        print("You have used these letter", '' .join(used_letters))

        word_list = [
            letter if letter in used_letters else '-' for letter in word]

        print("Current Word", ''.join(word_list))

        user_letter = input("Guess a Letter ?").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letter:
                word_letter.remove(user_letter)

            elif user_letter in used_letters:
                print("You have already used that charcater ? Please Try again ")

            else:
                print("Invalid charcter please try again ")


hangman()
# get_valid_word()


# user_input=input("type in something ?")
# print(user_input)
