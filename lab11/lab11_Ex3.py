def play_hangman():
    # Get the word to be guessed
    word_to_guess = input("Word to be guessed (Player 1, please enter a word): ").lower()
    guessed_word = ["-" for _ in word_to_guess]

    print("".join(guessed_word))

    attempts = 0
    guessed_letters = set()

    # Game loop
    while "-" in guessed_word:
        guess = input("Guess a letter (Player 2): ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please guess a single letter.")
            continue

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You have already guessed this letter.")
            continue

        # Record the guess
        guessed_letters.add(guess)
        attempts += 1

        # Reveal letter if present
        if guess in word_to_guess:
            for i, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[i] = guess

        # Display the current state of the word
        print("".join(guessed_word))

    print(f"Congratulations! You guessed the word in {attempts} guesses.")

play_hangman()
