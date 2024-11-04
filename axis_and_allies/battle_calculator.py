import random

units_land = {"infantry": {"attack": 1, "defense": 2},
              "tank": {"attack": 3, "defense": 3},
              "fighter": {"attack": 3, "defense": 4},
              "bomber": {"attack": 4, "defense": 1}}

order_of_loss1 = ["infantry", "tank", "fighter", "bomber"]
order_of_loss2 = ["infantry", "tank", "bomber", "fighter"]

player1_win = 0
player2_win = 0
both_die = 0
N = 100000


for i in range(N):
    player1 = {"infantry": 0, "tank": 0, "fighter": 0, "bomber": 0}
    player2 = {"infantry": 0, "tank": 0, "fighter": 0, "bomber": 0}

    while sum(list(player1.values())) > 0 and sum(list(player2.values())) > 0:
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

        while hits2 > 0 and sum(list(player1.values())) > 0:
            for unit in order_of_loss1:
                if player1[unit] > 0:
                    player1[unit] -= 1
                    hits2 -= 1
                    break
            
        while hits1 > 0 and sum(list(player2.values())) > 0:
            for unit in order_of_loss2:
                if player2[unit] > 0:
                    player2[unit] -= 1
                    hits1 -= 1
                    break

    if sum(list(player1.values())) > 0:
        player1_win += 1
    elif sum(list(player2.values())) > 0:
        player2_win += 1
    else:
        both_die += 1

print(f"Player 1 (attacker) wins: {round(player1_win / N * 100, 2)}%")
print(f"Player 2 (defender) wins: {round(player2_win / N * 100, 2)}%")
print(f"Both die: {round(both_die / N * 100, 2)}%")
