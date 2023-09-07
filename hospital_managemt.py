import mysql.connector as mysq
mycon=mysq.connect(host="localhost",user="root",password="Narmatha@24")
if mycon:
    print("Successfully connection established.....")
cursor_obj=mycon.cursor()
query="create database Hospital_Management"
cursor_obj.execute(query)
print("Database created successfully")



