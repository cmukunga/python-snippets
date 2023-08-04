class Car:
    wheels = 4
    def __init__(self,make,color,year,country):
        self.make = make
        self.country = country
        self.year = year
        self.color = color
    def Purchase(self):
        print(f"On {self.year}  {self.make} was the leading car model from {self.country}")
    def Selling(self):
        print(f"The {self.color} {Car.wheels} wheeled {self.make} was the most expensive car model from {self.country} costing about 35 million dolars")
if __name__ == "__main__":
    customer1 = Car("Isuzu","Blue",2022,"China")
    print(customer1.make)
    print(customer1.color)
    print(customer1.year)
    print(customer1.country)
    customer1.Purchase()
    customer1.Selling()