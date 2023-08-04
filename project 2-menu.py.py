#!/usr/bin/env python
# coding: utf-8

# In[ ]:


### CLASS MENU ###
# We have four different menus: brunch, early-bird, dinner, and kids
class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    # string representation method that show the name of the menu and indicate when the menu is available
    def __repr__(self):
        return (
            f"{self.name} menu is available from {self.start_time} to {self.end_time}"
        )

    # return the total price of a purchase consisting of all the items in purchased_items
    def calculate_bill(self, purchased_items):
        bill = 0
        for purch_item in purchased_items:
            if purch_item in self.items:
                bill += self.items[purch_item]
        return f"The {self.name} order costs ${bill}"


### CLASS FRANCHISE ###
# we’ve decided to create more restaurants to offer our services
class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    # string representation the address of the restaurant
    def __repr__(self):
        return f"Store address: {self.address}"

    # method that takes in a time parameter and returns a list of the Menu objects that are available at that time
    def available_menus(self, time):
        available_menus = []
        for menu in self.menus:
            if time >= menu.start_time and time <= menu.end_time:
                available_menus.append(menu)
        return available_menus


## CLASS BUSINESS ##
# we’ve decided to diversify and create a restaurant that sells arepas
class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises


# WORKING WITH MENUS #
# 1st menu 'brunch' served from 11am to 4pm with the following items
brunch = Menu(
    "Brunch",
    {
        "pancakes": 7.50,
        "waffles": 9.00,
        "burger": 11.00,
        "home fries": 4.50,
        "coffee": 1.50,
        "espresso": 3.00,
        "tea": 1.00,
        "mimosa": 10.50,
        "orange juice": 3.50,
    },
    11,
    16,
)

# 2nd menu 'early-bird' served from 3pm to 6pm with the following items
early_bird = Menu(
    "Early-bird",
    {
        "salumeria plate": 8.00,
        "salad and breadsticks (serves 2, no refills)": 14.00,
        "pizza with quattro formaggi": 9.00,
        "duck ragu": 17.50,
        "mushroom ravioli (vegan)": 13.50,
        "coffee": 1.50,
        "espresso": 3.00,
    },
    15,
    18,
)

# 3rd menu 'dinner' served from 5pm to 11pm with the following items
dinner = Menu(
    "Dinner",
    {
        "crostini with eggplant caponata": 13.00,
        "ceaser salad": 16.00,
        "pizza with quattro formaggi": 11.00,
        "duck ragu": 19.50,
        "mushroom ravioli (vegan)": 13.50,
        "coffee": 2.00,
        "espresso": 3.00,
    },
    17,
    23,
)

# 4th menu 'kids' served from 11am until 9pm with the following items
kids = Menu(
    "Kids",
    {
        "chicken nuggets": 6.50,
        "fusilli with wild mushrooms": 12.00,
        "apple juice": 3.00,
    },
    11,
    21,
)

# new menu "Take a’ Arepa", available from 10am until 8pm
arepas_menu = Menu(
    "Take a’ Arepa",
    {
        "arepa pabellon": 7.00,
        "pernil arepa": 8.50,
        "guayanes arepa": 8.00,
        "jamon arepa": 7.50,
    },
    10,
    20,
)

# print(brunch)

# price of breakfast order for one order of pancakes, one order of home fries, and one coffee
print(brunch.calculate_bill(["home fries", "coffee", "pancakes"]))

# price of early-bird purchase for salumeria plate and the vegan mushroom ravioli
print(early_bird.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"]))


# WORKING WITH FRANCHISES #
# passing in all four menus along with these franchises
all_menus = [brunch, early_bird, dinner, kids]

# create our first two franchises
flagship_store = Franchise("1232 West End Road", all_menus)
new_installment = Franchise("12 East Mulberry Street", all_menus)

# print available menus in our franchises with a specific hour as a parameter
print(flagship_store.available_menus(12))
print(flagship_store.available_menus(17))

# create our first 'Take a’ Arepa' franchise "189 Fitzgerald Avenue"
arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menu)

# WORKING WITH BUSINESSES #
# create our first Business "Basta Fazoolin' with our franchises flagship_store and new_installment
basta_fazoolin = Business(
    "Basta Fazoolin' with my Heart", [flagship_store, new_installment]
)

# create our second Business "Take a' Arepa"
arepa_business = Business("Take a' Arepa", [arepas_place])

