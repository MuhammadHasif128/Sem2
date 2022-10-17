make = input("Enter the make of the phone: ")
model = input("Enter the model of the phone: ")
price = input("Enter the price of the phone: ")

class Phone:
    def __init__(self):
        self.__make = None
        self.__model = None
        self.__price = 0

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_price(self, price):
        if price.isnumeric():
            self.__price = price
        else:
            print("Price should be in numbers")

    def get_phone_info(self):
        return f"The price of the {self.__make} {self.__model} is {self.__price}"

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_price(self):
        return self.__price

c = Phone()
c.set_make(make)
c.set_model(model)
c.set_price(price)
print(c.get_phone_info())



