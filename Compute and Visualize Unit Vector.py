#@title Default title text { vertical-output: true }
#plot of 2-d vectors and its unit vector 
import numpy as np
import matplotlib.pyplot as plt 

#create a 2d vector 
v = np.array([-3,6,])

#compute the scaling factor 

mu = 1/np.linalg.norm(v)

mu

# unit vector with magnitude 1 and direction along v
vn = v * mu
print(vn)
vn ** 2

plt.figure(figsize = (5 * 1, 5 * 1)) # width by height 
plt.plot(0, v[0], v[1], 'b', label = "v")
plt.plot(0, vn[0], vn[1], 'r', label = "v-norm", linewidth = 5)

# set up the coordinate 

plt.axis('square')
plt.axis((-6,6,-6,6))
plt.grid()
plt.legend()
plt.show()
