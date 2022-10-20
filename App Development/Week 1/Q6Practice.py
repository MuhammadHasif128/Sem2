import Q4Practice
import Q5Practice

input_make = input("Enter the make of the phone: ")
input_model = input("Enter the model of the phone: ")
input_price = input("Enter the price of the phone: ")

q4 = Q4Practice.Phone()
q4.set_make()
q4.set_model()
q4.set_price()
print(q4.__str__())

input_name1 = input("Enter salesperson name: ")
input_payment = int(input("Enter payment received by salesperson: "))


q5 = Q5Practice.SalesPerson()
q5.set_name()
q5.salesperson_commission(input_payment)
q5.salesperson_sold(q4)
q5.set_phone()
print(q5.__str__())


