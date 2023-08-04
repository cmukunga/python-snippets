class P:
    x_var = 10

    @classmethod
    def main_class_method(cls):
                print("This is a class method.")
                print("The value of main_var is:", cls.x_var)


          # Call the class method on the class itself
P.main_class_method()

          # Create an instance of MainClass
main_instance = P()

          # Call the class method on the instance
main_instance.main_class_method()