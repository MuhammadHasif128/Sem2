import shelve


class Phone:
    count = 0

    def __init__(self):
        self.__id = None
        self.__make = None
        self.__model = None
        self.__price = 0
        self.__class__.count +=1

    def set_id(self, phone_id):
        self.__id = phone_id

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_price(self, price):
        if price.isnumeric():
            self.__price = price
        else:
            print('Price should be in numbers.')

    def get_id(self):
        return self

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_price(self):
        return self.__price

    def __str__(self):
        s = 'The phone created is {} {} priced at ${}. Now has {} phone in total'.format(self.__make, self.__model, self.__price, self.__class__.count)
        return s


command = 0


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
    phone_id = input("Enter the phone id: ")
    print(phone_dict[phone_id])


def add():
    phone_id = input("Enter the phone id: ")
    make = input("Enter phone make: ")
    model = input("Enter phone model: ")
    price = input("Enter price of the phone: ")

    phone = Phone()
    phone.set_id(phone_id)
    phone.set_make(make)
    phone.set_model(model)
    phone.set_price(price)
    phone_dict[phone.get_id()] = phone
    print('Phone', phone_id, 'has been added')


def update():
    phone_id = input("Enter the phone id to update: ")
    phone = phone_dict.get(phone_id)
    make = input("Enter make of phone: ")
    model = input("Enter model of phone: ")
    price = input("Enter price of phone: ")
    phone.set_make(make)
    phone.set_model(model)
    phone.set_price(price)


def delete():
    phone_id = input('Enter phone id to delete')
    phone_dict.pop(phone_id, None)
    print("Phone", phone_id, "Deleted")


def display_all():
    for key in phone_dict:
        print(phone_dict[key])


db = shelve.open('storage', 'c')
phone_dict = {}
display_menu()
