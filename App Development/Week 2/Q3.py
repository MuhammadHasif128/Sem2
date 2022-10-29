class Player:
    def __init__(self, name):
        self.__name = name

    def set_name(self, player_name):
        self.__name = player_name

    def get_name(self):
        return self.__name


class BasketballPlayer(Player):
    positions = ['Guard', 'Forward', 'Center']

    team_name = input("Enter the basketball team name: ")

    def __init__(self, name):
        super().__init__(name)
        self.__position = ''

    def set_position(self, position):
        if position in BasketballPlayer.positions:
            self.__position = position
        else:
            print('Invalid position for basketball player')

    def __str__(self):
        print(f"Team {BasketballPlayer.team_name} consists of the following positions")
        return f"{super().get_name()} playing as {self.__position}"
