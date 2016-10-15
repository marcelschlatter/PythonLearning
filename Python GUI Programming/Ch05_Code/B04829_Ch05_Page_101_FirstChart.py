'''
Created on Jul 18, 2015

@author: Burkhard
'''

import numpy as np
import matplotlib.pyplot as plt
from pylab import show

x = np.arange(0, 5, 0.1);
y = np.sin(2*x)
plt.plot(x, y)

show()
