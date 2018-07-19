import random

number_1 = random.randint(1, 10)
number_2 = 0

while number_1 != number_2:
    print('num1: ' , number_1)
    print('num2: ' , number_2, "\n")
    number_2 = number_1
    number_1 = random.randint(1, 10)

print('Their vaules are\nnum1: ', number_1, '\nnum2: ', number_2)