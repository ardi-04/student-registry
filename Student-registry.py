class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []


    def add_grade(self, grade):
        self.grades.append(grade)        
    def get_average(self):
        final_average = sum(self.grades) / len(self.grades)
        return final_average

    def get_highest_grade(self):
        highest_grade = max(self.grades)
        print(f"The highest grade is {highest_grade}")
    
    
    def get_lowest_grade(self):
        lowest_grade = min(self.grades)
        print(f"The lowest grade is {lowest_grade}")

    def introduce(self):
        print(f"Hi! my name is {self.name}, I'm {self.age} years old and my average is {self.get_average()}. My highest grade is {max(self.grades)} and my lowest is {min(self.grades)}")

class GraduateStudent(Student):
    def __init__(self, name, age, thesis_title):
        super().__init__(name, age)
        self.thesis_title = thesis_title

    def defend_thesis(self):
        print(f"{self.name} is defending: {self.thesis_title}")

    def introduce(self):
        super().introduce()
        print(f"and my thesis is {self.thesis_title}")

def save_students(filename, students):
    with open(filename, "w") as f:
        for student in students:
            studentStrGrade = ",".join(map(str, student.grades))
            final = f"{student.name} , {student.age}, {studentStrGrade}"
            finalNa = final.strip()
            f.write(finalNa + "\n")
            

def load_students(filename):

    students = []
    try:    
        with open(filename, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                parts = line.split(",")
                print(line)
                print(parts)
                new_student  = Student(parts[0], int(parts[1]))
                for studGrades in parts[2:]:
                    gradeFloat = float(studGrades)
                    new_student.add_grade(gradeFloat)
                students.append(new_student)
    except FileNotFoundError:
        print("File is not exising!")

    return students           

def add_students(students):
    counter = 0
    gradeInput = 0
    userChecker = "y"
    
    while userChecker == "y":
        try:
            studentname = input("What is the student name?: ")
        except ValueError:
            print("Please enter a valid input!")
        try:    

            studentAge = int(input("What is the student age?: "))
            gradesQuantity = int(input("How many grades to enter?: "))
            new_students = Student(studentname, studentAge)  
            while counter != gradesQuantity:
                gradesInput = float(input(f"Enter the {counter + 1} grade: "))
                new_students.add_grade(gradesInput)
                counter += 1

            counter = 0
            userChecker = input("Do you want to add more student? y or n: ").lower() 
            students.append(new_students)
        except ValueError:
            print("Please enter a valid input!")

    return students 

    
def main():
    quitMenu = 3;
    menu_input = 0

    students = load_students("registry.txt")
    while menu_input != 3:
        try:
            menu_input = int(input(" \n1. Add Student \n2.View all students \n3.Save and quit \nWhat do you want to do?:"))
            if menu_input > 3 or menu_input < 1:
                print("Please choose in the following choices")
            else:
                if menu_input == 1:
                    add_students(students)
                elif menu_input == 2:
                    for student in students:
                        student.introduce()
                elif menu_input == 3:
                    save_students("registry.txt", students)
            
        except ValueError:
            print("Please put a valid input!")
        



main()
