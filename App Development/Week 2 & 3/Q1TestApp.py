from Q1Student import *
from Q1Lecturer import *

l_name = input("Enter Lecturer Name: ")
l_nric = input("Enter Lecturer NRIC: ")
l_staff_id = input("Enter Staff ID: ")
l_total_teachinghour = int(input("Enter Total Teaching Hour: "))


s_name = input("Enter Student Name: ")
s_nric = input("Enter Student NRIC: ")
s_admin_no = input("Enter Student Admin No: ")
s_test_mark = int(input("Enter Test Mark: "))
s_exam_mark = int(input("Enter Exam Mark: "))

l = Lecturer(l_name, l_nric, l_staff_id, l_total_teachinghour)
print(l.__str__())
s = Student(s_name, s_nric, s_admin_no, s_test_mark, s_exam_mark)
print(s.__str__())

