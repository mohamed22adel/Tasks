import random

# list of words
words = ["apple", "banana", "lemon", "orange", "cherry"]

def scramble_word(word):
    scrambled = list(word)
    random.shuffle(scrambled)
    return ''.join(scrambled)

def word_scramble_game():
    # choose an original word
    original_word = random.choice(words)
    scrambled_word = scramble_word(original_word)
    
    attempts = 5

    print("Welcome to the Word Scramble Game!")
    print(f"Try to guess the original word from the scrambled word: {scrambled_word}")
    print(f"You have {attempts} attempts.")
    
    while attempts > 0:
        guess = input("Enter your guess: ").strip()
        
        if not guess:
            print("Invalid input! Please enter a guess.")
            continue
        
        if guess == original_word:
            print("Congratulations! You guessed the correct word!")
            return
        
        attempts -= 1
        if attempts > 0:
            print(f"Incorrect! Try again. You have {attempts} attempts left.")
        else:
            print(f"Sorry, you've run out of attempts. The correct word was '{original_word}'.")

                #start game
word_scramble_game()