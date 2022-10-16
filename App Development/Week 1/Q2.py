class Phone:
    def __init__(self, make, model, price):
        self.__make = make
        self.__model = model
        self.__price = price

    def get_phone_info(self):
        print(f"{self.__make} for {self.__model} is {self.__price}.")


instance = Phone("The price for", "Samsung S22", "$1568")
instance.get_phone_info()
