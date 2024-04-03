# Todays LAB - Date 03/04-2024
# In this lab, we will create a Python program to model a basic student database using OOP concepts.

# 1. Define a Student Class:

# Define a class named Student with the following attributes:
# name: Name of the student (string).
# age: Age of the student (int).
# grade: Grade level of the student (int).

# 2. Add Methods:
# Add the following methods to the Student class:
# get_info( ): Method to display the student's information.
# promote ( ): Method to promote the student to the next grade level.

# 3. Test the Class:
# Create instances of the Student class and test its methods:
# Create a student named "Anna" with age 15 and grade 9. Use the get_info() method to display her information.
# Promote Anna to the next grade level using the promote() method, then use get_info() to display her updated information


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def promote(self):
        return self.grade + 1