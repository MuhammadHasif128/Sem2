from Q1Person import *


class Student(Person):
    def __init__(self, name, nric, admin_no, test_mark, exam_mark):
        super().__init__(name, nric)
        self.__admin_no = admin_no
        self.__test_mark = test_mark
        self.__exam_mark = exam_mark

    def set_admin_no(self, s_admin_no):
        self.__admin_no = s_admin_no

    def get_admin_no(self):
        return self.__admin_no

    def set_test_mark(self, s_test_mark):
        self.__test_mark = s_test_mark

    def get_test_mark(self):
        return self.__test_mark

    def set_exam_mark(self, s_exam_mark):
        self.__exam_mark = s_exam_mark

    def get_exam_mark(self):
        return self.__exam_mark

    def computefinalmark(self):
        return self.__test_mark/2 + self.__exam_mark/2

    def __str__(self):
        return f"{super().get_name()}, Admin No: {self.__admin_no} final mark is ${self.computefinalmark()}"



