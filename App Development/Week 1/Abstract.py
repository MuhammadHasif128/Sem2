class Customer:
    def __init__(self, name, email, mobile):
        self.__name = name
        self.__email = email
        self.__mobile = mobile
    def get_customer_info(self):
        return "Name: " + self.__name + "\nEmail: " + self.__email + "\nMobile: " + self.__mobile


c = Customer("Ah Kaw", "ahkaw@gmail.com", "91234567")
c2 = Customer("Hasif", "mhasif175@gmail.com", "83436485")
print(c.get_customer_info())
print("\n")
print(c2.get_customer_info())
