"create a company's payroll"

class Employee:
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    #method
    def calculate_paycheck(self):
        return self.salary/52