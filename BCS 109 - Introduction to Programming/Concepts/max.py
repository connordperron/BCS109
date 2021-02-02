#main module
def main():
            #Local variables
            average = 0.0
            grade1 = 0.0
            grade2 = 0.0
            grade3 = 0.0
            grade4 = 0.0
            grade5 = 0.0
    

            #get grades
            print("Enter the grades as scores from 0 to 100")
            grade1 = float(input("Please enter test grade 1: "))
            grade2 = float(input("Please enter test grade 2: "))
            grade3 = float(input("Please enter test grade 3: "))
            grade4 = float(input("Please enter test grade 4: "))
            grade5 = float(input("Please enter test grade 5: "))

            #calculate average
            average = calc_average(grade1, grade2, grade3, grade3, grade4, grade5)

            #display grade and average info
            print("\nGrade\t\Numeric Grade\tLetter Grade")
            print("---------------------------------------")
            print("Grade 1:\t",grade1,"\t\t",determine_grade(grade1))
            print("Grade 2:\t",grade2,"\t\t",determine_grade(grade2))
            print("Grade 3:\t",grade3,"\t\t",determine_grade(grade3))
            print("Grade 4:\t",grade4,"\t\t",determine_grade(grade4))
            print("Grade 5:\t",grade5,"\t\t",determine_grade(grade5))
            print("---------------------------------------")
            print("Average Grade:\t",average,"\t\t",determine_grade(average))

#The calc function returns the average of 5 grades
def calc_average(grade1, grade2, grade3, grade3, grade4, grade5):
            return (grade1+grade2+grade3+grade4+grade5)/5.0

def determine_grade(grade):
            if grade >= 90:
                        return "A"
            elif grade >= 80:
                        return "B"
            elif grade >= 70:
                        return "C"
            elif grade >= 60:
                        return "D"
            else:
                        return "F"

main()
