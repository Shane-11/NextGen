import random

x = random.randint(1, 10)

print('Think of a number between 1 and 10. I am going to guess. Ready?')

print('Is it ', x, '?', sep='')

answer = input()

no = 'Guess again'

tries = 3

while answer.lower() == 'no' and tries > 1:
    x = random.randint(1, 10)
    print('Is it ', x, '?', sep='')
    answer = input()
    tries -=1

if answer == 'yes':
    print("I got it")

