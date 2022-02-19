import random


def guess(x):
    random_number = random.randint(1, x)
    guess_number = 0

    while guess_number != random_number:
        guess_number = int(input(f"guess a number between 1 and {x} "))
        if guess_number > random_number:
            print(f"Sorry, {guess_number} is higher than my selected number. Guess Again!")
        elif guess_number < random_number:
            print(f"Sorry, {guess_number} is lower than random number. Guess Again!")
    print(f"Hurray! You guessed the number {random_number} correctly")


guess(10)
