#customers.py
class Customer:
    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address

    def get_name(self):
        return self.name

    def get_phone(self):
        return self.phone

    def get_address(self):
        return self.address