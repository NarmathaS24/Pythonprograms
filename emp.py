"""Create a class employee and mention following details:

Employee name, Department and Address of Employee,
Salary in each department hourly base and inherit the class to payroll class
and calculate salary of each person monthly and annually."""
class Employee:
    def __init__(self,Employee_name,Department,Address,Salary):
        self.Employee_name=Employee_name
        self. Department=Department
        self.Address=Address
        self.Salary=Salary
class Payroll(Employee):
    def __init__(self, Employee_name, Department, Address, Salary):
        Employee.__init__(Employee_name, Department, Address, Salary)
    def monthly_sal(self,Employee_name, Department, Address, Salary):
        sal=Employee.__init__(Employee_name, Department, Address, Salary)
        print(sal)


    def anual_sal(self):
        pass
                          
emp1=Employee("Narmatha","CSE","Coimbatore","20000")
person=Payroll(Employee)
person.monthly_sal()
