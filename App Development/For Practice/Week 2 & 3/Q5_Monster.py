class Monster:
    def __init__(self, name, health, attack, defence):
        self.__name = name
        self.__health = health
        self.__attack = attack
        self.__defence = defence

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_health(self, health):
        self.__health = health

    def get_health(self):
        return self.__health

    def set_attack(self, attack):
        self.__attack = attack

    def get_attack(self):
        return self.__attack

    def set_defence(self, defence):
        self.__defence = defence

    def get_defence(self):
        return self.__defence

    def display(self):
        return f"{self.__name} is a monster"


class FireMonster(Monster):
    def __init__(self):
        super().__init__("firebug", 10, 9, 4)

    def display(self):
        return f"{self.get_name()} is a Fire Type monster"


class WaterMonster(Monster):
    def __init__(self):
        super().__init__("waterbird", 15, 6, 3)

    def display(self):
        return f"{self.get_name()} is a Water Type monster"


class GrassMonster(Monster):
    def __init__(self):
        super().__init__("grasshopper", 20, 5, 3)

    def display(self):
        return f"{self.get_name()} is a Grass Type monster"


