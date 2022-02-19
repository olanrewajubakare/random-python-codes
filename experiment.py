import random

def guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess_number = random.randint(low, high)
        else:
            guess_number = high
            print(f"Yay! The computer guessed the number {guess_number} correctly")
            break
        if feedback == 'h':
            high = guess_number
        elif feedback == 'l':
            low = guess_number
        else:
            print(f"The guessed number is {guess_number}")
