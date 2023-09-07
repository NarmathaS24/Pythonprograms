from tabulate import tabulate
import mysql.connector as mysq
mycon=mysq.connect(host="localhost",user="root",password="Narmatha@24",database="Student")
if mycon:
    print("....................database connected........................")
def insert(RegNo,name,Age,Mailid):
    cur_obj=mycon.cursor()
    query="insert into student_details(RegNo,name,Age,Mailid) values(%s,%s,%s,%s)"
    values=(RegNo,name,Age,Mailid)
    cur_obj.execute(query,values)
    cur_obj.commit()
    cur_obj.close()

def update():
    pass
def delete():
    pass
def select():
    query = "Select * from Student_details"
    mycur = mycon.cursor()
    mycur.execute(query)
    res = mycur.fetchall()
    print(tabulate(res,headers=["RegNo","Name","Age","MailId"]))
    print("..................Selected Successfully.......................")
while True:

    print("1. Insert: ")
    print("2. Update: ")
    print("3. Delete: ")
    print("4. Select: ")
    print("5. Quit/Exit: ")
    x = int(input("Enter the choice:"))
    if x == 1:

        RegNo = input("Enter the Register Number to be inserted: ")
        name = input("Enter the name to be inserted: ")
        Age = input("Enter the age to be inserted: ")
        Mailid = input("Enter the mail id to be inserted: ")
        insert(RegNo,name,Age,Mailid)
        print(".................Successfully inserted...............")
    elif x == 2:
        pass
    elif x == 3:
        pass
    elif x == 4:
        select()
    else:
        print("Invalid input.....")







