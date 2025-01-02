import random
import matplotlib.pyplot as plt

N_players = 100
N_games_per_player = 400
K_Elo_update = 50

true_ratings = [random.gauss(1500, 300) for i in range(N_players)]
measured_ratings = [[1500] for i in range(N_players)]

measured_ratings_avg_dev = []
for i in range(N_players*N_games_per_player // 2):

    if (i>40*N_players//2):
        K_Elo_update = 20
    elif (i>100*N_players//2):
        K_Elo_update = 10

    p1 = random.randint(0, N_players-1)
    p2 = random.randint(0, N_players-1)
    measured_rating_diff = measured_ratings[p2][-1] - measured_ratings[p1][-1]
    while p1 == p2 or abs(measured_rating_diff) > 400:
        p1 = random.randint(0, N_players-1)
        p2 = random.randint(0, N_players-1)
        measured_rating_diff = measured_ratings[p2][-1] - measured_ratings[p1][-1]

    true_rating_diff = true_ratings[p2] - true_ratings[p1]    
    true_p1_win_prob = 1 / (1 + 10**(true_rating_diff/400))
    if random.random() < true_p1_win_prob:
        score_p1 = 1
        score_p2 = 0
    else:
        score_p1 = 0
        score_p2 = 1

    measured_p1_win_prob = 1 / (1 + 10**(measured_rating_diff/400))
    measured_ratings[p1].append(measured_ratings[p1][-1] + K_Elo_update*(score_p1 - measured_p1_win_prob))  
    measured_ratings[p2].append(measured_ratings[p2][-1] + K_Elo_update*(score_p2 - (1 - measured_p1_win_prob)))

    measured_ratings_avg_dev.append(sum([abs(r[-1] - t) for r, t in zip(measured_ratings, true_ratings)]) / N_players)


measured_ratings_last = [ratings[-1] for ratings in measured_ratings]
plt.plot(true_ratings, measured_ratings_last, 'o')
plt.plot([500, 2500], [500, 2500])
plt.title("True vs. measured ratings")
plt.show()

plt.plot([v/N_players*2 for v in range(0,len(measured_ratings_avg_dev))], measured_ratings_avg_dev)
plt.plot([0,N_games_per_player],[50,50])
plt.plot([40,40],[0,200])
plt.plot([100,100],[0,200])
plt.title("Average deviation of measured ratings from true ratings")
plt.show()

plt.hist([measured_ratings_last[i]-true_ratings[i] for i in range(N_players)], bins=20)
plt.title("Histogram of rating errors")
plt.show()

for i in range(3):
    plt.plot(measured_ratings[i])
    plt.title(f"player {i} | rating {round(true_ratings[i],1)}")
    plt.ylim(800, 2200)
    plt.plot([0,len(measured_ratings[i])],[true_ratings[i],true_ratings[i]])
    plt.plot([40,40],[0,2500])
    plt.plot([100,100],[0,2500])
    plt.show()
