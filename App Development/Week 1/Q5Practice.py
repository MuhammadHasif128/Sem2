input_name1 = input("Enter salesperson name: ")
input_payment = int(input("Enter payment received by salesperson: "))


class SalesPerson:
    def __init__(self):
        self.__name = None
        self.__commission = 0
        self.__phone = None

    def set_name(self):
        self.__name = input_name1

    def salesperson_commission(self, payment_received):
        self.__commission = payment_received
        self.__commission = input_payment * 2/100

    def salesperson_sold(self, phone):
        self.__phone = phone

    def set_phone(self):
        self.__phone.get_make()
        self.__phone.get_model()
        self.__phone.get_price()

    def __str__(self):
        return f"Salesperson {self.__name} sold {self.__phone} {self.__phone} at ${self.__phone} and earned a commission of {self.__commission:.2f}"


q5 = SalesPerson()
q5.set_name()
q5.salesperson_commission(input_payment)
print(q5.__str__())
