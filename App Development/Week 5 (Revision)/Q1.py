input_intake = input("Enter new intake: ")


class Course:
    count = 0

    def __init__(self, name, intake):
        self.__name = name
        self.__intake = intake
        Course.count += 1

    def set_name(self, name):
        self.__name = name

    def set_intake(self, intake):
        self.__intake = intake

    def get_name(self):
        return self.__name

    def get_intake(self):
        return self.__intake

    def get_course_info(self):
        return f"Name: {self.__name}, intake: {self.__intake}"


c = Course("Diploma of IT", 80)
c.set_intake(input_intake)
print(c.get_course_info())
print(f"{Course.count} Course(s) created")
