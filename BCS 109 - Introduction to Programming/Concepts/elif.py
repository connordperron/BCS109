num = int(input("Enter an integer number: "))
if num % 2 == 0:
    if num % 3 == 0:
        print(f"{num} is divisible by both 2 and 3")
    else:
        print(f"{num} is divisible by 2, but not by 3")

else:
    if num % 3 ==0:
        print(f"{num} is divisible by 3, but not by 2")
    else:
        print(f"{num} is not divisible by 2 or 3")
