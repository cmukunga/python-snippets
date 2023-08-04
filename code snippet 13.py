class Employee:

    def __init__(self, fullname, age, gender, salary):
        self.fullname = fullname
        self.age = age
        self.gender = gender
        self.salary = salary

    @classmethod
    def func_string_split(cls, employee_str):
        fullname, age, gender, salary = employee_str.split('-')
        return cls(fullname, age, gender, salary)


emp_from_csv1 = 'Suresh-27-Male-120000'
emp_from_csv2 = 'John-29-Male-100000'
emp_from_csv3 = 'Tracy-25-Female-155000'

emp1 = Employee.func_string_split(emp_from_csv1)
print(emp1.fullname)
print(emp1.gender)
print(emp1.salary)
print(emp1.age)

print('----------')
emp3 = Employee.func_string_split(emp_from_csv3)
print(emp3.fullname)
print(emp3.gender)
print(emp3.age)