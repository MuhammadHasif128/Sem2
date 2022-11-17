import shelve


class Question:
    def __init__(self, id, question_desc, answer):
        self.__id = id
        self.__question_desc = question_desc
        self.__answer = answer

    def get_id(self):
        return self.__id

    def get_ques_desc(self):
        return self.__question_desc

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
            break


def add():
    id = input("Enter question id: ")
    question_desc = input("Enter question description: ")
    answer = input("Enter question answer: ")
    question_dict[id] = Question(id, question_desc, answer) # store id key
    db['question'] = question_dict # saving into dictionary, name of database question
    print("A question is added to shelve")


def display():
    id = input('Enter question id to display')
    if id in question_dict:
        q = question_dict[id]
        print("Question id:", q.get_id(), "Description: ", q.get_ques_desc(), "Answer", q.get_answer())
    else:
        print("No such question")


db = shelve.open("questionDB", "c")  # c means if database not there it will automatically create for you
question_dict = {}
try:
    if "question" in db:
        question_dict = db['question']  # will become database
    else:
        db['question'] = question_dict
except:
    print("Error in opening storage file")
else:
    menu()
