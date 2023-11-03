class Employee():
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
    def middlename(self, mname):
        self.name +=  mname

"""def creat_empl(name, sex):
    emp = Employee()
    emp.name =name
    emp.sex =sex
    return emp
sales = creat_empl("fred", "not unknown")
manager = creat_empl("Jed", "male")
print(manager.sex)"""

sales = Employee("Fred", "Male")
Manager = Employee("Maria", "F")
Manager.middlename("Joe") 

print(Manager.name)