#Connor Perron

#main function
def main():

    #Local Variables
    feet = 0.0
    inches = 0.0

    #Get the number of feet from the user
    feet = float(input('Enter the number of feet: '))
    
    #Display the corresponding number of inches
    inches = feet_to_inches(feet)
    print(feet, ' Feet =' ,inches, " Inches")


#The feet_to_inches function recieves the number of feet and returns the number of inches

def feet_to_inches(feet):
    return 12 * feet


#Call the main function
main()
    
