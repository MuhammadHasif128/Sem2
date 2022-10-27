class Person:
    def __init__(self, name, nric):
        self.__name = name
        self.__nric = nric

class Student(Person):
    def __init__(self, name, nric, admin_no, test_mark, exam_mark):
        Person.__init__(self, name, nric)
        self.__admin_no = admin_no
        self.__test_mark = test_mark
        self.__exam_mark = exam_mark

    def computeFinalMark(self):
        return self.__test_mark/2 + self.__exam_mark/2

class Lecturer(Person):
    def __init__(self, name, nric, staff_id, total_teachinghour):
        Person.__init__(self, name, nric)
        self.__staff_id = staff_id
        self.__total_teachinghour = total_teachinghour
    def computeSalary(self):
        return self.__total_teachinghour*90

