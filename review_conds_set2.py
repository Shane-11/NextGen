# answer = input('Want a job?')
#
# if answer.lower() == 'no':
#     print('Good bye')
# elif answer.lower() == 'yes':
#     answer = input('Do you have experience? (yes/no)')
#     if answer.lower() == 'no':
#         print(('You can apply to an entry-level job'))
#     elif answer.lower() == 'yes':
#         answer = int(input('How many years?'))
#         if answer <= 3:
#             print('You can apply to a mid-level job')
#         else:
#             print('You can apply for a senior-level job.')
# else:
#     print('Thats not a valid answer')

# hungry = input('Are you hungry?')
# money = input('Do you have a money?')

# hungry = 'yes'
# money = 'no'
#
# if hungry == 'yes' and money == 'yes':
#     print("Here's a menu")
# elif hungry == 'yes' and money == 'no':
#     print('Time for leftovers')
# elif hungry == 'no'and money == 'yes':
#     print('Buy yourself something')
# elif hungry == 'no' and money == 'no':
#     print("Let's read a book")
#
# if hungry == 'yes':
#     if money == 'yes':
#         print("Here's a menu")
#     elif money == 'no':
#         print('Time for leftovers')
# elif hungry == 'no':
#     if money == 'yes':
#         print('Buy yourself something')
#     elif money == 'no':
#         print("Let's read a book")

import random

dice_one = random.randint(1, 6)
dice_two = random.randint(1, 6)

print(dice_one)
print(dice_two)

if dice_one == dice_two or dice_one+dice_two == 6 or dice_one+dice_two == 3:
    print('You win')
else:
    print('You lost')
