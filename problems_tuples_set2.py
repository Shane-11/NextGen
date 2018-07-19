# correct_guesses = ()
# all_letters = ()
# word = input('Pick a word')
#
# T = 0
#
# while len(correct_guesses) != len(word) and T < 6:
#     print(all_letters)
#     guess = input('Guess a letter?') .lower()
#     if guess in word and guess not in correct_guesses:
#         print('Good Guess', end = ' ')
#         correct_guesses += (guess,)
#     else:
#         T += 1
#     all_letters += (guess,)
#     for w in word:
#         if w in correct_guesses:
#             print(w, end=' ')
#         else:
#             print('_', end=' ')
#     print()
# if len(correct_guesses) == len(word):
#     print('You win')
# else:
#     print('You lost. Better luck next time')

import random

word_list = ('dog', 'bird', 'truck')
word = random.choice(word_list)
correct_guesses = ()
num_turns = 0
print(word)

for letter in word:
    print('_', end = ' ')

# print()
# player_letter = input('\nGuess a letter?')
# player_letter = player_letter.lower()
#
# if player_letter in word:
#     print('Good guess!')
#     correct_guesses += (player_letter,)
#
# for w in word:
#     if w in correct_guesses:
#         print(w, end=' ')
#     else:
#         print('_', end=' ')

while len(word) > len(correct_guesses):
    num_turns += 1

    print()
    print(num_turns)

    player_letter = input('\nGuess a letter?')
    player_letter = player_letter.lower()

    if player_letter in word:
        print('Good guess!')
        correct_guesses += (player_letter,)

    for w in word:
        if w in correct_guesses:
            print(w, end=' ')
        else:
            print('_', end=' ')
if len(word) > len(correct_guesses):
    print('\nYou lost. The word was', word)
else:
    print('\nYou got it!')