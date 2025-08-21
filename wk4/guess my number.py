"""
Guess my Number Game
By
Otuekong Akpan
"""

import random

play_again = 'yes'
while play_again == 'yes':
    
    random_number = random.randint(0,100)
    guess = None
    count = 0

    while guess != random_number:
        guess = int(input("What is your guess? "))
        count += 1

        if guess > random_number:
            print("Lower")

        elif guess < random_number:
            print("Higher")

    print(f"You guessed it. It took you {count} guesses!")

    play_again = input("Would you like to play again? (yes/no) ")

print("Thank you for playing. Goodbye!")