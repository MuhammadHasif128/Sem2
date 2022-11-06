from Q5_Monster import *

m = Monster("Giant", 17, 6, 7)
f = FireMonster()
w = WaterMonster()
g = GrassMonster()
i = " "


def display_info(monster):
    if isinstance(monster, Monster):
        print(monster.display())
    else:
        print("Invalid Monster")


display_info(m)
display_info(f)
display_info(w)
display_info(g)
display_info(i)

