from tabulate import tabulate
import mysql.connector as mys
my_con=mys.connect(host="localhost",username="root",password="Narmatha@24",database="employee_management")
cur_object=my_con.cursor()
hod_age="select  employee_id,HOD_Name,Department_id,Age from (Select employee.employee_id,Department.HOD_Name,Department.Department_id,(TIMESTAMPDIFF(YEAR, employee.dob, CURDATE())) AS age from employee join Department on employee.department_id=Department.department_id and employee.employee_name=Department.HOD_Name order by (TIMESTAMPDIFF(YEAR, dob, CURDATE())) asc  limit 1)a union select  employee_id,HOD_Name,Department_id,Age from (Select employee.employee_id,Department.HOD_Name,Department.Department_id,(TIMESTAMPDIFF(YEAR, employee.dob, CURDATE())) AS age from employee join Department on employee.department_id=Department.department_id and employee.employee_name=Department.HOD_Name order by (TIMESTAMPDIFF(YEAR, dob, CURDATE())) desc  limit 1)a"
cur_object.execute(hod_age)
res=cur_object.fetchall()
print(tabulate(res,headers=["employee_id","HOD_Name","Department_id","Age"]))
my_con.close()
