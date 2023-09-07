import pandas as pd
employee_register = pd.DataFrame(columns=["EmpName", "EmpSalary", "EmpDesignation"], index=["EmpID"])
employee_register = employee_register.append({"EmpName": "Narmu", "EmpSalary": 50000, "EmpDesignation": "Manager"}, ignore_index=True)
print(employee_register)
employee_register = employee_register.append({"EmpName": "Keerthu", "EmpSalary": 35000, "EmpDesignation": "Assistant Manager"}, ignore_index=True)
print(employee_register)
