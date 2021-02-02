def welcome():
    myString ='Welcome to the integer calculator'
    print(myString.upper())
welcome()

def calculate():
    operation=input('''
        Please type the operator for the math operation you would like to complete:
        + for addition
        - for subtraction
        * for multiplication
        / for division
        % for modulus
        Type your choice please: ''')
    num1=int(input('Please enter the first integer number: '))
    num2=int(input('Please enter the second integer number: '))

    if operation == '+':
                print('The addition result is:', num1+num2)

    elif operation == '-':
                print('The subtraction result is:', num1-num2)

    elif operation == '*':
                print('The multiplication result is:', num1*num2)

    elif operation == '/':
                print('The division result is:', num1/num2)

    elif operation == '%':
                print('The remainder (if any) is:', num1%num2)

    else:
                print('You have not entered a valid operator, please run the program again.')

    again()

def again():
    calc_again = input('Do you want to calculate again> Please type Y for YES and N for NO ')

    if calc_again.upper()=='Y':
        calculate()

    elif calc_again.upper()=='N':
        print('See you later!')

    else:
        again()

calculate()
                
    
