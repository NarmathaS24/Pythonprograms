import mysql.connector as mysq
mycon=mysq.connect(host="localhost",user="root",password="Narmatha@24",database="Hospital_Management")
cursor_obj1=mycon.cursor()
doctor="create table doctor (doctor_id int(20) not null primary key,doctor_name varchar(20),adrress varchar(20),phoneno int(20))"
cursor_obj1.execute(doctor)

