#Connor Perron

#Prompting Questions
billAmount=float(input("How much was the bill? $"))
tipAmount=float(input("What percentage of a tip would you like to leave? (Please enter in .xx format) "))
numPersons=int(input("How many people did you dine with?(Include yourself): "))

#Calculating tip
tipAmount=(tipAmount * billAmount)

#Calculating total w/ tip
totalBill=(tipAmount + billAmount)

#Calculating how much each person will pay
personPays=(totalBill / numPersons)


print(f"Reciept \nTip Amount: ${tipAmount:.2f} \nTotal Bill: ${totalBill:.2f} \nEach person SHOULD pay ${personPays:.2f}")
