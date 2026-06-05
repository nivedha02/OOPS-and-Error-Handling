"""Problem 9 — super() (medium)
Create a base class Employee with name and salary. Create a child class Manager that adds a team_size attribute. 
Use super().__init__() in Manager to avoid repeating the parent's init code."""

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def __str__(self):
        return (f"Employee name: {self.name} Salary: {self.salary}")
class Manager(Employee):
    def __init__(self,name,salary,team_size):
        self.team_size=team_size
        super().__init__(name,salary)

    def __str__(self):
        #return (f"Employee name: {self.name}Salary: {self.salary} Team size: {self.team_size}")
        return f"{super().__str__()} Team size: {self.team_size}"


#Testcase
Emp1=Employee("Sajay","80k")
print(Emp1)
Ma1=Manager("Sai","8L","8")
print(Ma1)
