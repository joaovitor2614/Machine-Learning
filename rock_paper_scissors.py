import random
def play():
    user = input("'r' for rocks, 'p' for paper, 's' for scissors")
    computer = random.choice(['r', 's', 'p'])

    if (user == computer):
        return 'It\'s a tie'
    if isWin(user, computer):
        return 'You won!'
    
    return 'You lost!'

def isWin(player, opponent):
    if (player == 's' and opponent == 'p') \
    or (player == 'r' and opponent == 's') \
    or (player == 'p' and opponent == 'r'):
        return True
    
play()
