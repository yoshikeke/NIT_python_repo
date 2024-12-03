import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.0,2*np.pi,360//5+1)
f = 2*np.sin(2*x)

plt.plot(x,f)
plt.show()