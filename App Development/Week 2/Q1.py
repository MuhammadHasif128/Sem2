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

    def __str__(self):
        return self.__test_mark/2 + self.__exam_mark/2

    def computefinalmark(self):
        return f"{super().get_name(),} Admin No: {self.__admin_no}  "
