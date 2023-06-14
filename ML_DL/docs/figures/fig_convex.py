import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,1, num=50)

y1 = np.square(x)
y2 = -y1
x1, x2 = x[0:30], x[30:]
y3= np.concatenate((np.square(x1+0.3), np.square(x2-0.7) + 0.1)) 

plt.subplot(1, 3, 1)
plt.plot(x, y1)
plt.title('Convex')
plt.xticks([])
plt.yticks([])


plt.subplot(1, 3, 2)
plt.plot(x, y2)
plt.title('Concave')
plt.xticks([])
plt.yticks([])

plt.subplot(1, 3, 3)
plt.plot(x, y3)
plt.title('non Convex')
plt.xticks([])
plt.yticks([])

plt.savefig('convex_func.png')
plt.clf()