from Q4 import *

c = Monster("Giant", 17, 6, 7)
d = FireMonster()
e = WaterMonster()
f = GrassMonster()

def display_info(monster):
    if isinstance(monster, Monster):
        print(monster.display())
    else:
        print("Invalid Monster")


display_info(d)
display_info(e)
display_info(f)
display_info(c)
