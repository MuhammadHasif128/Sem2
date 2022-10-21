class Phone:
    count = 0

    def __init__(self):
        self.__make = None
        self.__model = None
        self.__price = 0
        Phone.count += 1

    def set_make(self, input_make):
        self.__make = input_make

    def set_model(self, input_model):
        self.__model = input_model

    def set_price(self, input_price):
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
        return f"The phone created is {self.__make} {self.__model} priced at {self.__price}. Now has {Phone.count} phone in total."
