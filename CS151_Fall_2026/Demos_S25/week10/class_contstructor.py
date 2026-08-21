class Employee():
    pass

def create_clerk():
  clerk = Employee()
  clerk.name = "Bob Cratchit"
  clerk.title = "clerk"
  clerk.salary = 15
  return clerk
new_clerk=create_clerk()

#print(new_clerk.title)

def create_employee(name, title, salary):
  emp = Employee()
  emp.name = name
  emp.title = title
  emp.salary = salary
  return emp

clerk =create_employee("Grace Frank", "Chief clerk", 3000)
#print(clerk.salary)

class Car:
  def __init__(self, color, year):
    self.color = color
    self.year = year
    self.make = 'Toyota'
  
  def change_model(self, yr): # Setter Function 
    self.year += yr
    
  def get_color(self):
    return self.color
  
  def __str__(self): # Dunder Function
    return f"{self.make} ({self.year}:) {self.color}"


A = Car('blue', 2008)
B = Car('red', 2006)
A.make = 'Honda'
A.year = B.year
A.change_model(10)
print(A.make, A.color, A.year)
print(A)
print(A.get_color())

################ CLASS EXERCISE ###########
class BankAccount:
    def __init__(self, account_number, balance, owner_name):
        self._account_number = account_number
        self._balance = balance
        self._owner_name = owner_name
    
    # Getter methods
    def get_account_number(self):
        return self._account_number
    
    def get_balance(self):
        return self._balance
    
    def get_owner_name(self):
        return self._owner_name
    
    # Setter methods
    def set_account_number(self, account_number):
        self._account_number = account_number
    
    def set_owner_name(self, owner_name):
        self._owner_name = owner_name
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            return True
        return False
    
    def display_info(self):
        print(f"Account Number: {self._account_number}")
        print(f"Owner: {self._owner_name}")
        print(f"Balance: ${self._balance:.2f}")

# Test
account = BankAccount("1234567", 1000.0, "John Doe")
account.display_info()
account.deposit(account.get_balance()+500)
account.withdraw(200)
print("--------------------------")
account.display_info()



######### FIRST CLASS DEMO #####################
class Employee:
    def __init__(self, name, salary, title):
        self.sal = salary
        self.name = name
        self.title = title
        
    def change_title(self, t):
        return self.title
    
    def increase_sal(self, salary): # Setter function
        newSal = self.sal + salary
        return newSal
    
    def __str__(self):
        return f"{self.name} ----{self.title} ---- {self.sal}"

    
clerk = Employee("Fred", 2000, "Instructor")

# print(f"{clerk.name}: {clerk.title} {clerk.sal}")

# print("-------------------")
# print(f"{clerk.name}: {clerk.change_title("Professor")} {clerk.increase_sal(1000)}")

print(clerk)