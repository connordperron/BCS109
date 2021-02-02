print("Calculator")
print("Type + for additiom, - for subtraction, * for multiplication, and / for division")
operation=(input("Enter thr operation you want to complete: "))
num1= int(input("Enter your first number: "))
num2= int(input("Enter your second number: "))

if operation == '+':
    result = num1 + num2
    print("The numbers added are equal to: ",result)

elif operation == '-':
    result = num1 - num2
    print("The numbers subtracted are equal to: ",result)

elif operation == '*':
    result = num1 * num2
    print("The numbers multiplied are equal to: ",result)

elif operation == '/':
    result = num1 / num2
    print("The numbers divided are equal to: ",result)

else:
    print("You have no entered a valid operator ")
