class Student:
    def __init__(self, studentname: str, studentrollno: int):
        self.studentname = studentname
        self.studentrollno = studentrollno

    def display(self):
        print(f"Student Name: {self.studentname}")
        print(f"Student Roll No: {self.studentrollno}")
student = Student("Narmatha", 305)
student.display()
