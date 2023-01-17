print('                        SIMPLE CALCULATOR                        ')
print('1. ADDITION')
print('2. MULTIPLY')
print('3. SUBTRACT')
print('4. DIVISION')
print('5. stop')
math_symbols = int(input('ENTER 1, 2, 3, 4: '))

######################addition##########################
while True:

    if math_symbols == 1:
        first_number = int(input('Enter first number '))
        second_number = int(input('Enter second number '))
        sum = first_number + second_number
        print(sum)
        math_symbols = int(input('ENTER 1, 2, 3, 4: '))
        if math_symbols == 5:
            break
###############################MULTIPLY##################################


    elif math_symbols == 2:
        first_number = int(input('Enter first number '))
        second_number = int(input('Enter second number '))
        sum = first_number * second_number
        print(sum)
        math_symbols = int(input('ENTER 1, 2, 3, 4: '))
        if math_symbols == 5:
            break
###########################SUBTRACT#########################


    elif math_symbols == 3:
        first_number = int(input('Enter first number '))
        second_number = int(input('Enter second number '))
        sum = first_number - second_number
        print(sum)
        math_symbols = int(input('ENTER 1, 2, 3, 4: '))
        if math_symbols == 5:
            break
##############################DIVIDE##############################


    elif math_symbols == 4:
        first_number = int(input('Enter first number '))
        second_number = int(input('Enter second number '))
        sum = first_number / second_number
        print(sum)
        math_symbols = int(input('ENTER 1, 2, 3, 4: '))
        if math_symbols == 5:
            break

    else:
        print('invalid')
        break

