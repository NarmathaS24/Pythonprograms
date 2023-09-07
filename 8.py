class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def __del__(self):
        print("Deleting object")

    def delete_data_member(self):
        del self.a
        print("Data member 'a' deleted")

    def delete_member_function(self):
        del self.add
        print("Member function 'add' deleted")

    def __hide(self):
        print("Data hidden")

obj = MyClass(2, 3)
print(obj.add())

# Deleting object
del obj

# AttributeError: 'MyClass' object has no attribute 'a'
print(obj.a)

# AttributeError: 'MyClass' object has no attribute 'add'
print(obj.add())

obj = MyClass(2, 3)
obj.delete_data_member()

# AttributeError: 'MyClass' object has no attribute 'a'
print(obj.a)

obj = MyClass(2, 3)
obj.delete_member_function()

# AttributeError: 'MyClass' object has no attribute 'add'
print(obj.add())

# AttributeError: 'MyClass' object has no attribute '__hide'
obj.__hide()

# Data hidden
obj._MyClass__hide()
