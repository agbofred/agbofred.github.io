class Employee:
    def __init__(self, name, title, salary):
        self.name = name
        self.title = title
        self.salary = salary
    def raise_salary(self, amount):
        self.salary +=amount
    def __repr__(self):
        return (f'name = {self.name}: title = {self.title}: salary = {self.salary}')
    
    def get_salary(self):
        return self.salary()
    
    def set_salary(self, new_salary):
        self.salary = new_salary

emp1 = Employee("Bob", "manager", 1000)
emp2 = Employee("Fred", "Sales", 2000)
emp2.set_salary(2500)
#print(emp2)
#print(f'Manager: {emp1.salary}:::: Sales: {emp2.salary}')
"""class Pet:
    def __init__(self, name, color, age):
        self.name = name
        self.color="black"
        self.age = age

    def bmi(self, weight, height):
        if weight/height >2:
            self.age = self.age*2
        else:
            self.age += 1
dog = Pet("Loly", "brown", 2)
dog.bmi(180,45)
print(f'{dog.name}, {dog.color}, {dog.age}')
"""

class BestCounter:
    def __init__(self, start):
        self.counter = start
    def increment(self, value):
        self.counter += self.value
    #def increment(self, value):
        #self.counter += value

b = BestCounter(30)
b.increment(2)
print(b.counter)