import random

print('-----------------------------------')
print('        GUESS THE NUMBER APP       ')
print('-----------------------------------')
print()

the_number = random.randint(0, 100)
guess = -1

while the_number != guess:
    guess = int(input('Guess a number between 1 and 100: '))
    if guess == the_number:
        print('Congratulations!! {} was the right number!!'.format(guess))
    elif the_number > guess:
        print('Sorry... {} was to low, try again!'.format(guess))
    else:
        print('Sorry... {} was to high, try again!'.format(guess))