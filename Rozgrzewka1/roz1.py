#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np

plt.title("Rozgrzewka 1")
plt.xlabel("Os X")
plt.ylabel("Os Y")
plt.grid()

plt.xlim([-3, 3])
plt.ylim([-0.5, 1.5])

arrX = [-0.2, 0.4, 0.6, 1.2, 1.9, 0.5]
arrY = [0, 0, 1, 1, 1, 0]
x = np.arange(-3, 3, 0.01)
y1 = 1/(1+np.exp(-x))
y2 = 1/(1+np.exp(4*x))
y3 = 1/(1+np.exp(-100*(x-0.55)))

plt.scatter(arrX, arrY, color='black', s=10)
plt.plot(x, y1, color='#cc80ff', label='f1(x)')
plt.plot(x, y2, color='#9900ff', label='f2(x)')
plt.plot(x, y3, color='#4c0080', label='f3(x)')

legend = plt.legend(loc='upper center', ncol=3)
plt.savefig("Rozgrzewka1.png")
plt.show()
