input_make = input("Enter the make of the phone: ")
input_model = input("Enter the model of the phone: ")
input_price = input("Enter the price of the phone: ")

class Phone:
    count = 0

    def __init__(self):
        self.__make = None
        self.__model = None
        self.__price = 0
        Phone.count += 1

    def set_make(self):
        self.__make = input_make

    def set_model(self):
        self.__model = input_model

    def set_price(self):
        if input_price.isnumeric():
            self.__price = input_price
        else:
            print("Price should be in numbers")

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_price(self):
        return self.__price

    def __str__(self):
        return f"The phone created is {self.__make} {self.__model} priced at {self.__price}. Now has {Phone.count} phone in total"


q4 = Phone()
q4.set_make()
q4.set_model()
q4.set_price()
print(q4.__str__())
