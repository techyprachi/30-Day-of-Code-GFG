class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        average = sum(self.scores) / len(self.scores)
        if average >= 90:
            return 'O'  # Outstanding
        elif average >= 80:
            return 'E'  # Exceeds Expectations
        elif average >= 70:
            return 'A'  # Acceptable
        elif average >= 55:
            return 'P'  # Poor
        elif average >= 40:
            return 'D'  # Dreadful
        else:
            return 'T'  # Troll

# Input handling
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # Not used directly, but part of input format
scores = list(map(int, input().split()))

# Create Student object and display results
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
