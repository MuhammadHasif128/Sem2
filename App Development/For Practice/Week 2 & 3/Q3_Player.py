class Player:
    def __init__(self, name):
        self.__name = name

    def set_name(self, input_player_name):
        self.__name = input_player_name

    def get_name(self):
        return self.__name


class BasketballPlayer(Player):
    positions = ['Guard', 'Forward', 'Center']

    def __init__(self, name):
        super().__init__(name)
        self.__position = ''

    def set_position(self, position):
        if position in BasketballPlayer.positions:
            self.__position = position
        else:
            print("Invalid position for basketball player")

    def get_position(self):
        return self.__position

    def __str__(self):
        return f"{super().get_name()} playing as a {self.__position}"
