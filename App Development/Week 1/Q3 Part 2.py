class Customer:
    def __init__(self):
        self.__name = input("Enter your name: ")
        self.__email = input("Enter your email: ")
        self.__mobile_number = input("Enter your mobile number: ")

    def __set_name__(self, name):
        self.__name = name

    def __set_email__(self, email):
        self.__email = email

    def __set_mobile_number__(self, mobile_number):
        self.__mobile_number = mobile_number

    def get_name(self):
        return "Name: " + self.__name

    def get_email(self):
        return "Email: " + self.__email

    def get_mobile_number(self):
        return "Mobile Number: " + self.__mobile_number


c = Customer()
print(c.get_name())
print(c.get_email())
print(c.get_mobile_number())



