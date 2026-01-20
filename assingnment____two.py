class Employee:
    def _init_(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_pay(self):
        return self.salary



class Manager(Employee):
    def _init_(self, name, salary, bonus):
        super()._init_(name, salary)
        self.bonus = bonus

    def calculate_pay(self):
        return self.salary + self.bonus



emp = Employee("Sarah", 500000)
mgr = Manager("David", 700000, 200000)

print("Employee Pay:", emp.calculate_pay())
print("Manager Pay:", mgr.calculate_pay())