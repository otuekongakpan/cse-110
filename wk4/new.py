secret = "church"
count = 0
letter_count = len(secret)

play_again = 'yes'
while play_again == 'yes':
    hint = "_" * letter_count
    count = 0

    print("Welcome to the wordle game!")
    print("Your hint is:", hint)

    while hint != secret:
        guess = input("What is your guess? ")
        count += 1

        if len(guess) > letter_count:
            print("The word is six letters and not more than.")
            continue
        elif len(guess) < letter_count:
            print("The word is six letters and not less than.")
            continue
        updated_hint = ""
        for i in range(len(secret)): 
            if guess[i] == secret[i]:  # Correct letter, correct position
                updated_hint += guess[i].upper()
            elif guess[i] in secret:  # Correct letter, wrong position
                updated_hint += guess[i].lower()
            else:  # Letter not in the secret word
                updated_hint += "_"

        hint = updated_hint
        print("Your hint is:", hint)

    print("You guessed it. Congratulations!")
    print(f"It took {count} guesses.")

    play_again = input("Do you want to play again? (yes/no) ").strip().lower()

print("Thank you for playing. Goodbye!")
