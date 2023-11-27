## Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

This is an easy to play game in Python based on the childhood game of Hangman. This Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts. This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. I have based the game based on guessing a favourite fruit.

## Building the Code
On this project the code has been built line by line starting with creating a simple list and then printing that list. 
Subsequent updates have entailed building the game, first of all changing the code so that it generates a random word
from the list to adding an input asking for the user to enter one word only. 

This is the first process of building the game.  Files milestone_2 is where the list of 5 words was generated and is further used to build out the completion of the code through to milestone_3. 

Files milestone_3 and milestone_4 use object oriented programming principles to build out the final game.  

The code uses the random module to randomy choose a word from the following list: 
["Banana", "Apple", "Guava", "Peach", "Melon"]

## How to Play the Game
The code starts by asking the player to enter a letter which are derived from the secret word, chosen at random by the game from the list of the above words.  

The job of the player is to input a single letter to guess the word chosen randomly from the list.  The player has 5 tries.  

The letter must be a single alphabetical letter.  There are checks coded in the game to ensure that the player: 

a) does not input a letter(character) that is not an alphabetical letter
b) enter a letter they have previously entered.  

If all five tries have been used, and the player has not guessed the word, the game will print "You Lost1".  If the user guesses correctly that game will print
"Congratulations.  You won the game!".


The game is coded in Python.


