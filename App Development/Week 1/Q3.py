class Customer:
    def __init__(self):
        self.__name = None
        self.__email = None
        self.__mobile_number = None

    def get_name(self):
        return self.__name()

    def set_name(self, name):
        self.__name = name

    def get_email(self):
        return self.__email()

    def set_email(self, email):
        self.__email = email

    def get_mobile_number(self):
        return self.__mobile_number()

    def set_mobile_number(self, mobile_number):
        self.__mobile_number = mobile_number







