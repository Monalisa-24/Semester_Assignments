class Person:
    def __init__(self):
        self.name = "John Doe"
        self.age = 30
        self.country = "Unknown"
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Country: {self.country}")
person = Person()
person.display_info()
