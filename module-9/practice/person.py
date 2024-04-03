import stdio

class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def birthday(self):
        self.age += 1
        
    def change_last_name(self, newname):
        self.lastname = newname
    
    def __str__(self):
        return "Hello, " + self.firstname + " " + self.lastname + "! You are " + str(self.age) + " years old."