import matplotlib.pyplot as plt
import numpy

(fig, ax) = plt.subplots()
x = numpy.linspace(0, 2 * numpy.pi, 100)
y = numpy.sin(x)
ax.plot(x, y, label='chart 1')
plt.show()
