from tabulate import tabulate
import mysql.connector as mys
my_con=mys.connect(host="localhost",username="root",password="Narmatha@24",database="employee_management")
cur_object=my_con.cursor()
dept_query="create table Department ( Department_id int not null primary key,Department_name varchar(60) not null,HOD_name varchar(60)not null)"
cur_object.execute(dept_query)
cur_object1=my_con.cursor()
val_query="insert into department (Department_id,Department_name,HOD_Name) values(%s,%s,%s)"
values=[('101','CSE','Narmatha'),('102','ECE','Lalitha'),('103','EEE','Karthika'),('104','ICE','Surya')]
cur_object1.executemany(val_query,values)
my_con.commit()
cur_object2=my_con.cursor()
query="select * from department"
cur_object2.execute(query)
res=cur_object2.fetchall()
print(tabulate(res,headers=["Department_id","Department_name","HOD_Name"]))
my_con.close()


