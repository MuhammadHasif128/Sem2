class Customer:
    def __init__(self, name, email, mobile):
        self.__name = name
        self.__email = email
        self.__mobile = mobile

    def get_customer_info(self):
        return "Name: " + self.__name + "\nEmail: " + self.__email + "\nMobile: " + self.__mobile


c = Customer("John", "john@nyp.edu.sg", "92345678")
print(c.get_customer_info())
