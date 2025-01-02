import random
import matplotlib.pyplot as plt

N_players = 100
N_games_per_player = 1000
K_Elo_update = 50

true_ratings = [random.gauss(1500, 300) for i in range(N_players)]
print(min(true_ratings), max(true_ratings))
measured_ratings_p1 = [1000]
true_rating_p1 = 2000

for i in range(N_games_per_player):

    if (i>40):
        K_Elo_update = 20
    elif (i>100):
        K_Elo_update = 10


    p2 = random.randint(0, N_players-1)
    measured_rating_diff = true_ratings[p2] - measured_ratings_p1[-1] 
    while abs(measured_rating_diff) > 400:
        p2 = random.randint(0, N_players-1)
        measured_rating_diff = true_ratings[p2] - measured_ratings_p1[-1] 

    true_rating_diff = true_ratings[p2] - true_rating_p1    
    true_p1_win_prob = 1 / (1 + 10**(true_rating_diff/400))
    if random.random() < true_p1_win_prob:
        score_p1 = 1
        score_p2 = 0
    else:
        score_p1 = 0
        score_p2 = 1

    measured_p1_win_prob = 1 / (1 + 10**(measured_rating_diff/400))
    measured_ratings_p1.append(measured_ratings_p1[-1] + K_Elo_update*(score_p1 - measured_p1_win_prob))  


plt.plot(measured_ratings_p1)
plt.plot([0, N_games_per_player], [true_rating_p1, true_rating_p1])
plt.show()