from Q3_Player import *

store = []  # players only not position

input_team_name = input("Enter basketball team name: ")

for i in range(1, 6):
    input_player_name = input("Enter player name: ")
    input_position = input("Which position is he/she playing? ")
    b = BasketballPlayer(input_player_name)
    b.set_position(input_position)
    store.append(b)

print(f"Team {input_team_name} consists of the following players")

for b in store:
    print(b)



