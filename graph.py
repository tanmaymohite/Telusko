
import sys
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Tesla", "Tata", "Ola", "Ather 450"])
y = np.array([9, 10, 7, 5])
plt.bar(x,y)
plt.bar(x, y, color = "green")
plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
