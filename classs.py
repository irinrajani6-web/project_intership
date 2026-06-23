class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def get(self):
        print(self.name, self.age, self.course)

    def post(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course


class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def get(self):
        print(self.name, self.salary, self.department)

    def post(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department


class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def get(self):
        print(self.title, self.author, self.price)

    def post(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


s1 = Student("Irin", 17, "IT")
s2 = Student("Ayan", 18, "CE")

e1 = Employee("Rahul", 50000, "HR")
e2 = Employee("Priya", 60000, "IT")

b1 = Book("Python", "ABC", 500)
b2 = Book("Java", "XYZ", 700)

s1.get()
s2.get()

e1.get()
e2.get()

b1.get()
b2.get()

s1.post("Irin", 18, "Computer")
s1.get()