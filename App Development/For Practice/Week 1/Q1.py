class Customer:
    def __init__(self, name, email, mobile_number):
        self.__name = name
        self.__email = email
        self.__mobile_number = mobile_number

    def get_customer_info(self):
        return f"Name {self.__name}, Email: {self.__email}, Mobile Number {self.__mobile_number}"


c = Customer("John", "John@nyp.edu.sg", "92345678")
print(c.get_customer_info())
