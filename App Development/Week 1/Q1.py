class Customer:
    def __init__(self, name, email, mobile_number):
        self.__name = name
        self.__email = email
        self.__mobile = mobile_number

    def get_customer_info(self):
        return f"Name:, {self.__name}, Email: {self.__email}, Mobile Number: {self.__mobile}"


call_out = Customer("Muhammad Hasif", "mhasif175@gmail.com", "83436485")
print(call_out.get_customer_info())
