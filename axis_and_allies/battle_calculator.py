import random

units_land = {"infantry": {"attack": 1, "defense": 2},
              "tank": {"attack": 3, "defense": 3},
              "fighter": {"attack": 3, "defense": 4},
              "bomber": {"attack": 4, "defense": 1}}

order_of_loss1 = ["infantry", "tank", "fighter", "bomber"]
order_of_loss2 = ["infantry", "tank", "bomber", "fighter"]

player1 = {"infantry": 2, "tank": 0, "fighter": 1, "bomber": 0}
player2 = {"infantry": 1, "tank": 1, "fighter": 0, "bomber": 0}


hits1 = 0
for unit, count in player1.items():
    attack_value = units_land[unit]["attack"]
    for i in range(count):
        if random.randint(1, 6) <= attack_value:
            hits1 += 1

hits2 = 0
for unit, count in player2.items():
    defense_value = units_land[unit]["defense"]
    for i in range(count):
        if random.randint(1, 6) <= defense_value:
            hits2 += 1

while hits2 > 0:
    for unit in order_of_loss1:
        if player1[unit] > 0:
            player1[unit] -= 1
            break
    hits2 -= 1
    
while hits1 > 0:
    for unit in order_of_loss2:
        if player2[unit] > 0:
            player2[unit] -= 1
            break
    hits1 -= 1
