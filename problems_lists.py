# main_course = ['steak', 'salmon', 'rice']
# main_course.insert(0, 'stew')
# print(main_course)
# food_1= str(input('Enter a food'))
# food_2= str(input('Enter a food'))
# food_3= str(input('Enter a food'))
# main_course.extend([food_1, food_2, food_3])
# main_course.extend(['burger', 'tilapia', 'gulash'])
# print(main_course)
# side_course = ['carrots', 'fries', 'salad']
# course_style = ['seared', 'boiled', 'baked']
# import random
# main = random.choice(main_course)
# side = random.choice(side_course)
# style = random.choice(course_style)
# print('Tonight I will serve', style, main, 'with', side)

# problem = input("enter an problem: ") # 1 + 2
# list = problem.split()
# operand_one = int(list[0])
# operator = list[1]
# operand_two = int(list[2])
#
# if operator == '+':
#     print(operand_one+operand_two)
# elif operator == '-':
#     print(operand_one - operand_two)
# elif operator == '*':
#     print(operand_one * operand_two)
# elif operator == '/':
#     print(operand_one / operand_two)
# else:
#     print("Can't recognize operator")

list = [1, 2, 3, 4]
for x in list:
    y = 0
    y += x
    print(y)