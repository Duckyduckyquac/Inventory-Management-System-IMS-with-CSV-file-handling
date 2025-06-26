import csv
import os
items = [
    ["Item", "Quantity", "Price"],
    ["pen", 50, 10.5],
    ["notebook", 20, 45.0],
    ["eraser", 100, 5.25],
         ]
def initialize_csv():
    if not os.path.exists("inventory.csv"):

        with open('inventory.csv', 'w', newline="") as x:
            writer = csv.writer(x)
            for row in items:
                writer.writerow(row)
def view_inventory():
    items = load_from_csv()
    for row in items:
        if row[0] != "item":
            print(row)

def add_item():
    try:
        current_items = load_from_csv()
        new_item = input("What's the name of the item you'd like to add?").strip().lower()
        quantity = int(input("How many is in stock? "))
        price = float(input("What's the item's price? "))
        to_add = [new_item, quantity, price]
        with open('inventory.csv', 'a', newline="") as x:
            writer = csv.writer(x)
            writer.writerow(to_add)
    except ValueError:
        print("Something went wrong, try again! ")
def remove_item():
    try:
        current_items = load_from_csv()
        new_items = []
        item_to_remove = input("Which item would you like to remove? ").strip().lower()
        for row in current_items:
            if row[0].lower() != item_to_remove or row[0].lower() == "item":
                new_items.append(row)
        with open('inventory.csv', 'w', newline="") as x:
            writer = csv.writer(x)
            for row in new_items:
                writer.writerow(row)
        print("The item has been successfully removed! ")
    except ValueError:
        print("Something went wrong, try again! ")

def update_item():
    current_items = load_from_csv()
    new_items = []
    found = False
    to_upd = input("Which item would you like to update? ").strip().lower()
    for row in current_items:
        if row[0].lower() == to_upd:
            found = True
        if row[0].lower() != to_upd or row[0].lower() == "item":
            new_items.append(row)
    if found:
        quantity = int(input("What's the updated quantity for this item? "))
        price = float(input("What's the updated price for this item? "))
        to_add = [to_upd, quantity, price]
        new_items.append(to_add)
        with open('inventory.csv', 'w', newline="") as x:
            writer = csv.writer(x)
            for row in new_items:
                writer.writerow(row)
    else:
        print("The item does not exist, or something went wrong ")
def load_from_csv():
    with open('inventory.csv', 'r') as x:
        reader = csv.reader(x)
        items = []
        for row in reader:
            items.append(row)
    return items

def get_userchoice():
    while True:
        try:
            x = int(input("What would you like to do?\n1. View Inventory\n2. Add Item\n3. Remove Item\n4. Update Item\n5. Quit"))
            if x > 6 or x < 1:
                print("Input a valid number from 1 to 5. Try again!")
            else:
                return x
        except ValueError:
            print("Something went wrong, try again! ")
#main code
choice = get_userchoice()
initialize_csv()

while choice != 5:
    if choice == 1:
        view_inventory()
    if choice == 2:
        add_item()
    if choice == 3:
        remove_item()
    if choice == 4:
        update_item()
    choice = get_userchoice()
print("Thank you! ")
