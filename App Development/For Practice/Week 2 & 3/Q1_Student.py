from Q1_Person import *


class Student(Person):
    def __init__(self, name, nric, admin_no, test_mark, exam_mark):
        Person.__init__(self, name, nric)
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
        return self.__test_mark*50/100 + self.__exam_mark*50/100

    def __str__(self):
        return f"{Person.get_name(self)}, Admin No: {self.__admin_no} final mark is {self.computefinalmark():.2f}"

