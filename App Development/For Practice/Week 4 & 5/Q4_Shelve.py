from Q4_Person import *
import shelve

command = 0

dictionary = {}

def display_menu():
    while True:
        print('Select the program (1-6) to run: ')
        print('1. Search for a phone')
        print('2. Add a new phone')
        print('3. Update phone details')
        print('4. Delete a phone')
        print('5. Display all phones')
        print('6. Quit the program')
        val = int(input('Enter your command (1-6): '))
        if val == 6:
            print('End of program')
            break
        elif val == 1:
            search()
        elif val == 2:
            add()
        elif val == 3:
            update()
        elif val == 4:
            delete()
        elif val == 5:
            display_all()


def search():
    input_id = input("Enter the phone id to search: ")
    print(dictionary[id])

def add():
    input_id = input("Enter the phone id to search: ")
    input_make = input("Enter phone make: ")
    input_model = input("Enter phone model: ")
    input_price = input("Enter phone make: ")

    p = Phone()
    p.set_id(input_id)
    p.set_make(input_make)
    p.set_model(input_model)
    p.set_price(input_price)

    dictionary[id] = p

    print("Phone successfully added")

def update():
    input_id = input("Enter the phone id to update: ")
    input_make = input("What is the new make? (Leave empty to remain unchange): ")
    input_model = input("What is the new make? (Leave empty to remain unchange): ")
    input_price = input("What is the new make? (Leave empty to remain unchange): ")

    if input_make != "":
        dictionary[id].set_make(input_make)
    else:
        pass

    if input_model != "":
        dictionary[id].set_model(input_model)
    else:
        pass

    if input_price != "":
        dictionary[id].set_price(input_price)
    else:
        pass

    print("Phone:", dictionary[id].get_id(), "price updated")

    s["Phone"] = dictionary


def delete():
    pass

def display_all():
    pass

display_menu()
