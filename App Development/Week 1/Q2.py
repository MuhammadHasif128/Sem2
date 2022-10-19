class Phone:
    def __init__(self, make, model, price):
        self.__make = make
        self.__model = model
        self.__price = price

    def get_phone_info(self):
        return f"The price for {self.__make} {self.__model} is ${self.__price}"


call_out = Phone("Samsung", "S22", "1568")
print(call_out.get_phone_info())
