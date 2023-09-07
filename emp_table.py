from tabulate import tabulate
import mysql.connector as mys
my_con=mys.connect(host="localhost",username="root",password="Narmatha@24",database="employee_management")
cur_object=my_con.cursor()
emp_query="create table Employee(Employee_id int not null primary key,Employee_Name varchar(150), DoB date,Salary int, Department_id int , foreign key(Department_id) references Department(Department_id))"
cur_object.execute(emp_query)
cur_object1=my_con.cursor()
val_query="insert into Employee(Employee_id,Employee_Name,DoB,Salary,Department_id) values(%s,%s,%s,%s,%s)"
values=[('111','Karishma','1990-12-01','10000','101'),('112','Narmatha','1995-11-21','40000','101'),
        ('113','reshma','1994-08-31','20000','101'),('114','lisa','1992-07-11','30000','101'),
        ('115','swathi','1990-06-19','25000','101'),
        ('116','Lalitha','1980-07-15','60000','102'),('117','Karthick','1986-05-16','40000','102'),
        ('118','Dhinesh','1987-03-18','35000','102'),('119','Jerome','1998-04-20','22000','102'),
        ('120','Hema','1980-02-22','32000','102'),
        ('121','Pregya','1980-01-01','50000','103'),('122','Karthika','1983-03-04','55000','103'),
        ('123','Sathish','1976-06-06','50000','103'),('124','Selvi','1988-11-08','42000','103'),
        ('125','Ganesh','1994-12-09','25000','103'),
        ('126','Deiva','1979-08-12','15000','104'),('127','Anjali','1981-09-15','30000','104'),
        ('128','Manoj','1980-05-25','10000','104'),('129','Surya','1990-07-25','68000','104'),('130','Magisha','1998-01-30','32000','104')]
cur_object1.executemany(val_query,values)
my_con.commit()
cur_object2=my_con.cursor()
query="select * from Employee"
cur_object2.execute(query)
res=cur_object2.fetchall()
print(tabulate(res,headers=["Employee_id","Employee_Name","DoB","Salary","Department_id"]))
my_con.close()

