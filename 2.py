class Employee:
    def __init__(self, name, department, address, hourly_salary):
        self.name = name
        self.department = department
        self.address = address
        self.hourly_salary = hourly_salary
class Payroll(Employee):
    def __init__(self, name, department, address, hourly_salary):
        super().__init__(name, department, address, hourly_salary)
    def calculate_monthly_salary(self, hours_worked):
        monthly_salary = self.hourly_salary * hours_worked
        return monthly_salary
    def calculate_annual_salary(self, hours_worked):
        annual_salary = self.calculate_monthly_salary(hours_worked) * 12
        return annual_salary
employee1 = Payroll("Narmatha", "Developer", "123 Tamilnadu", 25.0)
monthly_salary = employee1.calculate_monthly_salary(160)
print(monthly_salary)
annual_salary = employee1.calculate_annual_salary(160)
print(annual_salary)