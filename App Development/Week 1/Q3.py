prompt_name = input("Enter your name: ")
prompt_email = input("Enter your email: ")
prompt_mobile_number = input("Enter your mobile number: ")


class Customer:
    def __init__(self):
        self.__name = None
        self.__email = None
        self.__mobile_number = None

    def set_name(self, name):
        self.__name = name

    def set_email(self, email):
        self.__email = email

    def set_mobile_number(self, mobile_number):
        self.__mobile_number = mobile_number

    def get_name(self):
        self.__name = prompt_name

    def get_email(self):
        self.__email = prompt_email

    def get_mobile_number(self):
        self.__mobile_number = prompt_mobile_number

    def get_customer_info(self):
        return f"Name: {self.__name}\nEmail: {self.__email}\nMobile Number: {self.__mobile_number}"


call_out = Customer()
call_out.get_name()
call_out.get_email()
call_out.get_mobile_number()
print(call_out.get_customer_info())


# Another solution without following the UML Diagram for Q3 and using set ONLY!
"""name = input("Enter your name: ")
email = input("Enter your email: ")
number = input("Enter your mobile number: ")


class Customer:
    def __init__(self):
        self.__name = None
        self.__email = None
        self.__mobile_number = None

    def set_name(self):
        self.__name = name

    def set_email(self):
        self.__email = email

    def set_mobile_number(self):
        self.__mobile_number = number

    def get_customer_info(self):
        return f"Name: {self.__name}\nEmail: {self.__email}\nMobile Number: {self.__mobile_number}"


call_out = Customer()
call_out.set_name()
call_out.set_email()
call_out.set_mobile_number()
print(call_out.get_customer_info())"""
