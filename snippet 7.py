class Manager:
    country ="Kenya"
    # constructor
    def __init__(self, name, department):
        # Instance variable
        self.name = name
        self.dpt = department

    # instance method access instance variable
    def show(self):
        print('Name:', self.name, 'Department:', self.dpt)

# create first object
print('Manager One')
Catherine = Manager("Catherine", "ict")
# call instance method
Catherine.show()
