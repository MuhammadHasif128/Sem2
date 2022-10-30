from Q3 import *

player_list = []

team_name = input("Enter the basketball team name: ")

for i in range(5):
    player_name = input("Enter player name: ")
    position = input("Which position is he/she playing: ")
    s = BasketballPlayer(player_name)
    s.set_position(position)
    player_list.append(s)

print(f"Team {team_name} consists of the following players")

for a in player_list:
    print(a)



