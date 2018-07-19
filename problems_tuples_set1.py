# text = "How are you today good sir? I hope you are well."
# text = text.replace('?' ' ')
# text = text.replace('.' ' ')
# text.split()
# tuple(text.split())
# text = tuple(text.split())
# print(len(text))

# y = ('Kathy', 'Benji', 'Ian', 'Alejandro')
# for x in y:
#     print(len(x))
# import random
#
# first_names = ('Emilio', 'Victoria', 'Neil', 'Julia', 'Rachel', 'Stephen', 'Robert')
# last_names = ('Howard', 'Lane', 'Ortiz', 'Franklin', 'Butler', 'Cole', 'Byrne')
#
# names = int(input('How many names?'))
#
# for n in range(names):
#     print(random.choice(first_names), random.choice(last_names))

import random
x = random.randint(1, 10)
old_guesses = (x,)
print('Think of a number between 1 and 10. I am going to guess. Ready?')
print('Is it ', x, '?', sep='')
answer = input()
no = 'Guess again'
while answer.lower() == 'no':
    x = random.randint(1, 10)
    while x in old_guesses:
        x = random.randint(1, 10)
    print(old_guesses)
    old_guesses = old_guesses + (x,)
    print('Is it ', x, '?', sep='')
    answer = input()
if answer == 'yes':
    print("I got it")