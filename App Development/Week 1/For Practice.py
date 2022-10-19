prompt_maker = input("Enter the make of the phone: ")
prompt_model = input("Enter the model of the phone: ")
prompt_price = input("Enter price of the phone: ")


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
        if prompt_price.isnumeric():
            self.__price = price
        else:
            print("Price should be in numbers")

    def get_make(self):
        self.__make = prompt_maker

    def get_model(self):
        self.__model = prompt_model

    def get_price(self):
        self.__price = prompt_price

    def get_phone_info(self):
        return f"The price of {self.__make} {self.__model} is ${self.__price}"


call_out = Phone()
call_out.get_make()
call_out.get_model()
call_out.get_price()
print(call_out.get_phone_info())


