import random
stats = [0, 1, 2, 3, 4, 5, 6, 7]  # 0 = hp, 1 = damage_resist, 2 = magic_resist, 3 = speed, 4 = strength, 5 = mana,
# 6 = intelligence, 7 = luck
# Average hit = 10 pts, standard hp = 500
name = input("Who are you?")
# character_class = input("WHAT are you? (You can only say 'I don't know' for now)")
equips = [0, 1, 2, 3, 4, 5]
bag_o_items = []
spells = ["Fire spell", "Healing spell", "Ice spell"]
effects = ["flame", "freeze", "poison"]
stats[7] = random.randint(-13, 7)
"""
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

if "I don't know" in character_class:
    stats[0] = 500  # hp
    stats[1] = 7 # damage_resist
    stats[2] = 7 # magic resist
    stats[3] = 7 # speed
    stats[4] = 7 # strength
    stats[5] = 200 # mana
"""

def you_attacked(a, b, c, e_l, ):
    if action.lower in "attack":
        print("You attacked it!")
        enemy_hp = enemy_hp - (stats[4] - enemy_luck)



actions = ["attack", "spell", "defend"]
def battle ():
    enemy_hp = random.randint(200, 600)
    enemy_strength = random.randint(1, 10)
    enemy_intelligence = (random.randint (1, 10))
    enemy_resist = random.randint(1, 10)
    enemy_luck = random.randint(-13, 7)
    while enemy_hp > 0:
        action = input("What is your next move? ie:attack, spell, defend")
        enemy_action = random.choice(actions)




