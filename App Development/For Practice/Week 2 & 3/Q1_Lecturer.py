from Q1_Person import *


class Lecturer(Person):
    def __init__(self, name, nric, staff_id, total_teachinghour):
        super().__init__(name, nric)
        self.__staff_id = staff_id
        self.__total_teachinghour = total_teachinghour

    def set_staff_id(self, staff_id):
        self.__staff_id = staff_id

    def get_staff_id(self):
        return self.__staff_id

    def set_total_teachinghour(self, total_teachinghour):
        self.__total_teachinghour = total_teachinghour

    def get_total_teachinghour(self):
        return self.__total_teachinghour

    def computesalary(self):
        return self.__total_teachinghour*90

    def __str__(self):
        return f"{super().get_name()}, Staff Id: {self.__staff_id} earns ${self.computesalary():.2f}"

