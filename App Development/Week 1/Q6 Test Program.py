import Q4
import Q5


make = input("Enter the make of the phone: ")
model = input("Enter the model of the phone: ")
price = input("Enter the price of the phone: ")

d = Q4.Phone()
d.set_make(make)
d.set_model(model)
d.set_price(price)
print(d.__str__())

name = input("Enter salesperson name: ")
payment = int(input("Enter payment received by Salesperson: "))

c = Q5.SalesPerson()
c.set_name(name)
c.salesperson_commission(payment)
c.salesperson_sold(d)
print(c.__str__())
