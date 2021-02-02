inches = float(input("Enter a length in inches: "))
centimeters = inches * 2.54
print(f"There are {centimeters:.2f} centimeters in ",inches,"inches")
pounds = int(input("Enter a number of pounds: "))
kg = pounds/2.2
print(f"There are {kg:.2f} kilograms in",pounds,"pounds")


faren = float(input("Enter a farenheight temperature: "))
cel = (faren-32) *(5/9)
print(f"Ther are {cel:.2f} celsius degrees in", faren,"farenheight degrees,")
payRate = float(input("What is your hourly pay in dollars and cents? "))
hours = int(input("How many hours did you work this week? "))
pay = payRate * hours
print(f"You made ${pay:.2f} this week.")
