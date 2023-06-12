# binary log loss = -(ylogp + (1-y)log(1-p))
import numpy as np
import matplotlib.pyplot as plt

p = np.linspace(0.01, 1, num=50, endpoint = False)
colors = ['r', 'b']
for y in range(2):

    loss = -(y * np.log(p) + (1-y) * np.log(1-p))
    plt.plot(p, loss, colors[y], label= "label = " + str(y))

plt.xlabel('Predicted probability')
plt.ylabel('Binary Cross Entropy Loss')
plt.legend()
plt.title('Binary Cross Entropy Loss')
plt.savefig('binary_crossentropy_loss.png')
plt.close()