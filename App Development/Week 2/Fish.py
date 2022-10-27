class Fish:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def swim(self):
        print("swim print")

    def swim_backwards(self):
        print("swim print backwards")



class ClownFish(Fish):
    def lives_in_sea(self):
        print("lives sin sea function")
