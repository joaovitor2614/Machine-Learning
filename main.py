import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if (guess < random_number):
            print('To low!')
        elif (guess > random_number):
            print('To high!')
    print(f'You guessed right, the number is {random_number}')

def computerGuess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} to high(H), to low (L), or correct(C) ?').lower()
        if (feedback == 'h'):
            high = guess - 1
        elif (feedback == 'l'):
            low = guess + 1
    print(f'The computer guessed you number! {guess} is the correct one!')
computerGuess(600)