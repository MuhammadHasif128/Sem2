import shelve

q3_dictionary = {}


class Question:
    def __init__(self, ques_id, ques_desc, answer):
        self.__ques_id = ques_id
        self.__ques_desc = ques_desc
        self.__answer = answer

    def get_ques_id(self):
        return self.__ques_id

    def get_ques_desc(self):
        return self.__ques_desc

    def get_answer(self):
        return self.__answer


def menu():
    while True:
        print('Select the program (1-3) to run: ')
        print('1. Add a Question')
        print('2. Display a Question (by id)')
        print('3. Quit the program')
        try:
            val = int(input('Enter your command (1-3): '))
        except ValueError:
            val = 3
        if val == 1:
            add()
        elif val == 2:
            display()
        else:
            print('End of program')
            db.close()
            break


def add():
    input_id = input("Enter question id: ")
    input_description = input("Enter question description: ")
    input_answer = input("Enter question answer: ")

    q3_dictionary[input_id] = Question(input_id, input_description, input_answer)
    db['q3 label'] = q3_dictionary
    print("A question is added to shelve")


def display():
    input_id = input("Enter the question id to display: ")
    if input_id in q3_dictionary:
        q = q3_dictionary[input_id]
        print("Question id:", q.get_ques_id(), "\nDescription:", q.get_ques_desc(), "\nAnswer:", q.get_answer())
    else:
        print("No such question")


db = shelve.open("q3shelve", "c")
try:
    if "q3 label" in db:
        q3_dictionary = db["q3 label"]
    else:
        db["q3 label"] = q3_dictionary
except:
    print("Error in opening storage file")
else:
    menu()
