from matplotlib import pyplot as plt
import numpy as np
plt.figure()
plt.title('boo hoo')
plt.plot([1,5,10,2], color='g', label='onions')
plt.plot([5,10,7,2], color='r', label='potatoes')
plt.xticks(np.arange(0,10,2))
plt.legend()
plt.show()