input_make = input("Enter the make of the phone: ")
input_model = input("Enter the model of the phone: ")
input_price = input("Enter the price pf the phone: ")


class Phone:
    count = 0

    def __init__(self):
        self.__make = None
        self.__model = None
        self.__price = 0

    def set_make(self, input_make):
        self.__make = input_make

    def get_make(self):
        return self.__make

    def set_model(self, input_model):
        self.__model = input_model

    def get_model(self):
        return self.__model

    def set_price(self, input_price):
        if input_price.isnumeric():
            self.__price = input_price
        else:
            print("Price should be in numbers")

    def get_price(self):
        return self.__price

    def get_phone_info(self):
        return f"The phone created is {self.__make} {self.__model} priced at ${self.__price}. Now has {Phone.count} phone in total"


