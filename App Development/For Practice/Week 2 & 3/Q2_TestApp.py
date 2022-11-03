from Q1_Student import *
from Q1_Lecturer import *


l_name = input("Enter Lecturer Name: ")
l_nric = input("Enter Lecturer NRIC: ")
l_staff_id = input("Enter Staff ID: ")
while l_nric != l_staff_id:
    print("Staff ID needs to be the same as NRIC")
    l_staff_id = input("Enter Staff ID: ")
else:
    pass
l_total_teachinghour = int(input("Enter Total Teaching Hour: "))

s_name = input("Enter Student Name: ")
s_nric = input("Enter Student NRIC: ")
s_admin_no = input("Enter Student Admin No: ")
while True:
    s_test_mark = int(input("Enter Test Mark: "))
    if s_test_mark < 0 or s_test_mark > 100:
        print('Test marks must be between 0 to 100 (inclusive)')
    else:
        break
while True:
    s_exam_mark = int(input("Enter Exam Mark: "))
    if s_exam_mark < 0 or s_exam_mark > 100:
        print("Exam Marks must be between 0 to 100 (inclusive)")
    else:
        break

l = Lecturer(l_name, l_nric, l_staff_id, l_total_teachinghour)
print(l.__str__())

s = Student(s_name, s_nric, s_admin_no, s_test_mark, s_exam_mark)
print(s.__str__())
