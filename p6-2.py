import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.0,8*np.pi,360//5+1)
f = np.sin(x)

plt.plot(x,f)
plt.show()