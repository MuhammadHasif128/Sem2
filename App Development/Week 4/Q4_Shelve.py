from Q4_Phone import *
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
            s["Phone"] = dictionary
            s.close()
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
    id = input("Enter phone id: ")
    print(dictionary[id])


def add():
    id = input("Enter phone id: ")
    id_make = input("Enter phone make: ")
    id_model = input("Enter phone model: ")
    id_price = input("Enter price of phone: ")

    d = Phone()
    d.set_id(id)
    d.set_make(id_make)
    d.set_model(id_model)
    d.set_price(id_price)

    dictionary[id] = d

    print("Phone successfully added")


def update():
    id = input("Enter phone id to update? ")
    id_make = input("What is the new make? (Leave empty to remain unchange): ")
    id_model = input("What is the new model? (Leave empty to remain unchange):  ")
    id_price = input("What is the new price? (Leave empty to remain unchange): ")
    if id_make != "":
        dictionary[id].set_make(id_make)
    else:
        pass
    if id_model != "":
        dictionary[id].set_model(id_model)
    else:
        pass
    if id_price != "":
        dictionary[id].set_price(id_price)
    else:
        pass
    print("Phone:", id, "price updated")

    s["Phone"] = dictionary


def delete():
    id = input("Enter the phone id to delete: ")
    dictionary[id].pop(id)
    print("Phone", id, "is deleted")


def display_all():
    for i in dictionary:
        print(dictionary[i])


s = shelve.open('storagecbappdev', 'c')
try:
    if 'Phone' in s:  # is key exist?
        dictionary = s["Phone"]  # retrieve data
    else:
        s["Phone"] = dictionary  # start with empty
except:
    print("Error in opening storage.db.")
else:
    display_menu()
