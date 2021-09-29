import matplotlib.pyplot as plt

(fig, ax) = plt.subplots()
ax.grid(True)
ax.plot([1, 2, 3, ], [1, 4, 2, ], label='chart 1')
ax.plot([1, 2, 3, ], [4, 2, 3, ], label='chart 2')
ax.set_xlabel('x label')
ax.set_ylabel('y label')
ax.set_title("Simple Plot")
ax.legend()
plt.show()
