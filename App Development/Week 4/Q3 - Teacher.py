class Student:
    def __init__(self, name):
        self.name = name  # [0]
        self.math = 0  # [1]
        self.chinese = 0  # [2]
        self.english = 0  # [3]
        self.science = 0  # [4]
        self.choices = []

    def get_score(self):
        return (self.math + self.chinese + self.english + self.science) / 4


def main():
    students = load_result()
    for s in students:
        s.choices.append('School A')
        s.choices.append('School B')
        s.choices.append('School C')
        print(f"{s.name} scores {s.get_score()}, the choices are {s.choices[0]}, {s.choices[1]}, {s.choices[2]}")


def load_result():
    students = []
    try:
        result_file = open('results (1).txt', "r")
        for r in result_file:
            r_list = r.split(', ')
            s1 = Student(r_list[0])
            s1.math = float(r_list[1])
            s1.chinese = float(r_list[2])
            s1.english = float(r_list[3])
            s1.science = float(r_list[4])
            students.append(s1)
    except IOError:
        print('File not accessible')
    return students


# start the test program
main()
