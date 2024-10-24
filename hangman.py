#hangman console game
import requests

def generate_five_letter_word():
    response = requests.get("https://random-word-api.herokuapp.com/word?number=1&length=5")
    if response.status_code == 200:
        return response.json()[0]
    else:
        return "apple"  # Fallback word in case of an error
    
word_to_guess = generate_five_letter_word().casefold()

print("Welcome to Hangman!")
print("I'm thinking of a word with 5 letters.")
print("You have 6 guesses to guess the word.")
print("Good luck!", end="\n\n")

counter = 0
guessed_letters = []

word_display = ["_"] * len(word_to_guess)

def print_hangman_stage(stage):
    stages = [
        """
         -----
         |   |
         |
         |
         |
         |
        -----
        """,
        """
         -----
         |   |
         |   O
         |
         |
         |
        -----
        """,
        """
         -----
         |   |
         |   O
         |   |
         |
         |
        -----
        """,
        """
         -----
         |   |
         |   O
         |  /|
         |
         |
        -----
        """,
        """
         -----
         |   |
         |   O
         |  /|\\
         |
         |
        -----
        """,
        """
         -----
         |   |
         |   O
         |  /|\\
         |  /
         |
        -----
        """,
        """
         -----
         |   |
         |   O
         |  /|\\
         |  / \\
         |
        -----
        """
    ]
    print(stages[stage])

def get_user_guess(guessed_letters):
    guess = input("Guess a letter: ").casefold()
    if len(guess) != 1:
            print("Please enter a single letter.")
    else:
        guessed_letters.append(guess)
    return guess


def check_guess(guess, word_to_guess, word_display):
    correct = False
    for i, letter in enumerate(word_to_guess):
        if letter == guess:
            word_display[i] = guess
            correct = True
    return correct
    
while counter < 6:
    print("Current word:", " ".join(word_display))
    guess = get_user_guess(guessed_letters)
    
    if guess in guessed_letters[:-1]: 
        print("You already guessed that letter. Try again.", end="\n\n")
        continue
    
    if check_guess(guess, word_to_guess, word_display):
        print("Correct guess!", end="\n\n")
    else:
        counter += 1
        print_hangman_stage(counter)
        print(f"Wrong guess. You have {6 - counter} guesses left.", end="\n\n")
    
    if "_" not in word_display:
        print(f"Congratulations! You guessed the word: {word_to_guess}",end="\n\n")
        break
    
    if counter == 6:
        print(f"Game over! The word was: {word_to_guess}", end="\n\n")
        break
