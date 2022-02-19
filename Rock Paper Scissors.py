import random


def game():
    user = input("What is your choice 'r' for rock, 'p' for paper and 's' for scissors \n")
    computer = random.choice(['r', 'p', 's'])
    print(f"{computer} is computer's choice")

    if user == computer:
        return 'Tie'

    if is_win(user, computer):
        return 'You Win!!!'
    else:
        return 'You lost!'


# r > s, s > p, p > r
def is_win(player1, player2):
    if (player1 == 'r' and player2 == 's') or (player1 == 's' and player2 == 'p') \
            or (player1 == 'p' and player2 == 'r'):
        return True

print(game())