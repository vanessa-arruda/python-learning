from employee import Employee

class Company:
 def __init__(self):
  self.employees = []

  def add_employee(self, new_employee):
   self.employees.append(new_employee)


def main():
 my_company = Company()

 