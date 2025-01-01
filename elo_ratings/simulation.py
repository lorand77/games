import random

N = 100
true_ratings = []
measured_ratings = []

N_games_per_player = 200
K_elo_update = 32

for i in range(N):
    true_ratings.append(random.gauss(1500, 300))
    measured_ratings.append([1500])

for i in range(N*N_games_per_player):
    p1 = random.randint(0, N-1)
    p2 = random.randint(0, N-1)
    true_rating_diff = true_ratings[p2] - true_ratings[p1]
    measured_rating_diff = measured_ratings[p2][-1] - measured_ratings[p1][-1]
    if p1 == p2 or abs(measured_rating_diff) > 400:
        continue
    true_p1_win_prob = 1 / (1 + 10**(true_rating_diff/400))
    measured_p1_win_prob = 1 / (1 + 10**(measured_rating_diff/400))
    if random.random() < true_p1_win_prob:
        score_p1 = 1
        score_p2 = 0
    else:
        score_p1 = 0
        score_p2 = 1
    measured_ratings[p1].append(measured_ratings[p1][-1] + K_elo_update*(score_p1 - measured_p1_win_prob))  
    measured_ratings[p2].append(measured_ratings[p2][-1] + K_elo_update*(score_p2 - (1 - measured_p1_win_prob)))

import matplotlib.pyplot as plt
for i in range(5):
    plt.plot(measured_ratings[i])
    plt.title(f"player {i} rating {round(true_ratings[i],1)}")
    plt.ylim(800, 2200)
    plt.show()

measured_ratings_last = [ratings[-1] for ratings in measured_ratings]
plt.plot(true_ratings, measured_ratings_last, 'o')
x = [500, 2500]
plt.plot(x, x)
plt.show()