# word = input('Choose a word?')

# if word[-1] == 'x' or word[-2:] == 's':
#     print(word + 'es')

# if word[-1] in ('x', 's'):
#     print(word + 'es')
# elif word[-2:] in ('th', 'sh', 'ch'):
#     print(word + 'es')
# else:
#     print(word + 's')

# z = 0
# for x in range(20):
#     print(2 ** x)
#     z += (2 ** x)
# print(z)

# highest_num = 0
#
# places = 1099511627776
#
# for p in range(places):
#     highest_num += 2 ** p
#
# print(highest_num)

total = 0
for x in range(256):
    total += 2 ** x
    print(x, total)