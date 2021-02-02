#Connor Perron

age = int(input("Enter your age as an integer: "))

if age >= 3 and age <= 21:
    print("You are still young!")

elif age >= 22 and age <= 40:
    print("You are getting to be more mature!")

elif age >= 41 and age <= 64:
    print("You are on a roll!")

elif age >= 65 and age <= 100:
    print("Your golden years. Enjoy them!")

else:
    print("I can't believe you are less than 3 or older than a hundred!")
    
