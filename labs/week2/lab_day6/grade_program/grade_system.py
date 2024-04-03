from student import Student

class GradeSystem:
    def __init__(self):
        self.student = []
    def add_student(self, new_student):
      self.student.append(new_student)
    def get_info(self):
        print("Student's information`\n")
        for i in self.student:
            print(f"Name: {i.name}\nAge: {i.age}\nCurrent grade: {i.grade}")
            print("---------------------------")
    def display_new_grade(self):
        print("Student's Grade promotion\n")
        for i in self.student:
            print(f"{i.name} new grade is: {i.promote()}")
            print("---------------------------")
def main():
    grade_data = GradeSystem()

    student1 = Student('Anna', 15, 9)
    grade_data.add_student(student1)
    student2 = Student('Johnny', 14, 8)
    grade_data.add_student(student2)
    student3 = Student('Carla', 7, 3)
    grade_data.add_student(student3)

    grade_data.get_info()
    grade_data.display_new_grade()
main()