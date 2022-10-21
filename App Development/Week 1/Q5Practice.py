class SalesPerson:
    def __init__(self):
        self.__name = None
        self.__commission = 0
        self.__phone = None

    def set_name(self, input_name1):
        self.__name = input_name1

    def salesperson_commission(self, payment_received):
        self.__commission = payment_received * 2/100

    def salesperson_sold(self, phone):
        self.__phone = phone

    def __str__(self):
        return f"Salesperson {self.__name} sold {self.__phone.get_make()} {self.__phone.get_model()} at ${self.__phone.get_price()} and earned a commission of ${self.__commission:.2f}"



