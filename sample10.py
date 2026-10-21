import numpy as np
import matplotlib.pyplot as plt
 
x = np.linspace(-10, 10, 100)
y1 = x
y2 = x ** 2
y3 = np.sin(x)
 
plt.plot(x, y1, label="y = x")
plt.plot(x, y2, label="y = x^2")
plt.plot(x, y3, label="y = sin(x)")
 
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Mathematical Functions")
plt.legend()
plt.grid(True)
plt.show()
