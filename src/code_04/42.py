import matplotlib.pyplot as plt

(fig, ax) = plt.subplots()
ax.plot([1, 2, 3, ], [1, 4, 2, ], label='chart 1')
ax.set_xlabel('x label')
ax.set_ylabel('y label')
ax.set_title("Simple Plot")
ax.legend()
plt.show()
