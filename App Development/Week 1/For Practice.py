prompt_maker = input("Enter the make of the phone: ")
prompt_model = input("Enter the model of the phone: ")
prompt_price = input("Enter price of the phone: ")


class Phone:
    def __init__(self):
        self.__make = None
        self.__model = None
        self.__price = 0

    def set_make(self):
        self.__make = prompt_maker

    def set_model(self):
        self.__model = prompt_model

    def set_price(self):
        if prompt_price.isnumeric():
            self.__price = prompt_price
        else:
            print("Price should be in numbers")

    def get_phone_info(self):
        return f"The price of {self.__make} {self.__model} is ${self.__price}"


call_out = Phone()
call_out.set_make()
call_out.set_model()
call_out.set_price()
print(call_out.get_phone_info())


