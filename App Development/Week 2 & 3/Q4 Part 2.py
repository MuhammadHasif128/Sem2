from Q4 import *

c = Monster("Giant", 17, 6, 7)
d = FireMonster()
e = WaterMonster()
f = GrassMonster()

def display_info(Monster):
    if "Fire" in Monster.get_name():
        print(Monster)
    elif "Water" in Monster.get_name():
        print(Monster)
    elif "Grass" in Monster.get_name():
        print(Monster)
    else:
        print("Invalid Monster")


display_info(d)
display_info(e)
display_info(f)
display_info(c)
