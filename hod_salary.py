from tabulate import tabulate
import mysql.connector as mys
my_con=mys.connect(host="localhost",username="root",password="Narmatha@24",database="employee_management")
cur_object=my_con.cursor()
hod_salary="Select Department.Department_id,Department.Hod_Name,(employee.Salary)as Salary FROM employee join Department on Employee.Department_id=Department.Department_id  and Employee.Employee_Name=Department.HOD_Name where Salary> (select (Salary/HODCount)as Salary from  (Select count(Department.HOD_Name)as HODCount, sum(employee.Salary)as Salary FROM employee join Department on Employee.Department_id=Department.Department_id and Employee.Employee_Name=Department.HOD_Name)a)"
cur_object.execute(hod_salary)
res=cur_object.fetchall()
print(tabulate(res,headers=["Department_id","HOD_Name","Salary"]))
my_con.close()
