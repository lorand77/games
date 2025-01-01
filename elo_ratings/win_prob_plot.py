import matplotlib.pyplot as plt

x = []
y = []
for i in range(-1000, 1000, 10):
    x.append(i)
    y.append(1 / (1 + 10 ** (i / 400)) * 100)


plt.plot(x, y)
plt.yticks(range(0, 101, 10))
plt.xticks(range(-1000, 1001, 200))
plt.grid()
plt.show()