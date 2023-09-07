from tabulate import tabulate
import mysql.connector as mys
my_con=mys.connect(host="localhost",username="root",password="Narmatha@24",database="employee_management")
cur_object=my_con.cursor()
avg_salary="select department.Department_name as Department_name,avg(employee.salary)as Salary from employee join department  on employee.Department_id=department.Department_id group by department.Department_name"
cur_object.execute(avg_salary)
res=cur_object.fetchall()
print(tabulate(res,headers=["Department_name","Salary"]))
my_con.close()
