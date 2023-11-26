import random

class Hangman:  #defines class named Hangman

    def __init__(self, word_list, num_lives=5): #initalises 
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []
        self.word = self._get_random_word() #will secretely retrieve a random word from the word_list
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))

    def _get_random_word(self):
        return random.choice(self.word_list)

    def check_guess(self, guess):
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")

            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess

            self.num_letters -= 1

        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")


    def ask_for_input(self):
        while True:
            guess = input("guess a letter:  ")


            if not guess.isalpha() or len(guess) != 1:
                 print("Invalid letter.  Please enter a single alphabetical letter.")

            elif guess in self.list_of_guesses:
                 print("You have already tried that letter. Please try again")

            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break


def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print("You Lost!")
            break

        elif game.num_letters > 0:
            game.ask_for_input()

        else:
            print("Congratulations. You won the game!")
            break

word_list = (["Banana", "Apple", "Guava", "Peach", "Melon"])
play_game(word_list)

