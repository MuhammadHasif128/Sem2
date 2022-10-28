team_name = input("Enter the basketball team name: ")
player_name = input("Enter player name: ")
position = input("Which position is he/she playing: ")

class Player:
    def __init__(self, name):
        self.__name = name

    def set_name(self, player_name):
        self.__name = player_name


class BasketballPlayer(Player):
    positions = ['Guard', 'Forward', 'Center']

    def __init__(self, name, position):
        super().__init__(name)
        self.__position = position

    def set

    def set_position(self, positions):
        self.__position = positions

    def __str__(self):

