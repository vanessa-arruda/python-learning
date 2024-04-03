#create class
class Student:
    # instanciate the innitial atributes of the class
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    # method to get innitial information about the student
    def get_info(self):
        print("---------------------------")
        print("Student's information\n")
        print(f"Name: {self.name}\nAge: {self.age}\nCurrent grade: {self.grade}")
        print("---------------------------")
    # method to promote the student grade
    def promote(self):
        self.grade += 1
        print("Student's Grade promotion\n")
        print(f"{self.name} new grade is: {self.grade}")
        print("---------------------------")
    

#creating students
student1 = Student('Anna', 15, 9)
student1.get_info()
student1.promote()


