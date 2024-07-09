import random

def hangman():
    word = 'candycrush'
    guessed_word = ['_'] * len(word)
    guessed_chars = set()
    guess_count = 6

    while guess_count > 0:
        print("\nCurrent word:", ' '.join(guessed_word))
        print("Guessed characters:", sorted(guessed_chars))
        print("Remaining guesses:", guess_count)

        guess = input("Enter your guess (a single letter): ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single alphabetical character.")
            continue
        
        if guess in guessed_chars:
            print("You have already guessed this character. Try a different one.")
            continue

        guessed_chars.add(guess)

        if guess in word:
            print("Good guess!")
            for i, char in enumerate(word):
                if char == guess:
                    guessed_word[i] = guess
            if '_' not in guessed_word:
                print("Congratulations! You've guessed the word:", word)
                break
        else:
            print("Incorrect guess.")
            guess_count -= 1

        if guess_count == 0:
            print("Game Over! You've run out of guesses. The word was:", word)


hangman()
