class Students:
    def __init__(self,first,last,major,gpa,probation):
        self.first=first
        self.last=last
        self.major=major
        self.gpa=gpa
        self.probation=probation

student1= Students("Connor", "Perron", "CPIS", 4.0, False)
print(student1.first)
print(student1.last)
print(student1.major)
print(student1.gpa)
print(student1.probation)
