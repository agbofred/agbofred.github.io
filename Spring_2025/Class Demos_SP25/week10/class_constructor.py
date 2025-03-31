class Employee:
    def __init__(self, n, t, s):
        self.name = n
        self.title = t
        self.salary = s
        self.office= "Ford 209"
        
    def get_title(self): # getter mehtod
        return self.title
    
    def set_salary(self, amount): # setter method
        Newamount = self.salary + amount
        return Newamount
    
    def __str__(self):
        return f"You are printing the object location and ---"

clerk = Employee("Frank", "Instructor", 1000)
sales= Employee("Frank", "Professor", 3000)

#print(f"{clerk.name}-----{clerk.get_title()}--------{clerk.set_salary(1000)}")
print(clerk)