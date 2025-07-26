class Employee():
    def __init__(self, name, surname, position, level):
        self.name = name
        self.surname = surname
        self.position = position
        self.level = level

    def __str__(self):
        return f"Hello, my name is {self.name} {self.surname}, I am a {self.position} at this organisation,  level {self.level}."

employee_1 = Employee("Divine", "Victory", "Manager", 3)
employee_2 = Employee("Victoria", "Vik", "Janitor", 1)
print(employee_1)
print(employee_2)
