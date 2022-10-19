maker = input("Enter the make of the phone: ")
model = input("Enter the model of the phone: ")
price = input("Enter the price of the phone: ")


class Phone:
    def __init__(self):
        self.__make = None
        self.__model = None
        self.__price = None

    def get_maker(self):
        self.__make = maker

    def get_model(self):
        self.__model = model

    def get_price(self):
        self.__price = price

    def get_phone_info(self):
        return f"The price for {self.__make} {self.__model} is ${self.__price}"


call_out = Phone()
call_out.get_maker()
call_out.get_model()
call_out.get_price()
print(call_out.get_phone_info())



