# grade = int(input('What was your number grade?'))
#
# if grade >= 93:
#     print('A')
# elif grade >= 90:
#     print('A-')
# elif grade >= 87:
#     print('B+')
# elif grade >= 85:
#     print('B')
# elif grade >= 83:
#     print('B-')
#
operand_one = int(input("Enter operand: "))
operator = input("Enter + or - or * or / ")
operand_two = int(input("Enter operand: "))

if operator == '+':
    print(operand_one+operand_two)
elif operator == '-':
    print(operand_one - operand_two)
elif operator == '*':
    print(operand_one * operand_two)
elif operator == '/':
    print(operand_one / operand_two)
else:
    print("Can't recognize operator")
