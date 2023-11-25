#Define a list of chosen fruits
#Choose a random letter from the list
#use the random module which allows the code to generate a random word from the variable word_list      

import random

word_list = ["Banana", "Apple", "Guava", "Peach", "Melon"]

def word (word_list):
    word = random.choice(word_list)
    return word

word = word(word_list)

while True:
    guess = input("Enter a single letter: ")
    if len(guess) == 1 and guess.isalpha():
        print("Good guess!")
        break
    else:
        print("Oops! That is not a valid input.  Please enter a single alphabetical character.")



