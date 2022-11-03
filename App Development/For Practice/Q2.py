input_make = input("Enter the make of the phone: ")
input_model = input("Enter the model of the phone: ")
input_price = input("Enter the price of the phone: ")


class Phone:
    def __init__(self, make, model, price):
        self.__make = make
        self.__model = model
        self.__price = price

    def set_make(self, input_make):
        self.__make = input_make

    def set_model(self, input_model):
        self.__model = input_model

    def set_price(self, input_price):
        self.__price = input_price

    def get_phone_info(self):
        return f"The price for {self.__make} {self.__model} is ${self.__price}"


p = Phone(input_make, input_model, input_price)
print(p.get_phone_info())

