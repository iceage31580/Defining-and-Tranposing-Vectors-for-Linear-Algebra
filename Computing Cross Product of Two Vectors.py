# define two vectors 
v = [-3, 2, 5]
w = [4,-3,0]

# manually compute the cross product
#cs_vw = [()],[()],[()]
v = [-3, 2, 5]
w = [4,-3,0]

cs_vw = [(v[1] * w[2]) - (v[2] * w[1]), 
         (v[2] * w[0]) - (v[0] * w[2]), 
         (v[0] * w[1]) - (v[1] * w[0])]
                         

#cs_vw1, cs_vw2, cs_vw3 = [()], [()], [()] 

print(f"Vector v = {v} \nVector w = {w}\n")
print(f"The cross product using native python is v x w = {cs_vw}")

import numpy as np
#define two vectors 

v = [-3,2,5]
w = [4,-3,0]

# python numpy corss product method 

cs_vw_p = np.cross(v,w) # v and w, v will have a minus sign difference 
# define two vectors 
v = [-3,2,5]
w = [4,-3,0]

print(f"Vector v = {v} \nVector w = {w}\n")
print(f"The cross product using native python is v x w = {cs_vw_p}")
