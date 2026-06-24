import random

words = ["python", "rocket", "jungle", "castle", "bridge"]

def play():
    word = random.choice(words)
    guessed = []
    wrong = 0
    max_wrong = 6


    hangman = [
        "  _____",
        " |     |",
        " |     O",
        " |    /|\\",
        " |    / \\",
        " |",
        "_|_"
    ]

    while wrong < max_wrong:
        # Draw hangman
        print("\n")
        for i in range(wrong + 2):
            if i < len(hangman):
                print(hangman[i])

        # Show word
        display = ""
        for letter in word:
            if letter in guessed:
                display += letter + " "
            else:
                display += "_ "

        print("\nWord:", display)
        print(f"Wrong guesses: {wrong}/{max_wrong}")
        
        if guessed:
            print("Letters guessed:", ", ".join(sorted(guessed)))

        # Check win
        if "_" not in display:
            print("\n🎉 You guessed it! The word was:", word)
            return

        # Get input
        guess = input("\nGuess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
        elif guess in guessed:
            print("You already guessed that letter!")
        elif guess in word:
            guessed.append(guess)
            print("Correct!")
        else:
            guessed.append(guess)
            wrong += 1
            print(f"Wrong! {max_wrong - wrong} chances left.")

    print("\nYou lost! The word was:", word)

# Main loop
while True:
    print("=" * 30)
    print("WELCOME TO HANGMAN GAME")
    print("=" * 30)
    play()
    
    again = input("\nPlay again? (y/n): ").lower()
    if again != "y":
        print("Thanks for playing!")
        break