class Customer:
    def set_name(self, name):
        if name.isalpha():
            self.__name = name
        else:
            print("Error")
    def get_name(self, name):
        return set.__name

cust1 = Customer()
cust1.set_name("Beng")

cust2 = Customer()
cust2.set_name("123456")
