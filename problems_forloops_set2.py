# for x in range(9):
#     for x in range(9):
#         print('*', end = ' ')
#     print()

# for x in range(10, 0, -1):
#     print(x)

# number = int(input('Choose a number'))
# for x in range(number):
#     for x in range(number):
#         print('*', end = ' ')3
#     print()

number = int(input('Choose a number'))
for x in range(1, number+1):
    for y in range(1, x+1):
        print('*', end = ' ')
    print()
for x in range(number+1, 1, -1):
    for y in range(x-1, 1, -1):
        print('*', end = ' ')
    print()