#Connor Perron

def main():
            x = 0.0
            y = 0.0
            z = 0.0

            print("Enter three numbers")
            x = float(input("Please enter the first number: "))
            y = float(input("Please enter the second number: "))
            z = float(input("Please enter the third number: "))

            sumAndAverage(x,y,z)


def sumAndAverage(x,y,z):
            sum= x+y+z
            average= sum/3
            print(f"The sum of your three numbers is:",sum)
            print(f"The average of your three numbers is:",average)

main()
