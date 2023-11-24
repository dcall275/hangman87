word_list = ["Banana", "Apple", "Guava", "Peach", "Melon"] #create a word list
print(word_list)

import random  #import the random module

word_list = ["Banana", "Apple", "Guava", "Peach", "Melon"] #create a word list

def select_random_word(word_list):
    random_word = random.choice(word_list)
    return random_word

selected_word = select_random_word(word_list)
print("Random word:", selected_word) #prints random word in the word_list

import random # imports the random module

word_list = ["Banana", "Apple", "Guava", "Peach", "Melon"] #word list choice of 5 fruits

def select_random_word(word_list): 
    random_word = random.choice(word_list)
    return random_word

selected_word = select_random_word(word_list)
print("Random word:", selected_word)

guess = input("Enter a single letter: ")

if len(guess) == 1 and guess.isalpha():  #Python isalpha() method returns true if all characters in the string are alphabetic and returns false if not
                                         #single leter must be comparable to one single letter only
    print("Good guess!")
      
else:
    print("Oops! That is not a valid input. Please enter a single alphabetical character.")