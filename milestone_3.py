import random

word_list = ["Banana", "Apple", "Guava", "Peach", "Melon"]

selected_word = random.choice(word_list)  # Randomly select a secret word

while True:
    guess = input("Enter a letter: ")  # Prompt for user input

    if len(guess) == 1 and guess.isalpha():  #check iof the guess is a single alphabetical character
        if guess in selected_word:  #if guess is in random word chosen by computer from word list
            print("Good guess!", guess, "is in the word.")
            break  # Exit loop if input is valid and guess is correct
        else:  #letter in an alphabetical character but is not in the selected word 
            print("Sorry,", guess, "is not in the word. Try again.")
    else:  # If input is invalid and is not an alphabetical character
        print("Invalid letter. Please, enter a single alphabetical character.")

