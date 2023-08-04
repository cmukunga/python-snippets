class Policy:
    def __init__(self, Policy_No, Policy_Type, Coverage_Amount, Upgrade):
        self.Policy_No = Policy_No
        self.Policy_Type = Policy_Type
        self.Coverage_Amount = Coverage_Amount
        self.Upgrade = Upgrade

    def __str__(self):
        return f"Policy Number: {self.Policy_No}, Policy_Type: {self.Policy_Type}, Coverage: {self.Coverage_Amount}, Upgrade: {self.Upgrade}"

class Customer:
    def __init__(self, customer_id, name, address):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.policies = []

    def New_Policy(self, policy):
        self.policies.append(policy)

    def Find_Policies(self):
        return self.policies

    def __str__(self):
        return f"Customer ID: {self.customer_id}, Name: {self.name}, Address: {self.address}"

class InsuranceCompany:
    def __init__(self, name):
        self.name = name
        self.customers = {}
        self.policies = {}

    def create_customer(self, customer_id, name, address):
        if customer_id not in self.customers:
            customer = Customer(customer_id, name, address)
            self.customers[customer_id] = customer
            print(f"Customer {name} with ID {customer_id} added successfully.")
        else:
            print("A customer with the same ID already exists.")

    def create_policy(self, Policy_No, Policy_Type, Coverage_Amount, Upgrade):
        if Policy_No not in self.policies:
            policy = Policy(Policy_No, Policy_Type, Coverage_Amount, Upgrade)
            self.policies[Policy_No] = policy
            print(f"Policy {Policy_No} added successfully.")
        else:
            print("A policy with the same number already exists.")

    def New_customer_Policy(self, customer_id, Policy_No):
        if customer_id in self.customers and Policy_No in self.policies:
            customer = self.customers[customer_id]
            policy = self.policies[Policy_No]
            customer.New_Policy(policy)
            print(f"Policy {Policy_No} added to customer {customer_id} successfully.")
        else:
            print("Customer or policy not found.")

# Usage example:
if __name__ == "__main__":
    insurance_company = InsuranceCompany("Kenya Insurance Company")

    insurance_company.create_customer(1, "John Doe", "Naku St")
    insurance_company.create_customer(2, "Jane Smith", "east Elm St")

    insurance_company.create_policy(101, "Health", 10000, 5000)
    insurance_company.create_policy(102, "Auto", 5000, 2500)

    insurance_company.New_customer_Policy(1, 101)
    insurance_company.New_customer_Policy(2, 102)
    insurance_company.New_customer_Policy(2, 101)  # Adding the same policy to another customer

    customer1 = insurance_company.customers.get(1)
    if customer1:
        print("\nCustomer Details:")
        print(customer1)
        print("Policies:")
        for policy in customer1.Find_Policies():
            print(policy)
    else:
        print("Customer not found.")

    customer2 = insurance_company.customers.get(2)
    if customer2:
        print("\nCustomer Details:")
        print(customer2)
        print("Policies:")
        for policy in customer2.Find_Policies():
            print(policy)
    else:
        print("Customer doesn't exist.")
