import matplotlib.pyplot as plt
import numpy as np

def random(r):
    return r * np.random.rand()


def random_point(r_max):
    rr = random(r_max**2)
    theta = random(np.pi/2.)
    r = np.sqrt(rr)
    return r, theta

def r_theta_to_x_y(r, theta):
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y
    
N = 1000
points = np.array([random_point(4) for x in range(N)])

rs = points[:, 0]
thetas = points[:, 1]

points2 = np.array([r_theta_to_x_y(r, theta) for (r, theta) in points])

x = points2[:, 0]
y = points2[:, 1]

plt.scatter(x, y)
