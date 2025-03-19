class Employee:
    pass

def create_employee(name, year, salary, major="CS"):
    emp = Employee() # Here we created an object -> instance of a class
    emp.name= name
    emp.year = year
    emp.salary= salary
    another_emp= Employee()
    another_emp.major = major
    return emp, another_emp

clerk = create_employee("Frank", 2020, 3000, "PHY")
salesman= create_employee("Ruth", 2025, 4000)
x=clerk[0]
y=clerk[1]
print(x.name,y.major)

