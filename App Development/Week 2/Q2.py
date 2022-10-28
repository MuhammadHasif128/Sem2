lname = input("Enter Lecturer Name: ")
lnric = input("Enter Lecturer's NRIC: ")
staff_id = input("Enter Staff ID: ")

while staff_id != lnric:
    print('Staff ID needs to be the same as Lecturer NRIC')
    staff_id = input("Enter Staff ID: ")
else:
    pass

totalhours = float(input("Enter Total Teaching Hour: "))
sname = input("Enter Student Name: ")
snric = input("Enter Student NRIC: ")
sadmin = input("Enter Student's Admin No: ")
while True:
    stest = float(input("Enter Test mark: "))
    if stest < 0 or stest > 100:
        print('Test marks must be between 0 and 100 (inclusive)')
    else:
        break

while True:
    sexam = float(input("Enter Exam mark: "))
    if sexam < 0 or sexam > 100:
        print('Exam marks must be between 0 and 100 (inclusive)')
    else:
        break


class Person:
    def __init__(self, name, nric):
        self.__name = name
        self.__nric = nric

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_nric(self, nric):
        self.__nric = nric

    def get_nric(self):
        return self.__nric


class Student(Person):
    def __init__(self, name, nric, admin_no, test_mark, exam_mark):
        super().__init__(name, nric)
        self.__admin_no = admin_no
        self.__test_mark = test_mark
        self.__exam_mark = exam_mark

    def set_admin_no(self, admin_no):
        self.__admin_no = admin_no

    def get_admin_no(self):
        return self.__admin_no

    def set_test_mark(self, test_mark):
        self.__test_mark = test_mark

    def get_test_mark(self):
        return self.__test_mark

    def set_exam_mark(self, exam_mark):
        self.__exam_mark = exam_mark

    def get_exam_mark(self):
        return self.__exam_mark

    def computefinalmark(self):
        return self.__test_mark/2 + self.__exam_mark/2

    def __str__(self):
        return f"{super().get_name()} Admin No: {self.__admin_no} final mark is ${self.computefinalmark():.2f}"


class Lecturer(Person):
    def __init__(self, name, nric, staff_id, total_teachinghour):
        super().__init__(name, nric)
        self.__staff_id = staff_id
        self.__total_touchinghour = total_teachinghour

    def set_staff_id(self, staff_id):
        self.__staff_id = staff_id

    def get_staff_id(self):
        return self.__staff_id

    def set_total_teachinghour(self, total_teachinghour):
        self.__total_touchinghour = total_teachinghour

    def get_total_teachinghour(self):
        return self.__total_touchinghour

    def computesalary(self):
        return self.__total_touchinghour*90

    def __str__(self):
        return f"{super().get_name()} Staff Id: {self.__staff_id} earns ${self.computesalary():.2f}"


lecturer = Lecturer(lname, lnric, staff_id, totalhours)
print(lecturer)
student = Student(sname, snric, sadmin, stest, sexam)
print(student)
