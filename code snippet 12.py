class Employee:
    company = "Brainovate"
    @classmethod
    def message(cls):
        print("The company name is %s" %cls.company)
        print("The message is from %s Class" %cls.__name__)
        cls.fun_msg()

    @staticmethod
    def func_msg():
        print("welcome to programming in python")
    #Employee.message(cls)