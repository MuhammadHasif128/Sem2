from Q3 import *

team_name = input("Enter the basketball team name: ")

player_list = []

for i in range(5):
    player_name = input("Enter player name: ")
    position = input("Which position is he/she playing: ")
    s = BasketballPlayer(player_name)
    s.set_position(position)
    player_list.append(s)


for a in player_list:
    print(a)




