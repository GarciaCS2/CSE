import random
stats = [0, 1, 2, 3, 4]  # 0 = hp, 1 = damage_resist, 2 = magic_resist, 3 = speed, 4 = strength, 5 = mana
# Average hit = 10 pts, standard hp = 500
stats[0] = 500
name = input("Who are you?")
character_class = input("WHAT are you?")
if "wizard" or "sorcerer" in character_class:
    stats[1] = 3
    magic_resist = 20
elif "warrior" or "fighter" or "swordsman" in character_class:
    stats[1] = 7
elif "marksman" or "archer" in character_class:

elif "chameleon" in character_class:
    stats[1] = 5

print("play game = 0, fight simulator = 1, ")
gameplay = input("Which will you do?")

if