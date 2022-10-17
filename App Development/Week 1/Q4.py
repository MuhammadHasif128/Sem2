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

    def __str__(self):
        return f"The phone created is {self.__make} {self.__model} priced at {self.__price}. Now has 1 phone in total."

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_price(self):
        return self.__price



