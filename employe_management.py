import mysql.connector as mys
my_con=mys.connect(host="localhost",username="root",password="Narmatha@24")
if my_con:
    print("Connection established successfully")
cur_object=my_con.cursor()
query="CREATE DATABASE employee_management"
cur_object.execute(query)
my_con.close()