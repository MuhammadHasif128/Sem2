from Q4 import *
from Q5 import *


p = Phone()
p.set_price(input_price)
p.set_model(input_model)
p.set_make(input_make)
Phone.count += 1
print(p.get_phone_info())

input_name = input("Enter salesperson name: ")
input_payment_received = int(input("Enter payment received by salesperson: "))

s = SalesPerson()
s.set_name(input_name)
s.salesperson_commission(input_payment_received)
s.salesperson_sold(p)
print(s.__str__())
