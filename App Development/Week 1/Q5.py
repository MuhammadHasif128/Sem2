class SalesPerson:
    def __init__(self):
        self.__phone = None
        self.__name = None
        self.__commission = 0

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def salesperson_sold(self, phone):
        self.__phone = phone

    def salesperson_commission(self, payment_received):
        self.__commission = 0.02 * payment_received

    def __str__(self):
        return f"Salesperson {self.__name} sold {self.__phone.get_make()} at {self.__phone.get.price()} and earned a commission of {self.__commission}"
