import matplotlib.pyplot as plt
import math, numpy

x_ax = []
y_ax = []

for x in numpy.arange(0, 2 * math.pi, 0.1):
    x_ax .append(x)
    y_ax.append(math.sin(x))

(fig, ax) = plt.subplots()
ax.grid(True)
ax.plot(x_ax, y_ax, label='sin')
plt.show()
