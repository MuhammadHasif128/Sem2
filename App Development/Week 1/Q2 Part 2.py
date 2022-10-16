class Phone:
    def __init__(self):
        self.__make = input("Enter the make of the phone: ")
        self.__model = input("Enter the model of the phone: ")
        self.__price = input("Enter the price of the phone: ")

    def price(self):
        print(f"The price of {self.__make} {self.__model} is ${self.__price}")


c = Phone()
c.price()




