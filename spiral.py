import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl

def plotSpiral(core, fixed, phase=0, circle=4):
    plt.axis("equal")
    plt.plot([core[0]], [core[1]], c='red', marker='+', markersize=10)
    fixed_rad = np.radians(90 + fixed)
    theta = np.linspace(0, circle*2*np.pi, 361) + phase*2*np.pi
    r = fixed_rad*np.exp(theta/np.tan(fixed_rad))
    x = r*np.cos(theta) + core[0]
    y = r*np.sin(theta) - core[1]
    plt.plot(x, y, c='blue')
    plt.show()

plotSpiral( (530,496) , -9, 4, circle=4)
