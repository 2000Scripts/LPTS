# Base Class
class Person:

    def __init__(self):
        self.name = None
        self.age = None

    def get_person_details(self):
        self.name = input("Enter student's name: ")
        self.age = int(input("Enter student's age: "))