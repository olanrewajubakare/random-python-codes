import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            trial = random.randint(low, high)
        else:
            trial = low
            print(f"Yay! The computer guessed the number {trial} correctly")
            break
        feedback = input(f"if {trial} is too high enter h, if {trial} is too low enter l, if {trial} is correct enter c ")
        if feedback == 'h':
            high = trial - 1
        elif feedback == 'l':
            low = trial + 1
        else:
            print(f"Yay! The computer guessed the number {trial} correctly")

computer_guess(100)