myString="     Hello, World!     "
print(myString.upper())
print(myString.lower())
print(myString.title())
print(myString.capitalize())
print(myString.lstrip())
print(myString.rstrip())
print(myString.center(61,"*"))
print(myString.isdigit())
print(myString.istitle())
print(myString.swapcase())
print(myString.join("!*!"))
print(myString.replace("World","There"))
print(max(myString))

text = input("Enter 'y' or 'n' and type a lowercase 'y' or 'n':")
text = text.upper()
print("Your respons was converted to uppercase", text)

text = input("Enter 'y' or 'n' and type an uppercase 'y' or 'n':")
text = text.lower()
print("Your respons was converted to lowercase", text)
